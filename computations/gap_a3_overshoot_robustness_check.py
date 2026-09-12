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
# ── MIGRATED TO CONVENTION D AT THE PROTON PIN, 2026-09-12 (bean qou-46ys) ──
#
# WHAT THIS REPLACED, and why the replacement is cheap rather than "authorial
# work" as the banner above claimed. The two literals below were:
#
#   Q0  = mp.mpf("1.1099785955541805")                      # MUON anchor
#   TRM = {"D": 0.38835725751524, "3He": 0.20657850,        # CONVENTION C
#          "4He": 0.05535844}
#
# The convention-D values at the proton pin were ALREADY COMMITTED, in
# `canonical-mass-table-extended.witness.json` (q0Anchor: proton, computed
# 2026-09-07, nine nuclides). So this is a READ, not a re-derivation, and it
# fixes the convention and the anchor in one move.
#
# INDEPENDENTLY REDERIVED BEFORE BEING TRUSTED. `tr_M = Σ_λ y_λ χ_λ`, and the
# `χ_λ` are representation characters -- INDEPENDENT of the Markov parameter, so
# only `y_λ` carries the convention. Recomputing from the committed 50-digit
# `χ_λ` in `atom-chi-rust-{d,3he,4he}.witness.json` against the convention-D
# weights `y_λ = [n-2k+1]_q/[2]_q^n` (ℓ(λ) ≤ 2; 0 otherwise) reproduces the
# table EXACTLY for all three -- 0.1519683392042316 / 0.05859625365443638 /
# 0.01123741765976742. Both live `y_λ` implementations
# (`y_lambda_su_n` and `regenerate_chi_atom_conventionD.y_lambda`) agree to 60
# dps, so there is no second convention-D weight in the corpus.
#
# 🛑 DO NOT CALIBRATE THIS AGAINST `docs/audits/2026-08-15-rho-k-co-casimir-
# stale-convention-c-needs-d-refresh.md`. That audit records the D deuteron as
# 0.5751, which was correct ON 2026-08-15 and is now STALE: the table was
# regenerated at the proton pin and the value moved to 0.15197. Calibrating
# against it reads as a failure of a correct computation -- it did here first.
#
# NOTE the swap IS legitimate here, unlike the c_k ladder. AGENTS.md warns that
# migrating the LADDER is "not a z-swap" because its offset mixes bar-weights.
# `tr_M = Σ_λ y_λ χ_λ` has no such coupling: `χ_λ` is convention-free, so
# substituting the D weights IS the rederivation.
import json as _json
from pathlib import Path as _Path

_TBL = _json.loads(
    (_Path(__file__).resolve().parent / "canonical-mass-table-extended.witness.json"
     ).read_text())
