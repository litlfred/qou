"""qbeta_prearchimedean_z_recursion.py — pre-archimedean recursion for the
Q_β Markov-parameter Taylor coefficients (PR #1727 follow-up).

Owner directives: "recursion ↔ PDE via q-difference" + "do as much
pre-archimedean". This probe derives — SYMBOLICALLY, in formal q, NOT
fitted at q_0 — the explicit recursion the Taylor coefficients of the
Markov parameter z(q) = √q/(1+q) satisfy around q=1, and extends them
to arbitrary order.

## The pre-archimedean object

τ_M(T_β)(q) is an EXACT algebraic function (sum of z(q)^k, per
`qbeta-decay-sdp-knot-operator.witness.json`). Since z² = q/(1+q)² ∈ ℚ(q),
every power z^k reduces to A_k(q) + B_k(q)·z, so

    τ_M(T_β)(q) = A(q) + B(q)·z(q),   A, B ∈ ℚ(q).

Its Taylor coefficients around q=1 are therefore (rational-function
coefficients) + (B-convolved z-coefficients). The ONLY non-rational
ingredient is z(q); its coefficients carry all the holonomic structure.

## The recursion = the q-difference equation = the "PDE"

z = √(1+w)/(2+w), w = q−1, is ALGEBRAIC ⇒ D-finite. It satisfies the
first-order ODE (derived by hand, verified below):

    (4 + 6w + 2w²)·z'(w) + w·z(w) = 0.

Writing z = Σ a_n w^n and collecting the coefficient of w^n gives the
explicit 3-term recursion:

    4(n+1)·a_{n+1} + 6n·a_n + (2n−1)·a_{n−1} = 0
    ⇒  a_{n+1} = −[ 6n·a_n + (2n−1)·a_{n−1} ] / (4(n+1)),

with a_0 = z(1) = 1/2, a_1 = 0. This is EXACT, pre-archimedean, and
extends to ALL n (answers "c_k for k≫10"). It is the discrete shadow
of the q-difference equation z satisfies — the recursion ↔ PDE identity.

This probe:
  1. Verifies the closed-form recursion against a sympy series expansion.
  2. Extends a_n to n=30 via the recursion (no fitting).
  3. Confirms the coefficients are EXACT rationals (pre-archimedean).

Ref: docs/coordination/2026-06-02-qbeta-habiro-recursion-prearchimedean-scope.md
Ref: qbeta-decay-sdp-knot-operator.witness.json (τ_M = Σ z^k structure)
"""
from __future__ import annotations

import sys
from pathlib import Path

# computations/ on sys.path — for _path_bridge (substrate/_precision) + witness_base
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _bridge

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def z_recursion_coeffs(n_max: int) -> list[sp.Rational]:
    """Exact Taylor coefficients a_n of z(q)=√q/(1+q) around q=1,
    via the derived recursion 4(n+1)a_{n+1} + 6n·a_n + (2n−1)a_{n−1} = 0.

    Pre-archimedean: every a_n is an EXACT rational. No q_0, no fitting.
    """
    if n_max < 0:
        raise ValueError("n_max must be a non-negative integer")
    a = [sp.Rational(0)] * (n_max + 1)
    a[0] = sp.Rational(1, 2)              # z(1) = 1/2
    if n_max >= 1:
        a[1] = sp.Rational(0)             # z'(1) = 0
    for n in range(1, n_max):
        # 4(n+1) a_{n+1} = -[6n a_n + (2n-1) a_{n-1}]  (Python ints coerce via a[·] ∈ ℚ)
        a[n + 1] = -(6 * n * a[n] + (2 * n - 1) * a[n - 1]) / (4 * (n + 1))
    return a


def zk_recursion_coeffs(k: int, n_max: int) -> list[sp.Rational]:
    """Exact Taylor coefficients of z(q)^k around q=1, via the
    one-parameter recursion family

        4(n+1) b_{n+1} + 6n·b_n + (2(n−1)+k)·b_{n−1} = 0,
        b_0 = (1/2)^k,  b_1 = 0.

    Derived from (4+6w+2w²)·(z^k)' + k·w·z^k = 0, which follows from
    z's own ODE since (z^k)' = k z^{k−1} z'. Pre-archimedean, exact.
    """
    if n_max < 0:
        raise ValueError("n_max must be a non-negative integer")
    b = [sp.Rational(0)] * (n_max + 1)
    b[0] = sp.Rational(1, 2) ** k
    if n_max >= 1:
        b[1] = sp.Rational(0)
    for n in range(1, n_max):
        b[n + 1] = -(6 * n * b[n] + (2 * (n - 1) + k) * b[n - 1]) / (4 * (n + 1))
    return b


