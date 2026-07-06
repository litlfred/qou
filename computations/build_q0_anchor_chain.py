#!/usr/bin/env python3
"""
Substrate-parameter anchor chain for q_0.

This is the **post-#481-reconceive** q_0 chain.  PR #481 originally
shipped a `q0-derivation-skeleton` chain enumerating three open
candidate paths (PSLQ via α-FSC, m_p/m_e tower-inversion, brane-tower
topology).  Two of those paths reference scripts that were never
landed on main (`m_p_breakdown_derived_vs_guessed.py`,
`atom_colored_jones_volume.py`); the third (`alpha_em_pslq_uniqueness`)
is a real witness but its 2000 dps variant was never written.

Per AGENTS.md, every step in a chain must be either a real
derivation or a script-cited debt with a reference to a script that
exists.  Enumerating speculative future-paths in a chain is not
methodological — those belong in a workplan document, not a
DerivationChain.

This chain is therefore the **honest, minimal anchor**:

  step 1 — AXIOM:        substrate parameter (def:substrate-parameter-planck)
  step 2 — SCRIPT_CITED: numerical anchor q_0 ≈ 1.110 from q_parameter.py
  step 3 — COMPUTATIONAL: leaf value matches `Q_0` literal

Trust profile {axiom: 1, script-cited: 1, computational: 1} — **NOT
fully-trusted by design**.  The single SCRIPT_CITED debt is
`q_parameter.py`, which currently records the empirical fit.  When
any of the three candidate derivations (PSLQ closure, m_p/m_e
tower-inversion, brane-tower volume conjecture) lands as a real
script, this chain rebases to consume it directly and the SCRIPT_CITED
step is upgraded to DERIVED.

Output: `q0-anchor.derivation.json`.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
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
OUTPUT = _pb.witness_path("q0-anchor.derivation.json", HERE)


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Substrate parameter axiom (manuscript definition)
    steps.append(DerivationStep(
        name="Substrate parameter q_0 ∈ ℝ_{>1}",
        operation=(
            "By `def:substrate-parameter-planck`, the QOU "
            "manuscript introduces a single real parameter "
            "`q_0 ∈ ℝ_{>1}` characterising the Hecke energy scale "
            "`(q − q^{-1})`.  Existence and uniqueness follow from "
            "the Planck-normalisation: `G(q_0) = 1` fixes `q_0` to "
            "be the unique positive solution of the gravitational-"
            "constant fixed-point equation."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name="q_0_axiom",
        output_value="q_0 ∈ ℝ_{>1}",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:QOU.AlgebraicSubstrate.SubstrateParameterPlanck",
        citation="manuscript:§Substrate-axiom",
        jet_order=0,
    ))

    # 2 — Numerical anchor (script-cited)
    steps.append(DerivationStep(
        name="Numerical value of q_0 from Planck normalisation",
        operation=(
            "Numerical solution of `G(q_0) = 1` (the Planck-"
            "normalised gravitational-constant fixed-point) at the "
            "canonical fit precision yields "
            f"`q_0 ≈ {Q_0:.16g}`.  The compute-pipeline source of "
            "truth is the pinned literal `derivation_chain.Q_0`; "
            "the upstream computation that produced this literal "
            "lives in `q_parameter.py` (which derives `Q` from the "
            "figure-eight knot volume and the muon-electron mass "
            "ratio).  The pin is manually synchronised — when "
            "`q_parameter.Q` is regenerated at higher precision, "
            "`derivation_chain.Q_0` must be updated to match."
        ),
        inputs=["q_0_axiom"],
        output_name="q_0_anchor",
        output_value=Q_0,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§Substrate-anchors",
        jet_order=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            "script: computations/q_parameter.py.  "
            "This SCRIPT_CITED step is the open frontier of the "
            "chain — the candidate derivations on the horizon are "
            "(A) closure of the α-FSC ↔ q_0 algebraic relation via "
            "`alpha_em_pslq_uniqueness.py` at higher precision, "
            "(B) inversion of the m_p/m_e mass-endomorphism tower, "
            "(C) a brane-tower topological invariant (e.g. a "
            "canonical-knot hyperbolic volume).  None has produced "
            "a closed form to date; this anchor remains the source "
            "of truth and every prediction inherits its precision."
        ),
    ))

    # 3 — Computational leaf
    steps.append(DerivationStep(
        name="q_0 leaf evaluation",
        operation=(
            "Bit-stable evaluation of the canonical `Q_0` literal "
            "from step 2.  Validator cross-check is exact equality."
        ),
        inputs=["q_0_anchor"],
        output_name="q_0_value",
        output_value=Q_0,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
    ))

    return DerivationChain(
        target="q_0",
        target_value=Q_0,
        target_tolerance=1e-15,
        content_block="def:substrate-parameter-planck",
        description=(
            "Substrate-parameter anchor chain.  Records the current "
            f"q_0 ≈ {Q_0:.6g} as a `script-cited` debt against "
            "`q_parameter.py` and pins the value via the AXIOM "
            "`def:substrate-parameter-planck`.  Trust profile "
            "{axiom: 1, script-cited: 1, computational: 1} — **not "
            "fully-trusted by design**: the SCRIPT_CITED frontier "
            "remains open until one of the three candidate "
            "derivations (α-FSC PSLQ closure, m_p/m_e tower "
            "inversion, brane-tower volume conjecture) lands as a "
            "real script.  Replaces PR #481's "
            "`q0-derivation-skeleton` (which referenced two scripts "
            "that were never written and one whose 2000 dps variant "
            "was never landed)."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"q_0 anchor chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
