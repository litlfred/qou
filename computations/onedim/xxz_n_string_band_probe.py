#!/usr/bin/env python3
# polynomial_q_not_applicable: numeric spectra at fixed anchors; no symbolic-q polynomial output.
"""MEASURE the XXZ n-string band — the positive result `xxz_string_band_probe`
could not reach, and the correction of its one over-scoped claim.

Bean `qou-6b9y`, continuing `computations/onedim/xxz_string_band_probe.py`
(read that first). That probe established the two-magnon bound state IS present
at the substrate in every momentum sector, and honestly reported that it could
NOT extract the band: the k=0 binding fell monotonically with N over N = 8..14
and the substrate/control ratio drifted 54.5 -> 70.2.

## THE BAND, MEASURED

    E_n(k) = -2 (q^n + q^-n - 2 cos k) / [n]_q ,   [n]_q = (q^n - q^-n)/(q - 1/q)

equivalently, with eta = log q  (so Delta = (q + 1/q)/2 = cosh eta),

    E_n(k) = -4 sinh(eta) (cosh(n eta) - cos k) / sinh(n eta)

measured against the vacuum, for H = sum_i (sx sx + sy sy + Delta sz sz) with
PAULI matrices and PERIODIC boundaries. It is validated three independent ways:

  * n = 1 reproduces the ED one-magnon dispersion EXACTLY at every finite N and
    every k (no finite-size correction at all) — a free, non-trivial check that
    the family is normalised correctly;
  * n = 2 is confirmed at the substrate to 1e-13 by pushing N to 4096, and the
    finite-size residual obeys the LAW |E_N - E_inf| ~ z^N with
    z = cos(k/2)/Delta — measured against z^(dN), not merely "small";
  * n = 3 converges to E_3(0) at a q = 3 control.

The two-magnon binding above the two-magnon continuum is

    B(k) = 4 (Delta - |cos(k/2)|)^2 / Delta ,      B(0) = 2 q^2 hbar_q^4 / [2]_q

with hbar_q = 1 - 1/q the substrate's own quantum. B(0) is 1.180983e-4 at q0
against exactly 0.2 at the q = 2 control — a ratio of 1693.5, i.e. 3.23 orders
of magnitude, not the "1.5 to 2" the earlier probe read off its N <= 14 table
(CHECK 12). That table's 54.5 -> 70.2 was a floor drifting towards 1693.5.

## WHY THE EARLIER PROBE COULD NOT SEE IT (its diagnosis was RIGHT)

The bound state's spatial extent is xi = 1/log(Delta) sites — 184.0 at q0
against 4.48 at the q = 2 control. The ring-wrapping error is ~z^N. At N = 14
the measured binding overstates the thermodynamic value by a factor of ~29, and
the N needed for 1% is ~1100. So the non-convergence was real and is now a
quantified mechanism, not slow convergence of an otherwise-sound measurement.

The suspected bug — that the finite-N continuum edge was the artifact — is NOT
the bug at k = 0, where every number in that probe's table lives: CHECK 3
measures the finite-N edge there to be the thermodynamic edge 8 - 8*Delta
EXACTLY, because the pair (a, -a) contains a = 0. So the non-convergence is not
an edge-definition error.

## BUT THE EDGE *IS* AN ARTIFACT AWAY FROM k = 0, AND IT MANUFACTURED A RESULT

In ODD momentum sectors the finite-N edge is depressed by
8|cos(pi m/N)|(1 - cos(pi/N)) — 0.195 at N = 14, m = 1, which is 53x the true
binding there (CHECK 3b). Measured against the THERMODYNAMIC edge instead
(CHECK 4/4b), the earlier probe's "a level above the two-magnon continuum in
EVERY momentum sector, at the substrate" does NOT hold: at N = 8, 10, 12, 14 the
m = 1 and m = N-1 sectors sit BELOW the true edge by 0.19 to 0.55, and were
counted only because the edge they were compared against was depressed further
still. The controls are unaffected — every sector is genuine there.

The mechanism is a box, not a tolerance. For N even and m ODD the r = N/2
symmetrised state vanishes identically, so the relative coordinate is a hard
Dirichlet box of N/2 - 1 sites; at the substrate that is 3..6 sites against a
bound state of extent xi = 184, and the confinement pushes the level below the
edge. CHECK 4c shows it is exactly that: at N = 1024 (box 511 > xi) all nine
sampled sectors recover, odd m included, and match E_2(k) to 1e-6.

So the earlier probe's CHECK 2 stands at the controls and in the EVEN sectors at
the substrate, and is an artifact in the two extreme odd sectors of each N. Its
headline conclusion — that the bound state is present at q0 — survives, because
the even sectors (k = 0 included) are genuine.

## THE "REFUTED" FORMULA IS NOT REFUTED — IT WAS THE WRONG VARIABLE

`xxz_string_band_probe` records `-2 sinh(eta) sinh(2 eta)/(cosh 2eta - cos k)`
as REFUTED ("gives -2.5 at q=2, k=0 against a measured +0.288"). Both numbers
are right and the verdict is over-scoped. Measured in CHECK 9:

  * that expression is exactly HALF the n = 2 string energy written in the
    string-centre RAPIDITY lambda, i.e. E_2^rap(lambda)
    = -4 sinh(eta) sinh(2 eta)/(cosh 2eta - cos lambda);
  * lambda is NOT the total momentum. They are related by
    cosh(n eta) - cos lambda = sinh^2(n eta)/(cosh(n eta) - cos k), and
    lambda(k = 0) = pi, not 0. Substituting k for lambda at k = 0 evaluates the
    band at the OPPOSITE end of its own zone;
  * supplied with lambda(k) and the factor 2 it reproduces E_2(k) identically.

So this is a scope-(a) negative ("this expression, as applied, does not
describe the data"), never a scope-(b) exclusion. The comparison number +0.288
in that docstring is also the N = 10 row, not N = 8 (0.341), and neither is the
thermodynamic binding 0.2.

## WHAT THIS IS AND IS NOT ABOUT (scope, before anything is carried onward)

The numerator q^n + q^-n is the Temperley-Lieb loop parameter delta = q + 1/q at
level n, and the denominator [n]_q is the quantum dimension, so the band reads
E_n(k) = -2(delta_n - 2 cos k)/[n]_q with delta_n = q^n + q^-n. That is a
suggestive shape for this corpus and it is NOT a measured bridge to the Hecke
tower. `tl_is_the_xxz_chain_probe` identifies TL_n(delta) with the
U_q(sl_2)-symmetric OPEN chain plus a boundary field
((q - 1/q)/2)(sz_1 - sz_n); the Hamiltonian diagonalised HERE is the PERIODIC
chain with no boundary term. The two differ by boundary operators.

  MEASURED 2026-09-15 (`tl_open_chain_string_band_probe.py`, 24/24, 50 dps,
  both pins). This paragraph used to continue "which do not change a bulk band
  in the thermodynamic limit — but that step is an argument, not something this
  probe measured". The argument has now been run, and it is **right about the
  BAND and incomplete about the SPECTRUM**:

  * **Right about the band.** At controls where the correlation length is small
    (q = 3, xi = 1.96), inverting the open chain's levels through the PERIODIC
    E_2(k) returns an evenly spaced ladder with one common L_eff — the open
    chain reproduces the WHOLE band, not merely its edge (10 levels clear the
    continuum at N = 24, ladder spread 3.9 %). The n = 3 band is there too.
  * **Incomplete about the spectrum, twice over.** The boundary operators ADD A
    STATE the ring does not have — at E = 0, degenerate with the vacuum, ABOVE
    the entire n = 2 band, in every magnon sector, exponentially localised at
    one end with amplitude ratio exactly 1/q and decay length 1/ln q = 9.584
    sites. It is the U_q(sl_2) descendant of the ferromagnetic vacuum and is
    NOT a finite-size effect. And they REMOVE MOMENTUM: only the k -> 0 edge
    survives an extremal search, and the ring's exponential z^N convergence
    becomes a power law.
  * **Also measured, and it is why the open route cannot replace this one at
    the substrate**: at q_0 the correlation length is xi = 1/ln(Delta) = 184
    SITES, so a box admitting even one level below the thermodynamic two-magnon
    edge needs N ~ 291 — far beyond dense ED. At N <= 24 the open chain does
    not resolve the string at all, and its finite-N edge manufactures an
    apparent positive. Scope (a).

  So the periodic band IS the TL chain's band; the periodic SPECTRUM is not the
  TL chain's spectrum. This probe's own formula stands.

Nothing here identifies the chain's sites with anything physical.

## METHOD

The m = 2 sector at fixed momentum reduces exactly to a real-symmetric
TRIDIAGONAL matrix in the relative coordinate r = 1..floor(N/2) — dimension
~N/2 rather than ~N^2/2 — whose top eigenvalue is found by Sturm-sequence
bisection in O(N) per evaluation. That is what makes N = 4096 cheap where dense
ED stalled at N = 14. CHECK 1 validates the reduction AND the Sturm solver
against `_xxz_momentum_ed.block` (the earlier probe's ED) in every momentum
sector at three anisotropies; nothing below is trusted until that passes.

Read-only: writes no witness, runs no producer.
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mpmath import (mp, mpf, nstr, pi, cos, sin, sinh, cosh, log, sqrt,  # noqa: E402
                    eighe, acos)
from qou_substrate.constants import q_at  # noqa: E402
from _xxz_momentum_ed import orbit_data, block, spectrum  # noqa: E402

mp.dps = 40

STURM_TOL = mpf(10) ** (-30)


# ---------------------------------------------------------------- the reduction

def tridiag(N, m, Delta):
    """Real-symmetric tridiagonal for the two-magnon momentum-m block.

    Relative coordinate r = n2 - n1.  Energies measured RELATIVE to the all-up
    vacuum.  Derived, not quoted; CHECK 1 validates it against the dense ED.

      diagonal   -8 Delta, except -4 Delta at r = 1 (the two down spins share a
                 bond, so only two of the four sigma^z sigma^z bonds flip)
      hopping    4 cos(k/2) in the gauge |r~> = exp(-i k r/2)|r; k>
      boundary   N even, m even : the r = N/2 orbit has period N/2, giving the
                                  last hop 4 cos(k/2) sqrt(2)
                 N even, m odd  : the r = N/2 symmetrised state VANISHES, so the
                                  chain simply truncates at r = N/2 - 1
                 N odd          : both up-hops from r = (N-1)/2 return to it,
                                  adding 4 cos(k/2) (-1)^m to that diagonal
    """
    c = cos(pi * mpf(m) / N)                       # = cos(k/2), k = 2 pi m / N
    if N % 2 == 1:
        R = (N - 1) // 2
    else:
        R = N // 2 if m % 2 == 0 else N // 2 - 1
    a = [(-8 * Delta if r >= 2 else -4 * Delta) for r in range(1, R + 1)]
    b = [4 * c for _ in range(R - 1)]
    if N % 2 == 1:
        a[R - 1] = a[R - 1] + 4 * c * (1 if m % 2 == 0 else -1)
    elif m % 2 == 0 and R >= 2:
        b[R - 2] = 4 * c * sqrt(mpf(2))
    return a, b


def sturm_count(a, b, lam):
    """Number of eigenvalues of the tridiagonal strictly below `lam`."""
    tiny = mpf(10) ** (-(mp.dps + 20))
    d = a[0] - lam
    cnt = 1 if d < 0 else 0
    for i in range(1, len(a)):
        if d == 0:
            d = tiny
        d = (a[i] - lam) - b[i - 1] ** 2 / d
        if d < 0:
            cnt += 1
    return cnt


def eig_from_top(a, b, j=0, tol=STURM_TOL):
    """j-th largest eigenvalue (j = 0 is the largest), by Sturm bisection."""
    n = len(a)
    target = n - 1 - j
    span = 2 * max(abs(x) for x in b) + 1 if b else mpf(1)
    lo, hi = min(a) - span, max(a) + span
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if sturm_count(a, b, mid) > target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


# ------------------------------------------------------------- the band formula

def q_int(n, q):
    """Balanced q-integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def E_string_q(n, q, k):
    """n-string band in q-form:  -2 (q^n + q^-n - 2 cos k) / [n]_q."""
    return -2 * (q ** n + q ** (-n) - 2 * cos(k)) / q_int(n, q)


