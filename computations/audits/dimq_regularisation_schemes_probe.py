#!/usr/bin/env python3
"""Regularising tr(id_A) = dim_q(A) for A = O_q(SU(2)): what the two standard schemes give.

CONTEXT.  The owner's 2026-09-15 ruling makes tr(id_X) the quantum dimension.
For the Frobenius-Hopf object A = O_q(SU(2)) the naive quantum dimension is
the Peter-Weyl sum

    dim_q(A) = sum_{m >= 1} [m]_q^2,     [m]_q = (q^m - q^-m)/(q - q^-1),

which DIVERGES at every real q > 1 (computations/audits/
trace_id_quantum_dimension_probe.py, merged as #7421).  So the value, if any,
is a REGULARISED one, and the owner's question -- "is -6 a single term of a
larger object which may or may not vanish" -- becomes: what do the standard
regularisations of this larger object give?

THE OBJECT.  With u = q - q^-1,

    [m]_q^2 = (q^{2m} + q^{-2m} - 2) / u^2,

so the generating function F(t) = sum_{m>=1} [m]_q^2 t^m is, for |t| < q^-2,

    F(t) = (1/u^2) * ( q^2 t/(1 - q^2 t) + q^-2 t/(1 - q^-2 t) - 2 t/(1 - t) ),

a rational function of t whose only singularity on |t| <= 1 is the simple pole
at t = 1 coming from the constant term -2.

TWO SCHEMES, both exact:

  (Z) zeta regularisation: sum q^{2m} -> q^2/(1 - q^2) and sum q^{-2m} ->
      q^-2/(1 - q^-2) (analytic continuation of the geometric series) and
      sum_{m>=1} 1 -> zeta(0) = -1/2.  The two geometric pieces sum to -1,
      the constant piece contributes -2 * zeta(0) = +1, so

          dim_q^Z(A) = 0     for EVERY q.

      Classically (q -> 1) the same scheme gives sum m^2 = zeta(-2) = 0.
      This is chi_eu(SU(2)) = chi(S^3) = 0, the Euler characteristic of the
      group manifold, which is what a regularised "dimension of the regular
      representation" ought to be.

  (H) Hadamard finite part at t = 1: drop the pole -2t/(1-t) and evaluate
      the rest at t = 1:

          dim_q^H(A) = -1/u^2 = -1/(q - q^-1)^2,

      which at the proton pin is about -22.9, and equals -6 only at
      q - q^-1 = 1/sqrt(6), i.e. q = (1/sqrt 6 + sqrt(1/6 + 4))/2 ~ 1.2247,
      not at q0.

So the regularised trace is SCHEME-DEPENDENT, and NEITHER scheme gives -6 at
the substrate parameter.  Under the ruling, -6 cannot be tr(id_A) for the
Frobenius-Hopf object; it belongs to the base curve (chi_eu(M_0) = 2 - 2g).

ALSO MEASURED, because the owner asked what acts on T_{M_0}: the S_5-module
H^1(T_{Sigma_4}) of first-order deformations of Bring's curve decomposes as
the standard 4-dimensional representation plus the 5-dimensional [3,2]
representation, with NO trivial and NO sign summand.  Derivation: Serre
duality H^1(T) = H^0(K^2)^vee; Max Noether's theorem H^0(K^2) = Sym^2 H^0(K)
modulo the unique quadric through the canonical curve; H^0(K) is the standard
representation V_4 of S_5 (the canonical embedding of Bring's curve in
P^3 = P(V_4) is S_5-equivariant) and the quadric is invariant.  The
character computation below is exact (integers), from the S_5 character
table.

WHAT THIS DOES NOT CLAIM.  It does not select a regularisation; it does not
derive -6; it says what the two standard schemes give and that they disagree.
Scope (b) for "neither scheme gives -6 at q0" (invariant: exact rational
identities in q, verified symbolically and numerically); scope (a) elsewhere.

No float anywhere: exact Fractions for the character computation, mpmath mpf
at 50 dps for the numerics, and the closed forms are checked against partial
sums of the SAME generating function at a convergent t.

Run:  python3 computations/audits/dimq_regularisation_schemes_probe.py
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402

from qou_substrate.constants import Q  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

FAILURES: list[str] = []
CHECKS = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


Q0 = mp.mpf(str(Q))


def q_int(q: mp.mpf, m: int) -> mp.mpf:
    return (q**m - q ** (-m)) / (q - 1 / q)


def gen_fn_closed(q: mp.mpf, t: mp.mpf) -> mp.mpf:
    """F(t) = sum_{m>=1} [m]_q^2 t^m in closed form (valid for |t| < q^-2)."""
    u2 = (q - 1 / q) ** 2
    return (q**2 * t / (1 - q**2 * t) + q ** (-2) * t / (1 - q ** (-2) * t)
            - 2 * t / (1 - t)) / u2


def gen_fn_partial(q: mp.mpf, t: mp.mpf, terms: int) -> mp.mpf:
    return mp.fsum(q_int(q, m) ** 2 * t**m for m in range(1, terms + 1))


def hadamard_finite_part(q: mp.mpf) -> mp.mpf:
    """Drop the pole -2t/(1-t) of F at t = 1 and evaluate the rest there."""
    u2 = (q - 1 / q) ** 2
    return (q**2 / (1 - q**2) + q ** (-2) / (1 - q ** (-2))) / u2


def zeta_regularised(q: mp.mpf) -> mp.mpf:
    """Geometric parts by analytic continuation, constant part by zeta(0)."""
    u2 = (q - 1 / q) ** 2
    return (q**2 / (1 - q**2) + q ** (-2) / (1 - q ** (-2)) - 2 * mp.zeta(0)) / u2


# ---------------------------------------------------------------- S_5 side
# Conjugacy classes of S_5 by cycle type, with sizes, and the character table
# rows we need (standard 4-dim V_4 = permutation rep minus trivial).
CYCLE_TYPES = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]
CLASS_SIZE = {(1, 1, 1, 1, 1): 1, (2, 1, 1, 1): 10, (2, 2, 1): 15, (3, 1, 1): 20,
              (3, 2): 20, (4, 1): 30, (5,): 24}


def fixed_points(ct: tuple[int, ...]) -> int:
    return sum(1 for c in ct if c == 1)


def chi_standard(ct: tuple[int, ...]) -> int:
    return fixed_points(ct) - 1


def square_class(ct: tuple[int, ...]) -> tuple[int, ...]:
    """Cycle type of g^2 for g of cycle type ct."""
    out: list[int] = []
    for c in ct:
        if c % 2 == 0:
            out += [c // 2, c // 2]
        else:
            out.append(c)
    return tuple(sorted(out, reverse=True))


def chi_sym2_standard(ct: tuple[int, ...]) -> Fraction:
    x, x2 = chi_standard(ct), chi_standard(square_class(ct))
    return Fraction(x * x + x2, 2)


# Full character table of S_5 (rows: irreps by partition), needed to decompose.
CHAR_TABLE = {
    "[5] trivial":      {(1,1,1,1,1): 1, (2,1,1,1): 1, (2,2,1): 1, (3,1,1): 1, (3,2): 1, (4,1): 1, (5,): 1},
    "[1^5] sign":       {(1,1,1,1,1): 1, (2,1,1,1): -1, (2,2,1): 1, (3,1,1): 1, (3,2): -1, (4,1): -1, (5,): 1},
    "[4,1] standard":   {(1,1,1,1,1): 4, (2,1,1,1): 2, (2,2,1): 0, (3,1,1): 1, (3,2): -1, (4,1): 0, (5,): -1},
    "[2,1^3]":          {(1,1,1,1,1): 4, (2,1,1,1): -2, (2,2,1): 0, (3,1,1): 1, (3,2): 1, (4,1): 0, (5,): -1},
    "[3,2]":            {(1,1,1,1,1): 5, (2,1,1,1): 1, (2,2,1): 1, (3,1,1): -1, (3,2): 1, (4,1): -1, (5,): 0},
    "[2,2,1]":          {(1,1,1,1,1): 5, (2,1,1,1): -1, (2,2,1): 1, (3,1,1): -1, (3,2): -1, (4,1): 1, (5,): 0},
    "[3,1,1]":          {(1,1,1,1,1): 6, (2,1,1,1): 0, (2,2,1): -2, (3,1,1): 0, (3,2): 0, (4,1): 0, (5,): 1},
}


def multiplicity(chi: dict, irrep: dict) -> Fraction:
    tot = Fraction(0)
    for ct in CYCLE_TYPES:
        tot += CLASS_SIZE[ct] * Fraction(chi[ct]) * irrep[ct]
    return tot / 120


def main() -> int:
    print(f"q0 = {mp.nstr(Q0, 20)}   (proton pin, qou_substrate.constants.Q)")
    print()

    # -- 1. the closed form is the generating function --------------------
    print("1. closed form of F(t) = sum [m]_q^2 t^m agrees with partial sums at a convergent t")
    t = Q0 ** (-2) / 3
    fc, fp = gen_fn_closed(Q0, t), gen_fn_partial(Q0, t, 400)
    check("closed form vs 400-term partial sum at t = q^-2/3", abs(fc - fp) < mp.mpf("1e-40"),
          f"closed = {mp.nstr(fc, 25)}\npartial = {mp.nstr(fp, 25)}")
    # The same identity at a generic exact q: q = 3/2 with t = 1/9.
    q32, t9 = mp.mpf(3) / 2, mp.mpf(1) / 9
    check("closed form vs partial sum at q = 3/2, t = 1/9",
          abs(gen_fn_closed(q32, t9) - gen_fn_partial(q32, t9, 400)) < mp.mpf("1e-40"))
    print()

    # -- 2. the two schemes ----------------------------------------------
    print("2. regularised values of dim_q(O_q(SU(2)))")
    z, h = zeta_regularised(Q0), hadamard_finite_part(Q0)
    # The vanishing is the EXACT rational identity q^2/(1-q^2) + q^-2/(1-q^-2) = -1
    # (so the numerator is -1 - 2*zeta(0) = 0); test the numerator, not the
    # quotient by u^2, which amplifies the cancellation noise by 1/u^2 near q = 1.
    zeta_num = Q0**2 / (1 - Q0**2) + Q0 ** (-2) / (1 - Q0 ** (-2)) - 2 * mp.zeta(0)
    check("zeta-regularised numerator is 0 at q0 (exact identity, mpf at 50 dps)",
          abs(zeta_num) < mp.mpf("1e-45"), f"numerator = {mp.nstr(zeta_num, 8)};  value = {mp.nstr(z, 8)}")
    for qq in (Fraction(3, 2), Fraction(2), Fraction(101, 100)):
        geom = qq**2 / (1 - qq**2) + qq ** (-2) / (1 - qq ** (-2))
        check(f"exact: q^2/(1-q^2) + q^-2/(1-q^-2) = -1 at q = {qq}, so the zeta value is 0",
              geom == Fraction(-1) and geom - 2 * Fraction(-1, 2) == 0)
    u2 = (Q0 - 1 / Q0) ** 2
    check("Hadamard finite part equals -1/(q - q^-1)^2 at q0", abs(h + 1 / u2) < mp.mpf("1e-45"),
          f"value = {mp.nstr(h, 20)}")
    check("neither scheme gives -6 at q0", abs(z + 6) > 1 and abs(h + 6) > 1,
          f"|zeta + 6| = {mp.nstr(abs(z + 6), 8)},  |hadamard + 6| = {mp.nstr(abs(h + 6), 8)}")
    q_star = (1 / mp.sqrt(6) + mp.sqrt(mp.mpf(1) / 6 + 4)) / 2
    check("the Hadamard value reaches -6 only at q - q^-1 = 1/sqrt(6), i.e. q ~ 1.2247, not q0",
          abs(hadamard_finite_part(q_star) + 6) < mp.mpf("1e-40") and abs(q_star - Q0) > mp.mpf("0.1"),
          f"q* = {mp.nstr(q_star, 20)},  q0 = {mp.nstr(Q0, 20)}")
    check("the fundamental keeps dim_q(V) = [2]_q, finite and positive",
          abs(q_int(Q0, 2) - (Q0 + 1 / Q0)) < mp.mpf("1e-45") and q_int(Q0, 2) > 0,
          f"[2]_q = {mp.nstr(q_int(Q0, 2), 20)}")
    print()

    # -- 3. S_5 acting on H^1(T) of Bring's curve ---------------------------
    print("3. H^1(T_{Sigma_4}) = (Sym^2 V_4 / quadric)^vee as an S_5-module")
    chi_sym2 = {ct: chi_sym2_standard(ct) for ct in CYCLE_TYPES}
    chi_h1 = {ct: chi_sym2[ct] - 1 for ct in CYCLE_TYPES}  # remove the invariant quadric
    check("dim Sym^2(V_4) = 10 and dim H^1(T) = 9 = 3g - 3 at g = 4",
          chi_sym2[(1, 1, 1, 1, 1)] == 10 and chi_h1[(1, 1, 1, 1, 1)] == 9)
    mults = {name: multiplicity(chi_h1, row) for name, row in CHAR_TABLE.items()}
    check("all multiplicities are non-negative integers",
          all(m.denominator == 1 and m >= 0 for m in mults.values()),
          "\n".join(f"{name:18s} x {m}" for name, m in mults.items()))
    check("H^1(T) = standard (4) + [3,2] (5): no trivial and no sign summand",
          mults["[4,1] standard"] == 1 and mults["[3,2]"] == 1
          and mults["[5] trivial"] == 0 and mults["[1^5] sign"] == 0
          and sum(mults.values()) == 2)
    check("consequence: the S_5-invariant deformation space of Bring's curve is 0 (rigidity)",
          mults["[5] trivial"] == 0)
    print()

    print(f"{CHECKS - len(FAILURES)}/{CHECKS} checks pass")

    w = WitnessBuilder("dimq-regularisation-schemes", engine="mpmath")
    out = w.save(
        {
            "q0Anchor": "proton",
            "description": (
                "Under the 2026-09-15 ruling tr(id_X) = dim_q(X), the Frobenius-Hopf "
                "object A = O_q(SU(2)) has a divergent naive quantum dimension; this "
                "witness records the two standard regularisations (zeta: 0 for every q, "
                "= chi_eu(SU(2)); Hadamard finite part: -1/(q-q^-1)^2), that neither is "
                "-6 at q0, and the S_5-decomposition H^1(T_{Sigma_4}) = [4,1] + [3,2] "
                "with no invariants."
            ),
            "q0Value": mp.nstr(Q0, 40),
            "zeta_regularised_dimq_A": mp.nstr(z, 30),
            "hadamard_finite_part_dimq_A": mp.nstr(h, 40),
            "hadamard_closed_form": "-1/(q - 1/q)^2",
            "q_at_which_hadamard_equals_minus_six": mp.nstr(q_star, 40),
            "dimq_fundamental_two_q": mp.nstr(q_int(Q0, 2), 40),
            "h1_tangent_bring_s5_decomposition": {k: int(v) for k, v in mults.items()},
            "checks": CHECKS,
            "failures": FAILURES,
            "scope": "b for 'neither scheme gives -6 at q0'; a elsewhere; no regularisation selected",
        }
    )
    print(f"witness -> {out}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
