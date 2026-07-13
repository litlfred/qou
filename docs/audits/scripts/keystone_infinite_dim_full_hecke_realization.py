#!/usr/bin/env python3
"""The keystone's infinite-dim full-Hecke realization — three faces, and the Habiro
ring as the QOU-relevant one (connecting to the Q_β Habiro element).

After #2406 ruled out any finite colour-SU(3) arena (the production trace is the FULL
Hecke / Wenzl principal specialization, all rows), the geometric leg's target is an
INFINITE-dimensional object.  This is not exotic — the full-Hecke Markov trace has
well-known infinite-dim homes.  This script verifies the two load-bearing identities
and names the three faces.

VERIFIED:
  (1) the full-Hecke Markov weight = principal Schur specialization
        s_λ(1, q, q^2, ...) = q^{n(λ)} / ∏_{c∈λ} (1 - q^{h(c)})       (Stanley EC2 7.21.2)
      -- the canonical Markov trace weight (sibling #2389: production y_λ).
      Checked STABLY via the SSYT generating function (the bialternant det is
      numerically ill-conditioned; SSYT is exact).
  (2) McKay: the binary icosahedral 2I (the spacetime spin lift, #2364/keystone) has
      irrep dimensions = the marks of the AFFINE E8 Dynkin diagram; S^3/2I = the
      Poincaré homology sphere = link of the E8 surface singularity.

THREE FACES of the infinite-dim full-Hecke realization:
  - COLOUR (type A): the principal specialization = character of the gl_∞ / infinite-
    wedge basic representation (boson-fermion); operator-algebraically the Jones II_1
    subfactor (GNS from the unique Markov trace). Infinite-variable.
  - SPACETIME: 2I ↔ affine E8 (McKay) ↔ the affine-E8 basic representation.
  - ARITHMETIC/ANALYTIC: the HABIRO ring (cyclotomic completion of Z[q] at all roots
    of unity) -- where the full-Hecke trace CONVERGES at the substrate q0 -- which is
    the SAME ring as the corpus's Q_β Habiro element (α_EM [2]_q(1-h²α)). This is the
    QOU-relevant face: q0 is the evaluation point, and Habiro is the home.

NOT a closure: this identifies the infinite-dim arena (and unifies it with the Q_β
Habiro work), verifies the weight + McKay, but the spacetime⊥colour COUPLING (the
generation shift) remains the open keystone. No fit.
"""
import itertools
import sys


def hooks(lam):
    H = []
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - 1 - j
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            H.append(arm + leg + 1)
    return H


def n_lambda(lam):
    return sum(i * p for i, p in enumerate(lam))


def ssyt_genfun(lam, N, q):
    """s_λ(1,q,q²,...) via the SSYT generating function (entries 0..N); stable."""
    rows = len(lam)
    cells = [(i, j) for i in range(rows) for j in range(lam[i])]

    def semistandard(g):
        for i in range(rows):
            for j in range(lam[i] - 1):
                if g[(i, j)] > g[(i, j + 1)]:
                    return False
            for j in range(lam[i]):
                if i + 1 < rows and j < lam[i + 1] and not (g[(i, j)] < g[(i + 1, j)]):
                    return False
        return True

    total = 0.0
    for fill in itertools.product(range(N + 1), repeat=len(cells)):
        g = dict(zip(cells, fill))
        if semistandard(g):
            total += q ** sum(fill)
    return total


print("=" * 70)
print("(1) full-Hecke Markov weight = principal specialization (Stanley EC2 7.21.2)")
print("=" * 70)
q = 0.3
ok1 = True
for lam in [(2, 1), (3, 1, 1), (3, 2), (2, 2)]:
    closed = q ** n_lambda(lam)
    for h in hooks(lam):
        closed /= (1 - q ** h)
    ssyt = ssyt_genfun(lam, 16, q)
    match = abs(closed - ssyt) < 1e-6
    ok1 = ok1 and match
    print(f"  s_{str(lam):<10}(1,q,q²,…) = q^{n_lambda(lam)}/∏(1-q^h): closed={closed:.8f} "
          f"SSYT={ssyt:.8f} match={match}")

print()
print("=" * 70)
print("(2) McKay: 2I (spacetime spin lift) ↔ affine E8")
print("=" * 70)
twoI = [1, 2, 2, 3, 3, 4, 4, 5, 6]
E8_marks = [1, 2, 3, 4, 5, 6, 4, 2, 3]
ok2 = sorted(twoI) == sorted(E8_marks) and sum(d * d for d in twoI) == 120
print(f"  2I irrep dims {sorted(twoI)} == affine E8 marks {sorted(E8_marks)}: "
      f"{sorted(twoI) == sorted(E8_marks)}")
print(f"  Σ dim² = {sum(d*d for d in twoI)} = |2I| ; S³/2I = Poincaré sphere = E8 link")

print()
print("=" * 70)
print("THREE FACES (no closure; the coupling is the open keystone)")
print("=" * 70)
print("  colour (type A): principal spec = gl_∞ infinite-wedge / Jones II_1 subfactor")
print("  spacetime: 2I ↔ affine E8 (McKay) ↔ affine-E8 basic representation")
print("  arithmetic: the HABIRO ring (cyclotomic completion) — converges at q0,")
print("    SAME ring as the corpus Q_β Habiro element. <-- the QOU-relevant face.")
print("  The spacetime⊥colour coupling (generation shift) remains OPEN.")

assert ok1, "principal specialization closed form must match SSYT"
assert ok2, "McKay 2I = affine E8 must hold"
print("\nINFINITE-DIM REALIZATION ASSERTIONS VERIFIED (weight + McKay).")
sys.exit(0)
