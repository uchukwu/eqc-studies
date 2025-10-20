"""Time-bin encoding utilities for entropy optical quantum computing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

import numpy as np


@dataclass(frozen=True)
class TimeBinState:
    """Representation of a single-qubit time-bin state."""

    amplitudes: Tuple[complex, complex]

    def normalize(self) -> "TimeBinState":
        """Return a normalized copy of the time-bin state."""

        norm = np.linalg.norm(self.amplitudes)
        if np.isclose(norm, 0.0):
            raise ValueError("Time-bin state has zero norm")
        normalized = tuple(amplitude / norm for amplitude in self.amplitudes)
        return TimeBinState(amplitudes=normalized)  # type: ignore[arg-type]

    def entropy(self) -> float:
        """Compute the von Neumann entropy of the reduced density matrix."""

        probs = np.abs(self.normalize().amplitudes) ** 2
        nonzero = probs[probs > 0]
        return float(-np.sum(nonzero * np.log2(nonzero)))


def kron_time_bins(states: Iterable[TimeBinState]) -> np.ndarray:
    """Compute the Kronecker product of multiple time-bin states."""

    tensor = None
    for state in states:
        vector = np.array(state.normalize().amplitudes, dtype=complex)
        tensor = vector if tensor is None else np.kron(tensor, vector)
    if tensor is None:
        raise ValueError("At least one state is required")
    return tensor
