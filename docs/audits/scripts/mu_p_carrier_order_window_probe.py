#!/usr/bin/env python3
"""mu-p residual: order-in-hbar_q window + entropy(precision) bound.

Bean qou-6gf9.  Angle: the MUON CARRIER  m_mu/m_e = Vol(4_1)/hbar_q^2,
NOT the Q_beta c_k ladder and NOT the F_Bor c_4 dressing.

Question: if the carrier is only the leading term of a series, at what
ORDER in hbar_q does its first correction live, and can that correction
be IDENTIFIED from the datum?

Pin: EXPERIMENTAL / proton (owner directive 2026-08-07).  No muon-built
cache is read anywhere in this file -- q0 comes from the package-layer
constant only, so there is no ideal/experimental layer straddle.
"""

import sys

from mpmath import mp, mpf, log, sqrt

sys.path.insert(0, "tools/qou-substrate/python")
from qou_substrate import constants as C  # noqa: E402

mp.dps = 60

# ---- inputs (experimental/proton layer only) -------------------------
q0 = mpf(C.Q_50_DIGIT_STR)  # proton pin
hbar = 1 - 1 / q0  # hbar_q = 1 - 1/q0
vol41 = mp.mpf(str(C.VOL_4_1))
# independent recomputation: Vol(4_1) = 2*Cl_2(pi/3) = 2*Im Li_2(e^{i pi/3})
vol41_series = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
R_exp = mpf("206.7682830")  # CODATA m_mu/m_e
R_exp_relerr = mpf("22e-9")  # ~22 ppb

print(f"q0 (proton pin)      = {mp.nstr(q0, 25)}")
print(f"hbar_q = 1 - 1/q0    = {mp.nstr(hbar, 25)}")
print(f"Vol(4_1) [constants] = {mp.nstr(vol41, 20)}")
print(f"Vol(4_1) [4*Im Li2]  = {mp.nstr(vol41_series, 20)}")

R_pred = vol41 / hbar**2
resid = R_pred / R_exp - 1  # relative miss of the prediction
t = 1 - R_exp / R_pred  # multiplicative correction: carrier * (1-t) = CODATA
print()
print(f"m_mu/m_e predicted   = {mp.nstr(R_pred, 20)}")
print(f"m_mu/m_e CODATA      = {mp.nstr(R_exp, 20)}")
print(f"residual (ppb)       = {mp.nstr(resid * 10**9, 10)}")
print(
    f"sigma_exp (ppb)      = {mp.nstr(R_exp_relerr * 10**9, 6)}"
    f"   -> {mp.nstr(resid / R_exp_relerr, 4)} sigma"
)
print(f"target correction t  = {mp.nstr(t, 12)}   (carrier * (1-t) = CODATA)")
print(
    f"relative resolution on t = {mp.nstr(R_exp_relerr / resid * 100, 4)} %  "
    f"-> t is a {mp.nstr(-mp.log10(R_exp_relerr / resid), 3)}-significant-digit datum"
)

# ---- ORDER of the correction in hbar_q -------------------------------
order = log(t) / log(hbar)
print()
print(f"hbar_q-order of t: ln(t)/ln(hbar_q) = {mp.nstr(order, 8)}  (NON-INTEGER)")
print()
print(" k | hbar_q^k        | c_k = t / hbar_q^k   | |c_k| in [1/5,5]?")
print("---+-----------------+----------------------+------------------")
adm = []
for k in range(1, 12):
    hk = hbar**k
    ck = t / hk
    ok = mpf(1) / 5 <= abs(ck) <= 5
    if ok:
        adm.append(k)
    print(f"{k:2d} | {mp.nstr(hk, 8):>15} | {mp.nstr(ck, 10):>20} | {'YES' if ok else 'no'}")
print(f"\nADMISSIBLE ORDERS (coefficient of small height, 1/5 <= |c| <= 5): {adm}")

