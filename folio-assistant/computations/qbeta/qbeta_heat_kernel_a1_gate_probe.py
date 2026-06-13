#!/usr/bin/env python3
# polynomial_q_not_applicable: structural gate probe (numerical readout).
"""Q_β heat-route candidate — the bar-odd a_1 gate (formalize-first prune).

Tests the ONE gate that matters for the §3-bis q-heat-kernel candidate for the
open c_k-recursion kernel R(q,ξ): does the natural heat-kernel leading
coefficient

    a_1  ~  e_1{ (q-1)·μ_λ : λ active }          (the t-coefficient of the
                                                  per-mode kernel A_λ(t) =
                                                  1 - (q-1)·μ_λ·t)

satisfy (i) bar-ODD  a_1(q⁻¹) = -a_1(q)  and (ii) |a_1(q_0)| ≈ √2·Φ₂ ≈ 2.07
(targets: 2.0693 proton-anchor, 2.0202 muon-anchor)?

μ_λ(q) = ℏ_q² · Σ_□ [c(□)]_q [c(□)+1]_q ,  ℏ_q = (q-1)/q ,
[k]_q = (1-q^k)/(1-q)  (Jackson)   — prop:q-heat-kernel-peter-weyl.

This is a STRUCTURAL gate test, NOT a c_3-value derivation: a pass is a
positive signal for the candidate family (kernel R still open / assembly
f-map unspecified); a fail PRUNES the natural heat-kernel a_1. No production
wiring, no c_3 claim. Per the flip-flop guard + docs/audits/
2026-06-10-qbeta-ck-state-of-play-synthesis.md §3-bis.
"""
from __future__ import annotations
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))  # computations/ — for _path_bridge, q_parameter
import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

mp.mp.dps = 40

from q_parameter import Q as Q0_STR  # noqa: E402
q0 = mp.mpf(str(Q0_STR))

A1_TARGET_P = mp.sqrt(2) * mp.mpf("1.46324616887618")   # 2.0693 (proton anchor)
A1_TARGET_MU = mp.sqrt(2) * mp.mpf("1.42849728553818")  # 2.0202 (muon anchor)


def jackson(k: int, q):
    """[k]_q = (1 - q^k)/(1 - q) = 1 + q + ... + q^{k-1}; [0]=0."""
    if k == 0:
        return mp.mpf(0)
    return (1 - q ** k) / (1 - q)


def partitions(n: int):
    if n == 0:
        yield ()
        return
    def rec(rem, mx):
        if rem == 0:
            yield ()
            return
        for first in range(min(rem, mx), 0, -1):
            for rest in rec(rem - first, first):
                yield (first,) + rest
    yield from rec(n, n)


def contents(part):
    """cell contents c = j - i (0-indexed row i, col j)."""
    return [j - i for i, row in enumerate(part) for j in range(row)]


def mu_lambda(part, q):
    """μ_λ(q) = ℏ_q² Σ_□ [c]_q [c+1]_q,  ℏ_q = (q-1)/q."""
    hbar2 = ((q - 1) / q) ** 2
    s = mp.mpf(0)
    for c in contents(part):
        s += jackson(c, q) * jackson(c + 1, q)
    return hbar2 * s


def hook_dim(part):
    """Classical dim S^λ (hook length formula) — q→1 Steinberg dim, used as the
    d_λ weight baseline."""
    n = sum(part)
    conj = [sum(1 for r in part if r > j) for j in range(part[0])] if part else []
    import math
    hooks = 1
    for i, row in enumerate(part):
        for j in range(row):
            hooks *= (part[i] - j) + (conj[j] - i) - 1
    return math.factorial(n) // hooks


def bar_ratio(fn):
    """fn(q0⁻¹)/fn(q0): −1 ⇒ bar-ODD, +1 ⇒ bar-EVEN."""
    a = fn(q0)
    b = fn(1 / q0)
    return b / a if a != 0 else mp.nan, a, b


