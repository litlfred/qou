---
name: qou-canonical-code-review
roles: [collaborator, owner]
user_invocable: false
description: >
  Expert procedural guidance for auditing QOU technical assets (Python, Lean,
  Rust). Enforces high-precision accuracy, canonical derivations, and
  traceability.
allowed-tools: Read Edit Write Bash Grep Glob AskUserQuestion
---

# QOU Canonical Code Review Standards

Use these criteria when performing a `compute-code-review` on any technical asset
in the Quantum Observable Universe repository.

## 1. High-Precision Integrity
*   **No Native Floats**: Use of `float` or `double` is FORBIDDEN for physical
    constants or derivation intermediate steps. Use `mpmath.mpf` (Python),
    `Real` (Lean), or high-precision FFI types (Rust).
*   **No Truncation**: Precision must be maintained at the level defined by
    the `_precision` or `_path_bridge` modules. Do not round until the final
    output step (witness emission).
*   **Literal Safety**: Never initialize a high-precision type from a float
    literal (e.g., `mpf(0.1)`). Always use a string literal (`mpf("0.1")`) to
    prevent IEEE-754 corruption at the bit level.

## 2. Canonical Derivation & Traceability
*   **No Hardcoded Constants**: Physical constants (m_e, m_p, Vol(4_1), etc.)
    MUST be imported from `q_parameter.py` or `qou_substrate.constants`.
*   **Proposition References**: Code MUST include `# Ref: prop:ID` or
    `# Ref: def:ID` comments linking the implementation to the authoritative
    mathematical block in the paper.
*   **Newton Solves**: Pinned parameters (like q0) must be derived via the
    canonical Newton-solver or fixed-point iteration defined in the framework,
    not "magic numbers."

## 3. Compute Optimization
*   **Avoid Redundant Solves**: Import derived constants from the bridge rather
    than re-solving them in every script.
*   **Parallelism**: Use `rayon` (Rust) or `multiprocessing`/`concurrent.futures`
    (Python) for batch computations (e.g., sweep over 2000+ isotopes).
*   **FFI Boundaries**: Large-scale Hecke/SnapPy calculations should be pushed
    to native extensions (PyHecke, SnapPea-WASM) rather than pure Python loops.

## 4. Verification & Witnesses
*   **Witness Parity**: Every script that computes a physical quantity MUST
    emit a `.witness.json` containing the result, the timestamp, the
    precision level, and the physical anchoring bound (e.g., CODATA sigma).
*   **Assertion Discipline**: Use `assert` for internal sanity checks on
    algebraic identities (e.g., `assert abs(sum(w_lambda) - 1) < eps`).

## Review Template for QA Sidecar
When logging a finding, identify which standard was violated:
*   `[Standard: Precision] Native float corrupted q0 solve.`
*   `[Standard: Traceability] Missing Ref: prop:ID for mass formula.`
*   `[Standard: Constants] Hardcoded m_mu value found.`
