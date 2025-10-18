"""Simulation pipelines for entropy optical quantum computing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict

import numpy as np

from entropy_optical_qc.analysis.metrics import entropy_production
from entropy_optical_qc.config import SimulationConfig
from entropy_optical_qc.entropy.process_models import EntropyProcessModel
from entropy_optical_qc.simulation.master_equation import solve_master_equation


@dataclass
class SimulationPipeline:
    """High-level orchestration for simulation experiments."""

    config: SimulationConfig
    process_model_factory: Callable[[SimulationConfig], EntropyProcessModel]

    def run(self, initial_state: np.ndarray, times: np.ndarray) -> Dict[str, object]:
        """Execute the simulation and collect summary metrics."""

        model = self.process_model_factory(self.config)
        result = solve_master_equation(model, initial_state, times)
        summary = {
            "trajectory_entropy": entropy_production(result.states),
            "metadata": result.metadata,
        }
        return {"result": result, "summary": summary}
