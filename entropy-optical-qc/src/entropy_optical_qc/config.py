"""Configuration dataclasses for entropy-optical quantum simulations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence


@dataclass(frozen=True)
class OpticalModeConfig:
    """Specification for a single optical mode.

    Attributes:
        label: Unique identifier for the mode (e.g., "signal_early").
        frequency: Central frequency in Hz.
        bandwidth: Spectral bandwidth in Hz.
        polarization: Polarization label or descriptor.
    """

    label: str
    frequency: float
    bandwidth: float
    polarization: str = "H"


@dataclass(frozen=True)
class EntropyReservoirConfig:
    """Configuration for engineered entropy reservoirs.

    Attributes:
        label: Unique identifier for the reservoir.
        coupling_rates: Mapping from optical mode labels to coupling strengths.
        temperature: Effective temperature (in Kelvin) of the reservoir.
        target_entropy_flow: Desired entropy flow rate (dimensionless units).
    """

    label: str
    coupling_rates: Mapping[str, float]
    temperature: float
    target_entropy_flow: float


@dataclass(frozen=True)
class GateSpecification:
    """Definition of a logical gate implemented via time-bin encoding."""

    name: str
    control_modes: Sequence[str]
    target_modes: Sequence[str]
    duration: float
    target_fidelity: float


@dataclass
class SimulationConfig:
    """Top-level configuration for a simulation experiment."""

    modes: Sequence[OpticalModeConfig]
    reservoirs: Sequence[EntropyReservoirConfig]
    gates: Sequence[GateSpecification]
    solver: str = "lindblad"
    solver_options: Mapping[str, float] = field(default_factory=dict)

    def as_dict(self) -> Mapping[str, object]:
        """Convert the configuration to a serializable dictionary."""

        return {
            "modes": [vars(mode) for mode in self.modes],
            "reservoirs": [vars(reservoir) for reservoir in self.reservoirs],
            "gates": [vars(gate) for gate in self.gates],
            "solver": self.solver,
            "solver_options": dict(self.solver_options),
        }
