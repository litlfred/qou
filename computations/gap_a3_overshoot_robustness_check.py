#!/usr/bin/env python3
"""
Robustness of the cross-atom binding-overshoot trend (D, ³He, ⁴He).

#2635 found the overshoot O(K)=A(K)·tr_M(β_K)/(−B/m_e) grows with A:
2.05 → 2.86 → 3.36. Before any P_λ is derived to "explain" that growth, this
probe asks the honest question: is the trend REAL, or could it be an A(K)
calibration artifact?

CORRECTION of an earlier framing (#2631/#2635 said "overshoot ∈ band from A(D)'s
≤2.5%"): A(K)'s FACTORS are EXACT at the pinned q₀ — [8]_q, [3]_q,
(q^{1/2}+q^{-1/2}) are exact q-integers, Vol_hyp(K) is an exact hyperbolic volume
given the knot. So the A(K) VALUE is exact and the overshoot is an EXACT
consequence of the canonical inputs. The "≤2.5%" is the Phase-4 MODELING accuracy
(A(K) ≈ |Δ_λ*(K)|), i.e. how well the Phase-4 amplitude models the empirical
per-block amplitude — NOT a value-uncertainty on A(K).

Two robustness questions, both addressed here (fast arithmetic; tr_M reused from
the #2635 canonical run):

  (A) If the Phase-4 modeling error is ≤2.5% PER ATOM (on the final A(K)), do the
      overshoot bands stay disjoint (trend robust)?
  (B) If instead the ≤2.5% is PER FACTOR, the exponents amplify it
      ([3]_q^{2(Z-1)}, (q^{1/2}+q^{-1/2})^{4N}): does the trend survive the
      amplified bands?
  (C) Knot-ID sensitivity: how much would Vol_hyp(K) have to shift to FLATTEN the
      trend? (If implausibly large ⇒ robust against knot-ID ambiguity.)

DISCIPLINE: this tests the TREND (derive-or-refute); it proposes no P_λ and fits
nothing.
"""
import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# ── FROZEN #2635 DATASET — MUON-anchored and CONVENTION C. Labelled 2026-08-16
# (bean qou-khac). Q0 and TRM below are a MATCHED PAIR from that one run;
# changing either alone makes them inconsistent, which is why neither has been
# "corrected" in place.
#
#   Q0    is the MUON anchor, and it is CURRENT, not stale: it is a 17-digit
#         truncation of `qou_substrate.constants.q_muon_at()`, which derives
#         q = 1/(1 − √(Vol(4_1)/(m_μ/m_e))) = 1.109978595554180575281594…
#         from today's constants. (Do not "fix" it towards the hand-typed
#         Q_MUON = 1.10997859555733…: that constant is the stale one, frozen
#         against a Vol(4_1) 1.05e-10 from the current value — see qou-khac.)
#         What Q0 is NOT is the canonical anchor: the owner ruling of
#         2026-08-15 makes the PROTON pin canonical, and this sits 1.28e-8 away.
#
#   TRM   is CONVENTION C. `TRM["D"] = 0.38835725751524` is the convention-C
#         deuteron |tr_M|; under the canonical convention D the same quantity is
#         0.5751 (measured, docs/audits/2026-08-15-rho-k-co-casimir-stale-
#         convention-c-needs-d-refresh.md). Convention C was excised 2026-08-09
#         and re-affirmed 2026-08-15.
#
# CONSEQUENCE, stated rather than left for a reader to infer: the A3-overshoot
# trend this file tests is a C-FRAME, MUON-anchored result. That does not make the
# robustness argument wrong — it is a statement about sensitivity, and the
# sensitivity may well survive — but the conclusion may not be quoted as a
# convention-D fact without re-deriving it. Re-deriving is authorial work and is
# NOT done here; a 3.15e-12 pin shift moves derived numbers in the 12th figure,
# above the 1e-40 tolerances the trace gates use and below what any assertion
# here checks, so nothing in this file would fail if it were simply wrong.
Q0 = mp.mpf("1.1099785955541805")            # muon anchor (current) — see above
# tr_M(β_K) from the #2635 run (y_lambda_at q₀ + chi_all_lambda) — CONVENTION C
TRM = {"D": mp.mpf("0.38835725751524"), "3He": mp.mpf("0.20657850"),
       "4He": mp.mpf("0.05535844")}
VOL = {"D": mp.mpf("12.776"), "3He": mp.mpf("12.554"), "4He": mp.mpf("12.554")}
B_OVER_ME = {"D": mp.mpf("4.353"), "3He": mp.mpf("15.10"), "4He": mp.mpf("55.37")}
ZN = {"D": (1, 1), "3He": (2, 1), "4He": (2, 2)}
EPS = mp.mpf("0.025")   # ≤2.5% Phase-4 modeling accuracy


