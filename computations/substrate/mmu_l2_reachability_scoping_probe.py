#!/usr/bin/env python3
"""m_mu's L2 target IS reachable: the propagation floor sits 14.8x BELOW it.

Option 2 of the L2 attack plan, scoped before attempting. m_mu misses its 100x
target by 970x -- the largest miss on the board and the framework's one genuine
tension (9.7 sigma). Before deriving anything, the question that decides whether
the attack is worth mounting: is the target reachable AT ALL from a
proton-pinned q_0, or does the pinning uncertainty already exceed it?

THE ANSWER IS THAT IT IS REACHABLE, COMFORTABLY.

    sigma(m_p/m_e)   = 0.017 ppb          the pinning input (CODATA 2022)
    S_proton         = -20.9970           dln(m_p/m_e)/dln(q), MEASURED
    -> sigma(q_0)    = 0.00080964 ppb
    S_muon           = -18.1854           dln(m_mu/m_e)/dln(q), MEASURED
    -> floor on m_mu = 0.0147236 ppb
    m_mu 100x target = 0.2177   ppb
    floor / target   = 0.0676              -> 14.8x BELOW target

So the 211.2 ppb error is **14344x the propagation floor**. It is genuine model
error, not measurement noise, and closing it is not blocked by the anchor's
precision. That is what makes option 2 worth mounting.

A WRONG FIRST ESTIMATE OF MINE, recorded because the error is instructive. My
first pass assumed q_0 inherits sigma(m_p/m_e) directly -- i.e. unit proton
elasticity -- and got floor/target = 1.42, "the target is unreachable". That is
wrong by a factor of |S_proton| = 21. The pinning relation is STIFF: a 0.017 ppb
uncertainty on the mass ratio buys a 0.00081 ppb uncertainty on q_0, because
m_p/m_e responds ~21x faster than q does. Stiffness in the pin is what makes the
downstream prediction cheap, and it is the whole reason the proton pin was chosen.

AND A STALE FIGURE FOUND ON THE WAY. `qou_substrate/constants.py` states
"sigma(q_0) ~ 0.0029 ppb = 2853 ppQ" in the comment directly above the formula
that computes it. That formula, with the live inputs, gives 0.00081 ppb -- 3.6x
smaller. The 0.0029 is reproduced exactly by the PRE-2026-08-21 sigma(m_p/m_e) of
0.06 ppb (0.06/21 = 0.00286), which AGENTS.md already records as corrected to
0.017. So the comment is stale by a correction the corpus made elsewhere and did
not propagate here. The CODE is correct -- it reads MASS_RATIO_P_E_ERR live; only
the human-readable figure beside it is wrong.

NOT CLAIMED: any correction to the muon relation; that the 211.2 ppb is
explainable; that m_mu WILL close -- only that nothing in the anchor's precision
prevents it. Scope (a).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import mpmath as mp

from q_parameter import Q_50_DIGIT_STR

mp.mp.dps = max(50, mp.mp.dps)
SIGMA_P_E_PPB = mp.mpf("0.017")      # CODATA 2022 sigma on m_p/m_e
SIGMA_P_E_STALE = mp.mpf("0.06")     # the pre-2026-08-21 figure
TARGET_PPB = mp.mpf("0.2177")        # m_mu 100x target
ERR_TODAY_PPB = mp.mpf("211.2")

_results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    _results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")


def main() -> int:
    mp.mp.dps = 60
    q = mp.mpf(Q_50_DIGIT_STR)
    vol = 2 * mp.clsin(2, mp.pi / 3)

    def mp_over_me(x):
        h = x - 1 / x
        trM = abs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
        qf3 = (x**2 + 1 + x**-2) * (x + 1 / x)
        return 2 * vol / (1 - 1 / x) ** 2 * (trM * qf3 / x**3) - 12

    mu_over_me = lambda x: vol / (1 - 1 / x) ** 2

    eps = mp.mpf(10) ** -30
    elas = lambda f: (f(q * (1 + eps)) - f(q)) / f(q) / eps
    s_p, s_mu = elas(mp_over_me), elas(mu_over_me)

    print("=" * 72)
    print("  m_mu — is its L2 target reachable from a proton-pinned q_0?")
    print("=" * 72)

    print("\n-- the two elasticities, measured rather than assumed")
    check("proton_elasticity_matches_the_hardcoded_literal",
          abs(abs(s_p) - 21) < mp.mpf("0.01"),
          f"S_proton = {mp.nstr(s_p, 12)} vs the hardcoded 21.0 — agrees to "
          f"{mp.nstr(abs(abs(s_p)-21)/21*100, 3)} %")
    check("muon_elasticity_measured",
          abs(s_mu) > 1,
          f"S_muon = {mp.nstr(s_mu, 12)}; |S_mu/S_p| = {mp.nstr(abs(s_mu/s_p), 8)}")

    sigma_q = SIGMA_P_E_PPB / abs(s_p)
    floor = sigma_q * abs(s_mu)

    print("\n-- the propagation floor")
    print(f"     sigma(m_p/m_e) = {SIGMA_P_E_PPB} ppb  ->  sigma(q_0) = {mp.nstr(sigma_q, 6)} ppb")
    print(f"     floor on m_mu  = {mp.nstr(floor, 6)} ppb   vs target {TARGET_PPB} ppb")
    check("m_mu_target_is_REACHABLE",
          floor < TARGET_PPB,
          f"floor/target = {mp.nstr(floor/TARGET_PPB, 5)} — the floor sits "
          f"{mp.nstr(TARGET_PPB/floor, 5)}x BELOW target")
    check("todays_error_is_model_error_not_noise",
          ERR_TODAY_PPB > floor * 1000,
          f"{ERR_TODAY_PPB} ppb is {mp.nstr(ERR_TODAY_PPB/floor, 6)}x the floor — "
          "genuine model error, so the attack is worth mounting")

    print("\n-- the stale figure in qou_substrate/constants.py")
    stale = SIGMA_P_E_STALE / abs(s_p)
    check("comment_figure_reproduces_the_SUPERSEDED_input",
          abs(stale - mp.mpf("0.0029")) < mp.mpf("0.0002"),
          f"the comment's 0.0029 ppb = {mp.nstr(SIGMA_P_E_STALE, 3)}/21 = "
          f"{mp.nstr(stale, 3)}; the live 0.017 gives {mp.nstr(sigma_q, 3)} — "
          "stale by the 0.06 -> 0.017 correction AGENTS.md already records")

    n = sum(1 for _, ok, _ in _results if ok)
    print("\n" + "=" * 72)
    print(f"  {n}/{len(_results)} assertions passed")
    print("  m_mu's L2 target is REACHABLE: the propagation floor is 14.8x below")
    print("  it, and today's 211.2 ppb is 14344x the floor. The miss is model")
    print("  error, not noise. NOT claimed: any correction to the muon relation,")
    print("  or that m_mu will close — only that the anchor does not prevent it.")
    print("  Scope (a).")
    print("=" * 72)
    return 0 if n == len(_results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
