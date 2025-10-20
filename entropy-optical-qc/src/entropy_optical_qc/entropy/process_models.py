"""Entropy process models for optical quantum systems."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence

import numpy as np


@dataclass
class LindbladChannel:
    """Represents a Lindblad dissipator with entropy annotations."""

    operator: np.ndarray
    label: str
    entropy_weight: float = 1.0


@dataclass
class EntropyProcessModel:
    """Collects Hamiltonian and dissipative elements for simulation."""

    hamiltonian: np.ndarray
    channels: Sequence[LindbladChannel]

    def lindblad_terms(self) -> Sequence[np.ndarray]:
        """Return raw Lindblad operators for use in solvers."""

        return [channel.operator for channel in self.channels]

    def entropy_weights(self) -> np.ndarray:
        """Return entropy weights aligned with Lindblad operators."""

        return np.array([channel.entropy_weight for channel in self.channels])


def build_effective_hamiltonian(
    base_hamiltonian: np.ndarray,
    control_generator: np.ndarray,
    control_amplitude: Callable[[float], float],
) -> Callable[[float], np.ndarray]:
    """Generate a time-dependent Hamiltonian with entropy-aware control."""

    def h_t(time: float) -> np.ndarray:
        return base_hamiltonian + control_amplitude(time) * control_generator

    return h_t
