#!/usr/bin/env python3
# polynomial_q_not_applicable: numeric spectra at fixed anchors; no symbolic-q polynomial output.
"""The n-string band on the OPEN chain the TL identification actually names —
measured, and compared with the PERIODIC band that was measured instead.

## The gap this closes

Two probes in this directory are about DIFFERENT chains, and neither says so in
its verdict:

  * `tl_is_the_xxz_chain_probe` (17/17) verifies, as an exact matrix identity,
        -2 sum_{i=1}^{N-1} e_i = H_XXZ^open - Delta (N-1) I - ((q-1/q)/2)(sz_1 - sz_N)
    i.e. TL_N(delta) at delta = q + 1/q IS the OPEN U_q(sl2)-symmetric XXZ chain
    plus a surface field.  Momentum is not a good quantum number there.
  * `xxz_n_string_band_probe` (16/16) extracts E_n(k) = -2(q^n + q^-n - 2cos k)/[n]_q
    and B(k) = 4(Delta - |cos(k/2)|)^2/Delta by momentum-block ED of the
    PERIODIC ring.

That probe's own scope note flags the mismatch and says the step across it is
"an argument, not something this probe measured".  This probe measures it.

## Convention, stated once because every sign below depends on it

H_TL := -2 sum_i e_i.  Each e_i is delta times a projector, so H_TL <= 0, and
the ferromagnetic vacuum (annihilated by every e_i) sits at E = 0 at the TOP of
the spectrum.  Binding is therefore measured UPWARD: a bound state lies ABOVE
its continuum.  The k = 0 end of E_n(k) is the band's least-negative edge and
carries the small gap B(0); the k = pi end is the most-negative edge and carries
B(pi) = 4 Delta.  The open chain is the i = 1..N-1 sum, the periodic chain the
i = 1..N ring sum (whose surface terms telescope to zero) -- one operator
family, two ranges.

## MEASURED — the four findings

1. **The Hamiltonian IS Hermitian.**  The surface field ((q-1/q)/2)(sz_1 - sz_N)
   is reflection-ODD, not anti-Hermitian: it is diagonal with real entries for
   real q > 1, so H_TL^open is real symmetric in the sz basis and ||H - H^T||
   is identically 0 (CHECK 2).  "Band" language is safe.  What the surface term
   does break is spatial reflection, ||H - P H P|| =/= 0 (CHECK 3).

2. **The open chain HAS a state the periodic chain does not**, in every magnon
   sector, at E = 0 -- degenerate with the vacuum, at the very top of the
   spectrum, above the whole n = 2 band.  It is the U_q(sl2) descendant of the
   ferromagnetic vacuum and it is exponentially localised at ONE end: in the
   one-magnon sector its amplitudes are exactly a geometric sequence of ratio
   1/q (CHECK 7), decay length 1/ln q = 9.5839859734 sites at the proton pin.
   The periodic chain has no zero mode in any m >= 1 sector (CHECK 8).

3. **The open one-magnon sector is exact at every N**, with no finite-size
   correction to the dispersion at all:
        spec = {0} u { -4 Delta + 4 cos(pi m / N) : m = 1..N-1 }
   (CHECK 6, residual at the 1e-49 diagonalisation floor).  The open chain
   samples the SAME cosine on the half-integer grid k = pi m/N -- finer than the
   ring's 2 pi r/N -- but cannot reach k = 0 or k = pi.

4. **The band survives the boundary field; the open chain reproduces the whole
   n = 2 band, sampled at quantised momenta** -- but only where the string is
   short compared with the box.  Inverting each level of the U_q block
   W_{N/2-2} through the PERIODIC formula E_2(k) returns an evenly spaced
   ladder k_m ~ pi m / L_eff with a single L_eff ~ N - 3 (CHECK 11).  The
   convergence of the band edge is a POWER LAW, measured local exponent -> 2
   (CHECK 12), not the exponential z^N of the ring: the residual is not an error
   but the band's own curvature between k = 0 and the smallest momentum the box
   admits.

## MEASURED — and the honest negative

At the substrate the extraction fails, and the reason is size, not the boundary
field.  The two-magnon bound state's extent is xi = 1/ln(Delta) = 184.04 sites
at the proton pin.  For even ONE open-chain level to clear the thermodynamic
two-magnon continuum edge, the box must admit k < 2 arccos(sqrt(1-(Delta-1)^2)),
which needs N ~ 291 (CHECK 14) -- far beyond dense ED.  At N <= 24 the top of
W_{N/2-2} sits ABOVE the finite-N two-magnon edge (apparently bound) and BELOW
the thermodynamic edge (not bound at all).  That is the finite-size-threshold
artifact recorded for this same chain family, re-measured here: the apparent
binding is the depression of the edge, not a level (CHECK 15).

The band BOTTOM is not extractable from the open chain at any N, for a reason
that is arithmetic rather than numerical: E_2(pi) = -4 Delta is strictly ABOVE
the two-magnon continuum bottom -8 Delta - 8 for every Delta > 0, so the k = pi
band edge is strictly INTERIOR to the spectrum and no extremal search reaches
it (CHECK 16).  Momentum is what separated it on the ring, and the open chain
does not have it.

## What this does NOT claim

* No scope-(b) structural exclusion is claimed anywhere in this probe.  Every
  negative here is scope (a): "this construction, at these sizes, did not
  reproduce the numbers."  CHECK 16 names an elementary invariant
  (-4 Delta > -8 Delta - 8 for Delta > 0) but it excludes an EXTRACTION ROUTE,
  not any physical ingredient, so it is not a scope-(b) refutation of anything.
* Nothing here identifies the chain's sites with anything physical, and nothing
  here is wired to production.  E_n(k) is quoted only as the periodic probe's
  measured formula, used as the reference curve to test against.
* Agreement at 1e-49 is the floor of the 50-dps diagonalisation and is reported
  as such, never as "exact" or "to N digits".
* The effective box length L_eff ~ N - 3 is DESCRIPTIVE -- a number read off the
  measured ladder, not derived.  It drifts with the level index at the few-per-
  cent level and that drift is reported, not fitted away.

## METHOD

Everything is done inside one magnon sector at a time.  (C^2)^{otimes N} splits
as a U_q(sl2) (x) TL_N bimodule, so the m-magnon spectrum of H_TL^open contains
the (m-1)-magnon spectrum as a sub-multiset; the genuinely-m-magnon TL standard
module W_{N/2-m} is the multiset difference, of dimension C(N,m) - C(N,m-1).
Both the containment and the dimension are verified (CHECK 9, CHECK 10) before
anything is read off the difference.  That keeps the matrices at C(N,2) = 276
for N = 24 rather than 2^24, and makes mpmath's real-symmetric `eigsy` -- not
the generic `eig`, which fails on matrices `eigsy` handles -- affordable.

Read-only: writes no witness, runs no producer, edits no existing file.
"""
import sys
import time
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mpmath import mp, mpf, matrix, nstr, eigsy, cos, pi, acos, log, norm  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402

