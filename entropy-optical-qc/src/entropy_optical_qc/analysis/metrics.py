"""Analysis metrics for entropy optical quantum simulations."""

from __future__ import annotations

from typing import Sequence

import numpy as np


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    """Compute the trace distance between two density matrices."""

    delta = rho - sigma
    singular_values = np.linalg.svd(delta, compute_uv=False)
    return 0.5 * float(np.sum(np.abs(singular_values)))


def average_gate_fidelity(process: Sequence[np.ndarray], target: np.ndarray) -> float:
    """Estimate average gate fidelity from Kraus operators."""

    dim = target.shape[0]
    accumulator = 0.0
    for kraus in process:
        accumulator += np.trace(target.conj().T @ kraus)
    return float((np.abs(accumulator) ** 2 + dim) / (dim * (dim + 1)))


def entropy_production(states: Sequence[np.ndarray]) -> float:
    """Compute cumulative entropy production across a trajectory."""

    total_entropy = 0.0
    for rho in states:
        eigenvalues = np.linalg.eigvalsh(rho)
        nonzero = eigenvalues[eigenvalues > 0]
        total_entropy += float(-np.sum(nonzero * np.log(nonzero)))
    return total_entropy
