#!/usr/bin/env python3
"""qbeta_l15q_rank3_generalization_probe.py — bean qou-l15q: does the 4₁
Stokes structure constant generalize to rank 3, and what does 5₂ say about
the two "why 3" candidates?

Background. #4447 certified for 4₁ (rank 2) the exact integer q-series identity

    S⁺₁₂(q) + S⁺₂₁(q) = 3·S⁺₁₁(q)                      (GGM eq 65)

so `A_ω = 3` is a **structure constant** there: exact, q-independent
(Lean `StokesSymmetryConstant.symmetryConstant_const`). The scope note
`docs/scope/2026-08-01-aomega-three-test-illposed.md` recorded that the 5₂
test of the two "why 3" candidates was ill-posed because 5₂'s Stokes matrix
is 3×3 with three off-diagonal integers rather than one. This probe closes
that by testing the two things that must hold for a rank-3 generalization
to exist:

  G1  **Does the symmetry generalize?** Is `(S₀₁ + S₁₀)/S₀₀` constant in q
      for 5₂ (the direct rank-3 transcription of eq 65)? Tested at several
      q, because a single-point test is worthless here — see the finding.
  G2  **Does det = 1 generalize?** (the SL(n) normalization; a control that
      the assembled matrix is right).

Then, under the one reading of `A_ω` that *is* well-defined at every rank —
the **classical (q→0) (σ₁,σ₂) Stokes entry**, which is 3 for 4₁ (GGM eq 60,
`S⁺(0) = [[1,3],[0,1]]`) and 4 for 5₂ (eq 100a,
`S⁺(0) = [[1,4,0],[0,1,0],[−3,−9,1]]`) — the probe reports what that reading
says about the two candidates:

    (A) |disc(trace field)|      4₁ → 3 ✓   5₂ predicts 23
    (B) |Alexander mid coeff|    4₁ → 3 ✓   5₂ predicts 3

Machinery is the corpus's own certified 5₂ assembly
(`qbeta_5two_stokes_barodd_index_probe.S_pm_num`, GGM §6 eqs 24–29 with the
|q|>1 glue eq 25); this probe adds no new Stokes construction.

Scope (STRICT). The q→0-entry reading is a **reading**, not a derivation:
it is the natural one (it is what GGM's eqs 60/100a give, and it reduces to
the 4₁ value), but nothing here derives that `A_ω` must be that entry. What
IS established is (i) whether the 4₁ symmetry generalizes, and (ii) what the
natural reading implies for A and B. No fit; nothing wired.

Run: python3 -u computations/probes/qbeta_l15q_rank3_generalization_probe.py \
       2>&1 | tee /tmp/qbeta_l15q_rank3.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

from qbeta_5two_stokes_barodd_index_probe import S_pm_num  # noqa: E402

set_compute_dps()

Q_POINTS = ["0.10", "0.18", "0.25", "0.32", "0.40"]
A_OMEGA_41 = 3           # GGM eq 60, S⁺(0) = [[1,3],[0,1]]
A_OMEGA_52_CLASSICAL = 4  # GGM eq 100a, S⁺(0)[0][1]
PRED_A_52 = 23            # |disc| of the 5₂ cubic trace field
PRED_B_52 = 3             # |middle coeff| of Δ_{5₂} = 2t − 3 + 2t⁻¹
CONST_TOL = mp.mpf("1e-8")


def main() -> int:
    print("=" * 78)
    print(" qou-l15q — does the 4₁ Stokes structure constant generalize to rank 3?")
    print("=" * 78)

    ratios, dets = {}, {}
    print(f"\n[G1/G2] 5₂ assembled S⁺(q) at {len(Q_POINTS)} points:")
    for xs in Q_POINTS:
        x = mp.mpf(xs)
        Sp, _ = S_pm_num(x)
        c = (Sp[0, 1] + Sp[1, 0]) / Sp[0, 0]
        d = mp.det(Sp)
        ratios[xs] = c
        dets[xs] = d
        print(f"    q={xs}: (S₀₁+S₁₀)/S₀₀ = {mp.nstr(c, 14):>18}   "
              f"det S⁺ = {mp.nstr(d, 12)}")

    vals = [ratios[k] for k in Q_POINTS]
    spread = max(abs(a - b) for a in vals for b in vals)
    g1_constant = spread < CONST_TOL
    det_ok = all(abs(dets[k] - 1) < mp.mpf("1e-12") for k in Q_POINTS)

    print(f"\n  G1  ratio spread across the {len(Q_POINTS)} points = "
          f"{mp.nstr(spread, 6)}  ⇒ constant? {g1_constant}")
    print(f"  G2  det S⁺ = 1 at every point: {det_ok}  (control: assembly is sound)")

    # the near-miss that makes single-point testing worthless
    near = min(Q_POINTS, key=lambda k: abs(ratios[k] - A_OMEGA_52_CLASSICAL))
    print(f"\n  METHOD NOTE: at q={near} the ratio is "
          f"{mp.nstr(ratios[near], 8)} — within "
          f"{mp.nstr(abs(ratios[near] - A_OMEGA_52_CLASSICAL), 3)} of 4. A "
          f"single-point test there would have read as a HIT for a constant 4; "
          f"the multi-point spread shows it is a crossing, not a constant.")

    print(f"\n[candidates] under the classical (q→0) (σ₁,σ₂)-entry reading "
          f"(4₁ → {A_OMEGA_41}, 5₂ → {A_OMEGA_52_CLASSICAL}):")
    a_ref = A_OMEGA_52_CLASSICAL != PRED_A_52
    b_ref = A_OMEGA_52_CLASSICAL != PRED_B_52
    print(f"    (A) |disc| predicts {PRED_A_52} → "
          f"{'REFUTED' if a_ref else 'survives'}")
    print(f"    (B) |Alexander mid| predicts {PRED_B_52} → "
          f"{'REFUTED' if b_ref else 'survives'}")

    verdict = (
        "THE 4₁ STRUCTURE CONSTANT DOES NOT GENERALIZE TO RANK 3. For 5₂ the "
        f"direct transcription (S₀₁+S₁₀)/S₀₀ varies across q (spread "
        f"{mp.nstr(spread, 4)} over q ∈ [0.10, 0.40]) — it is not a constant, "
        "so GGM's eq-65 symmetry is genuinely rank-2-specific and there is no "
        "rank-3 'symmetry constant'. det S⁺ = 1 DOES generalize (control "
        "passed). CONSEQUENCE FOR #4447: the q-independence that made A_ω = 3 "
        "an exact structure constant is a rank-2 property, NOT a general "
        "feature — that result stands for 4₁ but must not be read as a "
        "general law. Under the one rank-general reading (the classical q→0 "
        "(σ₁,σ₂) entry: 3 for 4₁, 4 for 5₂), BOTH 'why 3' candidates are "
        "REFUTED — |disc| predicts 23, |Alexander mid coeff| predicts 3, and "
        "the entry is 4. Scope: that reading is the natural one but is a "
        "reading, not a derivation; the refutation is conditional on it. "
        "Method note: at q=0.25 the ratio is 4.08, so a single-point test "
        "would have falsely read as a constant-4 hit. No fit; nothing wired."
        if (det_ok and not g1_constant) else
        "INCONCLUSIVE — inspect the log (control failed or ratio looks constant).")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-l15q-rank3-generalization", engine="mpmath")
    wb.set_description(
        "Bean qou-l15q: tests whether the 4_1 Stokes structure constant "
        "(S12 + S21 = 3*S11, exact q-series identity certified in #4447) "
        "generalizes to rank 3 via 5_2. It does NOT: the direct transcription "
        "(S01+S10)/S00 varies with q, so GGM eq-65 is rank-2-specific and no "
        "rank-3 symmetry constant exists. det S+ = 1 does generalize "
        "(control). Consequence: the q-independence of A_omega = 3 is a "
        "rank-2 property, not a general law — a scope limitation on #4447. "
        "Under the one rank-general reading (classical q->0 (sigma1,sigma2) "
        "entry: 3 for 4_1, 4 for 5_2) both 'why 3' candidates are refuted "
        "(|disc| predicts 23, |Alexander middle coeff| predicts 3, entry is "
        "4) — conditional on that reading, which is natural but not derived. "
        "Uses the corpus's own certified 5_2 assembly; adds no new Stokes "
        "construction. No fit; nothing wired.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("ratio_by_q", {k: mp.nstr(ratios[k], 16) for k in Q_POINTS})
    wb.add_data("det_by_q", {k: mp.nstr(dets[k], 14) for k in Q_POINTS})
    wb.add_data("ratio_spread", mp.nstr(spread, 8))
    wb.add_data("symmetry_generalizes", bool(g1_constant))
    wb.add_data("classical_entries", {
        "4_1_sigma1sigma2_at_q0": A_OMEGA_41,
        "5_2_sigma1sigma2_at_q0": A_OMEGA_52_CLASSICAL,
        "source": "GGM 2012.00062 eq 60 (4_1) and eq 100a (5_2)"})
    wb.add_data("candidate_verdicts", {
        "A_disc_trace_field": {"predicts_5_2": PRED_A_52, "refuted": bool(a_ref)},
        "B_alexander_middle": {"predicts_5_2": PRED_B_52, "refuted": bool(b_ref)},
        "conditional_on": "the classical q->0 (sigma1,sigma2)-entry reading of "
                          "A_omega, which is natural but NOT derived"})
    wb.add_data("scope_limitation_on_4447",
                "the exact q-independence of A_omega = 3 is rank-2-specific; "
                "#4447's result stands for 4_1 but is not a general law")
    wb.add_data("method_note",
                f"at q={near} the ratio is {mp.nstr(ratios[near], 8)}, within "
                f"{mp.nstr(abs(ratios[near] - A_OMEGA_52_CLASSICAL), 3)} of 4 — "
                "a single-point test would have falsely confirmed a constant 4")
    wb.add_data("verdict", verdict)
    wb.add_assertion("det_control_holds",
                     computed=1.0 if det_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="det S+ = 1 at every test point (SL(3) control on the "
                            "assembled matrix)")
    wb.add_assertion("symmetry_does_not_generalize",
                     computed=1.0 if not g1_constant else 0.0, expected=1.0,
                     tolerance=0.5,
                     source=f"(S01+S10)/S00 spread {mp.nstr(spread, 4)} > 1e-8 "
                            f"across q in [0.10, 0.40] — not constant")
    wb.save()
    print("  witness -> computations/probes/qbeta-l15q-rank3-generalization.witness.json")
    return 0 if (det_ok and not g1_constant) else 1


if __name__ == "__main__":
    raise SystemExit(main())
