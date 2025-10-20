"""SIGPLAN-aligned programming integration for entropy optical QC."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Sequence, Set


@dataclass(frozen=True)
class SIGPLANDomain:
    """Describes a SIGPLAN programming-language domain and its application."""

    name: str
    application: str


@dataclass(frozen=True)
class ProgrammingInfluenceProfile:
    """Captures how SIGPLAN domains inform the programming stack."""

    foundational_domains: Sequence[SIGPLANDomain]
    emerging_focus: Sequence[str]
    probabilistic_domains: Sequence[SIGPLANDomain]
    verification_targets: Sequence[str]

    def domain_names(self) -> Set[str]:
        """Return the set of foundational domain names in the profile."""

        return {domain.name for domain in self.foundational_domains}

    def probabilistic_domain_names(self) -> Set[str]:
        """Return the set of probabilistic domain names in the profile."""

        return {domain.name for domain in self.probabilistic_domains}


def default_quantum_sigplan_profile() -> ProgrammingInfluenceProfile:
    """Construct the default SIGPLAN-aware profile for this project."""

    foundational = (
        SIGPLANDomain(
            name="Category Theory & Semantics",
            application=(
                "Dagger compact closed categories formalize quantum processes "
                "and support quantum lambda calculi and monoidal semantics."
            ),
        ),
        SIGPLANDomain(
            name="Linear Type Systems",
            application=(
                "Enforce no-cloning constraints within domain-specific languages "
                "such as Quipper, Silq, Q#, and Proto-Quipper."
            ),
        ),
        SIGPLANDomain(
            name="Denotational & Operational Semantics",
            application=(
                "Connect language constructs with operator models in Hilbert "
                "space for provable correctness."
            ),
        ),
        SIGPLANDomain(
            name="IR Design and Compiler Infrastructure",
            application=(
                "Guide QIR, MLIR dialects, and circuit IRs used for photonic "
                "entropy gate compilation."
            ),
        ),
        SIGPLANDomain(
            name="Optimization & Verification",
            application=(
                "Adapt SSA, dataflow, and constraint techniques to simplify "
                "quantum circuits and entropy-aware schedules."
            ),
        ),
    )

    probabilistic = (
        SIGPLANDomain(
            name="Lambda Calculus & Semantics",
            application=(
                "Enable stochastic lambda calculi where evaluation corresponds "
                "to sampling procedures."
            ),
        ),
        SIGPLANDomain(
            name="Type Systems",
            application=(
                "Track probabilistic validity for random variables and "
                "approximate inference schemes."
            ),
        ),
        SIGPLANDomain(
            name="Category Theory / Monads",
            application=(
                "Use probability monads to formalize sampling, conditioning, "
                "and expectation operators."
            ),
        ),
        SIGPLANDomain(
            name="Compiler Techniques",
            application=(
                "Apply differentiation and stochastic graph lowering to entropy "
                "optimization loops."
            ),
        ),
        SIGPLANDomain(
            name="Formal Verification",
            application=(
                "Extend Hoare-style reasoning to probabilistic safety of entropy "
                "controllers."
            ),
        ),
    )

    emerging = (
        "Type-theoretic compilers for certifying entropy gate correctness via "
        "categorical reasoning",
        "Semantics for quantum control integrating measurement-driven branching",
        "Hybrid DSL composition across QIR, MLIR, and Python orchestrators",
    )

    verification_targets = (
        "HoTT or Cubical Agda encodings for entropy gate equivalence",
        "Probabilistic Hoare logic for entropy controller safety",
        "Compiler passes validating type and resource constraints",
    )

    return ProgrammingInfluenceProfile(
        foundational_domains=foundational,
        emerging_focus=emerging,
        probabilistic_domains=probabilistic,
        verification_targets=verification_targets,
    )


def _coverage_map(domain_names: Iterable[str], required: Sequence[str]) -> Dict[str, bool]:
    """Return a coverage map indicating which required names are present."""

    name_set = {name.lower() for name in domain_names}
    return {key: key.lower() in name_set for key in required}


def evaluate_sigplan_alignment(profile: ProgrammingInfluenceProfile) -> Dict[str, Dict[str, bool]]:
    """Evaluate how well a profile captures SIGPLAN priorities."""

    foundational_required = [
        "Category Theory & Semantics",
        "Linear Type Systems",
        "Denotational & Operational Semantics",
        "IR Design and Compiler Infrastructure",
        "Optimization & Verification",
    ]
    probabilistic_required = [
        "Lambda Calculus & Semantics",
        "Type Systems",
        "Category Theory / Monads",
        "Compiler Techniques",
        "Formal Verification",
    ]

    return {
        "foundational": _coverage_map(profile.domain_names(), foundational_required),
        "probabilistic": _coverage_map(
            profile.probabilistic_domain_names(), probabilistic_required
        ),
    }