mp.dps = 50

# the diagonalisation floor, measured below and reported with every comparison
TOL = mpf(10) ** (-40)

T0 = time.monotonic()


def el(msg):
    print(f"      [t+{time.monotonic() - T0:7.1f}s] {msg}", flush=True)


# ------------------------------------------------------------------ operators

I2 = matrix([[1, 0], [0, 1]])
SZ = matrix([[1, 0], [0, -1]])
SP = matrix([[0, 1], [0, 0]])
SM = matrix([[0, 0], [1, 0]])


def kron(a, b):
    m = matrix(a.rows * b.rows, a.cols * b.cols)
    for i in range(a.rows):
        for j in range(a.cols):
            for k in range(b.rows):
                for l in range(b.cols):
                    m[i * b.rows + k, j * b.cols + l] = a[i, j] * b[k, l]
    return m


def eye(d):
    m = matrix(d, d)
    for k in range(d):
        m[k, k] = 1
    return m


def op_at(op, k, n):
    m = matrix([[1]])
    for j in range(n):
        m = kron(m, op if j == k else I2)
    return m


def embed(op2, i, n):
    m = matrix([[1]])
    for _ in range(i):
        m = kron(m, I2)
    m = kron(m, op2)
    for _ in range(n - i - 2):
        m = kron(m, I2)
    return m


