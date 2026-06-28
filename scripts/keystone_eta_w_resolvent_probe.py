#!/usr/bin/env python3
"""η↔w resolvent probe — the last sliver of conj:klein-bring-icosahedral-bridge.

The bridge's group + orbifold + Möbius-realization layers are settled (merged
PR #2928). The sole residual is: realize the canonical A₅ as ONE icosahedral
Möbius action on ℙ(V), i.e. identify the corpus trefoil (acting on the spectral
ratios η) with the icosahedral 3-fold of the A₅ whose 5-fold is the ζ₅ pentad
(acting on the base z). This probe sharpens exactly what Klein's resolvent must
accomplish — and flags a trap.

OBSTRUCTION (the trap).  The so3-generators realization of the order-3 trefoil
is α = rotation by 2π/3 about e₃ — the SAME axis as the pentad S (w↦εw, 2π/5
about the Hopf polar axis e₃). Coaxial rotations commute, so

    ⟨α(e₃), pentad(e₃)⟩ = C₁₅   (abelian) — NOT A₅.

So the icosahedral 3-fold is NOT the so3 α-about-e₃. A naive "use the existing
geometric generators" assembly fails for the 3-fold exactly as the EM 2-fold
failed (dihedral, PR #2928).

TARGET (what the resolvent must hit).  The icosahedral 3-fold sits about an axis
at the icosahedral vertex→face angle from e₃. Placing the order-3 there (Klein's
ST, order 3, non-coaxial) with the pentad S DOES generate A₅ (order 60). So
Klein's resolvent must transport the trefoil's spectral-η 3-fold onto that
non-coaxial icosahedral-angle axis. That transport is the open geometric step.
"""
import cmath
import math


def so3_coaxial_obstruction():
    def Rz(t):
        c, s = math.cos(t), math.sin(t)
        return ((c, -s, 0.0), (s, c, 0.0), (0.0, 0.0, 1.0))

    def mul(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))

    def key(M):
        return tuple(round(M[i][j], 5) for i in range(3) for j in range(3))

    alpha, pent = Rz(2 * math.pi / 3), Rz(2 * math.pi / 5)  # both about e₃
    I = Rz(0.0)
    elems = {key(I): I}
    queue = [I]                          # queue-based BFS: each element multiplied once
    while queue:
        M = queue.pop()
        for g in (alpha, pent):
            P = mul(M, g)
            k = key(P)
            if k not in elems:
                elems[k] = P
                queue.append(P)
    commute = key(mul(alpha, pent)) == key(mul(pent, alpha))
    return len(elems), commute


def klein_icosahedral_target():
    # Klein Möbius S (=ζ₅ pentad, order 5) and T (icosahedral 2-fold); ST has
    # order 3 and is non-coaxial. ⟨S, ST⟩ = ⟨S, T⟩ = A₅ (order 60).
    eps = cmath.exp(2j * math.pi / 5)
    r5 = math.sqrt(5)
    S = [[eps, 0], [0, 1]]
    a, b = eps - eps ** 4, eps ** 2 - eps ** 3
    T = [[a / r5, b / r5], [b / r5, -a / r5]]

    def mm(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def pkey(M, tol=4):
        # projective key: normalize by first nonzero entry, round
        for i in range(2):
            for j in range(2):
                if abs(M[i][j]) > 1e-9:
                    lam = M[i][j]
                    N = [[M[r][c] / lam for c in range(2)] for r in range(2)]
                    return tuple(complex(round(N[r][c].real, tol), round(N[r][c].imag, tol)) for r in range(2) for c in range(2))
        return None

    ST = mm(S, T)  # order-3, non-coaxial
    gens = [S, ST]
    I = [[1, 0], [0, 1]]
    elems = {pkey(I): I}
    queue = [I]                          # queue-based BFS in PSL(2,C) (projective)
    for M in queue:
        for g in gens:
            P = mm(M, g)
            k = pkey(P)
            if k not in elems:
                elems[k] = P
                queue.append(P)
    return len(elems)


def main():
    n_coax, commute = so3_coaxial_obstruction()
    print("== OBSTRUCTION: so3 trefoil α and pentad are coaxial (both about e₃) ==")
    print(f"   ⟨α(e₃,2π/3), pentad(e₃,2π/5)⟩ order = {n_coax}  (expect 15 = C₁₅, abelian)")
    print(f"   commute (αS = Sα)? {commute}")
    assert n_coax == 15 and commute, "expected coaxial C₁₅"
    n_ico = klein_icosahedral_target()
    print("\n== TARGET: pentad S + non-coaxial icosahedral 3-fold (Klein ST) ==")
    print(f"   ⟨S, ST⟩ order = {n_ico}  (expect 60 = A₅)")
    assert n_ico == 60, "expected A₅"
    print("\nVERDICT: the icosahedral 3-fold is NOT the coaxial so3 α; Klein's resolvent")
    print("must transport the spectral-η trefoil to the non-coaxial icosahedral-angle")
    print("axis (Klein ST). That transport η↔w is the sole open step of the bridge.")


if __name__ == "__main__":
    main()