Q0 = mp.mpf(str(_TBL["q0Value"]))            # PROTON pin (owner ruling R2, 2026-08-15)
_BY_ZN = {(r["Z"], r["N"]): r["tr_M_q0_canonical_50dps"] for r in _TBL["data"]["rows"]}
# CONVENTION D, proton pin — read from the committed table, not hardcoded.
TRM = {lbl: mp.mpf(_BY_ZN[zn])
       for lbl, zn in (("D", (1, 1)), ("3He", (2, 1)), ("4He", (2, 2)))}
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
    # COMPUTED, not asserted. This line read "⇒ bands D/³He/⁴He are disjoint ⇒
    # trend ROBUST under per-atom error." unconditionally -- true in the
    # convention-C frame this file was written in, and printed regardless. Under
    # convention D the ordering INVERTS at ⁴He, so an unconditional "ROBUST"
    # would be prose contradicting the table three lines above it.
    _ba = {k: (O[k] * (1 - EPS), O[k] * (1 + EPS)) for k in ("D", "3He", "4He")}
    _mono_a = _ba["D"][1] < _ba["3He"][0] and _ba["3He"][1] < _ba["4He"][0]
    _ordered = O["D"] < O["3He"] < O["4He"]
    print(f"  monotone in A (point values)? {_ordered}"
          f"{'' if _ordered else f'  -- O(4He)={mp.nstr(O[chr(52)+chr(72)+chr(101)],5)} sits BELOW O(3He)' if O['4He'] < O['3He'] else ''}")
    print(f"  ⇒ bands D/³He/⁴He pairwise-increasing and disjoint? {_mono_a} ⇒ trend "
          f"{'ROBUST' if _mono_a else 'NOT ROBUST'} under per-atom error.\n")

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

    print(f"(C) Knot-ID / Vol_hyp sensitivity — shift to FLATTEN to "
          f"O(D)={mp.nstr(O['D'],4)}:")   # was hardcoded "2.05", the C-frame value
    for k in ("3He", "4He"):
        # O ∝ Vol_hyp, so required Vol scale = O[D]/O[k]
        scale = O["D"] / O[k]
        newvol = VOL[k] * scale
        print(f"  {k:<4} need Vol_hyp {mp.nstr(VOL[k],6)} → {mp.nstr(newvol,5)} "
              f"({mp.nstr((scale-1)*100,4)}%)")
    # COMPUTED against the file's OWN stated threshold. These three lines were
    # hardcoded as "~−28% / −39% ... far beyond any knot-ID ambiguity ...
    # ROBUST", which was the convention-C answer. The threshold the file itself
    # names is <20% (nearby-knot volumes), so test against that rather than
    # restating a conclusion.
    _KNOT_ID_TOL = mp.mpf("0.20")
    _shifts = {k: O["D"] / O[k] - 1 for k in ("3He", "4He")}
    _beyond = all(abs(v) > _KNOT_ID_TOL for v in _shifts.values())
    print(f"  ⇒ flattening needs "
          f"{' / '.join(mp.nstr(_shifts[k]*100, 4) + '%' for k in ('3He', '4He'))} "
          f"Vol_hyp shifts; the file's own knot-ID tolerance is "
          f"±{mp.nstr(_KNOT_ID_TOL*100,3)}% (nearby-knot vols).")
    print(f"    both beyond that tolerance? {_beyond} ⇒ trend "
          f"{'ROBUST' if _beyond else 'NOT ROBUST'} against knot-ID/Vol_hyp "
          f"uncertainty.\n")

    # ── VERDICT: COMPUTED, 2026-09-12 (bean qou-46ys) ────────────────────────
    # This block was six hardcoded print()s asserting "the overshoot is EXACT",
    # "the GROWTH with A is robust D→³He under every error model", and "the
    # atom-dependence is REAL, not a calibration artifact". Every one of those
    # was the convention-C / muon-anchor answer, and all three are FALSE under
    # the canonical convention D at the proton pin. They printed unconditionally.
    _overshoot = all(O[k] > 1 for k in ("D", "3He", "4He"))
    print("VERDICT (computed from the table above, not asserted):")
    print(f"  is there an OVERSHOOT at all (O > 1 for every atom)? {_overshoot}")
    if not _overshoot:
        print(f"    O = {', '.join(f'{k} {mp.nstr(O[k],5)}' for k in ('D','3He','4He'))}"
              " — all below 1, so this is an UNDERSHOOT. Under convention C at the"
              " muon anchor these read 2.05 / 2.86 / 3.36.")
    print(f"  monotone growth with A (point values)? {_ordered}")
    if not _ordered:
        print("    the A-trend INVERTS: ⁴He sits below ³He, so there is no monotone"
              " atom-dependence to explain.")
    print(f"  per-atom bands increasing and disjoint (A)? {_mono_a}")
    print(f"  amplified-error steps disjoint (B)? D→³He {dh}, ³He→⁴He {hhe}")
    print(f"  beyond the file's own knot-ID tolerance (C)? {_beyond}")
    print()
    if not (_overshoot and _ordered and _beyond):
        print("  ⇒ THE A3-OVERSHOOT TREND AND ITS ROBUSTNESS DO NOT SURVIVE THE")
        print("    CONVENTION MIGRATION. Both were convention-C, muon-anchored")
        print("    results. Under D at the proton pin there is no overshoot, the")
        print("    trend is non-monotone, and flattening needs Vol_hyp shifts")
        print("    INSIDE the ±20% knot-ID ambiguity this file itself cites.")
        print()
        print("  🛑 SCOPE-(a), NOT (b) (AGENTS.md §'Before declaring refuted'):")
        print("    this is one pin, one convention, one knot/Vol assignment and one")
        print("    error model. It refutes the trend AS COMPUTED HERE. It does NOT")
        print("    prove no atom-dependence exists — the Vol_hyp and B/m_e inputs")
        print("    are unchanged C-era assignments, and a D-consistent knot")
        print("    assignment has not been derived (that is bean qou-e5jf's arc).")
        print("    What is established is that the previous ROBUSTNESS argument")
        print("    fails on its own stated criterion.")
    else:
        print("  ⇒ the overshoot trend survives; see the per-criterion lines above.")
    print("\nROBUSTNESS CHECK COMPLETE (no fit; no P_λ proposed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