def E_string_eta(n, eta, k):
    """Same band in eta-form: -4 sinh(eta)(cosh(n eta) - cos k)/sinh(n eta)."""
    return -4 * sinh(eta) * (cosh(n * eta) - cos(k)) / sinh(n * eta)


def E_string_rapidity(n, eta, lam):
    """n-string energy as a function of the string-CENTRE RAPIDITY lambda:
    sum_j eps(lambda + i(n+1-2j) eta) = -4 sinh(eta) sinh(n eta)/(cosh n eta - cos lambda)."""
    return -4 * sinh(eta) * sinh(n * eta) / (cosh(n * eta) - cos(lam))


def lam_of_k(n, eta, k):
    """Invert cosh(n eta) - cos lambda = sinh^2(n eta)/(cosh(n eta) - cos k)."""
    cl = cosh(n * eta) - sinh(n * eta) ** 2 / (cosh(n * eta) - cos(k))
    return acos(cl)


def continuum_top(Delta, k):
    """Thermodynamic-limit top of the two-magnon continuum at total momentum k."""
    return 8 * abs(cos(k / 2)) - 8 * Delta


def binding(Delta, k):
    return 4 * (Delta - abs(cos(k / 2))) ** 2 / Delta


def herm_spectrum(H):
    return sorted(eighe(H, eigvals_only=True))


