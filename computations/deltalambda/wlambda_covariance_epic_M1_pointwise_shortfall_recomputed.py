#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): the pointwise route's shortfall factor is OVERSTATED ~2.9x -- a unit error in my
own decisive negative. The VERDICT survives; the number does not.

WHAT THIS CORRECTS. wlambda_covariance_epic_M1_pointwise_bound_insufficiency.py (merged, PR #6438)
established that a POINTWISE uniform Bessel remainder |J - S| <= eps cannot pin the variance
constant, because U/V = Sum w|S| / ((1/2) Sum w S^2) grows without bound. That structural conclusion
is correct and is NOT touched here. Its closing arithmetic is:

    "At theta = 78 the MEASURED U/V = 45.65 gives, for a pointwise remainder eps = K theta^{-1/2}, a
     relative error on V_A of about K * 5.17. Keeping that below m_inf = 0.3002 forces K < 0.058,
     whereas the leading Debye/Olver remainder coefficient is O(1): the pointwise route misses the
     required constant by ~17x."

The last step compares a RELATIVE error on V_A against m_inf, an ABSOLUTE margin. Those are different
objects and the conversion factor was dropped. The margin is

    m = rho_P - sigma_D/sigma_A,     sigma_D/sigma_A = sqrt(V_D/V_A),

so a relative perturbation delta_A on V_A moves the ratio by a factor sqrt(1 - delta_A) ~ 1 -
delta_A/2, i.e. it moves the MARGIN by

    |Delta m|  =  sig_ratio_inf * delta_A / 2  =  0.6796 * delta_A / 2  =  0.3398 * delta_A,

not by delta_A. So the admissible relative error on V_A is m_inf / 0.3398 = 0.8834, not 0.3002: the
merged threshold is 1/0.3398 = 2.94x TOO STRICT.

WHAT SURVIVES, AND WHAT DOES NOT.

  * The structural negative SURVIVES intact: U/V grows without bound, so no pointwise bound however
    sharp can control the variance uniformly in theta. That argument never used the threshold.
  * The SHORTFALL FACTOR does not. Recomputed below, the pointwise route is short by ~5.8x (V_A
    carrying the whole error budget) or ~11.7x (budget split evenly with the V_D leg), against the
    recorded ~17x.

This matters for how the route reads. "17x short" reads as hopeless; "5.8x short" reads as a gap a
sharp constant might close, and the honest figure should not decide that question by accident.

HONEST LIMIT OF THIS CORRECTION -- and it is stronger than "the O(1) is imprecise". The shortfall is
a ratio against "the leading Debye/Olver remainder coefficient is O(1)", which is not a pinned number
anywhere in the corpus. But wlambda_covariance_epic_M1_bulk_kernel_rate_probe.py has already measured
something sharper: the POINTWISE error |J(x,x+k;theta) - S(k,a)| does NOT decay cleanly at all -- its
log-log slope SCATTERS over b ~ [-2, +2] across r, k and theta, because the integer x quantises the
local density a = x/sqrt(theta) (and S is sensitive to a) and because the sub-leading term is
oscillatory. So there is no clean pointwise constant K to compare against: the ratio is not merely
imprecise, it is ILL-DEFINED.

That does not weaken this correction; it relocates it. What is measured here is K_admissible -- the
error budget the margin actually allows, which is a well-defined quantity and was computed 2.943x too
small. The "~5.8x" and "~17x" are both comparisons of that budget against an object the corpus says
is not a constant, and neither should be quoted as a measurement. Quote K_admissible = 0.17115 at
theta = 78, and say that the pointwise route fails for the STRUCTURAL reason (U/V unbounded), not
because of any factor.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 30

M_INF = mp.mpf('0.300186614161')          # merged #5901 IO leading (CS) margin
SIG_RATIO_INF = mp.mpf('0.679609581496')  # merged #5901 sigma_D/sigma_A limit


def _load_UV():
    """Import U_and_V() from the merged pointwise probe by explicit file path.

    By path, not by bare name: a sibling in a cluster subdir resolves only when the parent is already
    on sys.path (the _path_bridge bootstrap trap), and this probe must run with PYTHONPATH unset.
    """
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_pointwise_bound_insufficiency.py"
    spec = importlib.util.spec_from_file_location("_m1_pointwise", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.U_and_V


def main():
    U_and_V = _load_UV()
    print(f"# pointwise-route shortfall, RECOMPUTED; dps={mp.mp.dps}; NO float64")
    print(f"# m_inf = {mp.nstr(M_INF,9)}   sig_ratio_inf = {mp.nstr(SIG_RATIO_INF,9)}")
    print("#")
    print("# THE UNIT ERROR. A relative error delta_A on V_A perturbs sigma_D/sigma_A = sqrt(V_D/V_A)")
    print("#   by a factor ~ (1 - delta_A/2), hence perturbs the MARGIN by")
    print(f"#     |Delta m| = sig_ratio_inf * delta_A / 2 = {mp.nstr(SIG_RATIO_INF/2,6)} * delta_A,")
    print("#   NOT by delta_A. The merged probe compared delta_A directly against m_inf.")
    conv = SIG_RATIO_INF / 2
    print(f"#   Admissible delta_A = m_inf / {mp.nstr(conv,6)} = {mp.nstr(M_INF/conv,6)}  (merged: {mp.nstr(M_INF,6)})")
    print(f"#   => the merged threshold is {mp.nstr(1/conv,4)}x too strict.")
    print("#")
    print("#   theta      U/V     eps-mult    K_adm (V_A alone)   K_adm (split w/ V_D)")
    for e in (64, 78, 128, 256):
        th = mp.mpf(e)
        U, V = U_and_V(th)
        uv = U / V
        # eps = K theta^{-1/2}; relative error on V_A is eps * (U/V) = K * (U/V)/sqrt(theta)
        mult = uv / mp.sqrt(th)
        k_alone = (M_INF / conv) / mult
        k_split = (M_INF / (2 * conv)) / mult      # V_A and V_D each get half the margin budget
        print(f"  {e:>7}  {mp.nstr(uv,6):>8}  {mp.nstr(mult,6):>9}  {mp.nstr(k_alone,5):>17}  "
              f"{mp.nstr(k_split,5):>20}")
    print("#")
    th = mp.mpf(78)
    U, V = U_and_V(th)
    mult = (U / V) / mp.sqrt(th)
    k_alone = (M_INF / conv) / mult
    k_split = (M_INF / (2 * conv)) / mult
    print("# AT theta = 78 -- the largest n the exact Fraction table reaches, so the n at which the")
    print("#   asymptotic must take over, and the theta the merged probe quotes:")
    print(f"#     U/V                        = {mp.nstr(U/V,6)}")
    print(f"#     relative err on V_A per K  = {mp.nstr(mult,6)}   (merged quotes 5.17)")
    print(f"#     K admissible, V_A alone    = {mp.nstr(k_alone,5)}   (merged quotes 0.058)")
    print(f"#     K admissible, budget split = {mp.nstr(k_split,5)}")
    print("#   Against a Debye/Olver leading remainder coefficient of O(1) ~ 1, the shortfall is")
    print(f"#     ~{mp.nstr(1/k_alone,3)}x  (V_A alone)   or   ~{mp.nstr(1/k_split,3)}x  (budget split),")
    print("#   against the ~17x on record.")
    print("#")
    print("# WHAT IS UNCHANGED. The structural negative stands and did not use this threshold: U/V")
    print("#   GROWS without bound in theta (42.8, 45.7, 53.9, 70.7, 91.9 at theta=64..512), so no")
    print("#   pointwise bound, however sharp its constant, controls the variance uniformly. The")
    print("#   oscillatory cancellation (summation by parts / stationary phase) remains ESSENTIAL.")
    print("#   Only the quoted shortfall FACTOR is corrected.")
    print("#")
    print("# AND WHAT THIS DOES NOT SETTLE -- sharper than 'the O(1) is imprecise'. There is NO clean")
    print("#   pointwise constant to compare against at all: _bulk_kernel_rate_probe.py measures that")
    print("#   |J(x,x+k;theta) - S(k,a)| has no clean exponent, its log-log slope SCATTERING over")
    print("#   b ~ [-2,+2] (the integer x quantises the density a = x/sqrt(theta), and the sub-leading")
    print("#   term oscillates). So both '~17x' and the figures above compare a well-defined budget")
    print("#   against an ILL-DEFINED constant. Quote K_admissible = 0.17115 at theta=78; do not quote")
    print("#   a shortfall factor. The pointwise route fails STRUCTURALLY (U/V unbounded), not by a")
    print("#   factor -- which is why the correction above changes no verdict.")
    print(f"RESULT: K_admissible at theta=78 is {mp.nstr(k_alone,5)} (V_A alone) / {mp.nstr(k_split,5)} (split), "
          f"not 0.058 -- the merged threshold dropped the sig_ratio_inf/2 = {mp.nstr(conv,5)} unit "
          f"conversion and was {mp.nstr(1/conv,4)}x too strict. Do NOT quote a shortfall factor: the "
          f"pointwise constant it would divide by is ill-defined (_bulk_kernel_rate_probe). Structural "
          f"negative UNCHANGED. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
