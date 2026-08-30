#!/usr/bin/env python3
"""hecke_nf_laurent_scaling_probe — cost and q-degree of the atom Hecke NF.

WHAT THIS MEASURES
------------------
Two things about ``hecke_core_symbolic.build_atom_nf_laurent(Z, N)``:

1. **Wall cost vs A**, to state an honest ceiling for the symbolic route.
2. **The top q-degree of the NF coefficients vs A**, which is the reason
   the fold was wanted at all — see BACKGROUND.

BACKGROUND — why the degree is the interesting column
-----------------------------------------------------
The mass/binding arc needs an invariant of a nucleus that is **not affine
in A**, because a surface term must scale as ``A^(2/3)`` and an affine
function cannot (``QOU.Mass.AffineCountIsNotASurfaceTerm``, sorry-free).
Every count read off the braid word *is* affine: crossings ``12A-1``,
strands ``3A``, Seifert genus ``4A``, Euler characteristic ``-9A+1``,
components ``A+1``, inter-nucleon part exactly ``A-1``.

The q-degree of the NF coefficients is the first candidate that is not
obviously forced to be affine. It was untestable until 2026-08-30 because
the fold was exponential (see the Laurent-kernel note in
``hecke_core_symbolic``); with the ``LaurentQ`` kernel A=16 costs ~6 s.

RESULT, AND THE CAVEAT THAT GOES WITH IT
----------------------------------------
Measured over 23 values of A on the N=Z chain (``Z = A//2``), the top
degree of ``nf[0]`` obeys, EXACTLY for every measured ``A >= 9``:

        deg(A) = (A^2 + 14A + c) / 2,     c = 40  (A even)
                                          c = 31  (A odd)

Leading term ``A^2/2``. So the q-degree is **quadratic**, hence **not
affine** — the negative the arc asked for. Values at ``A <= 8`` fall
*below* this law by 2..14 (a small-A boundary regime), so the law is
quoted with its range and not extrapolated downward.

**This is NOT evidence of a surface term, and must not be reported as
one.** Two reasons, both measurable from the columns this probe prints:

  * Quadratic is not ``A^(2/3)``. Ruling out affine does not rule in the
    surface exponent; it rules out one alternative.
  * The fold's own step count is ``11A + A(A-1)/2 + Z ~ A^2/2 + 11.5A``,
    itself quadratic, because of the all-pairs inter-nucleon loop
    ``for prev in range(k)`` in ``build_atom_nf_laurent``. The measured
    ratio ``deg/steps`` oscillates with the parity of A inside 0.84..0.92
    and trends upward with A: 0.855 (A=16), 0.875 (A=32), 0.887 (A=40),
    0.898 (A=48). So the quadratic degree may be little more than a
    re-reading of that all-pairs loop rather than an emergent invariant of
    the nucleus. The ``deg`` and ``steps`` columns are printed side by side
    precisely so a reader can see this rather than take it on trust.

Two further structural facts, checked on every row rather than fitted, and
independent of the degree law:

  * The exponent support is **symmetric about 0** — ``min = -max`` on every
    row — so the coefficient is bar-symmetric in support under q <-> q^-1.
  * The support is **exactly the even exponents in [-deg, deg]**, with no
    gaps: ``terms == deg + 1`` on every row. Hence the term count is
    quadratic too, and the polynomial is dense in q^2.

MEASURED CEILING (this container, single core, 2026-08-30)
----------------------------------------------------------
Wall scales as roughly A^4 (269.1s at A=48 vs 57.6s at A=32 against a
predicted factor (48/32)^4 = 5.06; observed 4.67).

        A=16    6.2 s        <- the value the mass/binding arc asked for
        A=32   57.6 s        <- largest A under ~60 s (A=33 is 63.5 s)
        A=48  269.1 s
        A=56  536.5 s        <- largest A under ~600 s

Scope, per the refutation-scoping rule: the "not affine" finding is a
**scope-(a)** positive about this particular construction. No proved
invariant is cited to exclude anything, and nothing here refutes the
affine-count results — those are about braid-word counts, a different
object.

PRECISION
---------
Exact throughout: ``LaurentQ`` carries ``sympy.Rational`` coefficients over
integer exponents. No float enters any measured quantity. The only floats
are ``time.perf_counter`` wall times, which are timings and not physics.

Audit-only: emits no witness, changes no committed number.

Usage:
    python3 -u computations/probes/hecke_nf_laurent_scaling_probe.py \
        [--budget SECONDS] [--a-values 2,4,6,...]  2>&1 | tee /tmp/nf.log
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import hecke_core_symbolic as HCS  # noqa: E402


DEFAULT_A = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32]


def degree_law(A: int) -> int:
    """The fitted law. Valid for A >= 9; see module docstring."""
    c = 40 if A % 2 == 0 else 31
    return (A * A + 14 * A + c) // 2


def n_steps(Z: int, N: int) -> int:
    """Number of hm_laurent applications the fold performs."""
    A = Z + N
    return 11 * A + A * (A - 1) // 2 + Z


def run(a_values, budget):
    print("  A     Z   N      wall(s)   deg(nf0)  terms  steps  deg/steps  law  fits",
          flush=True)
    rows = []
    t_start = time.perf_counter()
    for A in a_values:
        Z, N = A // 2, A - A // 2
        t = time.perf_counter()
        nf = HCS.build_atom_nf_laurent(Z, N)
        el = time.perf_counter() - t
        exps = sorted(nf[0].coefs)
        deg, lo, nterms = exps[-1], exps[0], len(exps)
        st = n_steps(Z, N)
        law = degree_law(A)
        fits = "yes" if law == deg else ("no(%+d)" % (deg - law))
        print("%4d  %4d %4d  %11.4f  %8d  %5d  %5d  %9.3f  %5d  %s"
              % (A, Z, N, el, deg, nterms, st, deg / st, law, fits), flush=True)
        rows.append((A, el, deg, nterms, st, lo))
        elapsed = time.perf_counter() - t_start
        if elapsed > budget:
            print("  budget %.0fs exhausted after A=%d (elapsed %.1fs)"
                  % (budget, A, elapsed), flush=True)
            break

    print("", flush=True)
    # Structural checks that do not depend on the fit.
    bad = [r for r in rows if r[5] != -r[2]]
    print("exponent span is symmetric about 0 on every row: %s"
          % ("yes" if not bad else "NO -> %s" % bad), flush=True)
    dense = [r for r in rows if r[3] != r[2] + 1]
    print("support is exactly the even exponents -deg..deg (terms == deg+1): %s"
          % ("yes" if not dense else "NO -> %s" % dense), flush=True)

    fitted = [r for r in rows if r[0] >= 9]
    misses = [(r[0], r[2], degree_law(r[0])) for r in fitted if degree_law(r[0]) != r[2]]
    print("degree law (A^2+14A+c)/2 exact on all measured A>=9 (%d rows): %s"
          % (len(fitted), "yes" if not misses else "NO -> %s" % misses), flush=True)
    print("  -> leading term A^2/2: the q-degree is QUADRATIC, hence NOT affine.",
          flush=True)
    print("  -> but see the module docstring: steps is ALSO quadratic "
          "(all-pairs inter-nucleon loop), and deg/steps -> ~0.90.", flush=True)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--budget", type=float, default=180.0,
                    help="stop after this many seconds of total sweep time")
    ap.add_argument("--a-values", type=str, default=None,
                    help="comma-separated A values (default: 2..32)")
    args = ap.parse_args()
    a_values = ([int(x) for x in args.a_values.split(",")]
                if args.a_values else DEFAULT_A)
    run(a_values, args.budget)


if __name__ == "__main__":
    main()