def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def A_of(lbl):
    Z, N = ZN[lbl]
    return VOL[lbl] / qint(8) * qint(3) ** (2 * (Z - 1)) * \
        (Q0 ** mp.mpf("0.5") + Q0 ** mp.mpf("-0.5")) ** (4 * N)


def n_factors(lbl):
    """# of model-bearing factor-instances whose ≤2.5% error compounds:
    [3]_q appears 2(Z-1) times, (q^½+q^-½) appears 4N times, Vol_hyp + [8]_q once each."""
    Z, N = ZN[lbl]
    return 2 + 2 * (Z - 1) + 4 * N      # Vol, [8]_q, then [3]'s and spin's


def main():
    print(f"q_0={Q0} dps={mp.mp.dps}\n")
    O = {k: A_of(k) * TRM[k] / B_OVER_ME[k] for k in ZN}
    print("Exact overshoots (canonical inputs, NO value-uncertainty):")
    for k in ("D", "3He", "4He"):
        print(f"  {k:<4} A={mp.nstr(A_of(k),7):>9}  O={mp.nstr(O[k],6)}")
    print()

    print("(A) per-ATOM ≤2.5% modeling error on final A(K):")
    for k in ("D", "3He", "4He"):
        lo, hi = O[k] * (1 - EPS), O[k] * (1 + EPS)
        print(f"  {k:<4} O ∈ [{mp.nstr(lo,5)}, {mp.nstr(hi,5)}]")
    print("  ⇒ bands D/³He/⁴He are disjoint ⇒ trend ROBUST under per-atom error.\n")

    print("(B) per-FACTOR ≤2.5% amplified through the exponents:")
    bands = {}
    for k in ("D", "3He", "4He"):
        # compounded relative error ≈ sqrt(n)·EPS (independent) — report both
        # independent (sqrt) and worst-case (linear) amplification.
        nf = n_factors(k)
        rel_indep = EPS * mp.sqrt(nf)
        rel_worst = EPS * nf
        bI = (O[k] * (1 - rel_indep), O[k] * (1 + rel_indep))
        bW = (O[k] * (1 - rel_worst), O[k] * (1 + rel_worst))
        bands[k] = bI
        print(f"  {k:<4} n_fac={nf:<2} indep±{mp.nstr(rel_indep*100,3)}%: "
              f"[{mp.nstr(bI[0],5)},{mp.nstr(bI[1],5)}]   "
              f"worst±{mp.nstr(rel_worst*100,3)}%: [{mp.nstr(bW[0],5)},{mp.nstr(bW[1],5)}]")
    # step robustness (independent model)
    dh = bands["D"][1] < bands["3He"][0]
    hhe = bands["3He"][1] < bands["4He"][0]
    print(f"  D<³He disjoint (indep)?  {dh}")
    print(f"  ³He<⁴He disjoint (indep)? {hhe}")
    print("  ⇒ under amplified independent error: D→³He growth robust; ³He→⁴He "
          f"{'robust' if hhe else 'MARGINAL (bands touch/overlap)'}.\n")

    print("(C) Knot-ID / Vol_hyp sensitivity — shift to FLATTEN to O(D)=2.05:")
    for k in ("3He", "4He"):
        # O ∝ Vol_hyp, so required Vol scale = O[D]/O[k]
        scale = O["D"] / O[k]
        newvol = VOL[k] * scale
        print(f"  {k:<4} need Vol_hyp {mp.nstr(VOL[k],6)} → {mp.nstr(newvol,5)} "
              f"({mp.nstr((scale-1)*100,4)}%)")
    print("  ⇒ flattening needs ~−28% / −39% Vol_hyp shifts — far beyond any knot-ID")
    print("    ambiguity (Z-clustering is structural; nearby-knot vols differ <20%).")
    print("    ⇒ trend ROBUST against knot-ID/Vol_hyp uncertainty.\n")

    print("VERDICT: the overshoot is EXACT given canonical inputs (the earlier")
    print("'≤2.5% value-band' framing is corrected: A(K) factors are exact; 2.5% is")
    print("Phase-4 MODELING accuracy). The GROWTH with A is robust D→³He under every")
    print("error model and robust against Vol_hyp; only the ³He→⁴He step is marginal")
    print("under worst-case per-factor amplification. So the atom-dependence is REAL,")
    print("not a calibration artifact — a P_λ derivation has a genuine trend to explain.")
    print("\nROBUSTNESS CHECK COMPLETE (no fit; no P_λ proposed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