def main() -> int:
    w = sp.symbols("w")              # w = q - 1
    q = 1 + w
    z = sp.sqrt(q) / (1 + q)         # z(q) = √q/(1+q), pre-archimedean

    N = 30
    print("Q_β pre-archimedean Markov-parameter recursion")
    print("  z(q) = √q/(1+q),  w = q−1")
    print()

    # (1) verify the ODE (4 + 6w + 2w²) z' + w z = 0
    zp = sp.diff(z, w)
    ode_residual = sp.simplify((4 + 6 * w + 2 * w ** 2) * zp + w * z)
    print(f"  ODE check: (4+6w+2w²)·z' + w·z = {ode_residual}  "
          f"({'✓ ZERO' if ode_residual == 0 else '✗ NONZERO'})")
    print()

    # (2) sympy series expansion (ground truth)
    series = sp.series(z, w, 0, 12).removeO()
    series_coeffs = [series.coeff(w, n) for n in range(12)]

    # (3) recursion-generated coefficients
    rec_coeffs = z_recursion_coeffs(N)

    print("  n |   a_n (sympy series)   |   a_n (recursion)   | match")
    print("  --+------------------------+---------------------+------")
    all_match = True
    for n in range(12):
        s = series_coeffs[n]               # already an exact rational (no nsimplify needed)
        r = rec_coeffs[n]
        m = sp.simplify(s - r) == 0
        all_match = all_match and m
        print(f"  {n:>2d} | {str(s):>22s} | {str(r):>19s} | {'✓' if m else '✗'}")
    print()
    print(f"  Recursion reproduces sympy series exactly: {'YES ✓' if all_match else 'NO ✗'}")
    print()

    # (4) extension to high order — the point: NO new input needed
    print("  Extension via recursion (NO fitting, NO q_0) — c_k for k≫10:")
    for n in [12, 15, 20, 25, 30]:
        print(f"    a_{n:>2d} = {rec_coeffs[n]}  = {float(rec_coeffs[n]):.6e}")
    print()
    print("  All a_n are EXACT rationals (pre-archimedean). The recursion")
    print("  IS the discrete shadow of z's q-difference equation; it")
    print("  determines the full sequence from a_0=1/2, a_1=0.")

    # (5) the z^k recursion family — generates ALL of τ_M(T_β) = Σ d_k z^k
    print()
    print("  z^k recursion family:  4(n+1)b_{n+1} + 6n·b_n + (2(n−1)+k)b_{n−1} = 0")
    print("  Verify against sympy series of z^k for k=1,2,3 (the τ_M powers):")
    family_ok = True
    for k in (1, 2, 3):
        sk = sp.series(z ** k, w, 0, 8).removeO()
        bk = zk_recursion_coeffs(k, 8)
        ok_k = all(sp.simplify(sk.coeff(w, n) - bk[n]) == 0 for n in range(8))
        family_ok = family_ok and ok_k
        print(f"    k={k}: b_0..b_7 = {[str(bk[n]) for n in range(8)]}  "
              f"{'✓' if ok_k else '✗'}")
    print(f"  z^k family reproduces all powers exactly: {'YES ✓' if family_ok else 'NO ✗'}")
    print()
    print("  ⇒ τ_M(T_β) = Σ_{k=0..3} d_k·z^k is generated entirely by this")
    print("    explicit recursion family + the NF weights d_k (initial data).")
    print("    The Q_β precision-ladder c_k descend from τ_M via the finite")
    print("    Q_A·cos algebraic comparison — so they are RECURSION-GENERATED,")
    print("    not independently fitted. (Pre-archimedean; q_0 enters only at")
    print("    the final archimedean τ-functor evaluation.)")

    # Witness
    wn = WitnessBuilder("qbeta-prearchimedean-z-recursion", engine="sympy")
    wn.set_description(
        "Pre-archimedean (symbolic, formal q) derivation of the explicit "
        "3-term recursion for the Taylor coefficients of the Markov "
        "parameter z(q)=√q/(1+q) around q=1: 4(n+1)a_{n+1} + 6n·a_n + "
        "(2n−1)a_{n−1} = 0, from the ODE (4+6w+2w²)z'+wz=0. This is the "
        "recursion↔q-difference identity. Coefficients are EXACT "
        "rationals, extend to all orders with no q_0 / no CODATA fitting. "
        "τ_M(T_β) = A(q)+B(q)·z(q) inherits this structure (z² ∈ ℚ(q))."
    )
    wn.add_data("ode", "(4+6w+2w^2)*z' + w*z = 0")
    wn.add_data("recursion", "4(n+1)a_{n+1} + 6n*a_n + (2n-1)a_{n-1} = 0")
    wn.add_data("a_0", str(rec_coeffs[0]))
    wn.add_data("a_1", str(rec_coeffs[1]))
    for n in [2, 5, 10, 15, 20, 30]:
        wn.add_data(f"a_{n}", str(rec_coeffs[n]))
    wn.add_assertion(
        name="recursion_matches_sympy_series_exactly",
        computed=bool(all_match),
        expected=True,
        tolerance=0,
        source="3-term recursion vs sympy series of √q/(1+q), 12 orders",
    )
    wn.add_assertion(
        name="ode_residual_is_zero",
        computed=bool(ode_residual == 0),
        expected=True,
        tolerance=0,
        source="(4+6w+2w^2)z' + wz simplifies to 0",
    )
    wn.add_data("zk_recursion", "4(n+1)b_{n+1} + 6n*b_n + (2(n-1)+k)*b_{n-1} = 0")
    wn.add_assertion(
        name="zk_recursion_family_matches_series_k1_k2_k3",
        computed=bool(family_ok),
        expected=True,
        tolerance=0,
        source="z^k recursion family vs sympy series for k=1,2,3 (τ_M powers)",
    )
    out = wn.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
