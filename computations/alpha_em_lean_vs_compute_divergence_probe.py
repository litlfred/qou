#!/usr/bin/env python3
"""Do the Lean formalisation and the production compute of alpha_em agree?

They do not. They are two DIFFERENT constructions of the same quantity, and
the scorecard's only L2 "win" (m_K/m_pi) rests on the one the paper does not
cite as its formalisation.

    content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.lean

        alphaEmInvCorrected q = 45*[3]_q * (1 + delta + kappa*delta^2)
        delta = hbar_q^4 * [5]_q
        kappa = 8*q                      <- the file itself calls this EMPIRICAL

    computations/meson_em_sinh_closed_form.py :: _alpha_em_inv_derived

        alpha_em^-1 = q*[9]_q*[10]_q * (1 + c1/(1 - c1*kappa_gram))
        c1         = (CS(T_2,9)+CS(T_3,5)) * ([2]_q/2) * hbar_q^2 / bare
        kappa_gram = det G_classical / det G_q-deformed

Neither the prefactor nor kappa is shared. The point is not that one is wrong;
it is that "m_K/m_pi is conditional on the Chern-Simons conjecture class in
em-coupling-chern-simons.lean" names a premise the number does not rest on.

And the direction is the wrong way round for the framework: the construction
with the EMPIRICAL kappa lands ~180x closer to CODATA than the derived one.
Its own docstring says so -- "The '8 = dim(su(3)) = gluon octet' interpretation
is post-hoc; no structural derivation links su(3) gluon dimension to alpha_EM."

NO FLOAT64: every quantity is carried as mpmath.mpf end to end; float() appears
only inside f-strings for display. Per AGENTS.md, probes are not exempt.

Run:  PYTHONPATH=computations:computations/substrate python3 -u \
        computations/alpha_em_lean_vs_compute_divergence_probe.py
"""
from mpmath import mp

mp.dps = 60

# The 50-digit pin, NOT `q_parameter.Q`. `Q` is a Python float, so seeding a
# 60-dps computation from it would carry ~17 significant digits into a
# calculation that reports parts-per-billion -- flagged by
# `mpf_import_time_dps_audit` and correctly so. (The divergences below are
# 470 ppb and a factor of 5, far above float64 resolution either way, so this
# is discipline rather than a correction to the result.)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

CODATA_ALPHA_EM_INV = mp.mpf("137.035999177")


def qbal(k, q):
    """Balanced quantum integer [k]_q = (q^k - q^-k)/(q - q^-1)."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def lean_alpha_em_inv(q):
    """`alphaEmInvCorrected` exactly as the .lean declares it."""
    delta = ((1 - 1 / q) ** 4) * qbal(5, q)
    kappa = 8 * q                       # gluonOctetKappa -- empirical, per the file
    return 45 * qbal(3, q) * (1 + delta + kappa * delta ** 2)


def compute_alpha_em_inv(q):
    """`_alpha_em_inv_derived` at exact resummation, re-implemented here so the
    probe does not depend on the producer's import cone."""
    pi = mp.pi
    bare = q * qbal(9, q) * qbal(10, q)
    n2 = qbal(2, q)
    cs_29 = pi ** 2 * mp.mpf(10) / 9
    cs_35 = pi ** 2 * mp.mpf(16) / 15
    c1 = (cs_29 + cs_35) * (n2 / 2) * (1 - 1 / q) ** 2 / bare

    sl, linking = 8, 17
    g11 = cs_29 + pi ** 2 * sl ** 2 / mp.mpf(2 * 9) ** 2
    g22 = cs_35 + pi ** 2 * sl ** 2 / mp.mpf(3 * 5) ** 2
    g12 = pi ** 2 * linking ** 2 / (mp.mpf(2 * 9) * (3 * 5))
    det_cl = g11 * g22 - g12 ** 2

    lk_q = abs(n2 * qbal(5, q) - qbal(3, q) * qbal(9, q))
    cs_q_29 = pi ** 2 * (n2 ** 2 - 1) * (qbal(9, q) ** 2 - 1) / (12 * n2 * qbal(9, q))
    cs_q_35 = (pi ** 2 * (qbal(3, q) ** 2 - 1) * (qbal(5, q) ** 2 - 1)
               / (12 * qbal(3, q) * qbal(5, q)))
    sl_q_29 = (n2 - 1) * (qbal(9, q) - 1)
    sl_q_35 = (qbal(3, q) - 1) * (qbal(5, q) - 1)
    gq11 = cs_q_29 + pi ** 2 * sl_q_29 ** 2 / (n2 * qbal(9, q)) ** 2
    gq22 = cs_q_35 + pi ** 2 * sl_q_35 ** 2 / (qbal(3, q) * qbal(5, q)) ** 2
    gq12 = pi ** 2 * lk_q ** 2 / (n2 * qbal(9, q) * qbal(3, q) * qbal(5, q))
    det_q = gq11 * gq22 - gq12 ** 2

    kappa_gram = det_cl / det_q
    return bare * (1 + c1 / (1 - c1 * kappa_gram)), kappa_gram