def main() -> int:
    print("=" * 78)
    print("  Q_β heat-route a_1 gate — bar-parity + magnitude of (q-1)·μ_λ")
    print(f"  q_0 = {mp.nstr(q0, 12)}   targets |a_1| ≈ 2.0693 (p) / 2.0202 (μ)")
    print("=" * 78)
    for n in (2, 3, 4, 6):
        print(f"\n── H_{n}  (n strands) ──")
        modes = []
        for part in partitions(n):
            mu = mu_lambda(part, q0)
            km = (q0 - 1) * mu                      # t-coefficient of A_λ
            d = hook_dim(part)
            r_mu, _, _ = bar_ratio(lambda q, p=part: (q - 1) * mu_lambda(p, q))
            modes.append((part, mu, km, d, r_mu))
            tag = " (μ=0 equilibrium)" if abs(mu) < mp.mpf("1e-30") else ""
            print(f"   λ={str(part):14s} d_λ={d:3d}  μ_λ={mp.nstr(mu,6):>11}  "
                  f"(q-1)μ_λ={mp.nstr(km,6):>11}  bar(q⁻¹)/q={mp.nstr(r_mu,5):>9}{tag}")
        # candidate a_1 forms over NON-trivial modes
        nz = [m for m in modes if abs(m[1]) > mp.mpf("1e-30")]
        def e1_unw(q): return sum((q - 1) * mu_lambda(p, q) for (p, *_ ) in nz)
        def e1_dw(q):  return sum(d * (q - 1) * mu_lambda(p, q) for (p, _, _, d, _) in nz)
        for name, fn in (("Σ(q-1)μ_λ", e1_unw), ("Σ d_λ(q-1)μ_λ", e1_dw)):
            r, a, b = bar_ratio(fn)
            par = "ODD" if abs(r + 1) < mp.mpf("1e-6") else ("EVEN" if abs(r - 1) < mp.mpf("1e-6") else "neither")
            print(f"     a_1 cand [{name:16s}] = {mp.nstr(a,8):>12}  bar-ratio={mp.nstr(r,6):>10} [{par}]"
                  f"   |a_1|/2.069={mp.nstr(abs(a)/A1_TARGET_P,5)}")
    # ── q-dilog / log-sum route (the q-hyperbolic thread): the Peter–Weyl
    #    doc states the q-dilog generates Σ_λ log μ_λ. Test its bar-parity +
    #    magnitude as an alternative a_1 source. ──────────────────────────
    print("\n── q-dilog route: Σ_λ log μ_λ (+ d_λ-weighted) over non-trivial modes ──")
    for n in (2, 3, 4, 6):
        nz = [p for p in partitions(n) if abs(mu_lambda(p, q0)) > mp.mpf("1e-30")]
        def logsum(q): return sum(mp.log(mu_lambda(p, q)) for p in nz)
        def logsum_dw(q): return sum(hook_dim(p) * mp.log(mu_lambda(p, q)) for p in nz)
        for nm, fn in (("Σ log μ_λ", logsum), ("Σ d_λ log μ_λ", logsum_dw)):
            r, a, b = bar_ratio(fn)
            par = "ODD" if abs(r + 1) < mp.mpf("1e-6") else ("EVEN" if abs(r - 1) < mp.mpf("1e-6") else "neither")
            print(f"   H_{n}  [{nm:14s}] = {mp.nstr(a,8):>13}  bar-ratio={mp.nstr(r,6):>10} [{par}]"
                  f"   |·|/2.069={mp.nstr(abs(a)/A1_TARGET_P,5)}")

    print("\n  GATE: need bar-ratio = -1 (ODD) AND |a_1| ≈ 2.069.")
    print("  Reading: (q-1)μ_λ exactly ODD only for (2),(2,1) [c=1-dominated];")
    print("  magnitude off ~1.3x-900x at raw level (change-of-basis open).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
