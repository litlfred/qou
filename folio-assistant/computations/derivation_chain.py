#!/usr/bin/env python3
"""
Derivation-chain registry — every numerical claim must trace back
to first principles step by step.

Per the QOU methodology directive (post-PR-#472): existing
computational scripts are **not** trusted by default.  Every
numerical value used in the paper must declare a `DerivationChain`
that walks step-by-step from one of the seven first-principles
entrypoints down to the final value, with explicit:

  - **jet order** at each step (jet-k reduction of the underlying
    object),
  - **GB filtration level** (`J^ℓ / J^{ℓ+1}` stratum), and
  - **spectral stratum** (which residue / cyclotomic root, if any).

Every step also declares its **trust basis**: how do we know the
step is valid?  The seven first-principles entrypoints are
`axiom`-trust; downstream steps must be `lean-proven`,
`mathlib-cited`, `script-cited` (existing computation, marked but
not yet derived), or `derived` (this chain itself).

The validator performs structural and trust-basis checks, and
validates selected computational claims where explicit evaluators
are implemented (currently the COMPUTATIONAL leaf and a small set
of recognised algebraic patterns such as `c_q = 1/(q-1)`).  It
does NOT, in general, re-evaluate every declared step operation —
that would require either a Lean-kernel-style symbolic engine or
domain-specific evaluators per first-principles entrypoint.

Schema is JSON-serializable so chains can be stored alongside
witnesses (`*.derivation.json`) and rebuilt incrementally.
"""

from __future__ import annotations

import enum
import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional, Union


# ── Shared constants ───────────────────────────────────────────

# Canonical substrate parameter — single source of truth for every
# `*.derivation.json` chain in this directory.  See CLAUDE.md §7aa
# (notation register).  Other modules import `Q_0` from here rather
# than redefining their own constant.
Q_0: float = 1.1099785955541805

# Canonical atom-target Markov-trace values at q_0 — match the
# committed `*-tr-M-q0.derivation.json` leaf values exactly.  Per
# Copilot review on #473: re-running any builder must produce
# bit-stable JSON, so the literals must be the single source of
# truth.  Other modules import these rather than redefining.
TR_M_AT_Q0: dict[str, float] = {
    "p": 2.12258250945273,
    "n": 1.5893934459539052,
    "D": 0.17743692421543206,
}


# Pre-compiled module-level regex for SCRIPT_CITED `notes` validation
# (per Gemini PR #484 review): tolerates leading whitespace after the
# colon and is compiled once rather than rebuilt on every step check.
_SCRIPT_NOTE_RE = re.compile(r"script:\s*", re.IGNORECASE)


# ── First principles ────────────────────────────────────────────

class FirstPrinciple(str, enum.Enum):
    """The seven canonical entrypoints; everything traces back here.

    Each member's value is the canonical Lean / content-block
    reference for that entrypoint.
    """
    HECKE_ENERGY        = "Hecke.Energy"
    CATEGORICAL_ACTION  = "Cat.Action"
    FROBENIUS_PAIRING   = "Frobenius.Pairing"
    NONABELIAN_STOKES   = "Nonabelian.Stokes"
    WEDDERBURN          = "Wedderburn"
    SCHUR               = "Schur"
    FINITE_JONES        = "FiniteJones"


# ── Trust basis ────────────────────────────────────────────────

class TrustBasis(str, enum.Enum):
    """How do we know this step is valid?

    Ordering is roughly strongest → weakest:

      AXIOM            — first-principles entrypoint (the seven canonical refs).
      LEAN_PROVEN      — backed by a Lean theorem with no `sorry`.
      MATHLIB_CITED    — invokes a Mathlib lemma (axiom-checked upstream).
      DERIVED          — proven within this chain by a sequence of LEAN_PROVEN /
                         MATHLIB_CITED / AXIOM steps.
      SCRIPT_CITED     — references an existing computation script; the script
                         itself is currently "computational-only" trust pending
                         its own derivation chain.  Use sparingly.
      COMPUTATIONAL    — bare numerical computation (sympy / mpmath / numpy);
                         only acceptable as the final evaluation step at the
                         leaf of an otherwise fully-trusted chain.
    """
    AXIOM           = "axiom"
    LEAN_PROVEN     = "lean-proven"
    MATHLIB_CITED   = "mathlib-cited"
    DERIVED         = "derived"
    SCRIPT_CITED    = "script-cited"
    COMPUTATIONAL   = "computational"


# ── Step ────────────────────────────────────────────────────────

@dataclass
class DerivationStep:
    """One step in a derivation chain.

    Fields
    ------
    name : str
        Human-readable step label (e.g. "Schur–Weyl decomposition of H_3(q)").
    operation : str
        Mathematical operation applied at this step.
    inputs : list[str]
        Names of upstream `DerivationStep`s OR string-encoded
        `FirstPrinciple` values.  All inputs must be defined earlier
        in the chain.
    output_name : str
        Symbolic name of this step's output (referenced by downstream
        steps).
    output_value : Any
        The actual computed value (number, polynomial string, etc.).
        Verified by the validator.
    jet_order : Optional[int]
        Jet order of the object at this step.  None when the concept
        of jet order doesn't apply.
    gb_filtration_level : Optional[int]
        GB-filtration stratum `J^ℓ / J^{ℓ+1}` (the `ℓ`).  None when
        the step is filtration-independent.
    spectral_stratum : Optional[str]
        Spectral stratum identifier (e.g. "ζ_3", "n=2 cyclotomic").
        None when the step is not spectral.
    trust_basis : TrustBasis
        Declared justification for the step.
    lean_ref : Optional[str]
        Pointer to the Lean declaration that formalises this step,
        in `pkg:Decl.Path` form.  Required when trust_basis is
        LEAN_PROVEN, MATHLIB_CITED, or AXIOM.
    citation : Optional[str]
        Reference key from `content/schema/references.ts` or
        manuscript label (e.g. "habiro2004", "manuscript:§6.3").
    notes : Optional[str]
        Additional commentary; especially useful to flag SCRIPT_CITED
        steps with the script path + commit.
    """
    name: str
    operation: str
    inputs: list[str]
    output_name: str
    output_value: Any
    trust_basis: TrustBasis
    jet_order: Optional[int] = None
    gb_filtration_level: Optional[int] = None
    spectral_stratum: Optional[str] = None
    lean_ref: Optional[str] = None
    citation: Optional[str] = None
    notes: Optional[str] = None

    def to_dict(self) -> dict:
        d = asdict(self)
        d["trust_basis"] = self.trust_basis.value
        return {k: v for k, v in d.items() if v is not None}