def tl_generator(q):
    """e = |w><w|, |w> = q^{1/2}|ud> - q^{-1/2}|du>; e^2 = (q + 1/q) e."""
    e = matrix(4, 4)
    e[1, 1] = q
    e[1, 2] = -1
    e[2, 1] = -1
    e[2, 2] = 1 / q
    return e


def h_tl_full(N, q):
    """-2 sum_{i=1}^{N-1} e_i on the whole 2^N space (small cross-checks only)."""
    e = tl_generator(q)
    H = matrix(2 ** N, 2 ** N)
    for i in range(N - 1):
        H = H - 2 * embed(e, i, N)
    return H


def h_tl_sector(N, m, q, periodic=False):
    """-2 sum_i e_i restricted to the m-down-spin sector.  Real symmetric.

    e|ud> =  q|ud> - |du>   and   e|du> = -|ud> + (1/q)|du>,  e|uu> = e|dd> = 0,
    read off `tl_generator` -- so on a bond carrying exactly one down spin the
    diagonal picks up -2q (down on the RIGHT site) or -2/q (down on the LEFT),
    and the off-diagonal hop is +2 either way.
    """
    basis = list(combinations(range(N), m))
    ix = {s: a for a, s in enumerate(basis)}
    H = matrix(len(basis), len(basis))
    bonds = [(i, (i + 1) % N) for i in range(N)] if periodic \
        else [(i, i + 1) for i in range(N - 1)]
    for s in basis:
        a = ix[s]
        dn = set(s)
        for (i, j) in bonds:
            if (i in dn) == (j in dn):
                continue
            if j in dn:                                    # |ud>
                H[a, a] = H[a, a] - 2 * q
                t = tuple(sorted(dn - {j} | {i}))
            else:                                          # |du>
                H[a, a] = H[a, a] - 2 / q
                t = tuple(sorted(dn - {i} | {j}))
            H[ix[t], a] = H[ix[t], a] + 2
    return H, basis


def spec(H):
    return sorted(eigsy(H, eigvals_only=True))


def multiset_minus(big, small):
    """big \\ small by greedy nearest match; returns (remainder, worst residual)."""
    rem = list(big)
    worst = mpf(0)
    for v in small:
        j = min(range(len(rem)), key=lambda i: abs(rem[i] - v))
        worst = max(worst, abs(rem[j] - v))
        rem.pop(j)
    return sorted(rem), worst


# ------------------------------------------------------- the reference formulas
# All quoted from `xxz_n_string_band_probe`, which MEASURED them on the ring.

