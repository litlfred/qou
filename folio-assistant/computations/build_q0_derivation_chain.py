#!/usr/bin/env python3
"""
Skeleton chain — q_0 derivation (Phase B, SPECULATIVE).

The substrate parameter q_0 ≈ 1.10997855... is currently **fitted**
from observational data (CODATA m_p / m_e ratio, α-FSC, hyperbolic
volumes), not derived from first principles.  Per the post-#473
workplan to 1 ppb, closing q_0 via a derivation chain is the
highest-leverage Phase B move — every prediction inherits q_0's
fit uncertainty until this lands.

Three candidate derivation paths exist in the literature:

  (A) **From α-FSC**: the alpha-em-pslq witnesses (PR #457 family)
      identify candidate algebraic relations between q_0 and α via
      the PSLQ algorithm at 2000 dps.  No definitive closed form
      established yet; tracked under
      `alpha-em-pslq-uniqueness-2000dps.witness.json`.

  (B) **From m_p/m_e**: the Hecke-theoretic dimensionless mass
      ratio is a function of q_0; inverting gives q_0 = f(m_p/m_e).
      Concrete formula not derived; tracked under
      `m_p_breakdown_derived_vs_guessed.py` notes.

  (C) **From topology**: q_0 should arise as a transcendental
      invariant of the brane-tower hyperbolic geometry (e.g. from
      Vol(K) of a canonical knot K).  Speculative; no concrete
      candidate yet.

This chain provides the structural skeleton with all three paths
listed as SCRIPT_CITED steps.  When any one closes, the chain
becomes fully-trusted via that path.

Output: `q0-derivation-skeleton.derivation.json`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    Q_0,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT = HERE / "q0-derivation-skeleton.derivation.json"


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Substrate parameter as the unknown (manuscript-cited)
    # Per DERIVATION-CHAIN-METHODOLOGY.md, AXIOM is reserved for the
    # seven FirstPrinciple entrypoints.  The substrate parameter
    # itself is a manuscript axiom/definition; mark as SCRIPT_CITED
    # with citation pointing at the def-block + q_parameter.py.
    steps.append(DerivationStep(
        name="q_0 := unique substrate parameter",
        operation=(
            "By `def:substrate-parameter`, the QOU manuscript "
            "introduces a single real parameter q_0 ∈ ℝ_{>1} "
            "characterising the Hecke energy scale (q − q^{-1}).  "
            "Empirically q_0 ≈ 1.10997855... matches CODATA "
            "observables; the framework's claim of being "
            "**derivative** rather than empirical requires closing "
            "q_0 via a first-principles derivation."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name="q_0_axiom",
        output_value="q_0 ∈ ℝ_{>1} — substrate parameter",
        trust_basis=TrustBasis.SCRIPT_CITED,
        lean_ref="qou:STUB:SubstrateParameter",
        citation="manuscript:§Substrate-axiom",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/q_parameter.py — "
            "ships the canonical numeric value of q_0 used by every "
            "downstream chain.  This step is SCRIPT_CITED because "
            "AXIOM is reserved for the seven FirstPrinciple "
            "entrypoints (per DERIVATION-CHAIN-METHODOLOGY.md); "
            "extending FirstPrinciple to include `SubstrateParameter` "
            "is a candidate Lean-side refinement that would let this "
            "step become AXIOM, but the q_0 numerical value would "
            "still need to be sourced from the substrate definition "
            "(currently empirical-fitted)."
        ),
    ))

    # 2 — Path A: from α-FSC via PSLQ
    steps.append(DerivationStep(
        name="Path A: q_0 from α-FSC via PSLQ",
        operation=(
            "Per the alpha-em-pslq-uniqueness-2000dps protocol (PR "
            "#457 family), search for an integer linear relation "
            "between q_0 and the fine-structure constant α at 2000 "
            "dps.  The PSLQ algorithm returns a candidate relation "
            "if the rational coefficients have bounded norm.  As of "
            "this skeleton, **no definitive closed form has been "
            "established**; remains SCRIPT_CITED until PSLQ "
            "identifies an unambiguous relation."
        ),
        inputs=["q_0_axiom"],
        output_name="path_A_alpha",
        output_value="q_0 = f(α) — f unspecified (PSLQ search ongoing)",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§alpha-em-pslq",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/alpha_em_pslq_uniqueness_2000dps.py "
            "(2000 dps PSLQ search).  Currently SCRIPT_CITED — no "
            "stable rational relation found at 2000 dps within "
            "norm-bounded candidates.  Closing this step requires "
            "either a higher PSLQ precision or a theoretical insight "
            "constraining the form of f."
        ),
    ))

    # 3 — Path B: from m_p / m_e
    steps.append(DerivationStep(
        name="Path B: q_0 from m_p/m_e Hecke ratio",
        operation=(
            "The dimensionless mass ratio m_p/m_e is a function of "
            "q_0 via the mass-endomorphism tower (per "
            "`m_p_breakdown_derived_vs_guessed.py`).  Inverting gives "
            "q_0 = g(m_p/m_e) for some analytic function g.  CODATA "
            "supplies m_p/m_e = 1836.15267343 to 12-digit precision; "
            "if g were known, q_0 would inherit that precision.  "
            "**g is unspecified** in the current pipeline — the "
            "tower formula is forward (q_0 → ratio) but not closed-"
            "form invertible."
        ),
        inputs=["q_0_axiom", FirstPrinciple.SCHUR.value],
        output_name="path_B_mp_me",
        output_value="q_0 = g(m_p/m_e) — g unspecified",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§mass-endomorphism-tower-inversion",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/m_p_breakdown_derived_vs_guessed.py "
            "supplies the forward direction (q_0 → m_p/m_e); inversion "
            "requires solving a transcendental equation in q_0.  "
            "SCRIPT_CITED until a numerical-or-closed-form inverse "
            "ships."
        ),
    ))

    # 4 — Path C: from topology
    steps.append(DerivationStep(
        name="Path C: q_0 from brane-tower topology (speculative)",
        operation=(
            "Speculative: q_0 should arise as a transcendental "
            "invariant of a canonical knot K in the brane tower, e.g. "
            "via Vol(K) / 2π² or the Kashaev-Murakami-Murakami volume "
            "conjecture limit.  No concrete candidate K has been "
            "identified.  Tracked here as the highest-leverage Phase "
            "B target: a topological derivation would be both fully-"
            "trusted AND independent of CODATA observables."
        ),
        inputs=["q_0_axiom", FirstPrinciple.CATEGORICAL_ACTION.value],
        output_name="path_C_topology",
        output_value="q_0 = h(Vol(K_canonical)) — K, h unspecified",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§q_0-topology-conjecture",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/atom_colored_jones_volume.py "
            "(SnapPy/colored-Jones volumes for candidate knots).  "
            "SCRIPT_CITED — no canonical K identified; awaits "
            "theoretical input."
        ),
    ))

    # 5 — Numerical anchor
    steps.append(DerivationStep(
        name="q_0 numerical value (empirical fit)",
        operation=(
            "Until any of paths A/B/C closes, the canonical q_0 value "
            f"is the empirical fit q_0 ≈ {Q_0} from "
            "CODATA-bounded observables (`q_parameter.py`)."
        ),
        inputs=["path_A_alpha", "path_B_mp_me", "path_C_topology"],
        output_name="q_0_numerical",
        output_value=Q_0,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            "Empirical fit; replaces with derivation when any of "
            "paths A/B/C closes.  Until then, every prediction "
            "inherits the fit's uncertainty."
        ),
    ))

    return DerivationChain(
        target="q_0",
        target_value=Q_0,
        target_tolerance=1e-10,
        content_block="def:substrate-parameter",  # placeholder
        description=(
            "**Speculative skeleton chain** for the substrate "
            "parameter q_0 ≈ 1.110.  Phase B target of the post-"
            "#473 1 ppb workplan.  Three candidate derivation paths "
            "(α-FSC PSLQ / m_p/m_e inversion / brane-tower "
            "topology) recorded as SCRIPT_CITED steps; the "
            "COMPUTATIONAL leaf reads the empirical fit.  Trust "
            "profile {axiom: 1, mathlib-cited: 0, derived: 0, "
            "script-cited: 3, computational: 1} — **NOT fully-"
            "trusted**.  Closing any one of the three paths would "
            "discharge the chain to fully-trusted; closing all three "
            "would provide cross-validation independent of CODATA.  "
            "Highest-leverage Phase B item: every downstream "
            "prediction inherits q_0's fit uncertainty until this "
            "chain closes."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"q_0 derivation skeleton: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
