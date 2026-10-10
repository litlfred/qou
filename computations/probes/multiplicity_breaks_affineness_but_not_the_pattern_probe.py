"""Crossing multiplicity breaks affineness -- and still cannot make the pn bond extremal.

Bean `qou-brng`, escape class B.

## Why this exists

Class B's remaining escape was narrowed (2026-09-12) to exactly two hypotheses:

    "It must break the AVERAGING of the pn letter, or break AFFINENESS of the
     interface law.  Those are the only two hypotheses used, and neither
     mentions a numerical value."

The averaging half is closed at the corpus's own delta
(`pn_averaging_weight_is_derived_probe.py`: delta(q0) = 1.3757e-3, inside the
Lean hypothesis's (-2,2) by 1453.8x).  This probe attacks the AFFINENESS half,
and it finds the escape is REAL and DOES NOT DELIVER.

## Affineness is an m = 1 fact

The interface letter `sigma_g + d.I` has two-strand trace `z + d`
(`QOU.Mass.ChainTraceFactor.twoStrandTrace_eq`), affine in `d` -- which is what
makes `pn_betweenness_blocks_signMixed` work: an affine map sends the convex
combination `d_pn` to a convex combination, so `mu_pn` is strictly BETWEEN.

At crossing multiplicity `m` the letter is `(sigma_g + d.I)^m`, and by the
Hecke quadratic (`MonotoneWordTraceFactorizes.affine_mul_affine`) that is again
affine IN THE ALGEBRA -- but its trace is degree `m` in `d`:

    (d + g)^1 -> z + d                      affine
    (d + g)^2 -> (d^2 + 1) + (2d + h) z     QUADRATIC

So the affineness hypothesis genuinely fails for `m >= 2`, and measured here,
BETWEENNESS ITSELF fails from `m = 12`.  **The escape the bean asks for exists.**

## It breaks the wrong way

Diagonalising, `g` has Hecke eigenvalues `q` and `-1/q`, so

    F_m(d) = w+ (d + q)^m  +  w- (d - 1/q)^m,     w+ + w- = 1

(`ChainTraceFactor.wPlus_add_wMinus`), and `F_m' = m F_{m-1}` -- monotonicity in
`d`, hence betweenness, survives exactly while `F_{m-1} > 0`.  It stops at
`m = 7`, where `F_7(d_nn) < 0`, and betweenness first fails at `m = 12`.

But the `b_3 > 0` requirement needs `mu_pn` to be the strict MAXIMUM, and
**it never is**, at any `m` in 1..200.  Betweenness breaks by pn becoming the
strict MINIMUM instead.

## Why, and this is the invariant

The three letters' spectral radii are

    rho_pp = |0   + q| = q              rho_nn = |-h - 1/q| = q
    rho_pn = |d_pn + q| ~ [2]_q / 2

because **the pn letter sits at the spectral BALANCE POINT.**  At `d = -h/2`
exactly, `(d + q) + (d - 1/q) = 0`: the two eigenvalue magnitudes coincide, both
equal to `[2]_q/2`.  The corpus's `bring_color_weighted` pn letter is displaced
from that point by exactly `h.delta/4 = 7.190163e-05` -- the number
`pyhecke/constants.py` records in its own convention note.

AM-GM then decides it: for every `q > 1`,

    q  >  [2]_q / 2  >  1

so the like-pair channels grow strictly faster than the pn channel, at every
multiplicity, and pn cannot overtake them.  The gap has a closed form,

    q / ([2]_q/2) = 2q^2/(q^2+1) = 1 + tanh(ln q),

i.e. exactly `1 + delta_CP` -- the same crossing discriminant `qou-hjs8` proved
theta-free.

## Scope

**Scope (b)** for the asymptotic statement; invariant = AM-GM on the two Hecke
eigenvalues, which holds for every `q > 1` and needs no numerical value.  The
small-`m` statement is MEASURED (m = 1..200), not proved.

NOT claimed: that class B is excluded (a different derived pn letter, not at the
balance point, is untouched); anything about MAGNITUDE, which is qou-brng's real
open target.

NO ASSERTION HERE IS A FIT: every number is derived or measured.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_ROOT = _Path(__file__).resolve().parents[2]
for _p in (_ROOT / "computations", _ROOT / "tools" / "qou-substrate" / "python",
           _ROOT / "tools" / "pyhecke" / "python"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402

mp.mp.dps = 70

M_MAX = 200


def hdr(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


def main() -> int:
    from pyhecke.constants import flavor_split_leading, pn_interface_offset  # noqa: E402

    Q = q_at(dps=70)
    qi = 1 / Q
    h = Q - qi
    z = Q ** 3 / (Q ** 2 + 1)                 # convention D
    wp = (z + qi) / (Q + qi)
    wm = (Q - z) / (Q + qi)
    assert abs(wp + wm - 1) < mp.mpf(10) ** -60
    assert wp > 0 and wm > 0

    d_pp = mp.mpf(0)                          # f_pp = z(q)
    d_nn = -h                                 # f_nn = z(1/q) = z - h
    d_pn = pn_interface_offset(Q)             # bring_color_weighted
    d_bal = -h / 2                            # the spectral balance point

    def F(m, d):
        return wp * (d + Q) ** m + wm * (d - qi) ** m

    # ------------------------------------------------------------ section 1
    hdr("[1] Affineness is an m = 1 fact — the trace is degree m in d")

    ds, hs, zs = sp.symbols("d h z")
    g = sp.Symbol("g")
    # (a.1 + b.g)(a'.1 + b'.g) = (aa'+bb').1 + (ab'+a'b+h bb').g   (affine_mul_affine)
    def amul(A, B, A2, B2):
        return (A * A2 + B * B2), (A * B2 + A2 * B + hs * B * B2)

    A, B = ds, sp.Integer(1)                  # the letter d.1 + 1.g
    for m in (1, 2, 3):
        Fsym = sp.expand(A + B * zs)
        print(f"  m = {m}:  tr = {Fsym}")
        if m == 1:
            assert sp.expand(Fsym - (zs + ds)) == 0
        if m == 2:
            assert sp.expand(Fsym - ((ds ** 2 + 1) + (2 * ds + hs) * zs)) == 0
            assert sp.degree(sp.Poly(Fsym, ds)) == 2
        A, B = amul(A, B, ds, sp.Integer(1))
    print("\n  degree 1 at m = 1, degree 2 at m = 2 — the affineness hypothesis of")
    print("  `pn_betweenness_blocks_signMixed` fails for every m >= 2.")

    # numeric agreement of the eigen-form with the algebra form at m = 1
    for d in (d_pp, d_pn, d_nn):
        assert abs(F(1, d) - (z + d)) < mp.mpf(10) ** -60
    print("  eigen-form F_1(d) = z + d verified at all three letters.")

    # ------------------------------------------------------------ section 2
    hdr("[2] The pn letter sits at the spectral BALANCE POINT")

    print("     letter        d                 |d+q|            |d-1/q|          rho")
    for nm, d in (("pp", d_pp), ("pn", d_pn), ("bal = -h/2", d_bal), ("nn", d_nn)):
        a, b = abs(d + Q), abs(d - qi)
        print(f"   {nm:<12s} {mp.nstr(d, 14):>16s} {mp.nstr(a, 14):>16s} "
              f"{mp.nstr(b, 14):>16s} {mp.nstr(max(a, b), 14):>16s}")

    print(f"\n  at d = -h/2 the two eigenvalues are exact negatives:")
    print(f"    (d+q) + (d-1/q) = {mp.nstr((d_bal + Q) + (d_bal - qi), 5)}")
    assert abs((d_bal + Q) + (d_bal - qi)) < mp.mpf(10) ** -60
    print(f"    |d+q| = [2]_q/2 = {mp.nstr((Q + qi) / 2, 25)}")
    assert abs(abs(d_bal + Q) - (Q + qi) / 2) < mp.mpf(10) ** -60

    disp = d_pn - d_bal
    print(f"\n  and bring_color_weighted displaces it by exactly h.delta/4:")
    print(f"    d_pn - d_bal      = {mp.nstr(disp, 15)}")
    print(f"    h * delta(q0) / 4 = {mp.nstr(h * flavor_split_leading(Q) / 4, 15)}")
    print("    (pyhecke/constants.py's own convention note: 7.190163e-05)")
    assert abs(disp - h * flavor_split_leading(Q) / 4) < mp.mpf(10) ** -60

    # ------------------------------------------------------------ section 3
    hdr("[3] AM-GM decides it:  q > [2]_q/2 > 1  for every q > 1")

    two_half = (Q + qi) / 2
    print(f"  q        = {mp.nstr(Q, 25)}")
    print(f"  [2]_q/2  = {mp.nstr(two_half, 25)}")
    assert Q > two_half > 1
    ratio = Q / two_half
    print(f"\n  q / ([2]_q/2) = {mp.nstr(ratio, 25)}")
    print(f"  2q^2/(q^2+1)  = {mp.nstr(2 * Q ** 2 / (Q ** 2 + 1), 25)}")
    print(f"  1 + tanh(ln q)= {mp.nstr(1 + mp.tanh(mp.log(Q)), 25)}")
    assert abs(ratio - 2 * Q ** 2 / (Q ** 2 + 1)) < mp.mpf(10) ** -60
    assert abs(ratio - (1 + mp.tanh(mp.log(Q)))) < mp.mpf(10) ** -60
    qsym = sp.Symbol("q", positive=True)
    idt = sp.simplify(qsym / ((qsym + 1 / qsym) / 2) - 2 * qsym ** 2 / (qsym ** 2 + 1))
    print(f"\n  symbolic: q/([2]_q/2) - 2q^2/(q^2+1) = {idt}   (exact, all q)")
    assert idt == 0
    print("  So the like-pair channels outgrow the pn channel by exactly")
    print("  1 + delta_CP — the crossing discriminant qou-hjs8 proved theta-free.")

    # ------------------------------------------------------------ section 4
    hdr(f"[4] Measured, m = 1..{M_MAX}: betweenness breaks, pn is never the maximum")

    broken, ever_max, first_neg = [], [], None
    for m in range(1, M_MAX + 1):
        a, b, c = F(m, d_pp), F(m, d_pn), F(m, d_nn)
        lo, hi = min(a, c), max(a, c)
        if not (lo < b < hi):
            broken.append(m)
        if b > a and b > c:
            ever_max.append(m)
        if first_neg is None and c < 0:
            first_neg = m

    print("   m  |    F(d_pp)       F(d_pn)       F(d_nn)   | between | pn max")
    for m in list(range(1, 15)) + [20, 50, 100, M_MAX]:
        a, b, c = F(m, d_pp), F(m, d_pn), F(m, d_nn)
        lo, hi = min(a, c), max(a, c)
        print(f"  {m:3d} | {mp.nstr(a, 9):>13s} {mp.nstr(b, 9):>13s} {mp.nstr(c, 9):>13s} |"
              f" {str(lo < b < hi):>7s} | {str(b > a and b > c):>6s}")

    print(f"\n  F_m(d_nn) first negative at m = {first_neg}  "
          f"(so F_{first_neg + 1} is no longer monotone in d)")
    print(f"  betweenness BROKEN at m = {broken[:8]} ...  ({len(broken)} of {M_MAX})")
    print(f"  pn is the strict MAXIMUM at: {ever_max if ever_max else 'NO m in 1..%d' % M_MAX}")
    assert first_neg == 7
    assert broken and broken[0] == 12
    assert not ever_max                      # the headline

    print("\n  growth rates at m = %d:" % M_MAX)
    for nm, d, pred in (("pp", d_pp, Q), ("pn", d_pn, two_half), ("nn", d_nn, Q)):
        r = abs(F(M_MAX, d)) ** (mp.mpf(1) / M_MAX)
        print(f"    {nm}: |F|^(1/m) = {mp.nstr(r, 15):>18s}   -> {mp.nstr(pred, 15)}")
        assert abs(r - pred) < mp.mpf("0.01")

    # ------------------------------------------------------------ section 5
    hdr("[5] What this settles for class B")

    print("""  THE ESCAPE EXISTS.  Affineness is an m = 1 fact; at m >= 2 the interface
  trace is degree m in d, and betweenness itself fails from m = 12.  So the
  hypothesis of `pn_betweenness_blocks_signMixed` is genuinely breakable, which
  is what the 2026-09-12 entry said class B needs.

  AND IT DOES NOT DELIVER.  The pattern needs mu_pn to be the strict MAXIMUM.
  Betweenness breaks the other way — pn becomes the strict MINIMUM — and pn is
  never the maximum at any m in 1..200.  The reason is structural: the pn letter
  sits at the spectral balance point, where its growth rate is [2]_q/2, while
  both like-pair letters grow at q; AM-GM gives q > [2]_q/2 for every q > 1.

  Scope (b) asymptotically (invariant: AM-GM on the two Hecke eigenvalues);
  MEASURED, not proved, for small m.

  NOT excluded: a derived pn letter that is NOT at the balance point.  That is
  now the whole of class B's remaining room, and it is much narrower than
  "break affineness" — the displacement from balance is h.delta/4 = 7.19e-05,
  and it would have to be large enough to move rho_pn above q.

  Untouched: MAGNITUDE (qou-brng's real target), class D, and the extensive
  term itself.""")

    print("\nPROBE OK — all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