def ppb(x, ref):
    return (x - ref) / ref * mp.mpf(10) ** 9


def main():
    q = mp.mpf(Q_50_DIGIT_STR)
    print(f"q0 (proton pin) = {mp.nstr(q, 20)}\n")

    print("-" * 68)
    print("  The two constructions do not share a single ingredient")
    print("-" * 68)
    pre_lean = 45 * qbal(3, q)
    pre_comp = q * qbal(9, q) * qbal(10, q)
    a_comp, kappa_gram = compute_alpha_em_inv(q)
    a_lean = lean_alpha_em_inv(q)

    print(f"  prefactor  Lean  45*[3]_q          = {mp.nstr(pre_lean, 15)}")
    print(f"  prefactor  compute q*[9]_q*[10]_q  = {mp.nstr(pre_comp, 15)}")
    print(f"             differ by                 {mp.nstr((pre_lean - pre_comp) / pre_comp * 10**6, 6)} ppm\n")
    print(f"  kappa      Lean  8*q               = {mp.nstr(8 * q, 15)}   (EMPIRICAL, per the .lean)")
    print(f"  kappa      compute det ratio       = {mp.nstr(kappa_gram, 15)}")
    print(f"             differ by a factor of     {mp.nstr((8 * q) / kappa_gram, 6)}\n")

    print("-" * 68)
    print("  And the empirical one fits better")
    print("-" * 68)
    print(f"  Lean    alphaEmInvCorrected = {mp.nstr(a_lean, 15)}   {mp.nstr(ppb(a_lean, CODATA_ALPHA_EM_INV), 6)} ppb")
    print(f"  compute exact resummation   = {mp.nstr(a_comp, 15)}   {mp.nstr(ppb(a_comp, CODATA_ALPHA_EM_INV), 6)} ppb")
    print(f"  CODATA                      = {mp.nstr(CODATA_ALPHA_EM_INV, 15)}")
    print()
    print(f"  Lean vs compute             = {mp.nstr(ppb(a_lean, a_comp), 6)} ppb apart")
    ratio = abs(ppb(a_comp, CODATA_ALPHA_EM_INV)) / abs(ppb(a_lean, CODATA_ALPHA_EM_INV))
    print(f"  the EMPIRICAL-kappa form is {mp.nstr(ratio, 4)}x closer to CODATA")
    print()
    print("  The dashboard (per_observable_100x_status.py) imports")
    print("  alpha_em_inv_derived, i.e. the -467.6 ppb one. So the scorecard's")
    print("  only L2 win rests on the construction that is NOT the paper's cited")
    print("  formalisation, and the cited formalisation is the better fit.")


# ─────────────────────────────────────────────────────────────────────────
# Follow-on (bean qou-aemx, 2026-08-28): are they the same object, and is
# either kappa actually forced?
# ─────────────────────────────────────────────────────────────────────────


