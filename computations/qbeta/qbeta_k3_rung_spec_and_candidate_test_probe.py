#!/usr/bin/env python3
"""Q_beta k=3: the SPEC a derived rung must meet, and the standing candidate FAILS it.

Option 1 of the L2 attack plan. Q_beta misses its 100x target by 164x, and
because m_n = m_p + Q_beta + m_e and Delta_pn = m_n - m_p, that one miss carries
three of the five scoreable observables. The dashboard names the cause: its
source is `Q_N2`, the ladder truncated at k=2.

FIRST, A CIRCULARITY I ALMOST REPORTED AS A DISCOVERY. Computing |c_3| * u^3
gives 1278.58 ppb against a dashboard error of 1278.58 ppb -- ratio 0.999999.
That is NOT evidence. `c_3 = -2.069342577` is tier `cal-anchored`: it is
extracted by inverting Q_beta against experiment, so the extractor DEFINES it as
the quantity that absorbs the residual. The agreement is a tautology and is
recorded here only so the next reader does not mistake it for a result.

WHAT IS NOT CIRCULAR, and is the point of this probe:

  1. THE SPEC. A derived c_3 must reproduce the extracted value to within
     target/u^3. With u = 0.00851723455016, u^3 = 617.86817 ppb and the 7.797 ppb
     target, that is

         c_3 = -2.069342577  +/-  0.01262         (0.61 % relative)

     This is a REQUIREMENT, not a measurement: it says how accurate a derivation
     has to be before it changes the L2 verdict. Any candidate can now be tested
     against it before any wiring.

  2. THE STANDING CANDIDATE FAILS IT. `c_3 = -2 = J_Hopf(q=1)` -- the
     near-match the corpus has carried for months -- sits 0.0693426 away, which
     is 5.495x the tolerance. Wiring it would move Q_beta from 1278.58 ppb to
     42.845 ppb: a 29.8x improvement, and still 5.495x OUTSIDE target. So the
     Hopf candidate does not close L2 even if it is eventually derived.

  3. THE NEXT RUNG HAS ROOM, BUT NOT MUCH. Given a correct c_3, the residual is
     |c_4| * u^4 = |c_4| * 5.2625281 ppb, so Q_beta lands inside target iff

         |c_4| <= 1.4816        [denominator: target = 7.797 ppb = sigma_exp/100]

     NAME THE DENOMINATOR WHEN QUOTING THIS. A sibling (PR #6342, qou-cds1
     entry 9) reached the same bound independently and FIRST, reporting
     |c_4| <= 1.4822 -- the identical quantity computed against the ROUNDED
     target 7.80 rather than 7.797. The two differ by 0.038 % and are one
     number, not two measurements. Flagged because this corpus keeps being
     bitten by exactly this shape: AGENTS.md's c_3 note records "3.47 % vs
     3.35 %" as one gap under two normalisations, and qou-cds1 entry 12 hit
     the same 7.8-vs-7.797 split (7653x vs 7656x).

     A c_4 of order unity suffices; a c_4 of order 10 does not.

  4. AND K(delta) IS NECESSARY BUT NOWHERE NEAR SUFFICIENT. Entry 12 of
     `qou-cds1` measured the convention-D N=1 constant's freedom at 59694 ppb --
     46.7x LARGER than the entire current Q_beta error. So settling K is a
     prerequisite for a principled D-frame ladder, but it is a far coarser knob
     than the precision L2 needs: you need K settled AND a c_3 good to 0.61 %.

FRAME. The extracted c_3 and hence this spec are CONVENTION-C at the proton pin;
under convention D the ladder must be re-derived (`qou-cds1`) and the numerical
spec will move. The STRUCTURE of the argument -- tolerance = target/u^3,
sufficiency = target/u^4 -- is convention-independent.

NOT CLAIMED: any derivation of c_3; that the Hopf candidate is refuted as
MATHEMATICS (it is refuted only as a route to closing L2 for Q_beta); that
closing k=3 closes anything other than Q_beta, m_n and Delta_pn.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (HERE.parent, HERE.parent / "substrate"):
    sys.path.insert(0, str(p))

import mpmath as mp

from q_parameter import Q_50_DIGIT_STR
from qbeta_utils import c3_proton_extracted

mp.mp.dps = max(50, mp.mp.dps)
TARGET_PPB = mp.mpf("7.797")
ERR_TODAY_PPB = mp.mpf("1278.58")
K_FREEDOM_PPB = mp.mpf("59694.18")     # qou-cds1 entry 12

_results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    _results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")


def main() -> int:
    mp.mp.dps = 60
    # c_3 RECOMPUTED by the canonical extraction (qbeta_ck_cache's), not typed:
    # the literal this file carried until 2026-10-13 is reproduced by no producer.
    C3_EXTRACTED = c3_proton_extracted()
    q = mp.mpf(Q_50_DIGIT_STR)
    u = (q - 1) ** 2 * mp.sqrt(q**4 + q**2 + 1) / (q**4 + q**2)
    u3 = u**3 * mp.mpf(10) ** 9
    u4 = u**4 * mp.mpf(10) ** 9
    tol = TARGET_PPB / u3

    print("=" * 72)
    print("  Q_beta k=3 — the spec, and the candidate measured against it")
    print("=" * 72)
    print(f"\n  u = {mp.nstr(u, 12)}   u^3 = {mp.nstr(u3, 8)} ppb   u^4 = {mp.nstr(u4, 8)} ppb")

    print("\n-- the circularity, stated so it is not mistaken for evidence")
    check("extracted_c3_reproduces_the_error_TAUTOLOGICALLY",
          abs(abs(C3_EXTRACTED) * u3 - ERR_TODAY_PPB) < mp.mpf("0.01"),
          f"|c_3|*u^3 = {mp.nstr(abs(C3_EXTRACTED)*u3, 6)} ppb vs error {ERR_TODAY_PPB} ppb — "
          "c_3 is cal-anchored, so this is how it was DEFINED, not a finding")

    print("\n-- 1. the spec a derived c_3 must meet (this IS the non-circular content)")
    check("tolerance_is_target_over_u_cubed",
          tol > 0,
          f"c_3 = {mp.nstr(C3_EXTRACTED, 12)} +/- {mp.nstr(tol, 4)} "
          f"({mp.nstr(tol/abs(C3_EXTRACTED)*100, 3)} % relative)")

    print("\n-- 2. the standing candidate c_3 = -2 = J_Hopf(q=1)")
    dev = abs(mp.mpf(-2) - C3_EXTRACTED)
    resid = dev * u3
    check("hopf_candidate_is_outside_the_tolerance",
          dev > tol,
          f"|Δ| = {mp.nstr(dev, 6)} vs tol {mp.nstr(tol, 4)} — {mp.nstr(dev/tol, 4)}x outside")
    check("hopf_candidate_improves_but_does_NOT_close_L2",
          resid > TARGET_PPB and resid < ERR_TODAY_PPB,
          f"Q_beta would be {mp.nstr(resid, 5)} ppb = {mp.nstr(resid/TARGET_PPB, 4)}x target "
          f"({mp.nstr(ERR_TODAY_PPB/resid, 4)}x better than today, still failing)")

    print("\n-- 3. how much room the next rung has")
    c4max = TARGET_PPB / u4
    check("c4_sufficiency_bound",
          c4max > 1,
          f"|c_4| <= {mp.nstr(c4max, 5)} for Q_beta to land inside target — "
          "order unity suffices, order ten does not")

    print("\n-- 4. K(delta) is necessary but far coarser than L2 needs")
    check("K_freedom_dwarfs_the_current_error",
          K_FREEDOM_PPB > ERR_TODAY_PPB * 10,
          f"{K_FREEDOM_PPB} ppb is {mp.nstr(K_FREEDOM_PPB/ERR_TODAY_PPB, 4)}x the current "
          f"{ERR_TODAY_PPB} ppb error — settling K is a prerequisite, not the final step")

    n = sum(1 for _, ok, _ in _results if ok)
    print("\n" + "=" * 72)
    print(f"  {n}/{len(_results)} assertions passed")
    print(f"  A derived c_3 must hit {mp.nstr(C3_EXTRACTED, 11)} +/- {mp.nstr(tol, 4)} ({mp.nstr(tol/abs(C3_EXTRACTED)*100, 2)} %) to close L2")
    print("  for Q_beta -- and with it m_n and Delta_pn. The standing Hopf candidate")
    print("  c_3 = -2 misses that by 5.495x and would leave Q_beta at 5.495x target.")
    print("  Convention-C frame at the proton pin; the numbers move under D, the")
    print("  structure does not. No c_3 is derived here. Scope (a).")
    print("=" * 72)
    return 0 if n == len(_results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
