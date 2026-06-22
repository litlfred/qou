#!/usr/bin/env python3
"""
Spin-sector realisation attempt: the two sides of Schur–Weyl, and why W_λ is the
Hecke side while the WRT/Poincaré modular data is the SU(2) side.

Follows the row-count push (`2026-06-22-keystone-schurweyl-su2-rowcount.md`): the
2-row blocks {(5),(4,1),(3,2)} are SU(2)-reachable. The natural next step is "does
the SU(2)/WRT modular weight of the 2-row block reproduce W_λ?". This probe
computes BOTH sides of Schur–Weyl and answers it — sharply, and somewhat
deflationarily.

THE TWO SIDES OF SCHUR–WEYL  (ℂ²)^{⊗n} = ⊕_{λ:≤2row} S^λ ⊗ V_λ:
  • S^λ  — the S_n (Hecke) irrep.  Its q-dimension is the HOOK-CONTENT
           d_q^{Hecke}(λ) = [n]_q!/Π[hook]_q.  The corpus W_λ = d_q²/[n]_q! lives HERE.
  • V_λ  — the SU(2) irrep, spin j=(λ₁−λ₂)/2.  Its quantum dimension is the
           CHEBYSHEV/TL value [2j+1]_q.  The WRT(S³/2I) modular data lives HERE.

These are DUAL but DIFFERENT numbers.  This probe tabulates both for n=5 2-row
blocks and shows d_q^{Hecke}(λ) ≠ [2j+1]_q^{SU(2)} in general — so a direct
"WRT modular weight = W_λ" equality is a category error: the WRT (SU(2)/centralizer)
side and the W_λ (Hecke/S_n) side are Schur–Weyl DUAL, not equal.

DISCIPLINE: exact q-integer arithmetic; no fit; the finding is a (deflationary)
structural clarification, not a closure.
"""
from mpmath import mp, mpf, nstr

mp.dps = 30
Q0 = mpf("1.1099785955541805")


def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def q_factorial(m):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= qint(k)
    return r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def d_q_hecke(lam):
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h)
    return q_factorial(sum(lam)) / den


def f_lambda(lam):
    """ordinary S_n irrep dimension via hook-length formula."""
    from math import factorial, prod
    return factorial(sum(lam)) // prod(hooks(lam))


def main():
    print(f"q_0 = {Q0}  |  dps = {mp.dps}\n")
    two_row = [(5,), (4, 1), (3, 2)]   # the SU(2)-reachable blocks of n=5
    nfac = q_factorial(5)
    print("The two Schur–Weyl sides for the SU(2)-reachable (≤2-row) blocks of n=5:\n")
    print(f"{'λ':<8}{'spin j':>7}{'Hecke d_q (S_n side)':>22}{'SU(2) [2j+1]_q':>16}{'equal?':>8}{'f^λ':>6}{'W_λ':>11}")
    for lam in two_row:
        k = lam[1] if len(lam) > 1 else 0
        j = mpf(lam[0] - k) / 2
        dq = d_q_hecke(lam)
        su2 = qint(int(2 * j + 1))     # [2j+1]_q
        W = dq * dq / nfac
        eq = "yes" if abs(dq - su2) < mpf("1e-20") else "NO"
        role = " (muon)" if lam == (3, 2) else ""
        print(f"{str(lam):<8}{nstr(j,3):>7}{nstr(dq,12):>22}{nstr(su2,12):>16}{eq:>8}"
              f"{f_lambda(lam):>6}{nstr(W,8):>11}{role}")
    print()
    print("Reading the table:")
    print("  • d_q^{Hecke}(λ) (S_n side, the W_λ numerator) and [2j+1]_q (SU(2) side, the WRT")
    print("    modular dimension) are DIFFERENT for (5) and (3,2); they coincide only for (4,1).")
    print("    e.g. (3,2): d_q^{Hecke}=[5]_q≈5.22 (muon) vs SU(2) spin-1/2 dim [2]_q≈2.01.")
    print("  • So W_λ is built from the HECKE / S_n side of Schur–Weyl, while the WRT(S³/2I)")
    print("    modular data is the SU(2) / centralizer side. They are Schur–Weyl DUAL —")
    print("    PAIRED (V^⊗n = ⊕ S^λ⊗V_λ) but NOT EQUAL.")
    print()
    print("Honest (deflationary) verdict:")
    print("  A direct 'WRT(S³/2I) modular weight = W_λ' equality is a CATEGORY ERROR: the WRT")
    print("  lives on the SU(2) (V_λ) side; W_λ lives on the Hecke (S^λ) side. The WRT data")
    print("  CONSTRAINS W_λ only through the duality pairing (matched dimensions), not by")
    print("  equality. So the Poincaré-sphere invariant is the icosahedral SELECTOR of the")
    print("  modular data (confirmed: E₈ residues), but the W_λ numbers are the DUAL S_n-side")
    print("  q-dimensions — the keystone link is Schur–Weyl DUALITY, full stop, and there is")
    print("  no closer 'WRT = W_λ' identity to be had at the level of weights.")
    print("\nSCHUR–WEYL DUAL-SIDES PROBE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