# ---- entropy: how many 'categorical-looking' constants hit the window?
lo = t * (1 - R_exp_relerr / resid)
hi = t * (1 + R_exp_relerr / resid)
k = adm[0]
clo, chi = lo / hbar**k, hi / hbar**k
print(f"\nExperimentally indistinguishable window at order k={k}:")
print(
    f"  c in [{mp.nstr(clo, 8)}, {mp.nstr(chi, 8)}]  "
    f"(full width {mp.nstr((chi - clo) / ((chi + clo) / 2) * 100, 4)} %)"
)

q2 = q0 + 1 / q0  # [2]_q
q3 = q0**2 + 1 + 1 / q0**2  # [3]_q
cands = {
    "q0/5                (the R9 fit)": q0 / 5,
    "2/9": mpf(2) / 9,
    "1/(2*sqrt5)     (icosahedral)": 1 / (2 * sqrt(5)),
    "Vol(4_1)/9": vol41 / 9,
    "1/sqrt(20)": 1 / sqrt(20),
    "[3]_q/([2]_q*7)": q3 / q2 / 7,
    "0.2075   (refuted projector delta)": mpf("0.2075"),
    "9/40": mpf(9) / 40,
    "1/(4*q0**2)": 1 / (4 * q0**2),
    "pi/14": mp.pi / 14,
    "[2]_q/9": q2 / 9,
    "1/[2]_q^2/... = 1/(2*[2]_q+...)": mpf(1) / mpf("4.48"),
}
print("\n  small-height / 'categorical-looking' candidates vs the window:")
nin = 0
for name, v in sorted(cands.items(), key=lambda kv: kv[1]):
    inw = clo <= v <= chi
    if inw:
        nin += 1
    print(f"    {'IN ' if inw else '   '} {name:36s} = {mp.nstr(v, 8)}")
print(f"\n  -> {nin} of {len(cands)} hand-listed candidates are indistinguishable at 1 sigma_exp.")

# ---- is the second rung of the R9V9 closure even resolvable? ---------
dR9 = hbar**6 * q0 / 5
dV9 = hbar**8 * q3 / 25
sig_t = t * R_exp_relerr / resid
print("\nR9V9 closure audit (MmuR9V9Closure.lean):")
print(f"  delta_R9 = hbar^6*q/5      = {mp.nstr(dR9, 10)}   ({mp.nstr(dR9 / t * 100, 5)} % of t)")
print(f"  delta_V9 = hbar^8*[3]_q/25 = {mp.nstr(dV9, 10)}   ({mp.nstr(dV9 / t * 100, 5)} % of t)")
print(
    f"  sigma_exp on t             = {mp.nstr(sig_t, 10)}   "
    f"({mp.nstr(R_exp_relerr / resid * 100, 4)} % of t)"
)
print(
    f"  -> delta_V9 sits {mp.nstr(sig_t / dV9, 5)}x BELOW the experimental "
    f"resolution of the datum it closes."
)
print(
    f"  R9 alone leaves: {mp.nstr((t - dR9) / t * 100, 5)} % of t = "
    f"{mp.nstr((t - dR9) * 10**9, 5)} ppb  (vs sigma_exp {mp.nstr(R_exp_relerr * 10**9, 4)} ppb)"
)

# ---- BAR PARITY: which monomials survive q -> 1/q ? ------------------
# hbar_q(1/q) = 1 - q = -q*(1 - 1/q) = -q*hbar_q(q).   Hence
#   bar( hbar_q^k * q^m ) = (-1)^k q^(k-m) hbar_q^k,
# which equals hbar_q^k q^m for all q iff  k even AND m = k/2,
# i.e. exactly the tower of  w := q * hbar_q^2 = q + 1/q - 2 = [2]_q - 2.
print("\n" + "=" * 62)
print("BAR PARITY (q -> 1/q); the correction must be bar-EVEN")
print("  (precondition argued from 4_1 amphichirality: "
      "2026-06-20-keystone-branching-shift-first-crack.md)")
print("=" * 62)
qi = 1 / q0
hbar_bar = 1 - 1 / qi
print(f"  hbar_q(1/q0)                = {mp.nstr(hbar_bar, 15)}")
print(f"  -q0 * hbar_q(q0)            = {mp.nstr(-q0 * hbar, 15)}   <- identity holds")

