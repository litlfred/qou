#!/usr/bin/env python3
"""
WRT / Lawrence–Zagier path: is W_λ the modular-tensor-category block weight?

The corpus redirect (`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`,
SUPERSEDED banner #2406) points the equivariant-index = W_λ object at the
WRT TQFT of the Poincaré sphere S³/2I (Lawrence–Zagier), a q-deformed
(Habiro-ring) invariant — NOT a classical finite Sasakian index.

This probe makes the WRT reframing precise and quantifies the one gap.

STRUCTURAL IDENTITY (the reframing): in a modular tensor category the natural
weight of block λ is

    P_λ = d_λ² / D²,   D² = Σ_μ d_μ²   (the global / total quantum dimension),

which is the SAME FORM as the corpus target W_λ = d_q(λ)²/[n]_q!.  So
"index = W_λ" is, categorically, "[n]_q! is the global quantum dimension D² of
the relevant TQFT block system."  This probe tests that identification directly:
does D² = Σ_λ d_q(λ)² equal [n]_q!?

The Poincaré sphere S³/2I = Seifert (2,3,5) fibration; its WRT invariant
(Lawrence–Zagier 1999) is the Eichler integral of a weight-3/2 theta function
whose data is the E₈ / icosahedral lattice — the icosahedral SELECTOR. We do
not recompute that q-series here (it is a single number per level, not the
λ-family); we record it as the geometric selector and test the categorical
normalisation that any WRT identification must satisfy.

DISCIPLINE: no fit; report the exact normalisation gap; do not claim a
"WRT(S³/2I) = W_λ" identity that is not type-correct (number vs family).
"""
import sys
from pathlib import Path

from mpmath import mp, mpf, nstr

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations" / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0 = mpf("1.1099785955541805")


def qint(m):
    return (Q0**m - Q0**(-m)) / (Q0 - Q0**(-1))


def q_factorial(m):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= qint(k)
    return r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    out = []
    for i, row in enumerate(lam):
        for j in range(row):
            out.append((row - j - 1) + (conj[j] - i - 1) + 1)
    return out


def d_q(lam):
    num = q_factorial(sum(lam))
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h)
    return num / den


PARTS = {
    3: [(3,), (2, 1), (1, 1, 1)],
    5: [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)],
}


def main():
    print(f"q_0 = {Q0}  |  dps = {mp.dps}\n")
    print("Testing the WRT/modular reframing: D² = Σ_λ d_q(λ)²  vs  [n]_q!")
    print("(equal ⟹ W_λ = d_q²/[n]! IS the modular block weight d²/D² exactly)\n")
    for n in (3, 5):
        D2 = mpf(0)
        for lam in PARTS[n]:
            D2 += d_q(lam) ** 2
        nfac = q_factorial(n)
        ratio = D2 / nfac
        print(f"  n={n}:  D² = Σ d_q² = {nstr(D2,12)}   [n]_q! = {nstr(nfac,12)}")
        print(f"         D²/[n]_q! = {nstr(ratio,12)}   (gap = {nstr(abs(1-ratio),6)})")
        # modular-normalised weights vs corpus W_λ
        print(f"         block weights  P_λ=d²/D² (Σ=1)   vs   W_λ=d²/[n]! (corpus):")
        for lam in PARTS[n]:
            dq = d_q(lam)
            P = dq * dq / D2
            W = dq * dq / nfac
            print(f"           {str(lam):<14} P_λ={nstr(P,8):<12} W_λ={nstr(W,8)}")
        print()

    print("Reading the result:")
    print("  • The two weights differ ONLY by the overall factor D²/[n]_q! ≠ 1.")
    print("  • So the corpus W_λ = d_q²/[n]_q! is the modular weight d²/D² UP TO a")
    print("    fixed normalisation D²/[n]_q!; it is NOT a probability measure")
    print("    (Σ W_λ ≠ 1) because Σ d_q² ≠ [n]_q! at q≠1 (the q-dim is the Markov")
    print("    trace of 1, not the irrep dimension f^λ, and Σ (f^λ)² = n! is the")
    print("    identity that q-deforms to Σ d_q² = D² ≠ [n]_q!).")
    print()
    print("Honest WRT verdict (type-correct):")
    print("  • 'index = W_λ' reframes to: W_λ ARE the modular-tensor-category block")
    print("    weights of the SU(2)-type TQFT, up to the fixed factor D²/[n]_q!.")
    print("  • The Poincaré sphere S³/2I (Seifert (2,3,5), E₈ lattice; Lawrence–Zagier)")
    print("    is the GEOMETRIC SELECTOR of the icosahedral modular data — but its WRT")
    print("    invariant is one q-series per level, not the λ-family W_λ, so 'WRT(S³/2I)")
    print("    = W_λ' is a TYPE MISMATCH and is NOT claimed.")
    print("  • The genuine open content: pin the level/category whose quantum dims are")
    print("    the d_q(λ) above and whose global dim D² supplies the normalisation —")
    print("    THEN W_λ is its block measure. This is representation-theoretic (modular")
    print("    data), not finite-Sasakian geometry: the q-deformed home the corpus")
    print("    redirect named, now made precise.")
    print("\nWRT PROBE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
