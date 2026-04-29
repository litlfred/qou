#!/usr/bin/env python3
"""
Skeleton chain — σ_shell α_5 outer-scale derivation (SPECULATIVE).

Per `conj:shell-correction-term-seven`, σ_shell (Term 7) at A=2 has
a fully-trusted closed form `C_{(3,2,1)}(q)` (shipped via PR #476's
`sigma-shell-A2-closed-form.derivation.json`).  The remaining debt
is the outer empirical scale

    α_5 ≈ −4.2 × 10^5 MeV

obtained by fitting Term-7 residuals on A=1..4 isotopes
(`higher-a-shell-diagnostic.witness.json`).  The paper conjectures
that α_5 is derivable from substrate constants (q_0, ℏ_q, Catalan G)
without empirical fitting; this chain provides the structural
skeleton for that derivation, with the actual closed form **open**
and recorded as a SCRIPT_CITED step until established.

This is a **speculative** chain — it marks where the open work
lives without claiming a derivation that doesn't yet exist.  The
target_value is the empirical fit result; the trust profile shows
the debt explicitly.

Output: `sigma-shell-alpha5-skeleton.derivation.json`.
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
OUTPUT = HERE / "sigma-shell-alpha5-skeleton.derivation.json"

ALPHA_5_MEV_FIT = -4.2e5  # empirical fit result; target of this chain


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Substrate constants (anchor)
    steps.append(DerivationStep(
        name="Substrate constants q_0, ℏ_q, m_e",
        operation=(
            "Anchor inputs: substrate parameter q_0 ≈ 1.10997, derived "
            "constants ℏ_q := 1 − q^{-1} (per `def:hbar-q`) and "
            "M_E_MEV := 0.51099895 (CODATA electron mass).  α_5 should "
            "be expressible in terms of these by `conj:shell-correction-"
            "term-seven` step 'Status'."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name="substrate_constants",
        output_value={
            "q_0": Q_0,
            "hbar_q": 1.0 - 1.0 / Q_0,
            "m_e_MeV": 0.51099895,
        },
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:SubstrateConstants",
        citation="manuscript:§Substrate-anchors",
        jet_order=0,
    ))

    # 2 — Catalan-G constant (open analytic input)
    steps.append(DerivationStep(
        name="Catalan G constant",
        operation=(
            "Catalan G ≈ 0.9159655942...  Per the paper, α_5 conjecturally "
            "involves G as a transcendental factor.  G is well-defined "
            "as the special value of the L-function L(2, χ_4) for the "
            "non-trivial Dirichlet character mod 4; not derivable from "
            "the substrate constants in step 1.  Treated as an external "
            "mathematical constant (mathlib-cited)."
        ),
        inputs=["substrate_constants"],
        output_name="catalan_G",
        output_value=0.9159655941772190,
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:CatalanG",
        citation="manuscript:§Catalan-G",
        jet_order=0,
        notes=(
            "Mathlib's `Mathlib.NumberTheory.LSeries.Basic` could in "
            "principle define G via L(2, χ_4); not currently imported "
            "into the QOU package — qou:STUB: until the import lands."
        ),
    ))

    # 3 — Conjectured closed form (OPEN)
    steps.append(DerivationStep(
        name="Conjectured closed form for α_5 (OPEN)",
        operation=(
            "Per `conj:shell-correction-term-seven` step 'Status', the "
            "closed form for α_5 should derive from substrate constants "
            "via a formula schematic\n"
            "  α_5 = m_e · F(q_0, ℏ_q, G)\n"
            "for some analytic function F yet to be specified.  The "
            "Mayer/Jensen shell-model literature suggests F involves a "
            "residue at a height-6 pole of the GS spectral sequence "
            "(per `def:confinement-level` and the diagnostic in "
            "`higher-a-shell-diagnostic.witness.json`).\n\n"
            "**This step is SCRIPT_CITED with `script: TBD` because the "
            "closed form has not been derived yet.**  Until established, "
            "α_5 is the empirical fit value from the diagnostic witness."
        ),
        inputs=["substrate_constants", "catalan_G",
                FirstPrinciple.FROBENIUS_PAIRING.value],
        output_name="alpha5_closed_form",
        output_value="α_5 = m_e · F(q_0, ℏ_q, G) — F unspecified",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§sigma_shell-alpha5-conjecture",
        jet_order=0,
        gb_filtration_level=5,
        notes=(
            "script: folio-assistant/computations/higher_a_shell_diagnostic.py "
            "supplies the empirical α_5 fit; no closed-form derivation "
            "script exists yet.  This SCRIPT_CITED step is the **last "
            "open frontier** for σ_shell at A ≥ 4."
        ),
    ))

    # 4 — Numerical eval (empirical fit value)
    steps.append(DerivationStep(
        name="α_5 numerical value (empirical fit)",
        operation=(
            "From the BW-residual diagnostic on A=1..4 isotopes "
            "(`higher-a-shell-diagnostic.witness.json`), the best-fit "
            "level-5 coefficient is α_5 ≈ −4.2 × 10^5 MeV, with RMSE "
            "342 MeV across 4 isotopes.  Until step 3's closed form "
            "is established, this is the **only known value** of α_5; "
            "it functions as a COMPUTATIONAL leaf reading the "
            "diagnostic witness."
        ),
        inputs=["alpha5_closed_form"],
        output_name="alpha5_numerical",
        output_value=ALPHA_5_MEV_FIT,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        gb_filtration_level=5,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            "Empirical fit result.  Sign: negative — Term 7 is binding-"
            "enhancing at shell closures (matches ⁴He's doubly-magic "
            "anomaly).  When step 3's closed form is supplied, the "
            "trust basis here would be DERIVED via step 3, and the "
            "value would be a derived constant rather than fit data."
        ),
    ))

    return DerivationChain(
        target="α_5 (σ_shell outer scale, MeV)",
        target_value=ALPHA_5_MEV_FIT,
        target_tolerance=0.5,  # ±50% — empirical fit residual
        content_block="conj:shell-correction-term-seven",
        description=(
            "**Speculative skeleton chain** for the σ_shell outer scale "
            "α_5 ≈ −4.2 × 10^5 MeV.  Records the **open analytic "
            "derivation** as a SCRIPT_CITED step (no closed form "
            "established yet); the COMPUTATIONAL leaf reads the "
            "empirical fit from `higher-a-shell-diagnostic.witness.json`.  "
            "Trust profile {axiom: 1, mathlib-cited: 1, derived: 0, "
            "script-cited: 1, computational: 1} — **NOT fully-trusted**, "
            "and intentionally so.  When the closed form is derived "
            "(open work tracked in `conj:shell-correction-term-seven` "
            "step 'Status'), step 3 becomes DERIVED and the chain "
            "becomes fully-trusted."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"sigma-shell-alpha5 skeleton chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value} MeV (empirical fit)")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
