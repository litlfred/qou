#!/usr/bin/env python3
"""Keystone — Klein icosahedral construction of the (2,3,5) generators on ℙ(V),
with the order-5 product = the corpus ζ₅ pentad.

Discharges the *group-theoretic core* of `conj:klein-bring-icosahedral-bridge`
(the surviving part after the trefoil (2,3,2) refutation in
`dihedral_two_cycle_sq`). Parameter-free, no fit.

Construction (Klein, *Lectures on the Icosahedron*, 1888) on the projective
line ℙ(V) with coordinate w, ε = e^{2πi/5}:

  S : w ↦ ε·w           — the ζ₅ PENTAD (order 5), the corpus weak 5-fold,
                          fixing 0/∞; its equatorial orbit is {ζ₅ᵏ}.
  T = (1/√5)·[[ε−ε⁴, ε²−ε³], [ε²−ε³, −(ε−ε⁴)]]   — Klein's icosahedral 2-fold,
                          at the icosahedral angle (NOT the corpus EM β=exp(πe₁),
                          which is perpendicular and gives the (2,3,2) trefoil).

Then  c₂ := T (order 2),  c₃ := T·S (order 3),  and

  c₂·c₃ = T·T·S = S = the ζ₅ pentad   (order exactly 5).

So an order-2 / order-3 pair at the icosahedral angle exists whose product is
the corpus ζ₅ pentad — the icosahedral (2,3,5), with ⟨S,T⟩ ≅ A₅ (order 60).
The RESIDUAL open content is purely the orbifold identification
ℙ(V)/A₅ ≅ S²(2,3,5) = the keystone Seifert base of S³/2I.

Also emits the explicit A₅ permutation triple used by the sorry-free Lean
`icosahedral_235_realizable`.
"""
import cmath
import math
import itertools


def mm(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def mpow(M, n):
    R = [[1, 0], [0, 1]]
    for _ in range(n):
        R = mm(R, M)
    return R


def proj_is_I(M, tol=1e-9):
    return abs(M[0][1]) < tol and abs(M[1][0]) < tol and abs(M[0][0] - M[1][1]) < tol


def proj_eq(A, B, tol=1e-7):
    for i in range(2):
        for j in range(2):
            if abs(B[i][j]) > 1e-12:
                lam = A[i][j] / B[i][j]
                return all(abs(A[a][b] - lam * B[a][b]) < tol for a in range(2) for b in range(2))
    return False


def klein_construction():
    eps = cmath.exp(2j * math.pi / 5)
    r5 = math.sqrt(5)
    S = [[eps, 0], [0, 1]]                                   # ζ₅ pentad, w ↦ εw
    a, b = eps - eps ** 4, eps ** 2 - eps ** 3
    T = [[a / r5, b / r5], [b / r5, -a / r5]]                # Klein icosahedral 2-fold
    det_T = (T[0][0] * T[1][1] - T[0][1] * T[1][0]).real
    TS = mm(T, S)
    c2c3 = mm(T, TS)                                         # = S
    checks = {
        "det_T_eq_1": abs(det_T - 1) < 1e-9,
        "S^5 = I (pentad order 5)": proj_is_I(mpow(S, 5)),
        "T^2 = I (order 2)": proj_is_I(mpow(T, 2)),
        "(ST)^3 = I": proj_is_I(mpow(mm(S, T), 3)),
        "c3 = TS order 3": proj_is_I(mpow(TS, 3)),
        "c2*c3 = S (ζ5 pentad)": proj_eq(c2c3, S),
        "(c2*c3)^5 = I": proj_is_I(mpow(c2c3, 5)),
        "(c2*c3)^2 != I (order exactly 5)": not proj_is_I(mpow(c2c3, 2)),
    }
    return checks


def a5_triple():
    def compose(p, q):
        return tuple(p[q[i]] for i in range(5))

    def order(p):
        e = tuple(range(5))
        r, n = p, 1
        while r != e:
            r, n = compose(r, p), n + 1
        return n

    def even(p):
        s = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if p[i] > p[j]:
                    s ^= 1
        return s == 0

    A5 = [p for p in itertools.permutations(range(5)) if even(p)]
    five = (1, 2, 3, 4, 0)  # (0 1 2 3 4)
    for c2 in A5:
        if order(c2) != 2:
            continue
        for c3 in A5:
            if order(c3) == 3 and compose(c2, c3) == five:
                return c2, c3, compose(c2, c3)
    return None


def main():
    print("== Klein icosahedral construction on ℙ(V) (ε = e^{2πi/5}) ==")
    ok = True
    for k, v in klein_construction().items():
        print(f"  {'OK ' if v else 'FAIL'}  {k}")
        ok = ok and v
    c2, c3, prod = a5_triple()
    print("\n== explicit A₅ triple for Lean `icosahedral_235_realizable` ==")
    print(f"  c2 = {c2}  = (1 2)(3 4), order 2")
    print(f"  c3 = {c3}  = (0 2 4),   order 3")
    print(f"  c2∘c3 = {prod} = (0 1 2 3 4), order 5")
    assert ok, "Klein construction relations failed"
    print("\nVERDICT: icosahedral-angle (2,3,5) generators with c2·c3 = ζ₅ pentad "
          "EXIST (group core discharged); residual = ℙ(V)/A₅ ≅ S²(2,3,5) keystone base.")


if __name__ == "__main__":
    main()
