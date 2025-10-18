"""Master-equation simulation utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Optional, Sequence

import numpy as np

from entropy_optical_qc.entropy.process_models import EntropyProcessModel


@dataclass
class MasterEquationResult:
    """Container for master-equation simulation results."""

    times: np.ndarray
    states: Sequence[np.ndarray]
    metadata: Dict[str, float]


def solve_master_equation(
    model: EntropyProcessModel,
    initial_state: np.ndarray,
    times: np.ndarray,
    hamiltonian: Optional[Callable[[float], np.ndarray]] = None,
) -> MasterEquationResult:
    """Solve the Lindblad master equation using a placeholder integrator."""

    if hamiltonian is None:
        hamiltonian = lambda _t: model.hamiltonian

    dt = np.diff(times)
    if np.any(dt <= 0):
        raise ValueError("Time vector must be strictly increasing")

    rho = initial_state.astype(complex)
    states = [rho]
    for t, step in zip(times[:-1], dt):
        # Placeholder Euler integration; replace with high-order solver.
        drho = _lindblad_rhs(rho, hamiltonian(t), model.lindblad_terms())
        rho = rho + step * drho
        rho = _enforce_physicality(rho)
        states.append(rho)

    metadata = {
        "method": "euler",
        "entropy_weights": float(np.sum(model.entropy_weights())),
    }
    return MasterEquationResult(times=times, states=states, metadata=metadata)


def _lindblad_rhs(
    rho: np.ndarray,
    hamiltonian: np.ndarray,
    lindblad_ops: Sequence[np.ndarray],
) -> np.ndarray:
    """Compute the right-hand side of the Lindblad master equation."""

    commutator = hamiltonian @ rho - rho @ hamiltonian
    dissipators = np.zeros_like(rho, dtype=complex)
    for operator in lindblad_ops:
        dissipators += (
            operator @ rho @ operator.conj().T
            - 0.5 * (operator.conj().T @ operator @ rho + rho @ operator.conj().T @ operator)
        )
    return -1j * commutator + dissipators


def _enforce_physicality(rho: np.ndarray) -> np.ndarray:
    """Project onto the space of Hermitian, trace-one matrices."""

    hermitian = 0.5 * (rho + rho.conj().T)
    eigenvalues, eigenvectors = np.linalg.eigh(hermitian)
    eigenvalues = np.clip(eigenvalues, a_min=0.0, a_max=None)
    eigenvalues /= np.sum(eigenvalues)
    return eigenvectors @ np.diag(eigenvalues) @ eigenvectors.conj().T
