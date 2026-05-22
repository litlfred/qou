#!/usr/bin/env python3
"""Strategy F (alternative to D, from agent brief
`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`):
test the Markov-trace identity directly on β_Bor in H_3(q).

Hypothesis under test:

    λ_scale  =  |tr_M(β_Bor, q_0)| · ℏ_q² / Vol(𝓑_3)

where β_Bor = (σ_1^{-1} σ_2)^3 ∈ B_3 ⊆ H_3(q) is the canonical
6-crossing Borromean braid word whose link closure is the
Borromean rings 𝓑_3.

If this identity holds, λ_scale is structurally pinned by the
Markov-trace formalism — no PSLQ search, no LP/SDP, no Bring-Bloch
detour. The Markov trace `tr_M(β) = Σ_{λ ⊢ n} y_λ(q) · χ^λ(β)`
is the canonical Hecke pairing fully derivable from the substrate
(q_0, m_e); a match would close Migration Backlog #1.

This script is the "highest-leverage" check in §"Alternatives to
Strategy D" — single 5-min compute, instant verdict.

If the identity FAILS (the two formalisms disagree), the gap
itself is structurally informative: λ_scale := correction-factor
between Markov-trace formalism and Vol-form formalism, and that
correction is the actual research target.

Per brief, neither result resolves Strategy D's role — it just
tells us whether Strategy F is enough on its own.
"""
from __future__ import annotations
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from hecke_character_symbolic import q_character_on_braid_word  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402

mp.mp.dps = 80


def beta_bor_crossings() -> list:
    """β_Bor = (σ_1^{-1} σ_2)^3 — six crossings, three (σ_1^{-1}, σ_2) pairs.

    Gen-index is 0-based (σ_1 → 0, σ_2 → 1). cross_d is "sigma_inv"
    for σ_k^{-1} and "sigma" for σ_k.
    """
    return [(0, "sigma_inv"), (1, "sigma")] * 3


