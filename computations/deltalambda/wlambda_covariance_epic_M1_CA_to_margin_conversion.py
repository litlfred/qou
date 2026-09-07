#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): convert the V_A-remainder constant C_A into MARGIN units -- the conversion the
arc keeps dropping -- and read off the headroom a rigorous Olver/Debye bound actually has.

WHY. Two merged claims in this arc compared a constant belonging to V_A against a threshold belonging
to the MARGIN, with no conversion (PRs #6500 and #6528 correct them). A third site,
wlambda_covariance_epic_M1_debye_CA_investigation.py, states the question in its docstring as

    "decide whether a rigorous Olver/Debye C_A can land under the target C <= 2.668"

which reads as C_A vs C. THAT DOCSTRING IS LOOSE, BUT ITS VERDICT IS NOT: the probe's own conclusion
compares the TRUE MARGIN CONSTANT (~0.087) against 2.668, which is unit-correct, and no number in it
is derived from the conflation. So this is a phrasing defect, NOT a third numerical error -- recorded
that way deliberately, because miscounting the errors would be the same sin as the errors.

What is genuinely missing is the conversion itself, which nothing in the arc writes down. Here it is.

THE CONVERSION. C_A is defined by |V_A/theta^2 - v_A| <= C_A theta^{-1/2}: an ABSOLUTE deviation of
V_A/theta^2. The margin is m = rho_P - sigma_D/sigma_A with sigma_D/sigma_A = sqrt(V_D/V_A). So

    relative error on V_A:   delta_A = C_A theta^{-1/2} / v_A
    margin perturbation:     |Delta m| = (sig_ratio_inf / 2) * delta_A
                                       = (sig_ratio_inf / (2 v_A)) * C_A * theta^{-1/2}

i.e. the V_A leg contributes a MARGIN-level constant

    C_margin,A  =  (sig_ratio_inf / (2 v_A)) * C_A  =  0.41922 * C_A.

Inverting against the requirement C <= m_inf sqrt(79) = 2.6681, the V_A leg alone may spend

    C_A  <=  2.6681 / 0.41922  =  6.364,

NOT C_A <= 2.668. The naive reading is 2.39x too strict.

MEASURED (this probe re-runs the C_A extraction rather than quoting it): C_A^emp = 0.00775419 over
theta in [80, 2560], so the headroom on the V_A leg is ~821x. That is much larger than the 46x
headroom on the TOTAL margin (PR #6500) for a good reason: the V_A leg is only one of three
contributions to the margin's deviation, and the measurements say it is the small one -- rho_P's
deviation is 0.1329/theta, an order of magnitude larger at these theta.

TWO CAVEATS, both real.

  1. DE-POISSONIZATION IS NOT DONE HERE. C_A is poissonized (a theta-object); the margin requirement
     is at fixed n. The conversion above is exact for the SHAPE but the theta <-> n step is a further
     factor nobody in this arc has pinned. Read ~821x as "modulo de-poissonization", not as a bound.
  2. C_A^emp IS MEASURED AT THE WRONG RATE, CONSERVATIVELY. It is sup |.| sqrt(theta) while the true
     V_A remainder rate is theta^{-1} (exponent measured 0.9395 here, and c_1 ~ -0.0678 in
     _em_osc_constant_prediction). So |.|sqrt(theta) ~ |c_1|/sqrt(theta) DECREASES and the sup sits at
     the left end of the window. That makes C_A^emp an over-estimate of the sup over all theta >= 80,
     which is the safe direction -- but the window starts at 80 and the requirement is n >= 79, so the
     sup is not established below 80 by this probe.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 40

from _m1_io_constants import M_INF, SIG_RATIO_INF, RHO_INF  # merged #5901 IO leading constants -- single source, see that module
C_TARGET = M_INF * mp.sqrt(79)            # margin-level requirement (PR #5929 shape)


def _load_ingredients():
    """Import the C_A investigation's ingredient extractor by explicit file path (not bare name:
    the _path_bridge bootstrap trap -- this probe must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_debye_CA_investigation.py"
    spec = importlib.util.spec_from_file_location("_m1_debye_ca", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    mod = _load_ingredients()
    print(f"# C_A -> margin-units conversion; dps={mp.mp.dps}; NO float64")
    print(f"# m_inf={mp.nstr(M_INF,9)}  sig_ratio_inf={mp.nstr(SIG_RATIO_INF,9)}  "
          f"C_target={mp.nstr(C_TARGET,6)}")
    print("#")

    # Re-extract V_A/theta^2 across theta rather than quoting the sibling's printed number.
    rows = []
    for th in (80, 160, 320, 640, 1280, 2560):
        M = int(mp.floor(2 * mp.sqrt(th) + 8 * mp.power(mp.mpf(th), mp.mpf(1) / 6) + 20))
        VA, VW, P, rho = mod.ingredients(mp.mpf(th), M)
        rows.append((mp.mpf(th), VA / mp.mpf(th) ** 2, rho))

    # v_A by Richardson on the measured exponent; cross-check against exact 8/pi^2.
    s = [r[1] for r in rows]
    t = [r[0] for r in rows]
    a = mp.log(abs((s[-3] - s[-2]) / (s[-2] - s[-1]))) / mp.log(t[-2] / t[-3])
    r_ = t[-1] / t[-2]
    vA = s[-1] + (s[-1] - s[-2]) / (r_ ** a - 1)
    exact = 8 / mp.pi ** 2
    print(f"# V_A/theta^2 exponent a = {mp.nstr(a,5)}  (=> the remainder is ~theta^-1, not theta^-1/2)")
    print(f"# v_A extrapolated = {mp.nstr(vA,11)}   exact 8/pi^2 = {mp.nstr(exact,11)}   "
          f"rel diff {mp.nstr(abs(vA-exact)/exact,3)}")
    CA = max(abs(si - vA) * mp.sqrt(ti) for ti, si, _ in rows)
    print(f"# C_A^emp = max |V_A/theta^2 - v_A| sqrt(theta) = {mp.nstr(CA,6)}  (sup at the LEFT end)")
    print("#")

    conv = SIG_RATIO_INF / (2 * exact)
    print("# THE CONVERSION nothing in this arc writes down:")
    print("#   delta_A   = C_A theta^{-1/2} / v_A            (absolute -> relative on V_A)")
    print("#   |Delta m| = (sig_ratio_inf/2) * delta_A       (relative on V_A -> margin)")
    print(f"#   => C_margin,A = (sig_ratio_inf / (2 v_A)) * C_A = {mp.nstr(conv,6)} * C_A")
    print("#")
    print(f"#   admissible C_A (V_A leg alone) = C_target / {mp.nstr(conv,6)} = {mp.nstr(C_TARGET/conv,6)}")
    print(f"#   NOT C_A <= {mp.nstr(C_TARGET,5)} -- the naive reading is "
          f"{mp.nstr(1/conv,4)}x too strict.")
    print(f"#   measured C_A^emp               = {mp.nstr(CA,6)}")
    print(f"#   headroom on the V_A leg        = {mp.nstr((C_TARGET/conv)/CA,5)}x")
    print("#")

    # The rho_P leg, for scale: it enters the margin LINEARLY, so no conversion factor.
    dev = [(ti, abs(rho - RHO_INF) * ti) for ti, _, rho in rows]
    print("# FOR SCALE -- the rho_P leg enters m LINEARLY (no conversion), and it is the BIGGER one:")
    print("#   |rho_P - rho_inf| * theta = " + " ".join(mp.nstr(v, 4) for _, v in dev))
    print("#   flat => |rho_P - rho_inf| ~ 0.1329/theta, an order of magnitude above the V_A leg's")
    print(f"#   contribution ({mp.nstr(conv,4)} * {mp.nstr(CA,4)} = {mp.nstr(conv*CA,4)}) / sqrt(theta).")
    print("#   So the 46x headroom on the TOTAL margin (PR #6500) and the ~821x here are consistent:")
    print("#   the V_A leg is the small contribution, and most of the margin's finite-n deviation is")
    print("#   rho_P's. A rigorous C should be budgeted per leg, not as one number.")
    print("#")
    print("# CAVEATS, both real:")
    print("#   (1) DE-POISSONIZATION IS NOT DONE. C_A is a theta-object; the requirement is at fixed n.")
    print("#       The conversion is exact for the SHAPE; the theta<->n step is a further factor no one")
    print("#       in this arc has pinned. Read the headroom as 'modulo de-poissonization'.")
    print("#   (2) C_A^emp is measured at rate theta^{-1/2} while the true rate is theta^{-1}, so")
    print("#       |.|sqrt(theta) DECREASES and the sup sits at the window's left end -- conservative,")
    print("#       but the window starts at theta=80 and the requirement is n>=79, so the sup below 80")
    print("#       is not established here.")
    print("#")
    print("# ON THE THIRD SITE: _debye_CA_investigation's DOCSTRING reads 'whether a rigorous C_A can")
    print("#   land under the target C <= 2.668', which conflates C_A with C. Its VERDICT does not --")
    print("#   it compares the true MARGIN constant (~0.087) to 2.668, which is unit-correct, and no")
    print("#   number there is derived from the conflation. Phrasing defect, NOT a third numerical")
    print("#   error. Miscounting the errors would be the same sin as the errors.")
    print(f"RESULT: C_margin,A = {mp.nstr(conv,5)} * C_A, so the V_A leg may spend C_A <= "
          f"{mp.nstr(C_TARGET/conv,5)} (not 2.668); measured C_A^emp = {mp.nstr(CA,5)} => ~"
          f"{mp.nstr((C_TARGET/conv)/CA,4)}x headroom, modulo de-poissonization. rho_P is the bigger "
          f"leg. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
