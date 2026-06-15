#!/usr/bin/env python3
"""
meson_h6_typed_trace.py — compute m_K/m_π via FULL H₆ Markov trace
of the meson pair braid with per-flavor typed crossings.

STRUCTURE:
  Meson = qq̄ = 2 quarks × 3 strands = 6 strands → H₆(q)

  Pion π⁺ = ud̄:
    Quark 1 (u): gens 0,1 — torus knot T(2,3) → σ^3 per gen
    Inter-quark: gen 2 — Hopf link → single σ crossing
    Quark 2 (d̄): gens 3,4 — torus knot T(2,3) → σ^3 per gen

  Kaon K⁺ = us̄:
    Quark 1 (u): gens 0,1 — T(2,3) → σ^3 per gen (same as pion)
    Inter-quark: gen 2 — Hopf link (same)
    Quark 2 (s̄): gens 3,4 — T(2,5) → σ^5 per gen (different!)

The ONLY difference: quark 2 has 5 crossings (strange) vs 3 (down).
The H₆ Wedderburn sum distinguishes these via the 11 partitions of 6.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from hecke_characters import build_seminormal_matrices  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
    Q0 = float(Q_50_DIGIT_STR[:20])
except Exception:
    Q0 = 1.10997858275138


def partitions_of(n):
    """Generate all partitions of n."""
    if n == 0:
        yield ()
        return
    def _gen(n, max_val):
        if n == 0:
            yield []
            return
        for i in range(min(n, max_val), 0, -1):
            for rest in _gen(n - i, i):
                yield [i] + rest
    for p in _gen(n, n):
        yield tuple(p)


def dim_q(shape, q=Q0):
    """Quantum dimension of irrep λ at q."""
    n = sum(shape)
    h = q - 1.0 / q
    num = 1.0
    den = 1.0
    for i, li in enumerate(shape):
        for j in range(li):
            hook = li - j - 1
            for i2 in range(i + 1, len(shape)):
                if j < shape[i2]:
                    hook += 1
            content = j - i
            num_factor = q ** (n - 1 - content) - q ** (-(n - 1 - content))
            den_factor = q ** hook - q ** (-hook)
            if abs(den_factor) > 1e-15:
                num *= num_factor
                den *= den_factor
    return num / den if abs(den) > 1e-15 else 0.0


def qfac(n, q=Q0):
    """[n]_q! = [1]_q × [2]_q × ... × [n]_q."""
    h = q - 1.0 / q
    result = 1.0
    for k in range(1, n + 1):
        qk = (q ** k - q ** (-k)) / h
        result *= qk
    return result


def meson_braid_word(n_quark1: int, n_quark2: int, n_hopf: int = 1):
    """Build meson braid word in (c, d, gen) format for H₆.

    n_quark1: crossings per generator for quark 1 (u-quark = 3)
    n_quark2: crossings per generator for quark 2 (d̄=3, s̄=5)
    n_hopf: Hopf link crossings on the inter-quark generator
    """
    word = []
    # Quark 1 on generators 0, 1
    for _ in range(n_quark1):
        word.append((1.0, 0.0, 0))
    for _ in range(n_quark1):
        word.append((1.0, 0.0, 1))
    # Inter-quark Hopf on generator 2
    for _ in range(n_hopf):
        word.append((1.0, 0.0, 2))
    # Quark 2 on generators 3, 4
    for _ in range(n_quark2):
        word.append((1.0, 0.0, 3))
    for _ in range(n_quark2):
        word.append((1.0, 0.0, 4))
    return word


def h6_markov_trace(word, q=Q0, verbose=False):
    """Compute the full H₆ Wedderburn-weighted Markov trace of a braid word."""
    n_strands = 6
    n_gens = 5
    nfac = qfac(n_strands, q)

    word_by_gen = [[] for _ in range(n_gens)]
    for (c, d, g) in word:
        if 0 <= g < n_gens:
            word_by_gen[g].append((c, d))

    total_trace = 0.0
    for shape in partitions_of(n_strands):
        dq = dim_q(shape, q)
        w_lam = (dq * dq) / nfac
        if abs(w_lam) < 1e-20:
            continue

        sigmas, dim, _syts = build_seminormal_matrices(shape, q=q)
        if dim == 0:
            continue

        I_lam = np.eye(dim)
        gen_traces = []
        for i in range(n_gens):
            steps = word_by_gen[i]
            if not steps:
                gen_traces.append(dim)  # identity → trace = dim
                continue
            M = I_lam.copy()
            for (c, d) in steps:
                M = M @ (c * sigmas[i] + d * I_lam)
            gen_traces.append(float(np.trace(M)))

        # Full braid character = product of per-gen traces... NO!
        # The character of a PRODUCT of elements is NOT the product of characters.
        # We need the JOINT character: tr(W₀ · W₁ · W₂ · W₃ · W₄)
        # where W_i is the accumulated element at generator i.

        # CORRECT: compute the product matrix across ALL generators
        M_total = I_lam.copy()
        for i in range(n_gens):
            steps = word_by_gen[i]
            for (c, d) in steps:
                M_total = M_total @ (c * sigmas[i] + d * I_lam)
        chi = float(np.trace(M_total))
        total_trace += w_lam * chi / dim

        if verbose:
            print(f"  λ={shape}: dim={dim}, w={w_lam:.6f}, χ={chi:.6f}")

    return total_trace


def main():
    t0 = time.monotonic()
    wb = WitnessBuilder("meson-h6-typed-trace", engine="numpy/f64")

    q = Q0
    print("=" * 70)
    print(f"MESON H₆ TYPED TRACE: m_K/m_π from full Wedderburn sum")
    print(f"q₀ = {q:.10f}")
    print("=" * 70)
    print()

    # Build pion and kaon braid words
    pion_word = meson_braid_word(n_quark1=3, n_quark2=3, n_hopf=1)
    kaon_word = meson_braid_word(n_quark1=3, n_quark2=5, n_hopf=1)

    print(f"Pion π⁺ (ud̄): {len(pion_word)} crossings (3+3+1+3+3)")
    print(f"Kaon K⁺ (us̄): {len(kaon_word)} crossings (3+3+1+5+5)")
    print()

    # Compute H₆ traces
    print("Computing H₆ Markov trace for pion...")
    tr_pion = h6_markov_trace(pion_word, q, verbose=True)
    print(f"  tr_M(π) = {tr_pion:.10f}")
    print()

    print("Computing H₆ Markov trace for kaon...")
    tr_kaon = h6_markov_trace(kaon_word, q, verbose=True)
    print(f"  tr_M(K) = {tr_kaon:.10f}")
    print()

    # Ratio
    ratio = abs(tr_kaon) / abs(tr_pion) if abs(tr_pion) > 1e-20 else float('inf')
    seifert_sq = (9.0 / 5.0) ** 2

    # Target
    target = 493.677 / 139.57039  # PDG m_K/m_π

    # Test various formulas
    pred_raw = ratio
    pred_seifert = ratio * seifert_sq
    pred_seifert1 = ratio * (9.0 / 5.0)

    print(f"=== RESULTS ===")
    print(f"  |tr_K/tr_π| = {ratio:.10f}")
    print(f"  × (9/5)¹ = {pred_seifert1:.10f}")
    print(f"  × (9/5)² = {pred_seifert:.10f}")
    print(f"  target    = {target:.10f}")
    print()
    for label, pred in [("raw", pred_raw), ("×(9/5)", pred_seifert1),
                         ("×(9/5)²", pred_seifert)]:
        err = abs(pred - target) / target * 1e6
        print(f"  {label:10s}: {pred:.10f}  err = {err:.0f} ppm")

    elapsed = time.monotonic() - t0

    wb.set_description(
        f"Full H₆ Wedderburn Markov trace for meson pair (pion vs kaon). "
        f"|tr_K/tr_π| = {ratio:.6f}. "
        f"Tests (9/5)^n Seifert scaling."
    )
    wb.add_data("pion", {"word_length": len(pion_word), "tr_M": tr_pion})
    wb.add_data("kaon", {"word_length": len(kaon_word), "tr_M": tr_kaon})
    wb.add_data("ratio", {"raw": ratio, "seifert1": pred_seifert1,
                           "seifert2": pred_seifert, "target": target})
    wb.add_assertion("h6_computed", computed=abs(tr_pion) > 1e-20,
                     expected=True, tolerance=0,
                     source="H₆ trace is non-zero")
    wb.save()
    print(f"\nElapsed: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