def main() -> int:
    w = WitnessBuilder(
        "lambda-scale-alt-f-markov-trace-beta-bor",
        engine="mpmath+sympy",
    )
    w.set_description(
        "Strategy F: test the identity λ_scale = |tr_M(β_Bor, q_0)| · "
        "ℏ_q² / Vol(𝓑_3) where β_Bor = (σ_1^{-1} σ_2)^3 ∈ H_3(q). "
        "Direct Markov-trace evaluation; no PSLQ, no LP/SDP. Witness "
        "compares structural Markov-trace value to the CODATA-closure "
        "λ_p target 2.4599527869 and reports relative diff."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    w.add_parameter("dps", 80)
    w.add_parameter("braid_word", "(sigma_1^-1 sigma_2)^3")
    w.add_parameter("braid_group", "B_3 subset of H_3(q)")

    q = sp.Symbol("q", positive=True, real=True)
    Q0 = mp.mpf(Q_50_DIGIT_STR)
    HBAR = (Q0 - 1) / Q0
    VOL_B3 = 8 * mp.catalan  # = Vol(Borromean rings complement), Adams 1985

    print(f"q_0       = {mp.nstr(Q0, 20)}")
    print(f"ℏ_q       = (q_0 - 1)/q_0 = {mp.nstr(HBAR, 20)}")
    print(f"ℏ_q²      = {mp.nstr(HBAR**2, 20)}")
    print(f"Vol(𝓑_3) = 8·G = {mp.nstr(VOL_B3, 20)}")
    print()
    print("Computing tr_M(β_Bor) = Σ_{λ ⊢ 3} y_λ(q_0) · χ^λ(β_Bor):")
    print()

    crossings = beta_bor_crossings()
    print(f"  β_Bor crossings (gen, type): {crossings}")
    print()

    partitions_of_3 = [(3,), (2, 1), (1, 1, 1)]
    tr_M = mp.mpf("0")
    contributions = {}

    for shape in partitions_of_3:
        chi_sym = q_character_on_braid_word(list(shape), crossings, q)
        chi_at_q0 = mp.mpf(str(sp.N(chi_sym.subs(q, sp.Float(str(Q0), 80)), 80)))
        y_lam = y_lambda_wenzl_bridge_numeric(list(shape), Q0, dps=80)
        contrib = y_lam * chi_at_q0
        tr_M += contrib

        shape_label = "".join(str(p) for p in shape)
        print(f"  λ = {shape}:")
        print(f"      y_λ(q_0)       = {mp.nstr(y_lam, 16)}")
        print(f"      χ^λ(β_Bor,q_0) = {mp.nstr(chi_at_q0, 16)}")
        print(f"      product        = {mp.nstr(contrib, 16)}")
        contributions[shape_label] = {
            "y_lambda": mp.nstr(y_lam, 20),
            "chi_lambda_beta_bor": mp.nstr(chi_at_q0, 20),
            "product": mp.nstr(contrib, 20),
        }

    print()
    print(f"tr_M(β_Bor, q_0) = {mp.nstr(tr_M, 20)}")
    abs_trM = abs(tr_M)
    print(f"|tr_M(β_Bor, q_0)| = {mp.nstr(abs_trM, 20)}")
    print()

    candidate = abs_trM * HBAR ** 2 / VOL_B3
    target = mp.mpf("2.4599527869")

    rel_diff = (candidate - target) / target
    rel_ppm = rel_diff * mp.mpf("1e6")

    print(f"candidate (|tr_M|·ℏ_q²/Vol(𝓑_3)) = {mp.nstr(candidate, 20)}")
    print(f"target λ_p                       = {mp.nstr(target, 20)}")
    print(f"diff                             = {mp.nstr(candidate - target, 10)}")
    print(f"rel diff                         = {mp.nstr(rel_diff, 10)}")
    print(f"rel diff (ppm)                   = {mp.nstr(rel_ppm, 8)}")
    print()

    rel_thresh_ppb = mp.mpf("1e-9")
    rel_thresh_ppm = mp.mpf("1e-6")

    if abs(rel_diff) < rel_thresh_ppb:
        verdict = "MATCH-1ppb"
    elif abs(rel_diff) < rel_thresh_ppm:
        verdict = "MATCH-1ppm"
    elif abs(rel_diff) < mp.mpf("0.01"):
        verdict = "CLOSE-but-not-exact (<1%)"
    elif abs(rel_diff) < mp.mpf("0.1"):
        verdict = "FAR (>1%, <10%)"
    else:
        verdict = "FAR (>10%)"

    print(f"VERDICT: {verdict}")
    if verdict.startswith("MATCH"):
        print("  -> Strategy F succeeds: λ_scale is pinned by Markov-trace identity.")
    else:
        print(
            "  -> Strategy F FAILS or only approximate; the gap itself is the "
            "structural research target (representation-translation factor "
            "between Markov-trace and Vol-form formalisms)."
        )

    w.add_data("beta_bor_crossings", str(crossings))
    w.add_data("Vol_B3", mp.nstr(VOL_B3, 30))
    w.add_data("hbar_q_squared", mp.nstr(HBAR ** 2, 30))
    w.add_data("contributions_by_partition", contributions)
    w.add_data("tr_M_beta_bor_q0", mp.nstr(tr_M, 30))
    w.add_data("abs_tr_M_beta_bor_q0", mp.nstr(abs_trM, 30))
    w.add_data("candidate_lambda_scale", mp.nstr(candidate, 30))
    w.add_data("target_lambda_p", mp.nstr(target, 30))
    w.add_data("rel_diff", mp.nstr(rel_diff, 20))
    w.add_data("rel_diff_ppm", mp.nstr(rel_ppm, 10))
    w.add_data("verdict", verdict)

    w.add_assertion(
        "strategy_f_markov_trace_identity_holds",
        computed=mp.nstr(candidate, 12),
        expected=mp.nstr(target, 12),
        tolerance=str(float(rel_thresh_ppm)),
        source="Markov-trace formula tr_M(β) = Σ_λ y_λ · χ^λ(β) at H_3(q_0)",
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
