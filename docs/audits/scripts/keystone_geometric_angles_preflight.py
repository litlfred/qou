#!/usr/bin/env python3
"""
Geometric angles of the A₅ ↔ icosahedral fibre map, and the W_λ target —
the computable preflight for the equivariant-index = W_λ object
(`conj:s5-so3-fiber-action`, bean s5bb).

Owner-authorized exploration of the geometric angles (the owner-gated
`irrepToRotation` of `S5SO3FiberAction.lean`), made explicit, plus the forced
target W_λ and the McKay/E₈ algebraic shadow.

PATHS RUN HERE (3 of the 4 the owner picked):
  (1) EXPLICIT ANGLES   — the icosahedral conjugacy-class rotation angles, the
      A₅ character table, and the SO(3)-restriction validation (the exact
      golden-ratio character values φ = (1+√5)/2 that pin T₁←ℓ=1, H←ℓ=2).
  (3) W_λ TARGET        — W_λ = d_q(λ)²/[n]_q! (q-Plancherel / Ocneanu measure),
      via the balanced-q-integer hook-length formula; self-checked against the
      scope doc (`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`):
      (3,1,1)→0.29467, (3,2)→0.20754, [5]_q!→131.313.
  (4) McKAY / E₈ SHADOW — 2I (binary icosahedral) is the McKay group of affine
      Ê₈; its irrep dimensions ARE the E₈ marks {1,2,3,4,5,6,4,2,3}. Records the
      relation of the A₅ (= I) irreps to that, as the finite algebraic shadow of
      the equivariant index.

The deep target — WRT TQFT of S³/2I (Lawrence–Zagier) reproducing W_λ — is a
separate, follow-up probe.

DISCIPLINE: parameter-free; the angles are KNOWN group theory (not fitted); the
character validation is EXACT (φ closed form). No fit, nothing wired.
"""
from mpmath import mp, mpf, sqrt, cos, pi, acos, nstr

mp.dps = 40
Q0 = mpf("1.1099785955541805")

# ---------------------------------------------------------------------------
# (1) EXPLICIT ANGLES: A₅ conjugacy classes ↔ icosahedral rotation angles
# ---------------------------------------------------------------------------
# A₅ ≅ icosahedral rotation group I ⊂ SO(3).  Five conjugacy classes, each a
# rotation by a definite angle; class sizes sum to |A₅| = 60.
PHI = (1 + sqrt(5)) / 2          # golden ratio (1+√5)/2 ≈ 1.618
CLASSES = [
    # name,        size, rotation angle θ
    ("e",            1,  mpf(0)),
    ("2-fold",      15,  pi),
    ("3-fold",      20,  2 * pi / 3),
    ("5-fold",      12,  2 * pi / 5),
    ("5'-fold",     12,  4 * pi / 5),
]

# A₅ character table (standard; rows = irreps, cols = classes in CLASSES order).
# φ = (1+√5)/2,  1-φ = (1-√5)/2 = -1/φ.
ONE_M_PHI = (1 - sqrt(5)) / 2
CHAR = {
    "A":  [mpf(1), mpf(1),  mpf(1),  mpf(1),    mpf(1)],     # trivial, dim 1
    "T1": [mpf(3), mpf(-1), mpf(0),  PHI,       ONE_M_PHI],  # dim 3  (ℓ=1)
    "T2": [mpf(3), mpf(-1), mpf(0),  ONE_M_PHI, PHI],        # dim 3' (ℓ=1 twin)
    "G":  [mpf(4), mpf(0),  mpf(1),  mpf(-1),   mpf(-1)],    # dim 4  (ℓ=3 part)
    "H":  [mpf(5), mpf(1),  mpf(-1), mpf(0),    mpf(0)],     # dim 5  (ℓ=2)
}
DIM = {"A": 1, "T1": 3, "T2": 3, "G": 4, "H": 5}


def so3_character(ell, theta):
    """χ of the SO(3) spin-ℓ irrep at a rotation by θ: sin((2ℓ+1)θ/2)/sin(θ/2)."""
    from mpmath import sin
    if theta == 0:
        return mpf(2 * ell + 1)
    return sin((2 * ell + 1) * theta / 2) / sin(theta / 2)


