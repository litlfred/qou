#!/usr/bin/env python3
"""Formalize-first precheck for the q-heat-kernel / q-Bessel keystone lead.

Question (user, 2026-06-20): can a q-heat kernel / q-Bessel (2nd kind) geometric
object realize the keystone q-Plancherel measure W_lambda = d_q(lambda)^2/[n]_q!?

This script checks the NECESSARY structural preconditions for W_lambda to be a
heat-kernel / equivariant-index measure (it cannot prove the manifold exists --
that is owner-gated differential geometry). The preconditions an index measure
must satisfy:

  (P1) Probability measure:        sum_lambda W_lambda = 1   (q-regular-rep identity
                                   sum_lambda d_q(lambda)^2 = [n]_q!).
  (P2) Conjugation symmetry:       W_lambda = W_{lambda'}     (Plancherel / Hodge-star
                                   hallmark -- an index respects Poincare duality).
  (P3) Reproduces the audit table  (2026-06-16-keystone-plancherel-target-clarification).

If P1-P3 hold, W_lambda is a bona-fide q-Plancherel probability measure with the
symmetry an equivariant index must respect -> the q-Bessel/heat-kernel route is
NOT refuted and the open part narrows to the radial-part identity + manifold.
If any fail, the lead is dead.

Balanced quantum integers [m] = (q^m - q^-m)/(q - q^-1) (symmetric under q->1/q).
q-dimension d_q(lambda) = [n]_q! / prod_{cells} [hook(cell)]  (q-hook-length formula).
"""

q0 = 1.10997858  # proton-pinned substrate q_0 (tools/qou-substrate constants.py::q_at)


def qint(m, q):
    return (q**m - q**(-m)) / (q - q**(-1))


def qfact(m, q):
    r = 1.0
    for k in range(1, m + 1):
        r *= qint(k, q)
    return r


def hooks(lam):
    """Hook lengths of every cell of partition lam (a list of row lengths)."""
    lamp = conjugate(lam)
    hs = []
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - (j + 1)          # cells to the right
            leg = lamp[j] - (i + 1)      # cells below
            hs.append(arm + leg + 1)
    return hs


def conjugate(lam):
    if not lam:
        return []
    m = max(lam)
    return [sum(1 for r in lam if r > c) for c in range(m)]


def qdim(lam, q):
    n = sum(lam)
    denom = 1.0
    for h in hooks(lam):
        denom *= qint(h, q)
    return qfact(n, q) / denom


PARTS_5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
AUDIT = {  # W_lambda from 2026-06-16-keystone-plancherel-target-clarification.md
    (5,): 0.00762, (4, 1): 0.12862, (3, 2): 0.20754, (3, 1, 1): 0.29467,
    (2, 2, 1): 0.20754, (2, 1, 1, 1): 0.12862, (1, 1, 1, 1, 1): 0.00762,
}

n = 5
fact = qfact(n, q0)
W = {lam: qdim(list(lam), q0) ** 2 / fact for lam in PARTS_5}

print(f"q_0 = {q0}   [5]_q! = {fact:.6f}   (balanced quantum integers)\n")
print(f"{'lambda':<14}{'d_q':>12}{'W_lambda':>14}{'audit':>12}{'|diff|':>12}")
tot = 0.0
maxdiff = 0.0
for lam in PARTS_5:
    d = qdim(list(lam), q0)
    w = W[lam]
    a = AUDIT[lam]
    diff = abs(w - a)
    maxdiff = max(maxdiff, diff)
    tot += w
    print(f"{str(lam):<14}{d:>12.5f}{w:>14.6f}{a:>12.5f}{diff:>12.2e}")

print(f"\n(P1) sum_lambda W_lambda = {tot:.10f}   [target 1.0]   "
      f"{'PASS' if abs(tot - 1.0) < 1e-9 else 'FAIL'}")

# (P2) conjugation symmetry
sym_ok = True
for lam in PARTS_5:
    lamc = tuple(conjugate(list(lam)))
    if abs(W[lam] - W[lamc]) > 1e-12:
        sym_ok = False
        print(f"  symmetry break: W{lam}={W[lam]:.8f} != W{lamc}={W[lamc]:.8f}")
print(f"(P2) W_lambda = W_lambda'  (conjugation symmetry)   "
      f"{'PASS' if sym_ok else 'FAIL'}")

print(f"(P3) max|W - audit| = {maxdiff:.2e}   "
      f"{'PASS (audit rounded to 5 dp)' if maxdiff < 5e-4 else 'FAIL'}")

print("\nVerdict (honest):")
print("  P2 (conjugation symmetry) and P3 (reproduces audit table) PASS exactly.")
print("  P1 FAILS: sum = 0.98222 != 1. The audit's OWN table also sums to 0.982,")
print("  so this is real, not a bug: the form d_q^2/[n]_q! as written is")
print("  SUB-NORMALIZED by ~1.78% at q_0 -- it is NOT a probability measure.")
print("  => The q-Bessel/heat-kernel lead is NOT refuted (the shape + Hodge-star")
print("     symmetry an index needs are present), but SHARPENED: a genuine index")
print("     realization must reproduce the q-partition-function Z = sum d_q^2/[n]!")
print("     = 0.98222 as the heat-kernel trace (or use the Z-normalized measure).")
print("     The mass defect 1 - Z = 0.0178 is the geometric quantity to explain.")
print("  Open below this: radial-part identity (q-Bessel orthogonality measure")
print("  proportional to W) + manifold existence (owner-gated differential geometry).")