def same_function_check(q):
    """Are the two prefactors one function under a reparametrisation? NO.

    Settled symbolically -- it needs no anchor. Lean's is
    `45(q^6-1)/(q^2(q^2-1))`; the compute's is a degree-32 cyclotomic product
    over `q^16`. Evaluated away from q0 they diverge outright.
    """
    L = lambda x: 45 * qbal(3, x)
    C = lambda x: x * qbal(9, x) * qbal(10, x)
    print("-" * 68)
    print("  Same function? Evaluate both away from q0")
    print("-" * 68)
    for x in ["1.0001", "1.05", str(q), "1.5", "2"]:
        xx = mp.mpf(x)
        print(f"  q={x:<20s} Lean={mp.nstr(L(xx), 10):>16s}"
              f"  compute={mp.nstr(C(xx), 10):>16s}"
              f"  ratio={mp.nstr(L(xx) / C(xx), 8)}")
    qx = mp.findroot(lambda x: L(x) - C(x), (q * mp.mpf("0.99"), q * mp.mpf("1.05")),
                     solver="bisect", tol=mp.mpf("1e-40"))
    print()
    print(f"  they CROSS at q* = {mp.nstr(qx, 18)}")
    print(f"  q0               = {mp.nstr(q, 18)}")
    print(f"  q* is {mp.nstr((qx - q) / q * 100, 6)} % from q0 -- the agreement at q0 is")
    print("  where the crossing happens to sit, not shared structure. Both forms")
    print("  target ~137 near the same point, so proximity there is expected and")
    print("  is not evidence for either.")


def kappa_windows(q):
    """Is either kappa FORCED, or merely IN RANGE? (AGENTS.md genericity test.)

    Reports the interval of kappa giving |err| < 100 ppb against CODATA.
    """
    Lbare = 45 * qbal(3, q)
    d = ((1 - 1 / q) ** 4) * qbal(5, q)
    a_lean = lambda k: Lbare * (1 + d + k * d ** 2)

    pi = mp.pi
    cbare = q * qbal(9, q) * qbal(10, q)
    n2 = qbal(2, q)
    c1 = (pi ** 2 * mp.mpf(10) / 9 + pi ** 2 * mp.mpf(16) / 15) * (n2 / 2) \
        * (1 - 1 / q) ** 2 / cbare
    a_comp = lambda K: cbare * (1 + c1 / (1 - c1 * K))

    def window(f):
        lo = mp.findroot(lambda k: ppb(f(k), CODATA_ALPHA_EM_INV) + 100,
                         (mp.mpf(-5), mp.mpf(40)), solver="bisect", tol=mp.mpf("1e-20"))
        hi = mp.findroot(lambda k: ppb(f(k), CODATA_ALPHA_EM_INV) - 100,
                         (mp.mpf(-5), mp.mpf(40)), solver="bisect", tol=mp.mpf("1e-20"))
        return (lo, hi) if lo < hi else (hi, lo)

    print()
    print("-" * 68)
    print("  Is kappa forced, or merely in range?  (|err| < 100 ppb window)")
    print("-" * 68)
    for name, f, claimed in [("Lean  8q", a_lean, 8 * q),
                             ("compute Gram", a_comp, mp.mpf("1.72161420170879"))]:
        lo, hi = window(f)
        rel = (hi - lo) / claimed * 100
        inside = lo < claimed < hi
        print(f"  {name:14s} claimed={mp.nstr(claimed, 10):>14s}"
              f"  window=[{mp.nstr(lo, 8)}, {mp.nstr(hi, 8)}]")
        print(f"  {'':14s} width={mp.nstr(hi - lo, 6)} ({mp.nstr(rel, 4)} % of the claimed value)"
              f"   INSIDE={inside}")
    print()
    print("  Two facts that pull opposite ways, and both belong in the record:")
    print("   * Lean's 8q is INSIDE -- but its window is relatively WIDER, and it")
    print("     also admits the integer 9 (33 ppb). So 8q is IN RANGE, not FORCED.")
    print(f"     Bare kappa=8 -- the file's own 'dim su(3) gluon octet' reading --")
    print(f"     gives {mp.nstr(ppb(a_lean(mp.mpf(8)), CODATA_ALPHA_EM_INV), 6)} ppb and MISSES the window:")
    print("     the q factor does the work, not the 8.")
    print("   * compute's Gram kappa is 10 % OUTSIDE a relatively TIGHTER window.")
    print("     A parameter-free construction that misses is behaving like a")
    print("     prediction -- what an unfitted quantity looks like when it is")
    print("     not quite right.")


if __name__ == "__main__":
    main()
    q = mp.mpf(Q_50_DIGIT_STR)
    same_function_check(q)
    kappa_windows(q)
