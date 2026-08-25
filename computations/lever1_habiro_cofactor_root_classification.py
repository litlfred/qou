#!/usr/bin/env python3
"""
lever1_habiro_cofactor_root_classification.py — the non-cyclotomic Habiro-tail cofactors are
NOT Salem numbers (lever-1 / bean z2bn). Exact symbolic + numerical roots.

Follows `lever1_habiro_tail_closed_form.py`: the binding q-deformation Habiro tail
D(n) = S(n) − S(n−1) − [n−1]_q·S(n−2) factors as (q−1)²·(cyclotomic head)·(cofactor), with the
cofactor fully cyclotomic through n=5 and genuinely NON-cyclotomic (bar-even) from n=6. A natural
hypothesis is that the first non-cyclotomic factor is a distinguished arithmetic object — a
**Salem** or **Lehmer**-type number (as arises for the smallest Mahler measures / Coxeter systems).

This probe TESTS that hypothesis by classifying the cofactor roots. Bar-evenness forces roots into
reciprocal pairs {r, 1/r}; a Salem polynomial has exactly ONE root off the unit circle (with its
reciprocal) and all others ON it.

FINDING (scope-(a), REFUTATION): the non-cyclotomic cofactors are **NOT Salem** — each has
SEVERAL off-circle reciprocal pairs, not one:

  n | deg | on-circle | off-circle pairs | max|root|
  6 |  8  |    4      |       2          |  2.271
  7 | 10  |    6      |       2          |  1.407
  8 | 14  |    6      |       4          |  1.206
  9 | 28  |   14      |       7          |  2.523

So what appears at n=6 is NOT a distinguished number-theoretic class (Salem/Lehmer) — it is simply
the first genuinely non-cyclotomic, non-q-holonomic content (mixed on/off-circle bar-even roots).
The DERIVED structural facts stand (universal (q−1)² double root, bar-evenness, cyclotomic→non-
cyclotomic boundary at n=6); the specific root magnitudes are NOT interpreted (numerology guard).

Discipline: binding recurrence D(n), NOT the Q_β c_k ladder. Exact symbolic factorization + mpmath
roots. No fit, no wiring, no interpretation of magnitudes. Scope-(a).

Audit: docs/audits/2026-07-12-lever1-habiro-tail-closed-form.md (cofactor-roots section).
"""
from __future__ import annotations
import sys
from pathlib import Path

import sympy as sp
import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

set_compute_dps()
q = sp.symbols('q')


def qint(k):
    return sp.Integer(0) if k == 0 else sp.cancel((q ** k - q ** (-k)) / (q - 1 / q))

def qfac(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= qint(k)
    return sp.cancel(r)

def parts(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in parts(n - k, k):
            yield (k,) + r

def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]

def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return sp.cancel(d)

def S(n):
    return sp.cancel(sum(dimq(l) for l in parts(n))) if n > 0 else sp.Integer(1)

def is_cyclotomic(poly):
    if sp.Poly(poly, q).degree() < 1:
        return True
    for k in range(1, 80):
        if sp.expand(poly - sp.cyclotomic_poly(k, q)) == 0:
            return True
    return False


def main() -> int:
    print("=== Habiro-tail non-cyclotomic cofactors: Salem/Lehmer, or generic bar-even? ===\n")
    print(f"  {'n':>2} {'deg':>4} {'on-circle':>10} {'off-pairs':>10} {'max|root|':>10} {'Salem?':>8}")
    rows = {}
    any_salem = False
    for n in range(6, 10):
        D = sp.cancel(S(n) - S(n - 1) - qint(n - 1) * S(n - 2))
        num, _ = sp.fraction(sp.cancel(D))
        _, facs = sp.factor_list(sp.expand(num))
        for f, _mult in facs:
            deg = sp.Poly(f, q).degree()
            if deg >= 1 and not is_cyclotomic(f):
                coeffs = [complex(c) for c in sp.Poly(f, q).all_coeffs()]
                roots = mp.polyroots(coeffs, maxsteps=250, extraprec=120)
                mods = sorted(float(abs(r)) for r in roots)
                on = sum(1 for m_ in mods if abs(m_ - 1) < 1e-9)
                off_pairs = sum(1 for m_ in mods if m_ > 1 + 1e-9)     # each >1 root pairs with 1/r
                gt1 = off_pairs
                salem = (gt1 == 1 and on == deg - 2)                  # Salem: exactly one off pair
                any_salem = any_salem or salem
                rows[n] = dict(deg=deg, on_circle=on, off_pairs=off_pairs,
                               max_mod=max(mods), salem=salem)
                print(f"  {n:>2} {deg:>4} {on:>10} {off_pairs:>10} {max(mods):>10.4f} {str(salem):>8}")

    off_growth = [rows[n]["off_pairs"] for n in sorted(rows)]
    multiple_off = all(v >= 2 for v in off_growth)   # NOT Salem: ≥2 off-circle pairs each
    print(f"\n### Finding (scope-(a) — REFUTATION of the Salem/Lehmer hypothesis)")
    print(f"  • The non-cyclotomic cofactors are NOT Salem: each has ≥2 off-circle reciprocal pairs")
    print(f"    (off-pairs {off_growth}), not the single pair a Salem number requires.")
    print(f"  • They are GENERIC bar-even non-cyclotomic polynomials (mixed on/off-circle reciprocal")
    print(f"    roots). What appears at n=6 is the first non-q-holonomic content, NOT a distinguished")
    print(f"    number-theoretic class. Specific magnitudes are NOT interpreted (numerology guard).")
    print(f"  • Standing structural facts unchanged: universal (q−1)² double root, bar-evenness,")
    print(f"    cyclotomic→non-cyclotomic boundary at n=6 (the derived invariants).")

    ok = (not any_salem) and multiple_off
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-habiro-cofactor-root-classification", engine="sympy+mpmath")
        wb.set_description(
            "Classifies the Habiro-tail non-cyclotomic cofactor roots (lever-1/z2bn). REFUTES the "
            "Salem/Lehmer hypothesis: each cofactor (n=6..9) has ≥2 off-circle reciprocal pairs "
            "(off-pairs 2,2,4,7), not the single pair a Salem number requires — they are generic "
            "bar-even non-cyclotomic polynomials with mixed on/off-circle roots. So the n=6 boundary "
            "is the onset of non-q-holonomic content, NOT a distinguished number-theoretic class. "
            "Magnitudes not interpreted (numerology guard). Structural invariants ((q−1)² double "
            "root, bar-evenness, cyclotomic→non-cyclotomic at n=6) unchanged. Binding D(n), not Q_β "
            "c_k. Scope-(a), no fit, no wiring.")
        wb.add_data("cofactor_root_classification", rows)
        wb.add_assertion(
            name="habiro_cofactors_not_salem",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("each non-cyclotomic cofactor (n=6..9) has ≥2 off-circle reciprocal pairs "
                    "(off-pairs %s) — not the single off-circle pair a Salem polynomial requires — so "
                    "the cofactors are generic bar-even non-cyclotomic, not Salem/Lehmer; the n=6 "
                    "boundary is the onset of non-q-holonomic content." % off_growth))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
