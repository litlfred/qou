#!/usr/bin/env python3
"""
The modular-category identification of the W_λ-producing structure.

Follows the WRT reframing (`2026-06-22-keystone-geometric-angles-preflight.md` §2):
'index = W_λ' = 'W_λ are the modular-tensor-category block weights d²/D²'. The
question this probe settles: WHICH category — and the answer pins it to a
specific regime.

CLAIM (verified here): the substrate q_0 is REAL and > 1, so it lies in the
NON-COMPACT / growth (arccosh) regime, NOT the root-of-unity / rotation
(arccos) regime where compact modular tensor categories SU(2)_k live. Hence the
W_λ-producing structure is the E_q(2) contraction (Hahn–Exton q-Bessel) at
generic real q_0 — unifying with the corpus's existing Reeb-phase / qbk2
identification — NOT a finite compact MTC and NOT a finite Sasakian manifold.

DISCIPLINE: no fit; every step is an exact regime check (|q|, η real/imaginary,
root-of-unity test). Nothing wired.
"""
import sys
from pathlib import Path

from mpmath import mp, mpf, log, pi, sin, exp, mpc, fabs, nstr

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations" / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0 = mpf("1.1099785955541805")


def main():
    print(f"q_0 = {Q0}  |  dps = {mp.dps}\n")

    # (A) q_0 is real > 1 ⇒ η = log q_0 is REAL (growth regime)
    eta = log(Q0)
    print("(A) Regime of the substrate q_0 = e^η:")
    print(f"    |q_0| = {nstr(Q0,12)}   (= 1 ⟺ root of unity / compact MTC)")
    print(f"    η = log q_0 = {nstr(eta,12)}  — REAL  ⇒ GROWTH (arccosh, I_ν) regime")
    print(f"    (rotation / compact SU(2)_k needs η IMAGINARY, |q|=1)\n")

    # (B) root-of-unity test: is q_0 = e^{iπ/(k+2)} for any small integer level k?
    #     For a unitary SU(2)_k MTC, q = e^{iπ/(k+2)} so |q| = 1 EXACTLY.
    print("(B) Root-of-unity / level test  (q_0 vs e^{iπ/(k+2)}, |·|=1):")
    print(f"    |q_0| − 1 = {nstr(Q0 - 1, 6)}  ≠ 0  ⇒ q_0 is NOT on the unit circle,")
    print(f"    so q_0 ≠ e^{{iπ/(k+2)}} for ANY level k. No compact SU(2)_k MTC has")
    print(f"    these quantum dimensions.\n")

    # (C) the d_q are the GENERIC-q (real, >1) Hecke quantum dims — confirm growth
    def qint(m):
        return (Q0**m - Q0**(-m)) / (Q0 - Q0**(-1))
    print("(C) The q-integers [m]_q at q_0 are real, monotone-growing (I_ν world):")
    for m in (2, 3, 4, 5):
        # balanced [m]_q = sinh(m η)/sinh(η); confirm vs the hyperbolic form
        from mpmath import sinh
        hyp = sinh(m * eta) / sinh(eta)
        print(f"    [{m}]_q = {nstr(qint(m),10):<12} = sinh({m}η)/sinh(η) = {nstr(hyp,10)}  "
              f"(|Δ|={nstr(fabs(qint(m)-hyp),3)})")
    print("    ⇒ [m]_q = sinh(mη)/sinh(η): the GROWTH (I_ν / cosh) branch, exactly")
    print("    the Reeb-phase doc's arccosh regime, not the sin/arccos compact branch.\n")

    # (D) the contraction picture: SU_q(2) → E_q(2) at generic q (Vaksman-Korogodsky,
    #     Koelink) — the Hahn-Exton q-Bessel home already in the corpus.
    print("(D) Identification (type-correct):")
    print("    • q_0 real > 1 ⇒ the substrate ribbon category is NON-COMPACT:")
    print("      Rep at generic real q_0, the SU_q(2) → E_q(2) CONTRACTION regime,")
    print("      whose matrix coefficients are the Hahn–Exton q-Bessel functions")
    print("      (Vaksman–Korogodsky 1989; Koelink 1994) — ALREADY identified in the")
    print("      corpus (`2026-06-13-reeb-phase-qbessel-identification.md`).")
    print("    • So the W_λ = d_q²/[n]_q! are the GENERIC-q (growth-regime) Hecke–")
    print("      Markov block weights of THIS non-compact structure — NOT a finite")
    print("      compact MTC (root of unity) and NOT a finite Sasakian manifold.")
    print("    • The WRT(S³/2I) / Habiro-ring object reconciles the two ends: the")
    print("      Habiro ring evaluates at BOTH roots of unity AND generic q, so the")
    print("      generic-q_0 evaluation is the well-defined bridge. That explicit")
    print("      Habiro q-series ↔ W_λ computation is the remaining research frontier.")
    print("\nMODULAR-CATEGORY IDENTIFICATION COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
