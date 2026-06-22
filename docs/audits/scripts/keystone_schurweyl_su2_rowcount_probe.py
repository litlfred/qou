#!/usr/bin/env python3
"""
Pushing the SU(2)-coloured WRT through Schur–Weyl: the row-count selection rule,
and the spin/colour split of the lepton generations.

Follows the λ-colour / Schur–Weyl obstruction probe
(`2026-06-22-keystone-wrt-color-schurweyl.md`): the WRT colour index is
SU(2)-spin; W_λ is S_5-indexed; the bridge is Schur–Weyl duality. This probe
makes the bridge concrete via the one EXACT, parameter-free fact it carries:

    SCHUR–WEYL SELECTION RULE.  GL(2)/SU(2) Schur–Weyl duality on (ℂ²)^⊗n
    decomposes it as  ⊕_{λ : ≤2 rows} S^λ ⊗ V_λ^{SU(2)} —  ONLY partitions with
    AT MOST 2 ROWS appear (V_λ^{GL2} = 0 once λ has a 3rd row).  The 2-row block
    λ=(n−k,k) ↔ SU(2) spin j=(n−2k)/2 (Wilson-line colour 2j+1=n−2k+1).

So the SU(2)-coloured Poincaré-sphere (S³/2I) WRT can reach EXACTLY the ≤2-row
W_λ; a ≥3-row block is invisible to spin and requires ℂ³ colour (SU(3), 3 rows).

THE SHARP CONSEQUENCE (computed below, exact combinatorics — no fit):
  • muon home block (3,2)  : 2 rows  ⇒ SU(2)-REACHABLE (spin j=1/2)
  • electron home block (3,1,1): 3 rows ⇒ NOT SU(2)-reachable ⇒ needs SU(3) COLOUR
So the two lepton generations split across the spin/colour Schur–Weyl boundary —
the corpus's spacetime-spin-ℂ² ⊥ colour-ℂ³ split (#2364), now AT THE GENERATION
LEVEL: the Poincaré (spin) WRT gives the 2-row/muon sector; the electron block is
a genuinely colour (SU(3)) object.

DISCIPLINE: the row-count selection rule is EXACT representation theory (not a
fit). No SU(2)-component ↔ W_λ numerical match is asserted (that needs the level-k
S-matrix; forcing it would be numerology). W_λ values are the corpus q-Plancherel
weights, shown for context.
"""
from mpmath import mp, mpf, nstr

mp.dps = 30
Q0 = mpf("1.1099785955541805")
PARTS5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
ROLE = {(3, 1, 1): "electron", (3, 2): "muon", (2, 2, 1): "(3,2)-twin"}


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


def d_q(lam):
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h)
    return q_factorial(sum(lam)) / den


def main():
    print(f"q_0 = {Q0}  |  dps = {mp.dps}\n")
    print("Schur–Weyl SU(2) selection rule applied to λ ⊢ 5:")
    print(f"{'λ':<14}{'rows':>5}{'SU(2)?':>8}{'spin j':>8}{'min SU(N)':>10}{'W_λ':>12}{'role':>12}")
    nfac = q_factorial(5)
    reachable, needs_colour = [], []
    for lam in PARTS5:
        rows = len(lam)
        su2 = rows <= 2
        if su2:
            j = mpf(lam[0] - (lam[1] if len(lam) > 1 else 0)) / 2
            js = nstr(j, 4)
        else:
            js = "—"
        W = d_q(lam) ** 2 / nfac
        tag = ROLE.get(lam, "")
        print(f"{str(lam):<14}{rows:>5}{('yes' if su2 else 'NO'):>8}{js:>8}"
              f"{('SU('+str(rows)+')'):>10}{nstr(W,8):>12}{tag:>12}")
        (reachable if su2 else needs_colour).append(lam)
    print()
    print(f"SU(2)-reachable (≤2-row) blocks : {reachable}")
    print(f"   ↔ spins j = {{5/2, 3/2, 1/2}} (Wilson-line colours 6,4,2)")
    print(f"NEEDS colour SU(≥3) (≥3-row)    : {needs_colour}")
    print()
    print("Generation split across the spin/colour Schur–Weyl boundary:")
    print(f"  • muon     (3,2)   : 2 rows ⇒ SU(2)-REACHABLE (spin 1/2) — in the Poincaré (spin) WRT sector")
    print(f"  • electron (3,1,1) : 3 rows ⇒ NOT spin-reachable ⇒ requires ℂ³ colour (SU(3))")
    print()
    print("Conclusion (exact rep theory, no fit):")
    print("  The SU(2)-coloured WRT(S³/2I) reaches the ≤2-row (spin) sector of W_λ,")
    print("  which INCLUDES the muon block (3,2) but EXCLUDES the electron block (3,1,1).")
    print("  The electron is a genuinely COLOUR (SU(3)) object — so the keystone factors:")
    print("  spin sector ← Poincaré-sphere WRT;  colour/≥3-row sector ← SU(3) Schur–Weyl.")
    print("  This realises the corpus spin-ℂ² ⊥ colour-ℂ³ split (#2364) at the GENERATION level.")
    print("\nSCHUR–WEYL ROW-COUNT PROBE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
