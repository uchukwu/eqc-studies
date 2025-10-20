"""Programming-language integration utilities for entropy optical QC."""

from .sigplan_integration import (
    ProgrammingInfluenceProfile,
    SIGPLANDomain,
    evaluate_sigplan_alignment,
    default_quantum_sigplan_profile,
)

__all__ = [
    "ProgrammingInfluenceProfile",
    "SIGPLANDomain",
    "evaluate_sigplan_alignment",
    "default_quantum_sigplan_profile",
]