def q_int(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def E_string(n, q, k):
    return -2 * (q ** n + q ** (-n) - 2 * cos(k)) / q_int(n, q)


def k_of_E(n, q, v):
    """Invert E_string in k; returns None if v is outside the band."""
    c = (q ** n + q ** (-n) + q_int(n, q) * v / 2) / 2
    return acos(c) if abs(c) <= 1 else None


def one_magnon_levels(N, Delta):
    """The open chain's exact band levels (CHECK 6), excluding the zero mode."""
    return sorted(-4 * Delta + 4 * cos(pi * mpf(m) / N) for m in range(1, N))


# ------------------------------------------------------------------------ main

def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}",
              flush=True)
        if not ok:
            failures.append(name)

    print(__doc__.split("## The gap")[0].strip())
    print(f"\nmp.dps = {mp.dps}; eigenvalue comparisons at {nstr(TOL, 3)}\n")

    q_p, q_m = q_at(mp.dps), q_muon_at(mp.dps)
    ANCHORS = [("proton pin (production default)", q_p),
               ("muon pin   (ideal CAL-2)", q_m)]
    CONTROLS = [("q = 3 control", mpf(3)), ("q = 2 control", mpf(2))]
    ALLQ = ANCHORS + CONTROLS

    # ======================================================== A. the operator
    print("=" * 74)
    print("A.  THE OPERATOR:  is it the chain the TL identification names, and")
    print("    is it Hermitian?")
    print("=" * 74)

    check("1. the two pins are the documented anchors",
          nstr(q_p, 22) == "1.109978582751380807592"
          and nstr(q_m, 22) == "1.109978595642739046682",
          f"proton {nstr(q_p, 22)}  muon {nstr(q_m, 22)}")

    for lab, q in ANCHORS:
        Delta, hh = (q + 1 / q) / 2, q - 1 / q
        worst_open = worst_per = mpf(0)
        for N in (4, 5, 6):
            H = h_tl_full(N, q)
            XXYY = 2 * (kron(SP, SM) + kron(SM, SP))
            ZZ = kron(SZ, SZ)
            hx = matrix(2 ** N, 2 ** N)
            for i in range(N - 1):
                hx = hx + embed(XXYY + Delta * ZZ, i, N)
            rhs = (hx - Delta * (N - 1) * eye(2 ** N)
                   - (hh / 2) * (op_at(SZ, 0, N) - op_at(SZ, N - 1, N)))
            worst_open = max(worst_open, norm(H - rhs))
        check(f"1a. [{lab.split('(')[0].strip()}] open TL sum == XXZ - Delta(N-1) "
              f"- (hh/2)(sz_1 - sz_N), N=4,5,6",
              worst_open < TOL, f"residual {nstr(worst_open, 6)}")

    # Hermiticity + reflection, on the sector matrices actually used below
    q = q_p
    asym = refl = mpf(0)
    for N in (8, 10, 12):
        for m in (1, 2):
            H, basis = h_tl_sector(N, m, q)
            D = H.rows
            asym = max(asym, max(abs(H[i, j] - H[j, i])
                                 for i in range(D) for j in range(D)))
            # spatial reflection j -> N-1-j, as a permutation of the basis
            perm = [0] * D
            ix = {s: a for a, s in enumerate(basis)}
            for s in basis:
                perm[ix[s]] = ix[tuple(sorted(N - 1 - j for j in s))]
            refl = max(refl, max(abs(H[perm[i], perm[j]] - H[i, j])
                                 for i in range(D) for j in range(D)))
    check("2. H_TL^open is HERMITIAN in the sz basis: ||H - H^T|| == 0",
          asym == 0, f"max|H_ij - H_ji| = {nstr(asym, 3)} (identically zero, not a tolerance)")
    check("3. ... and is NOT reflection-symmetric: ||H - P H P|| =/= 0",
          refl > mpf("0.1"), f"max|(PHP - H)_ij| = {nstr(refl, 8)}")

    # magnon number: sector blocks reproduce the full spectrum
    N = 8
    full = sorted(spec(h_tl_full(N, q)))
    bysec = sorted(v for m in range(N + 1) for v in spec(h_tl_sector(N, m, q)[0]))
    d = max(abs(a - b) for a, b in zip(full, bysec))
    check("4. magnon number is conserved (sector blocks == full 2^N spectrum, N=8)",
          len(full) == len(bysec) and d < TOL, f"worst {nstr(d, 6)}")

    check("5. H_TL <= 0 with the vacuum at the TOP (binding is measured UPWARD)",
          max(full) < TOL and min(full) < 0,
          f"max spec = {nstr(max(full), 4)}, min spec = {nstr(min(full), 10)}")

    # ==================================== B. the one-magnon sector, exactly
    print()
    print("=" * 74)
    print("B.  THE ONE-MAGNON SECTOR IS EXACT AT EVERY N, AND CARRIES A STATE")
    print("    THE RING DOES NOT")
    print("=" * 74)

    worst = mpf(0)
    for lab, q in ALLQ:
        Delta = (q + 1 / q) / 2
        for N in (6, 8, 10, 12, 14, 16, 18, 20, 24):
            pred = sorted([mpf(0)] + one_magnon_levels(N, Delta))
            got = spec(h_tl_sector(N, 1, q)[0])
            worst = max(worst, max(abs(a - b) for a, b in zip(pred, got)))
    check("6. open m=1 spectrum == {0} u {-4 Delta + 4 cos(pi m/N)}, m=1..N-1; "
          "4 anchors x 9 sizes",
          worst < TOL,
          f"worst deviation {nstr(worst, 6)} -- this IS the diagonalisation floor")

    for lab, q in ANCHORS:
        H, basis = h_tl_sector(12, 1, q)
        E, Q = eigsy(H)
        z = min(range(len(E)), key=lambda i: abs(E[i]))
        v = [Q[j, z] for j in range(len(basis))]
        dev = max(abs(v[j + 1] / v[j] - 1 / q) for j in range(len(basis) - 1))
        check(f"7. [{lab.split('(')[0].strip()}] the E=0 state is the U_q(sl2) vacuum "
              f"descendant: psi_j ~ q^-j",
              abs(E[z]) < TOL and dev < TOL,
              f"|E| = {nstr(abs(E[z]), 4)}, max|ratio - 1/q| = {nstr(dev, 4)}, "
              f"decay length 1/ln q = {nstr(1 / log(q), 12)} sites")

    nz_open, nz_per, per_max = [], [], []
    for lab, q in ANCHORS:
        for m in (1, 2, 3):
            so = spec(h_tl_sector(12, m, q)[0])
            nz_open.append(sum(1 for x in so if abs(x) < TOL))
        for m in (1, 2):
            sp_ = spec(h_tl_sector(12, m, q, periodic=True)[0])
            nz_per.append(sum(1 for x in sp_ if abs(x) < TOL))
            per_max.append(max(sp_))
    check("8. OPEN has exactly one E=0 state in EVERY sector m=1,2,3; PERIODIC has "
          "none in m>=1  (N=12, both pins)",
          all(c == 1 for c in nz_open) and all(c == 0 for c in nz_per),
          f"open counts {nz_open}, periodic counts {nz_per}, "
          f"periodic max(E) = {[nstr(x, 8) for x in per_max]}")

    # ==================================== C. the U_q block split
    print()
    print("=" * 74)
    print("C.  THE U_q(sl2) BLOCK SPLIT  (verified before anything is read off it)")
    print("=" * 74)

    SIZES = (6, 8, 10, 12, 16, 20, 24)
    store = {}
    total = len(ALLQ) * len(SIZES)
    done = 0
    for lab, q in ALLQ:
        for N in SIZES:
            t0 = time.monotonic()
            s1 = spec(h_tl_sector(N, 1, q)[0])
            s2 = spec(h_tl_sector(N, 2, q)[0])
            W, resid = multiset_minus(s2, s1)
            store[(lab, N)] = (s1, s2, W, resid)
            done += 1
            dt = time.monotonic() - T0
            el(f"{lab:34s} N={N:3d} dim={len(s2):4d}  {done}/{total}  "
               f"({time.monotonic()-t0:5.1f}s, ETA {dt/done*(total-done):6.1f}s)")

    bad_dim = [(lab, N) for (lab, N), (_, s2, W, _) in store.items()
               if len(W) != N * (N - 3) // 2]
    check("9. dim W_{N/2-2} == C(N,2) - C(N,1) == N(N-3)/2, all 4 anchors x 7 sizes",
          not bad_dim, f"{len(store)} blocks checked, {len(bad_dim)} wrong")
    worst_embed = max(r for (_, _, _, r) in store.values())
    check("10. the m=1 spectrum EMBEDS in the m=2 spectrum (the W_{N/2-1} block)",
          worst_embed < TOL, f"worst match residual {nstr(worst_embed, 6)}")

    # ==================================== D. the band, at the controls
    print()
    print("=" * 74)
    print("D.  THE BAND AT THE CONTROLS  (xi small enough for the string to fit)")
    print("=" * 74)

    ladder_ok = True
    ladder_detail = []
    for lab, q in CONTROLS:
        Delta = (q + 1 / q) / 2
        ff_top = -8 * Delta + 8
        print(f"\n  --- {lab}:  Delta = {nstr(Delta, 12)}, "
              f"xi = 1/ln Delta = {nstr(1 / log(Delta), 8)} sites,")
        print(f"      E_2(0) = {nstr(E_string(2, q, 0), 16)}   "
              f"E_2(pi) = {nstr(E_string(2, q, pi), 16)}   "
              f"free-free top = {nstr(ff_top, 12)}")
        for N in (12, 16, 20, 24):
            W = store[(lab, N)][2]
            above = [v for v in reversed(W) if v > ff_top]
            ks = [k_of_E(2, q, v) for v in above]
            Ls = [pi * (i + 1) / k for i, k in enumerate(ks) if k is not None]
            if len(Ls) >= 3:
                sprd = (max(Ls) - min(Ls)) / min(Ls)
                ladder_detail.append((lab, N, len(Ls), Ls[0], sprd))
                ladder_ok = ladder_ok and sprd < mpf("0.10")
            print(f"      N={N:3d}: {len(above):2d} levels clear the continuum; "
                  f"top = {nstr(W[-1], 16)}  "
                  f"L_eff(m=1) = {nstr(Ls[0], 8) if Ls else '--'}"
                  + (f"  ladder spread {nstr(sprd*100, 4)}%" if len(Ls) >= 3 else ""))
    check("11. inverting the open levels through the PERIODIC E_2(k) gives an "
          "EVENLY SPACED k-ladder (one common L_eff to <10%)",
          ladder_ok and len(ladder_detail) >= 4,
          f"{len(ladder_detail)} (control, N) blocks with >=3 clear levels")

    print("\n  convergence of the band EDGE, top(W) -> E_2(0):")
    rate_ok = []
    for lab, q in CONTROLS:
        E0 = E_string(2, q, 0)
        gaps = [(N, E0 - store[(lab, N)][2][-1]) for N in (12, 16, 20, 24)]
        print(f"    {lab}:")
        for i, (N, g) in enumerate(gaps):
            line = f"      N={N:3d}  E_2(0) - top(W) = {nstr(g, 12)}"
            if i:
                Np, gp = gaps[i - 1]
                p = log(gp / g) / log(mpf(N) / Np)
                line += f"   local exponent p = {nstr(p, 8)}"
                if N == 24:
                    rate_ok.append(p)
            print(line)
    check("12. the edge converges as a POWER LAW with local exponent -> 2 "
          "(the band's own curvature over the box's smallest momentum)",
          all(mpf("1.8") < p < mpf("2.6") for p in rate_ok),
          f"exponents at the largest step: {[nstr(p, 6) for p in rate_ok]}")

    # n = 3 at the sharpest control
    q = mpf(3)
    t0 = time.monotonic()
    s2 = spec(h_tl_sector(12, 2, q)[0])
    s3 = spec(h_tl_sector(12, 3, q)[0])
    W3, r3 = multiset_minus(s3, s2)
    el(f"n=3 block at q=3, N=12 (dim {len(s3)}) in {time.monotonic()-t0:.1f}s")
    E3_0 = E_string(3, q, 0)
    check("13. the n=3 string band is there too: dim W_{N/2-3} == N(N-1)(N-5)/6 "
          "and top(W) approaches E_3(0)",
          len(W3) == 12 * 11 * 7 // 6 and r3 < TOL and W3[-1] < E3_0
          and abs(W3[-1] - E3_0) < mpf("0.1"),
          f"dim {len(W3)}, top = {nstr(W3[-1], 14)}, E_3(0) = {nstr(E3_0, 14)}, "
          f"gap {nstr(E3_0 - W3[-1], 8)}")

    # ==================================== E. the band at the two pins
    print()
    print("=" * 74)
    print("E.  THE BAND AT THE TWO SUBSTRATE PINS  (the honest negative)")
    print("=" * 74)

    need_N = []
    artefact = []
    for lab, q in ANCHORS:
        Delta = (q + 1 / q) / 2
        hbar = 1 - 1 / q
        E0, Epi = E_string(2, q, 0), E_string(2, q, pi)
        ff_top, ff_bot = -8 * Delta + 8, -8 * Delta - 8
        B0 = 4 * (Delta - 1) ** 2 / Delta
        print(f"\n  --- {lab}")
        print(f"      q0            = {nstr(q, 22)}")
        print(f"      Delta         = {nstr(Delta, 20)}      "
              f"xi = 1/ln Delta = {nstr(1 / log(Delta), 10)} sites")
        print(f"      band TOP    E_2(0)  = {nstr(E0, 20)}")
        print(f"      band BOTTOM E_2(pi) = {nstr(Epi, 20)}   (= -4 Delta)")
        print(f"      band width  8/[2]_q = {nstr(8 / q_int(2, q), 20)}")
        print(f"      B(0)  = 4(Delta-1)^2/Delta = 2 q^2 hbar_q^4/[2]_q "
              f"= {nstr(B0, 16)}")
        print(f"      B(pi) = 4 Delta                              "
              f"= {nstr(4 * Delta, 16)}")
        print(f"      two-magnon continuum (thermodynamic): "
              f"[{nstr(ff_bot, 12)}, {nstr(ff_top, 12)}]")
        # the closed-form B(0) identity, checked
        check(f"    [{lab.split('(')[0].strip()}] B(0) == 2 q^2 hbar_q^4 / [2]_q",
              abs(B0 - 2 * q ** 2 * hbar ** 4 / q_int(2, q)) < TOL,
              f"{nstr(B0, 16)}")
        # how big must the box be for ONE level to clear the continuum?
        kmax = 2 * acos(((1 - (Delta - 1) ** 2)) ** mpf("0.5"))
        need_N.append(pi / kmax)
        print(f"      a level clears the continuum only for k < {nstr(kmax, 10)},")
        print(f"      i.e. only once the box admits pi/L < that:  L > "
              f"{nstr(pi / kmax, 8)}  (=> N ~ {nstr(pi / kmax + 3, 6)})")
        print("      N    top(W)                  E_2(0)-top(W)   "
              "vs FINITE-N edge   vs THERMO edge")
        for N in SIZES:
            W = store[(lab, N)][2]
            eps = one_magnon_levels(N, Delta)
            fin_edge = eps[-1] + eps[-2]             # the two least-bound magnons
            print(f"      {N:3d}  {nstr(W[-1], 18):>20}  {nstr(E0 - W[-1], 10):>13}  "
                  f"{nstr(W[-1] - fin_edge, 10):>16}  {nstr(W[-1] - ff_top, 10):>14}")
            if N >= 12:
                artefact.append((W[-1] - fin_edge > 0, W[-1] - ff_top < 0))
    check("14. at BOTH pins the required box is N ~ 291, so no accessible N "
          "resolves the string (xi = 184 sites)",
          all(mpf("280") < x + 3 < mpf("300") for x in need_N),
          f"L needed = {[nstr(x, 7) for x in need_N]}")
    check("15. the finite-N EDGE is the artefact: at N=12..24 the top level is "
          "ABOVE the finite-N two-magnon edge and BELOW the thermodynamic one",
          all(a and b for a, b in artefact),
          f"{len(artefact)} (pin, N) rows, all apparently-bound / actually-unbound")

    # ==================================== F. what is NOT extractable
    print()
    print("=" * 74)
    print("F.  THE BAND BOTTOM IS NOT EXTRACTABLE FROM THE OPEN CHAIN")
    print("=" * 74)

    interior, below = [], []
    for lab, q in ALLQ:
        Delta = (q + 1 / q) / 2
        Epi, ff_bot = E_string(2, q, pi), -8 * Delta - 8
        interior.append(Epi > ff_bot)
        W = store[(lab, 24)][2]
        below.append(sum(1 for v in W if v < Epi))
        print(f"    {lab:34s} E_2(pi) = {nstr(Epi, 14):>17}   "
              f"continuum bottom = {nstr(ff_bot, 14):>17}   "
              f"levels of W_24 below E_2(pi): {below[-1]:4d}  "
              f"min W_24 = {nstr(W[0], 12)}")
    check("16. E_2(pi) = -4 Delta is STRICTLY INTERIOR to the two-magnon spectrum "
          "(invariant: -4 Delta > -8 Delta - 8 for every Delta > 0), and states "
          "are measured below it, so no extremal search can reach it",
          all(interior) and all(c > 0 for c in below),
          f"levels below E_2(pi) at N=24: {below}")

    # pin independence
    dp = (q_p + 1 / q_p) / 2
    dm = (q_m + 1 / q_m) / 2
    sep = abs(dm - dp) / dp * 10 ** 9
    check("17. every verdict above is pin-independent (the two pins' Delta agree "
          "to well under a part in 10^6)",
          sep < 100, f"|Delta_muon - Delta_proton|/Delta_proton = {nstr(sep, 8)} ppb")

    # ==================================================================== VERDICT
    print()
    print("=" * 74)
    print("VERDICT")
    print("=" * 74)
    print("""
  1. HERMITICITY -- the question does not bite.  The surface field
     ((q - 1/q)/2)(sz_1 - sz_N) is reflection-ODD, not anti-Hermitian: for real
     q > 1 it is a real diagonal operator, so H_TL^open is real symmetric and
     ||H - H^T|| is identically 0 (CHECK 2), not merely small.  "Band" language
     is safe.  What is genuinely broken is spatial reflection (CHECK 3), and
     that is what produces finding 2.

  2. THE OPEN CHAIN HAS A BOUND STATE THE RING DOES NOT.  At E = 0 -- degenerate
     with the vacuum, at the very top of the spectrum, above the whole n = 2
     band -- in EVERY magnon sector, exactly one such state, exponentially
     localised at one end with amplitude ratio 1/q (CHECKs 7, 8).  It is the
     U_q(sl2) descendant of the ferromagnetic vacuum; the ring has no zero mode
     in any m >= 1 sector.  This is not a numerical artefact and does not go
     away with N.

  3. THE BOUNDARY FIELD DOES NOT DESTROY THE BAND.  At the controls the open
     chain reproduces the PERIODIC band E_2(k) in full, sampled at a quantised
     ladder k_m ~ pi m / L_eff (CHECK 11), and the n = 3 band as well (CHECK 13).
     The band EDGE converges as a POWER LAW, local exponent -> 2 (CHECK 12),
     where the ring converges exponentially as z^N.  That is not a defect in the
     open chain: the residual is the band's own curvature between k = 0 and the
     smallest momentum a box of length L admits, so it is a statement about
     which k the geometry can reach, not about the Hamiltonian.

  4. AT THE SUBSTRATE THE EXTRACTION FAILS -- scope (a).  This construction, at
     N <= 24, did not reproduce the numbers: xi = 184 sites, and one level clears
     the two-magnon continuum only at N ~ 291 (CHECK 14).  At N = 12..24 the top
     level is above the FINITE-N edge and below the THERMODYNAMIC one (CHECK 15)
     -- the apparent binding is the depression of the edge.  No scope-(b)
     exclusion is claimed: nothing here shows the band is absent, only that a
     box this small cannot resolve it.

  5. THE BAND BOTTOM IS NOT EXTRACTABLE AT ANY N -- scope (a), with an invariant
     named for the mechanism but NOT as a scope-(b) refutation of any ingredient.
     E_2(pi) = -4 Delta is strictly above the two-magnon continuum bottom
     -8 Delta - 8 for every Delta > 0, so the k = pi edge is strictly interior to
     the spectrum (CHECK 16).  Momentum is what separated it on the ring; the
     open chain does not have momentum, so only the k -> 0 end of the band is
     reachable by extremal search, through a window of width B(0).

  RE-SCOPING.  Neither existing probe is wrong, and neither headline needs
  retraction.  What needs re-scoping is the PERIODIC probe's bridging sentence,
  "the two differ by boundary operators, which do not change a bulk band in the
  thermodynamic limit".  Measured, that is true of the band and incomplete about
  the spectrum: the boundary operators ADD a state, at E = 0, above the entire
  band, in every magnon sector -- and they remove momentum, which costs the
  band's k-resolution and turns exponential convergence into N^-2.
""")

    print(f"{checks - len(failures)}/{checks} checks pass"
          f"   (wall {time.monotonic() - T0:.1f}s)")
    if failures:
        print("FAILED: " + "; ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