def main():
    print(f"q_0 = {Q0}  |  dps = {mp.dps}\n")
    print("=" * 70)
    print("(1) EXPLICIT GEOMETRIC ANGLES — A₅ ⊂ SO(3) icosahedral rotations")
    print("=" * 70)
    print(f"{'class':<9}{'size':>5}{'angle θ':>16}{'θ (deg)':>10}")
    for name, size, th in CLASSES:
        print(f"{name:<9}{size:>5}{nstr(th,10):>16}{nstr(th*180/pi,6):>10}")
    print(f"  (Σ sizes = {sum(s for _,s,_ in CLASSES)} = |A₅|)\n")

    # SO(3)-restriction validation: T₁←ℓ=1, H←ℓ=2 must match the char table EXACTLY.
    print("SO(3)-restriction validation (χ_ℓ(θ) vs A₅ char table, must be ~0):")
    checks = [("T1", 1), ("H", 2)]
    for irrep, ell in checks:
        maxerr = mpf(0)
        for k, (name, _, th) in enumerate(CLASSES):
            pred = so3_character(ell, th)
            err = abs(pred - CHAR[irrep][k])
            maxerr = max(maxerr, err)
        print(f"  {irrep} = ℓ={ell} restriction : max|χ_ℓ − χ_table| = {nstr(maxerr,4)}")
    # the signature golden-ratio identity:
    g5 = so3_character(1, 2 * pi / 5)
    print(f"  signature: χ_(ℓ=1)(2π/5) = 1+2cos(72°) = {nstr(g5,16)}  vs  φ = {nstr(PHI,16)}")
    print(f"            |χ − φ| = {nstr(abs(g5 - PHI),4)}  (EXACT, parameter-free)\n")

    # Reeb phase per irrep on the principal (5-fold) rotation: θ_λ = arccos(χ_λ/dim).
    print("Reeb phase θ_λ = arccos(χ_λ(5-fold)/dim_λ)  — the explicit per-irrep angle:")
    idx5 = 3  # 5-fold class index
    for irrep in ["A", "T1", "T2", "G", "H"]:
        r = CHAR[irrep][idx5] / DIM[irrep]
        if abs(r) <= 1:
            th = acos(r)
            print(f"  {irrep:<3} χ/dim = {nstr(r,8):>12}   θ_λ = {nstr(th,10)} rad = {nstr(th*180/pi,7)}°")
        else:
            print(f"  {irrep:<3} χ/dim = {nstr(r,8):>12}   |χ/dim|>1 (growth regime, arccosh)")
    print()

    # -----------------------------------------------------------------------
    # (3) W_λ TARGET: W_λ = d_q(λ)² / [n]_q!  (q-Plancherel / Ocneanu measure)
    # -----------------------------------------------------------------------
    print("=" * 70)
    print("(3) W_λ TARGET — q-Plancherel measure d_q(λ)²/[n]_q! at q_0 (n=5)")
    print("=" * 70)

    def qint(m):                       # balanced q-integer [m]_q
        return (Q0**m - Q0**(-m)) / (Q0 - Q0**(-1))

    def hooks(lam):
        cells = [(i, j) for i, r in enumerate(lam) for j in range(r)]
        conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
        out = []
        for (i, j) in cells:
            arm = lam[i] - j - 1
            leg = conj[j] - i - 1
            out.append(arm + leg + 1)
        return out

    def q_factorial(m):
        from mpmath import mpf as _m
        r = _m(1)
        for k in range(1, m + 1):
            r *= qint(k)
        return r

    def d_q(lam):
        from mpmath import mpf as _m
        num = q_factorial(sum(lam))
        den = _m(1)
        for h in hooks(lam):
            den *= qint(h)
        return num / den

    PARTS5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
    q5fac = q_factorial(5)
    print(f"[5]_q! = {nstr(q5fac, 10)}   (scope doc: 131.313)\n")
    print(f"{'λ':<14}{'d_q(λ)':>12}{'W_λ = d_q²/[5]!':>18}{'role':>12}")
    role = {(3, 1, 1): "electron", (3, 2): "muon", (2, 2, 1): "(3,2)-twin"}
    Wsum = mpf(0)
    for lam in PARTS5:
        dq = d_q(lam)
        W = dq * dq / q5fac
        Wsum += W
        print(f"{str(lam):<14}{nstr(dq,8):>12}{nstr(W,10):>18}{role.get(lam,''):>12}")
    print(f"  Σ_λ W_λ = {nstr(Wsum, 12)}   (q-Plancherel normalisation ⇒ should = 1)")
    # self-check vs scope doc
    print("\nself-check vs scope doc:")
    print(f"  W_(3,1,1) = {nstr(d_q((3,1,1))**2/q5fac,8)}   (scope: 0.29467)")
    print(f"  W_(3,2)   = {nstr(d_q((3,2))**2/q5fac,8)}   (scope: 0.20754)")
    print()

    # -----------------------------------------------------------------------
    # (4) McKAY / E₈ SHADOW
    # -----------------------------------------------------------------------
    print("=" * 70)
    print("(4) McKAY / E₈ SHADOW — 2I (binary icosahedral) ↔ affine Ê₈")
    print("=" * 70)
    e8_marks = [1, 2, 3, 4, 5, 6, 4, 2, 3]   # affine E₈ Coxeter marks
    print(f"  2I irrep dims = affine Ê₈ Coxeter marks = {e8_marks}")
    print(f"    (Σ marks = {sum(e8_marks)} = Coxeter number h = 30 of E₈)")
    print(f"  A₅ = I irreps (the SO(3) quotient, faithful-on-I) dims = [1,3,3,4,5]")
    print(f"    (Σ dim² = {sum(d*d for d in [1,3,3,4,5])} = |A₅| = 60)")
    print("  Note: the equivariant index over C²/2I (McKay/ALE resolution) yields")
    print("  the E₈ marks as PF weights; the W_λ above are the q-Plancherel weights")
    print("  of the H_n(q) blocks. Whether the WRT(S³/2I) index reproduces W_λ is")
    print("  the deep target (separate probe).")
    print("\nPREFLIGHT COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
