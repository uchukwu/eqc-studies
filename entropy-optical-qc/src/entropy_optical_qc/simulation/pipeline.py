"""Simulation pipelines for entropy optical quantum computing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Optional

import numpy as np

from entropy_optical_qc.analysis.metrics import entropy_production
from entropy_optical_qc.config import SimulationConfig
from entropy_optical_qc.entropy.process_models import EntropyProcessModel
from entropy_optical_qc.programming.sigplan_integration import (
    ProgrammingInfluenceProfile,
    evaluate_sigplan_alignment,
)
from entropy_optical_qc.simulation.master_equation import solve_master_equation


@dataclass
class SimulationPipeline:
    """High-level orchestration for simulation experiments."""

    config: SimulationConfig
    process_model_factory: Callable[[SimulationConfig], EntropyProcessModel]
    language_profile: Optional[ProgrammingInfluenceProfile] = None

    def run(self, initial_state: np.ndarray, times: np.ndarray) -> Dict[str, object]:
        """Execute the simulation and collect summary metrics."""

        model = self.process_model_factory(self.config)
        result = solve_master_equation(model, initial_state, times)
        summary = {
            "trajectory_entropy": entropy_production(result.states),
            "metadata": result.metadata,
        }
        if self.language_profile is not None:
            summary["programming_alignment"] = evaluate_sigplan_alignment(
                self.language_profile
            )
        return {"result": result, "summary": summary}
