#!/usr/bin/env python3
"""
binding_wn_derive_or_refute.py — honest derive-or-refute of the weight kernel
`wₙ(K)` of `conj:binding-manybody-eq-jet-filtration`
(`B(K) = Σ_{n=2}^{A} mₑ·a_D^(n)·wₙ(K)`).

Two findings, no fit (AGENTS.md refuted-claim + Δ_λ "no seventh ansatz"
discipline):

  [1] scope-(b) STRUCTURAL EXCLUSION of K-independent (pure body-order) weights:
      T and ³He share identical body-order structure (both A=3) but differ in
      binding — a K-independent wₙ forces B(T)=B(³He). Invariant: binding is not
      a function of A alone (isospin/Coulomb split). ⇒ wₙ(K) must be K-dependent.

  [2] scope-(a) UNDERDETERMINATION of the K-dependent class: A−1 unknowns vs 1
      equation per isotope. Inverting the anchors = per-isotope fit = forbidden.

Verdict: wₙ(K) does not close now; closure needs a DERIVED q-difference kernel
R(q,x) (owner-gated). Non-fit route = hyperbolic link-volume (2026-07-03 audit,
Option 1). EXPLORATORY — no production wiring, no fitted constant.

Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

mp.mp.dps = 50
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
try:
    from q_parameter import Q as Q0  # muon-canonical q₀ (computations layer)
    q = mp.mpf(str(Q0))
except Exception:
    q = mp.mpf("1.10997859555733471")


def qint(k):
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p


def partitions(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1
            for i in range(len(lam)) for j in range(lam[i])]


def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d


def a_D(n):
    """na-Stokes SW jet period = mean quantum dimension lw(n−1) = S(n)/n."""
    return mp.fsum(dimq(l) for l in partitions(n)) / n


M_E = mp.mpf("0.51099895")  # MeV (CAL-1)
# AME2020 binding energies (MeV)
B = {"D": mp.mpf("2.224566"), "T": mp.mpf("8.481821"),
     "3He": mp.mpf("7.718058"), "4He": mp.mpf("28.295661")}
A = {"D": 2, "T": 3, "3He": 3, "4He": 4}


def main() -> int:
    print("=== derive-or-refute w_n(K) ===")
    print("a_D^(n)=S(n)/n:", {n: round(float(a_D(n)), 4) for n in range(2, 5)})

    print("\n[1] (b) K-INDEPENDENT (body-order) weights EXCLUDED — B(T)≠B(³He) at A=3:")
    w2 = B["D"] / (M_E * a_D(2))
    w3_T = (B["T"] / M_E - a_D(2) * w2) / a_D(3)
    w3_He = (B["3He"] / M_E - a_D(2) * w2) / a_D(3)
    print(f"    B(T)={float(B['T']):.4f}  B(³He)={float(B['3He']):.4f}  "
          f"Δ={float(B['T'] - B['3He']):.4f} MeV "
          f"({float((B['T'] - B['3He']) / B['3He']) * 100:.1f}%)")
    print(f"    w₂(D)={float(w2):.4f}   w₃|T={float(w3_T):.4f}   w₃|³He={float(w3_He):.4f}  "
          f"→ disagree {float((w3_T - w3_He) / w3_He) * 100:.1f}%")
    print("    invariant: binding ≠ f(A) ⇒ w_n(K) MUST be K-dependent.")

    print("\n[2] (a) K-DEPENDENT class UNDERDETERMINED (A−1 unknowns vs 1 eqn/isotope):")
    for K in ["D", "T", "3He", "4He"]:
        nunk = A[K] - 1
        tag = "determined" if nunk == 1 else f"{nunk - 1} free DOF (FIT)"
        print(f"    {K:<4} A={A[K]}: {nunk} unknown(s) w₂..w_{A[K]} vs 1 eqn → {tag}")

    print("\n[3] VERDICT: w_n(K) does NOT close now (no fit-free closure).")
    print("    Needs a DERIVED R(q,x) (owner-gated). Non-fit route: hyperbolic")
    print("    link-volume of the n-body sub-cluster (2026-07-03 audit, Option 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
