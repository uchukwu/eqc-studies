"""Factory helpers for building entropy process models."""

from __future__ import annotations

import numpy as np

from entropy_optical_qc.config import SimulationConfig
from entropy_optical_qc.entropy.process_models import (
    EntropyProcessModel,
    LindbladChannel,
)


def default_process_model_factory(config: SimulationConfig) -> EntropyProcessModel:
    """Construct a simple entropy process model from configuration data."""

    dim = 2 ** len(config.modes)
    hamiltonian = np.zeros((dim, dim), dtype=complex)
    channels = []
    for reservoir in config.reservoirs:
        for mode_label, rate in reservoir.coupling_rates.items():
            operator = _lowering_operator(dim, mode_index=0) * np.sqrt(rate)
            channels.append(
                LindbladChannel(
                    operator=operator,
                    label=f"{reservoir.label}_{mode_label}",
                    entropy_weight=reservoir.target_entropy_flow,
                )
            )
    return EntropyProcessModel(hamiltonian=hamiltonian, channels=tuple(channels))


def _lowering_operator(dimension: int, mode_index: int) -> np.ndarray:
    """Placeholder lowering operator for the specified mode."""

    operator = np.zeros((dimension, dimension), dtype=complex)
    if dimension >= 2:
        operator[0, 1] = 1.0
    return operator
