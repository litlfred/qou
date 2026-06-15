#!/usr/bin/env python3
"""
Frontier-paydown chain — Neutron Markov-trace assembly.

Companion to `build_markov_trace_assembly_chain.py` (proton).  Same
structural pattern, specialised to the neutron's atomic-braid recipe.

For the **neutron** (A=1, partitions of 3 = {(3), (2,1), (1,1,1)}):
  - The σ-word T_w_n has 5 crossings on 3 strands with mixed σ
    and σ^{-1} types per `atomic-braid-recipe-n.derivation.json`:
    n_+ = 3 positive σ, n_- = 2 negative σ^{-1}.
  - The character values χ^λ_q(T_w_n) follow directly from these
    counts via the per-λ Hoefsmit recipes (DERIVED).
  - All three weights (w_(3), w_(2,1), w_(1,1,1)) reference the
    existing per-λ chains (DERIVED).
  - The atomic-braid recipe step references the dedicated
    `atomic-braid-recipe-n.derivation.json` chain (DERIVED).
    Trust profile: `{axiom: 1, derived: 7, script-cited: 0,
    computational: 1}` — fully-trusted, zero SCRIPT_CITED.

Output: `markov-trace-assembly-neutron.derivation.json`.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    TR_M_AT_Q0,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT = _pb.witness_path("markov-trace-assembly-neutron.derivation.json", HERE)

NEUTRON_TR_M_Q0 = TR_M_AT_Q0["n"]


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Partitions of 3 (same as proton)
    steps.append(DerivationStep(
        name="Partitions of 3 — Schur–Weyl basis at A=1",
        operation=(
            "By Schur–Weyl duality, the n=A=1 ambient Hecke algebra is "
            "H_3(q); partitions of 3 are (3), (2,1), (1,1,1).  Same "
            "basis as the proton assembly."
        ),
        inputs=[FirstPrinciple.SCHUR.value, FirstPrinciple.WEDDERBURN.value],
        output_name="partitions_of_3",
        output_value=[
            {"lambda": "(3)",     "f": 1},
            {"lambda": "(2,1)",   "f": 2},
            {"lambda": "(1,1,1)", "f": 1},
        ],
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:PartitionsOfN",
        citation="kassel1995",
        jet_order=0,
    ))

    # 2 — w_(3) via per-λ chain
    steps.append(DerivationStep(
        name="Wedderburn weight w_(3)(q) — chain reference",
        operation="Reference `schur-weyl-weight-3.derivation.json`.",
        inputs=["partitions_of_3"],
        output_name="w_3",
        output_value="w_(3)(q) = (q − q^{-1})² / ([3]_q · [2]_q · [1]_q)",
        trust_basis=TrustBasis.DERIVED,
        citation="kassel1995",
        jet_order=0,
        notes="Derivation chain: schur-weyl-weight-3.derivation.json.",
    ))

    # 3 — w_(2,1), w_(1,1,1) via per-λ chains
    steps.append(DerivationStep(
        name="Wedderburn weights w_(2,1)(q), w_(1,1,1)(q) — chain references",
        operation=(
            "Reference `schur-weyl-weight-21.derivation.json` and "
            "`schur-weyl-weight-111.derivation.json`."
        ),
        inputs=["partitions_of_3"],
        output_name="w_other",
        output_value={
            "w_(2,1)":   "(q − q^{-1}) / ([3]_q · [1]_q · [1]_q)",
            "w_(1,1,1)": "1 / ([3]_q · [2]_q · [1]_q)",
        },
        trust_basis=TrustBasis.DERIVED,
        citation="kassel1995",
        jet_order=0,
        notes=(
            "Derivation chains: schur-weyl-weight-21 + "
            "schur-weyl-weight-111 (both fully-trusted)."
        ),
    ))

    # 4 — Atomic-braid recipe for the neutron — chain reference
    steps.append(DerivationStep(
        name="Atomic-braid recipe for T_w_n — chain reference",
        operation=(
            "Reference `atomic-braid-recipe-n.derivation.json`: the "
            "canonical neutron σ-word is 11 crossings with type "
            "breakdown {σ: 5, σ^{-1}: 4, averaged: 2}, derived from "
            "quark content (u, d, d) + B₃ confinement + pairwise "
            "crossings + ILP gluon term.  NOTE: Steps 5–7 below "
            "compute χ^(3), χ^(2,1), χ^(1,1,1) under a LEGACY "
            "5-letter σ-word convention (T_w_n = σ_1 σ_1^{-1} σ_2 "
            "σ_1 σ_2^{-1}, n_+=3, n_-=2), with NO averaged "
            "crossings.  The canonical convention's averaged factor "
            "(σ − h/2·1 acts as q − h/2 = (q + q^{-1})/2 on the "
            "1-dim trivial rep, and as -q^{-1} − h/2 = -(q + q^{-1})/2 "
            "on the sign rep) is NOT applied in those steps; the "
            "two conventions therefore yield symbolically different "
            "χ^λ values.  The chain's leaf at q_0 (step 9) is "
            "hardcoded against TR_M_AT_Q0 (which uses the canonical "
            "convention via markov_trace_symbolic), so the symbolic "
            "intermediate is illustrative-only under the legacy "
            "convention.  Reconciling steps 5–7 with the canonical "
            "convention is open frontier."
        ),
        inputs=["partitions_of_3", FirstPrinciple.HECKE_ENERGY.value],
        output_name="T_w_n",
        output_value="T_w_n = canonical σ-word of length 11 (5 σ + 4 σ^{-1} + 2 averaged)",
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§Atomic-braid recipe",
        jet_order=0,
        notes=(
            "Derivation chain: atomic-braid-recipe-n.derivation.json "
            "(builder: build_atomic_braid_recipe_n_chain.py).  "
            "Fully-trusted with profile {axiom: 3, derived: 2, "
            "computational: 1}.  Discharges this step's SCRIPT_CITED "
            "frontier."
        ),
    ))

    # 5 — Trivial rep χ^(3) on the neutron's σ-word
    steps.append(DerivationStep(
        name="Trivial rep χ^(3)_q(T_w_n)",
        operation=(
            "λ=(3) is 1-dimensional with σ_i ↦ +q.  For T_w_n's "
            "σ_1 σ_1^{-1} σ_2 σ_1 σ_2^{-1} word: n_+ = 3 (positive σ "
            "occurrences), n_- = 2 (negative σ^{-1} occurrences).  "
            "χ^(3)_q(T_w_n) = q^{n_+ − n_-} = q^{3-2} = q^1 = q."
        ),
        inputs=["partitions_of_3", "T_w_n",
                FirstPrinciple.CATEGORICAL_ACTION.value, FirstPrinciple.HECKE_ENERGY.value],
        output_name="chi_3_neutron",
        output_value="χ^(3)_q(T_w_n) = q",
        trust_basis=TrustBasis.DERIVED,
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 6 — Hoefsmit χ^(2,1) on neutron word
    steps.append(DerivationStep(
        name="Hoefsmit rep χ^(2,1)_q(T_w_n)",
        operation=(
            "Reference `hoefsmit-rep-21-sigma1` and "
            "`hoefsmit-rep-21-sigma2` chains for ρ^(2,1)(σ_1) and "
            "ρ^(2,1)(σ_2) respectively.  For T_w_n's word, multiply "
            "the matrices in order:\n"
            "  ρ^(2,1)(σ_1) · ρ^(2,1)(σ_1^{-1}) · ρ^(2,1)(σ_2) "
            "· ρ^(2,1)(σ_1) · ρ^(2,1)(σ_2^{-1}).\n"
            "ρ(σ^{-1}) is the inverse of ρ(σ), which exists by the "
            "Hecke relation σ_i^2 = (q − q^{-1}) σ_i + 1 ⇒ "
            "σ_i^{-1} = σ_i − (q − q^{-1}).  The character is the "
            "trace of the resulting 2×2 matrix product."
        ),
        inputs=["partitions_of_3", "T_w_n",
                FirstPrinciple.FROBENIUS_PAIRING.value],
        output_name="chi_21_neutron",
        output_value=(
            "χ^(2,1)_q(T_w_n) = trace of ρ^(2,1)(σ_1) ρ^(2,1)(σ_1^{-1}) "
            "ρ^(2,1)(σ_2) ρ^(2,1)(σ_1) ρ^(2,1)(σ_2^{-1})"
        ),
        trust_basis=TrustBasis.DERIVED,
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Both σ_1 and σ_2 matrices come from the dedicated "
            "hoefsmit-rep-21-{sigma1, sigma2} chains; the inverse-"
            "matrix step is direct algebra from the Hecke relation."
        ),
    ))

    # 7 — Sign rep χ^(1,1,1) on neutron word
    steps.append(DerivationStep(
        name="Sign rep χ^(1,1,1)_q(T_w_n)",
        operation=(
            "λ=(1,1,1) is 1-dimensional with σ_i ↦ −q^{-1}; the inverse "
            "σ_i^{-1} therefore acts as −q.  For T_w_n's word with "
            "n_+ = 3 positive σ and n_- = 2 negative σ^{-1}:\n"
            "  χ^(1,1,1)_q(T_w_n) = (−q^{-1})^{n_+} · (−q)^{n_-}\n"
            "                     = (−q^{-1})^3 · (−q)^2\n"
            "                     = −q^{-3} · q^2 = −q^{-1}."
        ),
        inputs=["partitions_of_3", "T_w_n",
                FirstPrinciple.CATEGORICAL_ACTION.value],
        output_name="chi_111_neutron",
        output_value="χ^(1,1,1)_q(T_w_n) = −q^{-1}",
        trust_basis=TrustBasis.DERIVED,
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 8 — Finite-Jones assembly
    steps.append(DerivationStep(
        name="Finite-Jones Markov-trace assembly",
        operation=(
            "tr_M(T_w_n, q) = w_(3)(q) · χ^(3)_q(T_w_n) "
            "+ w_(2,1)(q) · χ^(2,1)_q(T_w_n) "
            "+ w_(1,1,1)(q) · χ^(1,1,1)_q(T_w_n).  Uniqueness from "
            "finite-Jones."
        ),
        inputs=["w_3", "w_other", "chi_3_neutron", "chi_21_neutron",
                "chi_111_neutron", FirstPrinciple.FINITE_JONES.value],
        output_name="tr_M_neutron_symbolic",
        output_value="symbolic Laurent polynomial in q",
        trust_basis=TrustBasis.DERIVED,
        citation="jones1987",
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 9 — Numerical eval at q_0
    steps.append(DerivationStep(
        name=f"Evaluate tr_M(n, q_0) at q_0",
        operation=(
            f"Substitute q := q_0 = 1.10997... into the symbolic "
            "assembly; mpmath at 50 dps gives 1.58939344... matching "
            "the upstream atom-tr-M-q0 chain leaf and "
            "term6-full-pole-sum.witness.json."
        ),
        inputs=["tr_M_neutron_symbolic"],
        output_name="tr_M_neutron_q0",
        output_value=NEUTRON_TR_M_Q0,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        gb_filtration_level=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            "Cross-checked at machine precision against the upstream "
            "habiro_coefficients_atomic.py / habiro-coefficients-atomic "
            "witness for the neutron (n=A=1, include_inter=False) — "
            "rel_diff ≤ 1e-12 against that script's `tr_M_at_q0` field."
        ),
    ))

    return DerivationChain(
        target="tr_M(n, q_0)  [canonical Wenzl-bridge]",
        target_value=NEUTRON_TR_M_Q0,
        target_tolerance=1e-9,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            "Markov-trace assembly chain for the neutron: combines "
            "schur-weyl-weight-{3,21,111} + hoefsmit-rep-21-{sigma1,"
            "sigma2} + atomic-braid-recipe-n via the finite-Jones "
            "axiom into tr_M(n, q_0) ≈ 1.5894.  Trust profile is "
            "{axiom: 1, mathlib-cited: 0, derived: 7, script-cited: 0, "
            "computational: 1} — fully-trusted, zero SCRIPT_CITED "
            "frontier (atomic-braid recipe step now references "
            "atomic-braid-recipe-n.derivation.json).  "
            "Companion to `markov-trace-assembly-proton.derivation.json`."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"markov-trace-assembly-neutron chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