def one_magnon(N, Delta):
    reps, info = orbit_data(N, 1)
    out = {}
    for r in range(N):
        H, _ = block(N, 1, r, Delta, reps, info)
        sp = spectrum(H)
        assert len(sp) == 1, (r, len(sp))
        out[r] = sp[0] - Delta * N
    return out


# ------------------------------------------------------------------------ main

def main():
    checks, failures = 0, []
    t_start = time.monotonic()

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
        if not ok:
            failures.append(name)

    def tick(msg):
        print(f"    ... {msg}  [{int(time.monotonic() - t_start)}s]")

    Q0 = q_at(mp.dps)
    ANCHORS = [("substrate q0", Q0), ("control q=2", mpf(2)), ("control q=3", mpf(3))]

    print("XXZ n-string band: MEASURED (bean qou-6b9y, continuing "
          "xxz_string_band_probe)\n")
    for lab, q in ANCHORS:
        eta = log(q)
        D = (q + 1 / q) / 2
        print(f"  {lab:<13} q = {nstr(q, 20):<24} Delta = cosh(log q) = {nstr(D, 20)}")
        assert abs(cosh(eta) - D) < mpf(10) ** (-(mp.dps - 5))
    print("  (eta = log q exactly, since Delta = (q + 1/q)/2 = cosh(log q))\n")

    # ---- CHECK 1: the reduction + Sturm solver vs the earlier probe's dense ED
    worst = mpf(0)
    for N in (8, 9, 10, 11, 12, 13, 14):
        for _lab, q in ANCHORS:
            Delta = (q + 1 / q) / 2
            reps, info = orbit_data(N, 2)
            for m in range(N):
                H, D = block(N, 2, m, Delta, reps, info)
                ref = sorted((v - Delta * N for v in herm_spectrum(H)), reverse=True)
                a, b = tridiag(N, m, Delta)
                if len(a) != D:
                    worst = mpf(1)
                    break
                for j in range(min(3, D)):
                    worst = max(worst, abs(eig_from_top(a, b, j) - ref[j]))
        tick(f"CHECK 1 done N={N}")
    check("1. the relative-coordinate reduction + Sturm bisection reproduce the "
          "dense momentum-block ED",
          worst < mpf(10) ** (-28),
          f"worst |Sturm - eig| over N=8..14, all m, 3 anisotropies, top-3 = {nstr(worst, 6)}")

    # ---- CHECK 2: n = 1 is exact at every finite N
    worst1 = mpf(0)
    for N in (8, 9, 12, 13, 16):
        for _lab, q in ANCHORS:
            Delta = (q + 1 / q) / 2
            e1 = one_magnon(N, Delta)
            for r in range(N):
                k = 2 * pi * mpf(r) / N
                worst1 = max(worst1, abs(e1[r] - E_string_q(1, q, k)))
    check("2. n=1: the band formula reproduces the ED one-magnon dispersion "
          "EXACTLY at finite N",
          worst1 < mpf(10) ** (-25),
          f"worst |ED - E_1(k)| over N=8,9,12,13,16, all k, 3 anisotropies = {nstr(worst1, 6)}")

    # ---- CHECK 3: is the finite-N continuum edge the artifact?  (k=0: NO)
    print("\n  finite-N two-magnon continuum edge vs the thermodynamic edge"
          "  (the earlier probe's suspected bug):")
    print("      N  m |  finite-N edge - thermodynamic edge |  true binding B(k) at q0")
    exact_at_k0, deficit_odd = True, []
    for N in (8, 10, 12, 14):
        Delta = (Q0 + 1 / Q0) / 2
        e1 = one_magnon(N, Delta)
        for m in (0, 1):
            hi_N = max(e1[a] + e1[(m - a) % N] for a in range(N))
            k = 2 * pi * mpf(m) / N
            dev = hi_N - continuum_top(Delta, k)
            if m == 0 and abs(dev) > mpf(10) ** (-25):
                exact_at_k0 = False
            if m == 1:
                deficit_odd.append((N, -dev, binding(Delta, k)))
            print(f"    {N:3d} {m:2d} | {nstr(dev, 10):>34} | {nstr(binding(Delta, k), 10)}")
    check("3. at k=0 the finite-N edge IS the thermodynamic edge, exactly — the "
          "suspected bug is not there",
          exact_at_k0,
          "the pair (a,-a) contains a=0, so no discretisation deficit at m=0")
    ratios = [d / b for _N, d, b in deficit_odd]
    check("3b. but in ODD sectors the finite-N edge IS depressed, by far more "
          "than the binding it is used to detect",
          all(r > 10 for r in ratios),
          f"m=1 deficit / true binding = {nstr(min(ratios), 6)} .. {nstr(max(ratios), 6)}"
          f" over N=8..14")

    # ---- CHECK 4: re-run the earlier probe's sector count against the STRICTER
    #      edge.  It does NOT survive at the substrate, and the shortfall is
    #      exactly the sectors whose box is smaller than the bound state.
    print("\n  sectors carrying a level above the continuum: against the FINITE-N "
          "edge (the earlier probe's CHECK 2) vs the THERMODYNAMIC edge:")
    print("      anisotropy    N | finite-N edge | thermodynamic edge | false positives")
    counts, sub_bad = {}, []
    for lab, q in ANCHORS:
        Delta = (q + 1 / q) / 2
        for N in (8, 10, 12, 14):
            e1 = one_magnon(N, Delta)
            n_fin = n_thm = 0
            for m in range(N):
                a, b = tridiag(N, m, Delta)
                k = 2 * pi * mpf(m) / N
                e = eig_from_top(a, b)
                if e > max(e1[x] + e1[(m - x) % N] for x in range(N)):
                    n_fin += 1
                if e > continuum_top(Delta, k):
                    n_thm += 1
                elif lab == "substrate q0":
                    sub_bad.append((N, m))
            counts[(lab, N)] = (n_fin, n_thm)
            print(f"      {lab:<13}{N:3d} |    {n_fin:2d} / {N:<2d}     |      {n_thm:2d} / {N:<2d}"
                  f"        |  {n_fin - n_thm}")
        tick(f"CHECK 4 done {lab}")
    ctrl_ok = all(counts[(lab, N)] == (N, N)
                  for lab in ("control q=2", "control q=3") for N in (8, 10, 12, 14))
    check("4. the controls DO carry a level above the thermodynamic edge in every "
          "sector — their bound states fit in the ring",
          ctrl_ok, "q=2 and q=3, N=8,10,12,14, all m")
    odd_only = all(m % 2 == 1 for _N, m in sub_bad)
    check("4b. NEGATIVE, ASSERTED: at the SUBSTRATE the earlier probe's "
          "'every momentum sector' is partly an artifact of the depressed "
          "finite-N edge",
          bool(sub_bad) and odd_only,
          f"{len(sub_bad)} sector(s) sit BELOW the thermodynamic edge, all with m ODD "
          f"(N even + m odd kills the r=N/2 state, so the relative coordinate is a hard "
          f"box of N/2-1 < xi sites): " +
          ", ".join(f"N={N} m={m}" for N, m in sub_bad))

    # ---- CHECK 4c: the artifact is a BOX effect and it goes away once the box fits
    big_bad, big_worst = [], mpf(0)
    Delta0_ = (Q0 + 1 / Q0) / 2
    for m in (1, 2, 3, 5, 17, 64, 129, 256, 511):
        a, b = tridiag(1024, m, Delta0_)
        k = 2 * pi * mpf(m) / 1024
        e = eig_from_top(a, b)
        if not e > continuum_top(Delta0_, k):
            big_bad.append(m)
        big_worst = max(big_worst, abs(e - E_string_q(2, Q0, k)))
    check("4c. and it IS a box effect: at N=1024 (box 511 > xi = 184) every "
          "sampled sector recovers, odd m included",
          not big_bad and big_worst < mpf(10) ** (-5),
          f"9 sampled m at the substrate: {len(big_bad)} below the edge; "
          f"worst |E_N - E_2(k)| = {nstr(big_worst, 6)}")
    tick("CHECK 4c done")

    # ---- CHECK 5/6: n = 2 convergence and the z^N law
    print("\n  n=2 band at k=0: finite-N top eigenvalue vs E_2(0), and the "
          "ring-wrapping law |E_N - E_inf| ~ z^N, z = 1/Delta")
    law_dev, final_res = [], {}
    for lab, q in ANCHORS:
        Delta = (q + 1 / q) / 2
        z = 1 / Delta
        E_inf = E_string_q(2, q, mpf(0))
        B_inf = binding(Delta, mpf(0))
        xi = 1 / log(Delta)
        print(f"\n   {lab}:  E_2(0) = {nstr(E_inf, 25)}")
        print(f"      binding above continuum B(0) = {nstr(B_inf, 22)}"
              f"   z = {nstr(z, 12)}   xi = 1/log(Delta) = {nstr(xi, 8)}")
        Ns = ((8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096) if lab == "substrate q0"
              else (8, 16, 32, 48, 64, 96, 128, 192))
        prev = None
        for N in Ns:
            a, b = tridiag(N, 0, Delta)
            e = eig_from_top(a, b)
            res = e - E_inf
            line = (f"      N={N:5d} dim={len(a):5d}  E_N - E_2(0) = {nstr(res, 8):>14}")
            # the law is asymptotic, and below ~1e-25 the residual is round-off
            # (|E| ~ 4 at dps 40, Sturm tolerance 1e-30), so admit a pair only
            # when BOTH endpoints sit inside that window.
            if (prev is not None and mpf(10) ** (-25) < prev < mpf(10) ** (-6)
                    and mpf(10) ** (-25) < res):
                pred = z ** (N - prev_N)
                rel = abs(res / prev - pred) / pred
                law_dev.append(rel)
                line += (f"   ratio = {nstr(res / prev, 8):>13}   z^{N - prev_N}"
                         f" = {nstr(pred, 8):>13}   rel dev {nstr(rel, 4)}")
            print(line)
            prev, prev_N = res, N
        final_res[lab] = (prev, B_inf, E_inf, xi)
        tick(f"CHECK 5 done {lab}")

    check("5. the n=2 band is CONVERGED at the substrate: |E_N - E_2(0)| < 1e-12",
          final_res["substrate q0"][0] < mpf(10) ** (-12),
          f"residual {nstr(final_res['substrate q0'][0], 6)} at N=4096, "
          f"against a binding of {nstr(final_res['substrate q0'][1], 6)}")
    check("6. the finite-size residual obeys the LAW |E_N - E_inf| ~ z^N, "
          "z = cos(k/2)/Delta, to better than 1%",
          bool(law_dev) and max(law_dev) < mpf(1) / 100,
          f"worst relative deviation from z^dN over {len(law_dev)} consecutive "
          f"pairs = {nstr(max(law_dev), 6)}")

    # ---- CHECK 7: nonzero k
    worst7 = mpf(0)
    print("\n  n=2 at NONZERO k (both parities of m), substrate and q=2 control:")
    for lab, q in (("substrate q0", Q0), ("control q=2", mpf(2))):
        Delta = (q + 1 / q) / 2
        N = 4096 if lab == "substrate q0" else 256
        for m in (1, 2, 3, N // 8, N // 4, N // 2 - 1):
            a, b = tridiag(N, m, Delta)
            k = 2 * pi * mpf(m) / N
            d = abs(eig_from_top(a, b) - E_string_q(2, q, k))
            worst7 = max(worst7, d)
            print(f"      {lab}  N={N} m={m:<5} k/pi={nstr(k / pi, 8):>12}"
                  f"   |E_N - E_2(k)| = {nstr(d, 6)}")
        tick(f"CHECK 7 done {lab}")
    check("7. E_2(k) holds at nonzero k too, both parities of m",
          worst7 < mpf(10) ** (-10),
          f"worst |E_N - E_2(k)| = {nstr(worst7, 6)}")

    # ---- CHECK 8: n = 3
    print("\n  n=3 at the q=3 control, k=0, top eigenvalue of the m=3 momentum block:")
    q3 = mpf(3)
    D3 = (q3 + 1 / q3) / 2
    E3 = E_string_q(3, q3, mpf(0))
    print(f"      E_3(0) = {nstr(E3, 22)}")
    res3, prev3 = [], None
    for N in (9, 12, 15, 18, 21):
        reps, info = orbit_data(N, 3)
        H, D = block(N, 3, 0, D3, reps, info)
        top = herm_spectrum(H)[-1] - D3 * N
        r = top - E3
        res3.append(r)
        print(f"      N={N:3d} dim={D:4d}  top = {nstr(top, 20):>24}"
              f"   top - E_3(0) = {nstr(r, 8):>14}"
              f"   ratio = {nstr(r / prev3, 6) if prev3 else '-':>10}")
        prev3 = r
        tick(f"CHECK 8 done N={N}")
    check("8. n=3: the m=3 block's top level converges to E_3(0), monotonically "
          "and geometrically",
          all(res3[i] > res3[i + 1] > 0 for i in range(len(res3) - 1))
          and res3[-1] < mpf(10) ** (-5),
          f"residual {nstr(res3[0], 6)} -> {nstr(res3[-1], 6)} over N=9..21")

    # ---- CHECK 9: re-scope the "REFUTED" candidate
    print("\n  the candidate recorded as REFUTED, re-measured:")
    worst9a, worst9b = mpf(0), mpf(0)
    for lab, q in ANCHORS:
        eta = log(q)
        for m, N in ((0, 8), (1, 8), (3, 16), (7, 16)):
            k = 2 * pi * mpf(m) / N
            lam = lam_of_k(2, eta, k)
            cand = -2 * sinh(eta) * sinh(2 * eta) / (cosh(2 * eta) - cos(lam))
            worst9a = max(worst9a, abs(cand - E_string_rapidity(2, eta, lam) / 2))
            worst9b = max(worst9b, abs(2 * cand - E_string_q(2, q, k)))
    q2, eta2 = mpf(2), log(mpf(2))
    cand_at_k0 = -2 * sinh(eta2) * sinh(2 * eta2) / (cosh(2 * eta2) - cos(mpf(0)))
    lam0 = lam_of_k(2, eta2, mpf(0))
    print(f"      q=2: candidate evaluated at k=0 gives {nstr(cand_at_k0, 10)}"
          f"  (= -2 Delta; the earlier probe's -2.5)")
    print(f"      q=2: the CORRECT argument at k=0 is lambda = {nstr(lam0, 12)}"
          f" = pi, not 0; then 2 x candidate = {nstr(2 * (-2 * sinh(eta2) * sinh(2 * eta2) / (cosh(2 * eta2) - cos(lam0))), 12)}"
          f" = E_2(0) = {nstr(E_string_q(2, q2, mpf(0)), 12)}")
    check("9. the 'refuted' candidate is HALF the n=2 string energy in the "
          "string-centre rapidity lambda",
          worst9a < mpf(10) ** (-25),
          f"worst |candidate(lam) - E_2^rap(lam)/2| = {nstr(worst9a, 6)}")
    check("9b. supplied with lambda(k) and the factor 2 it reproduces the "
          "measured band identically — a scope-(a) negative, not a refutation",
          worst9b < mpf(10) ** (-25),
          f"worst |2 x candidate(lam(k)) - E_2(k)| = {nstr(worst9b, 6)}")

    # ---- CHECK 10: the q-form / hbar_q identity
    worst10 = mpf(0)
    for _lab, q in ANCHORS:
        eta = log(q)
        hbar = 1 - 1 / q
        for n in (1, 2, 3, 4, 5):
            for m in (0, 1, 5):
                k = 2 * pi * mpf(m) / 16
                worst10 = max(worst10, abs(E_string_q(n, q, k) - E_string_eta(n, eta, k)))
        Delta = (q + 1 / q) / 2
        worst10 = max(worst10,
                      abs(binding(Delta, mpf(0)) - 2 * q ** 2 * hbar ** 4 / q_int(2, q)))
    check("10. the q-form, the eta-form and B(0) = 2 q^2 hbar_q^4 / [2]_q agree",
          worst10 < mpf(10) ** (-25),
          f"worst discrepancy over n=1..5, 3 anisotropies = {nstr(worst10, 6)}")

    # ---- CHECK 11: the surviving NEGATIVE — dense ED cannot reach the substrate
    Delta0 = (Q0 + 1 / Q0) / 2
    B0 = binding(Delta0, mpf(0))
    e1 = one_magnon(14, Delta0)
    hi14 = max(e1[a] + e1[(0 - a) % 14] for a in range(14))
    a14, b14 = tridiag(14, 0, Delta0)
    meas14 = eig_from_top(a14, b14) - hi14
    overstate = meas14 / B0
    N_1pct = None
    for N in (512, 768, 1024, 1152, 1280, 1536):
        a, b = tridiag(N, 0, Delta0)
        if (eig_from_top(a, b) - E_string_q(2, Q0, mpf(0))) < B0 / 100:
            N_1pct = N
            break
    print(f"\n  the earlier probe's N=14 substrate binding {nstr(meas14, 12)} vs the "
          f"thermodynamic {nstr(B0, 12)}")
    check("11. NEGATIVE, ASSERTED: dense momentum-block ED at N <= 14 cannot "
          "resolve the substrate band — it overstates the binding by >25x",
          overstate > 25 and N_1pct is not None and N_1pct > 14,
          f"N=14 overstates by {nstr(overstate, 6)}x; xi = {nstr(1 / log(Delta0), 8)} "
          f"sites; smallest tested N reaching 1% is {N_1pct}")

    # ---- CHECK 12: the earlier probe's control/substrate RATIO was a floor
    D2_, D3_ = (mpf(2) + mpf(1) / 2) / 2, (mpf(3) + mpf(1) / 3) / 2
    r2 = binding(D2_, mpf(0)) / B0
    r3 = binding(D3_, mpf(0)) / B0
    print(f"\n  k=0 binding ratio control/substrate: the earlier probe measured "
          f"54.5 -> 70.2 over N=8..14 and called it 1.5-2 orders of magnitude.")
    print(f"      thermodynamic ratio q=2 / q0 = {nstr(r2, 12)}   "
          f"(log10 = {nstr(log(r2) / log(mpf(10)), 6)})")
    print(f"      thermodynamic ratio q=3 / q0 = {nstr(r3, 12)}   "
          f"(log10 = {nstr(log(r3) / log(mpf(10)), 6)})")
    check("12. that ratio was a FLOOR, not the answer: the true q=2/q0 separation "
          "is 3.2 orders of magnitude, not 1.5-2",
          r2 > 1000 and r2 / 70 > 20,
          f"{nstr(r2, 8)} against the N=14 reading of 70.2 — a factor "
          f"{nstr(r2 / mpf('70.2'), 6)} still to run")

    # ---------------------------------------------------------------- the band
    print("\n  THE SUBSTRATE n-STRING BAND (q0 = proton pin, production default):")
    eta0 = log(Q0)
    print(f"      eta0 = log q0 = {nstr(eta0, 25)}")
    for n in (1, 2, 3):
        print(f"      n={n}: [{n}]_q = {nstr(q_int(n, Q0), 20)}"
              f"   E_{n}(0) = {nstr(E_string_q(n, Q0, mpf(0)), 22)}"
              f"   E_{n}(pi) = {nstr(E_string_q(n, Q0, pi), 22)}")
    print(f"      n=2 binding above the two-magnon continuum:"
          f"  B(0)  = {nstr(binding(Delta0, mpf(0)), 22)}")
    print(f"                                                 "
          f"  B(pi) = {nstr(binding(Delta0, pi), 22)}  (= 4 Delta0)")

    print(f"\n{checks - len(failures)}/{checks} checks pass "
          f"[{int(time.monotonic() - t_start)}s]")
    print("""
VERDICT
  The n-string band IS extracted:  E_n(k) = -2 (q^n + q^-n - 2 cos k)/[n]_q,
  validated exactly at n=1 for every finite N, to 1e-13 at n=2 at the substrate
  (N = 4096), and to ~3e-6 at n=3 at a q=3 control. The two-magnon binding above
  the continuum is B(k) = 4(Delta - |cos(k/2)|)^2/Delta, with
  B(0) = 2 q^2 hbar_q^4/[2]_q.
  The earlier probe's non-convergence diagnosis was CORRECT and is now a
  quantified mechanism (xi = 1/log Delta = 184 sites at q0, ring error ~z^N),
  not a measurement artifact -- the k=0 continuum edge it used is exact.
  Two of its claims ARE re-scoped. 'a level above the continuum in EVERY
  momentum sector, at the substrate' is an artifact in the m=1 and m=N-1 sectors,
  where the finite-N edge is depressed by more than the binding and the relative
  coordinate is a box smaller than the bound state; the even sectors, k=0
  included, are genuine and carry the conclusion. And the 'REFUTED' verdict on
  the candidate formula becomes a scope-(a) negative: the candidate is the same
  object in the string-centre rapidity, at half this Hamiltonian's
  normalisation.""")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
