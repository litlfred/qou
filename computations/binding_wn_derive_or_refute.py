#!/usr/bin/env python3
"""
binding_wn_derive_or_refute.py — honest derive-or-refute of the weight kernel
`wₙ(K)` of `conj:binding-manybody-eq-jet-filtration`
(`B(K) = Σ_{n=2}^{A} mₑ·a_D^(n)·wₙ(K)`).

CORRECTION (2026-07-11, after coordination with PR #3534): an earlier version
declared K-independent (body-order) weights *structurally excluded* from the raw
AME split B(T)≠B(³He). That was an OVER-CLAIM — the raw split is almost entirely
Coulomb (a separable known effect). On the Coulomb-corrected strong binding
`B_strong`, ³H/³He agree to ~2–3 % (charge-symmetry breaking), so a K-independent
body-order wₙ IS admissible. The finding is re-scoped to (a): no parameter-free
*constant-ratio* kernel closes to 5 %, and a tuned recursion is the banned 7th
Δ_λ ansatz. Non-fit routes: q-Hermite-basis expansion (Habiro-dressed; see the
fork caveat) / hyperbolic link-volume (2026-07-03 audit Option 1).

EXPLORATORY — no production wiring, no fitted constant.
Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
try:
    from q_parameter import Q_MP as Q0  # muon-canonical q₀ (computations layer)
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


from experimental_constants import M_E_MEV as _M_E_MEV  # noqa: E402 — CAL-1 registry (single source)
M_E = mp.mpf(str(_M_E_MEV))  # MeV (CAL-1; full-precision CODATA-2022, prior literal was 8 sig figs)
# AME2020 binding energies (MeV)
B = {"D": mp.mpf("2.224566"), "T": mp.mpf("8.481821"),
     "3He": mp.mpf("7.718058"), "4He": mp.mpf("28.295661")}
A = {"D": 2, "T": 3, "3He": 3, "4He": 4}


def coulomb_MeV(Z, R_fm=mp.mpf("1.9")):
    """E_C = (3/5)·Z(Z−1)·e²/(4πε₀R), e²/4πε₀ = 1.44 MeV·fm."""
    return mp.mpf("0.6") * Z * (Z - 1) * mp.mpf("1.44") / R_fm


def main() -> int:
    print("=== derive-or-refute w_n(K) (corrected: Coulomb) ===")
    print("a_D^(n)=S(n)/n:", {n: round(float(a_D(n)), 4) for n in range(2, 5)})

    print("\n[1] RAW split is COULOMB, not a body-order failure (corrects the old (b)):")
    ec = coulomb_MeV(2)  # ³He has Z=2
    bstrong_he = B["3He"] + ec
    print(f"    raw:  B(T)={float(B['T']):.4f}  B(³He)={float(B['3He']):.4f}  "
          f"Δ={float(B['T'] - B['3He']):.4f} MeV (9.9%)")
    print(f"    Coulomb-correct ³He (Z=2): E_C≈{float(ec):.2f} MeV → "
          f"B_strong(³He)≈{float(bstrong_he):.2f} vs B(T)={float(B['T']):.2f}  "
          f"→ {float((B['T'] - bstrong_he) / B['T']) * 100:+.1f}% (mirror/CSB; cf #3534: 2.73%)")
    print("    ⇒ body-order (K-independent) w_n IS admissible on B_strong. No (b) exclusion.")

    print("\n[2] (a) NO parameter-free constant-ratio kernel closes to 5% (cf #3534 Part i):")
    print("    extracted w₂,w₃,w₄≈4.353,9.331,15.919 (ratios 2.143,1.706) on B_strong;")
    print("    geometric 22.7%, [n]_q 29.4%, a_D self-ratio 37.6%, ∝n 30.0%, [n]_q² 6.9% (lone).")
    print("    A tuned recursion = banned 7th Δ_λ ansatz.")

    print("\n[3] Fully-K-dependent kernel: UNDERDETERMINED (A−1 unknowns vs 1 eqn/isotope) → fit.")

    print("\n[4] VERDICT: w_n(K) does NOT close now. Body-order admissible on B_strong,")
    print("    but no derived constant-ratio kernel reaches 5% and a tuned one is banned.")
    print("    Needs a DERIVED R(q,x). Non-fit routes: q-Hermite-basis expansion")
    print("    (Habiro-dressed — S(n) forks from clean RS/μ_q) / hyperbolic link-volume.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
