# Entropy Optical Quantum Computing Research Program

This directory contains the working notes, theoretical framework, and reference
code skeleton for investigating an all-optical quantum computing architecture
based on entropy-driven processes and time-bin encoding. The materials are
organized to facilitate deep research and rapid iteration on modeling,
simulation, and benchmarking tasks. It now also encodes programming-language
considerations drawn from ACM SIGPLAN guidance for quantum and probabilistic
systems.

## Structure

- `docs/`: Research plans, proposals, and theoretical background.
- `src/entropy_optical_qc/`: Python package hosting modeling and simulation
  primitives together with SIGPLAN-aligned programming utilities.
- `pyproject.toml`: Project configuration (dependencies, tooling) for future
  development.

## Getting Started

1. Review `docs/research_plan.md` for prioritized investigative steps.
2. Consult `docs/theoretical_framework.md` to understand the theoretical and
   computational approaches.
3. Implement prototypes using the skeleton modules inside
   `src/entropy_optical_qc/`.
4. Track progress and update standards, benchmarks, and project documentation
   as insights evolve.

## SIGPLAN Programming Alignment

- Use `entropy_optical_qc.programming.default_quantum_sigplan_profile()` to seed
  projects with the canonical ACM SIGPLAN domains for quantum and probabilistic
  computing.
- Leverage `evaluate_sigplan_alignment` during reviews to verify coverage of
  categorical semantics, linear types, IR infrastructure, optimization, and
  probabilistic reasoning.
- Capture verification artifacts (Agda/Coq proofs, probabilistic Hoare logic
  reports) referenced in `docs/standards_benchmarks.md`.