w = q0 + 1 / q0 - 2
print(f"\n  w := q*hbar_q^2 = [2]_q - 2 = {mp.nstr(w, 15)}")
print(f"  q0*hbar^2                   = {mp.nstr(q0 * hbar**2, 15)}   <- identity holds")
print(f"  w(1/q0)                     = {mp.nstr(qi + 1 / qi - 2, 15)}   <- bar-INVARIANT")


def barparity(f):
    """Return 'even' / 'odd' / 'mixed' for f evaluated at q0 vs 1/q0."""
    a, b = f(q0), f(qi)
    if abs(a - b) < abs(a) * mpf("1e-30"):
        return "EVEN"
    if abs(a + b) < abs(a) * mpf("1e-30"):
        return "odd"
    return f"MIXED  (f(1/q)/f(q) = {mp.nstr(b / a, 8)})"


def _q3(x):
    return x**2 + 1 + 1 / x**2


print("\n  bar-parity of the corpus's own m_mu correction rungs:")
print(f"    delta_R9 = hbar^6*q/5       : {barparity(lambda x: (1 - 1 / x) ** 6 * x / 5)}")
print(f"    delta_V9 = hbar^8*[3]_q/25  : "
      f"{barparity(lambda x: (1 - 1 / x) ** 8 * _q3(x) / 25)}")
print(f"    w^3                         : {barparity(lambda x: (x + 1 / x - 2) ** 3)}")
print("  -> both R9 and V9 are bar-MIXED: they violate the bar-even precondition,")
print("     independently of how well they match numerically.")

# ---- the bar-even w-tower: does the residual live in it? -------------
print("\n  bar-even tower  t = c * w^j  (w = [2]_q - 2):")
print("   j |      w^j        |   c = t / w^j    | |c| in [1/5,5]?")
print("  ---+-----------------+------------------+----------------")
adm_w = []
for j in range(1, 7):
    wj = w**j
    cj = t / wj
    ok = mpf(1) / 5 <= abs(cj) <= 5
    if ok:
        adm_w.append(j)
    print(f"  {j:2d} | {mp.nstr(wj, 8):>15} | {mp.nstr(cj, 10):>16} | {'YES' if ok else 'no'}")
print(f"  order ln(t)/ln(w) = {mp.nstr(log(t) / log(w), 8)}   admissible j: {adm_w}")
print(f"  nearest small-height hit: 4/25 = {mp.nstr(mpf(4) / 25, 8)} vs c_3 = "
      f"{mp.nstr(t / w**3, 8)}  (off by {mp.nstr(abs(mpf(4) / 25 - t / w**3) / (t / w**3) * 100, 4)} %"
      f", window is {mp.nstr(R_exp_relerr / resid * 100, 4)} %) -> NEAR-MATCH, unidentifiable")

# ---- the 'order' is not an invariant of the residual -----------------
print("\n  the hbar-order is NOT an invariant -- it depends on the chosen parameter:")
for nm, val in [
    ("hbar_q = 1-1/q", hbar),
    ("hbar_q^2", hbar**2),
    ("w = [2]_q - 2  (bar-even)", w),
    ("(q-1/q)^2      (bar-even)", (q0 - 1 / q0) ** 2),
    ("ln(q)", log(q0)),
    ("ln(q)^2", log(q0) ** 2),
]:
    print(f"    {nm:28s} = {mp.nstr(val, 10):>14}  -> order {mp.nstr(log(t) / log(val), 6)}")

# ---- Ohtsuki / volume-conjecture asymptotic series order check -------
print("\nOhtsuki-series (asymptotic expansion of the 4_1 Kashaev invariant) order check:")
print("  a first-order coefficient kappa_1 would enter as kappa_1 * hbar_q^1;")
print(f"  matching t requires kappa_1 = {mp.nstr(t / hbar, 8)}  (i.e. O(1e-6)),")
print("  whereas the known 4_1 Ohtsuki coefficients are O(1) rationals over sqrt(-3).")
print(f"  => a 1-loop / 2-loop volume-conjecture correction overshoots by "
      f"~{mp.nstr(hbar / t, 6)}x and ~{mp.nstr(hbar**2 / t, 6)}x respectively.")