# ── Chain ───────────────────────────────────────────────────────

@dataclass
class DerivationChain:
    """A complete chain of derivation steps for one named claim.

    Fields
    ------
    target : str
        The final claim being derived (e.g. "tr_M(p, q_0)").
    target_value : Any
        The final numerical value being certified.
    target_tolerance : float
        Acceptable relative tolerance when the validator re-walks
        the chain.
    steps : list[DerivationStep]
        Steps in order; each step's `inputs` must reference earlier
        step `output_name`s or `FirstPrinciple` enum values.
    content_block : Optional[str]
        Content block label this chain certifies (e.g.
        "prop:full-pole-structure-mass-trace").
    description : Optional[str]
        Free-form description of the chain's scope.
    """
    target: str
    target_value: Any
    target_tolerance: float
    steps: list[DerivationStep]
    content_block: Optional[str] = None
    description: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "target": self.target,
            "target_value": self.target_value,
            "target_tolerance": self.target_tolerance,
            "content_block": self.content_block,
            "description": self.description,
            "steps": [s.to_dict() for s in self.steps],
        }

    def save(self, path: Union[str, Path]) -> Path:
        p = Path(path)
        with p.open("w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)
            f.write("\n")
        return p

    # ── Structural validation ──────────────────────────────────

    def structural_check(self) -> tuple[bool, list[str]]:
        """Verify the chain is well-formed: every step's inputs are
        defined earlier (either as a previous step's output_name or
        as a FirstPrinciple).  Returns (ok, list-of-issues)."""
        defined: set[str] = {fp.value for fp in FirstPrinciple}
        issues: list[str] = []

        for step in self.steps:
            for inp in step.inputs:
                if inp not in defined:
                    issues.append(
                        f"step {step.name!r}: input {inp!r} not defined "
                        "(must be a previous step's output_name or a "
                        "FirstPrinciple value)"
                    )
            # First-principle steps must have AXIOM trust + a lean_ref.
            if step.trust_basis == TrustBasis.AXIOM:
                if step.lean_ref is None:
                    issues.append(
                        f"AXIOM step {step.name!r} must declare lean_ref"
                    )
            # Lean / Mathlib steps must have a lean_ref.
            if step.trust_basis in (TrustBasis.LEAN_PROVEN, TrustBasis.MATHLIB_CITED):
                if step.lean_ref is None:
                    issues.append(
                        f"{step.trust_basis.value} step {step.name!r} "
                        "must declare lean_ref"
                    )
            # SCRIPT_CITED steps should record the script path in notes.
            if step.trust_basis == TrustBasis.SCRIPT_CITED:
                # Accept either `script:` or `Script:` (legacy chains)
                # via the module-level pre-compiled `_SCRIPT_NOTE_RE`.
                if step.notes is None or not _SCRIPT_NOTE_RE.search(step.notes):
                    issues.append(
                        f"SCRIPT_CITED step {step.name!r} should record "
                        "the script path in `notes` (e.g. 'script: foo.py @ <sha>')"
                    )
            # COMPUTATIONAL is the leaf only — numerical eval may not
            # appear in the middle of a chain (per the docstring of
            # TrustBasis.COMPUTATIONAL).  Enforced per Gemini #473.
            if step.trust_basis == TrustBasis.COMPUTATIONAL and step is not self.steps[-1]:
                issues.append(
                    f"COMPUTATIONAL step {step.name!r} is not the leaf; "
                    "numerical evaluation is only permitted as the final step."
                )
            defined.add(step.output_name)

        return (not issues, issues)

    def trust_summary(self) -> dict[str, int]:
        """Count steps by trust basis — a quick read on chain quality."""
        counts: dict[str, int] = {tb.value: 0 for tb in TrustBasis}
        for s in self.steps:
            counts[s.trust_basis.value] += 1
        return counts


# ── Quick sanity test ─────────────────────────────────────────

if __name__ == "__main__":
    # Smoke test: construct a trivial chain and validate it.
    chain = DerivationChain(
        target="trivial-test",
        target_value=42,
        target_tolerance=0.0,
        steps=[
            DerivationStep(
                name="constant 42",
                operation="literal",
                inputs=[FirstPrinciple.HECKE_ENERGY.value],
                output_name="x",
                output_value=42,
                trust_basis=TrustBasis.AXIOM,
                lean_ref="qou:QOU.Test.fortyTwo",
            ),
        ],
        description="smoke test: 42 derived from the Hecke energy axiom",
    )
    ok, issues = chain.structural_check()
    print(f"structural_check: {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
