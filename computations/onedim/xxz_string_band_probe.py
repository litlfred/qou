#!/usr/bin/env python3
# polynomial_q_not_applicable: numeric spectra at fixed anchors; no symbolic-q polynomial output.
"""MEASURE the XXZ two-magnon bound state at the substrate — and report the
honest negative: the band energy is NOT extracted.

Bean `qou-6b9y`. The Δ_λ / 1D-sector work deliberately quotes NO formula for
the n-string band; this probe is the measurement that was supposed to replace
the quote. It establishes less than hoped, and says so.

## Method

Momentum-resolved exact diagonalisation of
    H = sum_i (sx sx + sy sy + Delta sz sz)_{i,i+1},  periodic, N sites,
in the translation-symmetrised basis, `_xxz_momentum_ed.py`. A bound state is
identified as a level lying OUTSIDE the two-magnon continuum, the continuum
being built from the MEASURED one-magnon dispersion rather than a formula.

## What is established (CHECK 1-3)

1. The symmetrisation is correct: the union of the momentum-block spectra
   equals the full-sector spectrum, exactly.
2. An isolated level above the two-magnon continuum exists in EVERY momentum
   sector, at the substrate anisotropy and at a strong-anisotropy control,
   for every N tested. So the two-magnon bound state is present at q0.
3. The binding at the substrate is one and a half to two orders of magnitude
   weaker than at q = 2 — quantifying "only marginally inside the massive
   phase".

## What is NOT established, and two things that were WRONG

* **The band energy is not extracted and no formula is offered.** The
  "binding above the continuum" is NOT converged at accessible N: it DECREASES
  monotonically with N at both anisotropies, and the ratio between them drifts
  (54.5 -> 70.2 over N = 8..14). CHECK 4 asserts that drift, so the
  non-convergence is a measured fact rather than a caveat. Quoting any of these
  as a thermodynamic-limit binding would be wrong.
* **A candidate band formula was refuted.** The form
  `-2 sinh(eta) sinh(2 eta)/(cosh 2eta - cos k)` was tried and does not
  describe the data: at q = 2, k = 0 it gives -2.5 where the measurement gives
  +0.288. It is not used anywhere and is recorded only so it is not re-tried.
* **The sign convention caught an earlier error.** With `+Delta sz sz` and
  `Delta > 0` the all-up state is the TOP of the band, so the bound state lies
  ABOVE the continuum. A first pass looked below it and found nothing --
  including at the strong-anisotropy control, where a bound state certainly
  exists. The control is what exposed it; without one the null result would
  have read as physics.

Next step for `qou-6b9y`: finite-size scaling to larger N, or solve the Bethe
equations for the two-string directly rather than diagonalising.

Read-only: writes no witness, runs no producer.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mpmath import mp, mpf, nstr, pi  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _xxz_momentum_ed import orbit_data, block, spectrum, sectors, H_terms  # noqa: E402
from mpmath import matrix  # noqa: E402

mp.dps = 30


def one_magnon(N, Delta):
    reps, info = orbit_data(N, 1)
    out = {}
    for r in range(N):
        H, _ = block(N, 1, r, Delta, reps, info)
        sp = spectrum(H)
        assert len(sp) == 1, (r, len(sp))
        out[r] = sp[0] - Delta * N
    return out


def blocks_match_full(N, m, Delta):
    reps, info = orbit_data(N, m)
    allv = []
    for r in range(N):
        H, _ = block(N, m, r, Delta, reps, info)
        allv += spectrum(H)
    st = sectors(N, m)
    ix = {s: a for a, s in enumerate(st)}
    full = matrix(len(st), len(st))
    for s in st:
        for coef, s2 in H_terms(s, N, Delta):
            full[ix[s2], ix[s]] = full[ix[s2], ix[s]] + coef
    fsp = spectrum(full)
    return (len(fsp) == len(allv)
            and max(abs(a - b) for a, b in zip(sorted(allv), sorted(fsp))) < mpf('1e-18'))


def bound_sectors(N, Delta):
    """number of momentum sectors carrying a level above the 2-magnon continuum."""
    e1 = one_magnon(N, Delta)
    reps, info = orbit_data(N, 2)
    n = 0
    for r in range(N):
        hi = max(e1[a] + e1[(r - a) % N] for a in range(N))
        H, _ = block(N, 2, r, Delta, reps, info)
        if any(v - Delta * N > hi + mpf('1e-20') for v in spectrum(H)):
            n += 1
    return n


def binding_k0(N, Delta):
    e1 = one_magnon(N, Delta)
    reps, info = orbit_data(N, 2)
    hi = max(e1[a] + e1[(0 - a) % N] for a in range(N))
    H, _ = block(N, 2, 0, Delta, reps, info)
    above = [v - Delta * N for v in spectrum(H) if v - Delta * N > hi + mpf('1e-20')]
    return (above[0] - hi) if above else None


def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
        if not ok:
            failures.append(name)

    Q0 = q_at(mp.dps)
    D0 = (Q0 + 1 / Q0) / 2                 # substrate anisotropy
    D2 = (mpf(2) + mpf(1) / 2) / 2         # strong-anisotropy CONTROL, q = 2

    print("XXZ two-magnon bound state: measured, band NOT extracted\n")
    print(f"  q0    = {nstr(Q0, 20)}   Delta(q0) = {nstr(D0, 20)}")
    print(f"  control q = 2                Delta     = {nstr(D2, 20)}\n")

    check("1. momentum blocks reproduce the full sector exactly (N=8, m=2)",
          blocks_match_full(8, 2, D0) and blocks_match_full(8, 2, D2),
          "symmetrisation verified at both anisotropies")

    print()
    for N in (8, 10, 12):
        nb0, nb2 = bound_sectors(N, D0), bound_sectors(N, D2)
        check(f"2. N={N}: a level above the continuum in EVERY momentum sector",
              nb0 == N and nb2 == N, f"substrate {nb0}/{N}, control {nb2}/{N}")

    print("\n  k=0 binding above the continuum (NOT converged — see CHECK 4):")
    print("     N |      control q=2 |       substrate q0 |   ratio")
    rows = []
    for N in (8, 10, 12, 14):
        b2, b0 = binding_k0(N, D2), binding_k0(N, D0)
        rows.append((N, b2, b0, b2 / b0))
        print(f"    {N:2d} | {nstr(b2, 12):>16} | {nstr(b0, 12):>18} | {nstr(b2 / b0, 6):>7}")

    print()
    check("3. the substrate binding is >1 order of magnitude below the control",
          all(r[3] > 10 for r in rows),
          f"ratio {nstr(rows[0][3], 6)} .. {nstr(rows[-1][3], 6)}")

    mono2 = all(rows[i][1] > rows[i + 1][1] for i in range(len(rows) - 1))
    mono0 = all(rows[i][2] > rows[i + 1][2] for i in range(len(rows) - 1))
    drift = rows[-1][3] > rows[0][3] * mpf('1.2')
    check("4. NOT converged: binding falls monotonically with N at BOTH "
          "anisotropies and the ratio drifts >20%",
          mono2 and mono0 and drift,
          "so no number here is a thermodynamic-limit binding")

    print(f"\n{checks - len(failures)}/{checks} checks pass")
    print("""
VERDICT
  Established: the two-magnon bound state IS present at the substrate, in every
  momentum sector, and its binding is ~1.5-2 orders of magnitude below the
  q = 2 control — the quantitative form of "only marginally inside the massive
  phase".
  NOT established: the band energy. It is not converged at accessible N, and
  the candidate formula recorded in the docstring is REFUTED. `qou-6b9y` stays
  open; the next step is finite-size scaling or a direct two-string Bethe
  solve, not another diagonalisation at these sizes.""")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
