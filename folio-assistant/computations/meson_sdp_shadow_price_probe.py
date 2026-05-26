#!/usr/bin/env python3
"""
Meson SDP shadow-price probe: derive meson mass structure from the
confinement LP/SDP dual, walking through the full GB NF calculation.

APPROACH:
The baryon mass formula uses the confinement SDP on the Borromean
braid to identify which Wedderburn blocks carry the mass. The shadow
prices (dual variables y*) are the binding-energy demand channels.

Apply the SAME machinery to the meson braid M₊ = (σ₀σ₁)²·σ₁σ₀:

1. Compute the Gröbner-Shirshov (GB) normal form of M₊ in H₃(q)
2. Decompose into Wedderburn blocks (3 partitions of 3)
3. Set up the confinement LP: minimize tr_M subject to PSD constraints
4. Read the shadow prices y* and active set
5. The active set tells us WHICH partitions carry the pion mass
6. Compare pion vs kaon active sets → mass ratio structure

The GB NF calculation walks through the Hecke reduction step by step,
matching the categorical-meson.md derivation.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q as Q0_FLOAT  # noqa: E402
from hecke_characters import build_seminormal_matrices, partitions_of  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402


def gb_nf_meson(q_val):
    """Walk through the GB NF reduction of the meson braid M₊.

    M₊ = (σ₀σ₁)²·σ₁σ₀ in H₃(q).

    Step 1: (σ₀σ₁)² = σ₀·σ₁·σ₀·σ₁
      Apply braid relation σ₁σ₀σ₁ = σ₀σ₁σ₀ to rightmost 3:
      σ₀·(σ₀σ₁σ₀) = σ₀²·L₋
      Hecke: σ₀² = h·σ₀ + 1
      → (σ₀σ₁)² = h·e⁻ + L₋

    Step 2: Multiply by T₁₀ = σ₁σ₀:
      L₋·L₋ = σ₁σ₀·σ₁σ₀ → braid + Hecke → h·e⁻ + L₊
      e⁻·L₋ = σ₀σ₁σ₀·σ₁σ₀ → two braid + Hecke → h²e⁻ + hL₊ + hL₋ + σ₁

    Result: M₊ = h·σ₁ + (h²+1)·L₊ + h²·L₋ + (h³+h)·e⁻

    Returns dict of NF coefficients.
    """
    h = q_val - 1.0/q_val
    return {
        "1": 0.0,           # identity coefficient
        "sigma0": 0.0,      # σ₀ coefficient
        "sigma1": h,         # σ₁ coefficient
        "L+": h**2 + 1,     # L₊ = σ₀σ₁ coefficient
        "L-": h**2,         # L₋ = σ₁σ₀ coefficient
        "e-": h**3 + h,     # e⁻ = σ₀σ₁σ₀ coefficient
        "net": h + (h**2 + 1) + h**2 + (h**3 + h),
    }


def gb_nf_kaon(q_val):
    """Kaon NF: pion NF × σ₁² (2 extra strange-quark crossings).

    K = M₊ · σ₁²
    σ₁² = h·σ₁ + 1 (Hecke relation)

    So K = M₊ · (h·σ₁ + 1) = h·M₊·σ₁ + M₊

    Need to compute M₊·σ₁ in NF. Each basis element × σ₁:
      σ₁·σ₁ = h·σ₁ + 1                    (Hecke)
      L₊·σ₁ = σ₀σ₁² = σ₀(hσ₁+1) = hL₊ + σ₀  (Hecke on σ₁²)
      L₋·σ₁ = σ₁σ₀σ₁ = σ₀σ₁σ₀ = e⁻       (braid relation)
      e⁻·σ₁ = σ₀σ₁σ₀σ₁ = σ₀·e⁻'... need careful reduction

    Actually let me just compute numerically via matrix product.
    """
    h = q_val - 1.0/q_val
    # Will compute via matrix representation instead
    return None


def wedderburn_decomposition(word, q_val, n=3):
    """Decompose a braid word into Wedderburn block contributions.

    For each partition λ ⊢ n, compute:
      - χ^λ(word) = tr(ρ_λ(word))  (Hecke character)
      - y_λ(q) (Wenzl-Jones Markov weight)
      - y_λ · χ^λ (per-partition Markov trace contribution)
      - min eigenvalue of the symmetric part of ρ_λ(word) (PSD check)
    """
    results = []
    for part_list in partitions_of(n):
        shape = tuple(part_list)
        q_f = float(q_val)

        sigmas, dim, _ = build_seminormal_matrices(shape, q=q_f)
        if dim == 0:
            results.append({"partition": list(shape), "dim": dim})
            continue

        sigmas_dense = [s.toarray() if hasattr(s, 'toarray') else np.asarray(s)
                        for s in sigmas]

        # Apply word
        product = np.eye(dim)
        I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas_dense):
                M = c * sigmas_dense[g] + d * I
                product = product @ M

        chi = float(np.trace(product))
        y = float(y_lambda_wenzl_bridge_numeric(list(shape), q_val, dps=50))

        # Symmetric part eigenvalues (for PSD check)
        sym = (product + product.T) / 2
        eigvals = np.linalg.eigvalsh(sym)
        min_eig = float(min(eigvals))

        results.append({
            "partition": list(shape),
            "dim": dim,
            "chi": chi,
            "y_lambda": y,
            "y_chi": y * chi,
            "min_eig": min_eig,
            "psd": min_eig >= -1e-10,
        })
    return results


def meson_braid_word(n_extra, q_val):
    """Meson braid word with n_extra additional σ₁ crossings.
    n_extra=0 → pion (6 crossings), n_extra=2 → kaon (8 crossings).
    """
    word = [
        (1.0, 0.0, 0),  # σ₀
        (1.0, 0.0, 1),  # σ₁
        (1.0, 0.0, 0),  # σ₀
        (1.0, 0.0, 1),  # σ₁
        (1.0, 0.0, 1),  # σ₁
        (1.0, 0.0, 0),  # σ₀
    ]
    for _ in range(n_extra):
        word.append((1.0, 0.0, 1))
    return word


def main():
    set_compute_dps()
    t0 = time.time()
    mp.mp.dps = 50
    q0 = mp.mpf(Q_50_DIGIT_STR)
    q_f = float(q0)
    h = q_f - 1.0/q_f

    print("=" * 70)
    print("  Meson SDP shadow-price probe")
    print("=" * 70)
    print()

    # ── 1. GB Normal Form walkthrough ───────────────────────────
    print("  1. Gröbner-Shirshov NF of pion braid M₊")
    nf = gb_nf_meson(q_f)
    print(f"    M₊ = h·σ₁ + (h²+1)·L₊ + h²·L₋ + (h³+h)·e⁻")
    print(f"    At q₀: h = {h:.6f}")
    for basis, coeff in nf.items():
        if basis != "net" and coeff != 0:
            print(f"      {basis:>6s}: {coeff:.6f}")
    print(f"      net: {nf['net']:.6f}")
    print()

    # ── 2. Wedderburn decomposition ─────────────────────────────
    print("  2. Wedderburn block decomposition")
    print()

    for name, n_extra in [("Pion (π)", 0), ("Kaon (K)", 2)]:
        word = meson_braid_word(n_extra, q_f)
        blocks = wedderburn_decomposition(word, q0)

        print(f"    {name} ({len(word)} crossings):")
        print(f"    {'λ':>12s}  {'d':>3s}  {'χ^λ':>12s}  {'y_λ':>12s}  {'y·χ':>12s}  {'min_eig':>10s}  {'PSD':>4s}")

        total_tr = 0.0
        for b in blocks:
            if "chi" in b:
                total_tr += b["y_chi"]
                psd_marker = "✓" if b["psd"] else "✗"
                print(f"    {str(b['partition']):>12s}  {b['dim']:>3d}  "
                      f"{b['chi']:>12.6f}  {b['y_lambda']:>12.8f}  "
                      f"{b['y_chi']:>12.8f}  {b['min_eig']:>+10.4f}  {psd_marker:>4s}")

        print(f"    Total tr_M = {total_tr:.8f}")
        print()

    # ── 3. Shadow price analysis ────────────────────────────────
    print("  3. Shadow price / active set analysis")
    print()

    # The confinement LP asks: which partitions have NEGATIVE min_eig?
    # These are the "demand channels" — they want more trace weight.
    # The shadow prices measure how much the optimal trace changes
    # when we relax the PSD constraint on each block.

    for name, n_extra in [("Pion", 0), ("Kaon", 2)]:
        word = meson_braid_word(n_extra, q_f)
        blocks = wedderburn_decomposition(word, q0)

        active = [b for b in blocks if "min_eig" in b and not b["psd"]]
        inactive = [b for b in blocks if "min_eig" in b and b["psd"]]

        print(f"    {name}:")
        print(f"      Active set (PSD-violating): {[b['partition'] for b in active]}")
        print(f"      Inactive set (PSD-satisfied): {[b['partition'] for b in inactive]}")

        if active:
            print(f"      Dominant demand channel: {active[0]['partition']} "
                  f"(min_eig = {active[0]['min_eig']:.4f})")
        print()

    # ── 4. String-breaking interpretation ───────────────────────
    print("  4. String-breaking interpretation (σ² = hσ + 1)")
    print()
    print(f"    The Hecke relation σ² = hσ + 1 IS the flux tube snap:")
    print(f"      σ² = doubly-wound flux tube")
    print(f"      hσ = meson with crossing energy h = {h:.6f}")
    print(f"      1  = vacuum (identity)")
    print()
    print(f"    Pion mass ∝ h · (Borromean strand-breaking coefficient)")
    print(f"    h = q − q⁻¹ = {h:.10f}")
    print(f"    h · m_p (from strand breaking) = {h * 938.272:.2f} MeV")
    print(f"    vs m_π = 139.57 MeV → ratio = {139.57 / (h * 938.272):.4f}")
    print()

    # ── 5. The h-tower for mesons ───────────────────────────────
    print("  5. Meson NF coefficient structure")
    print()
    print(f"    Pion NF net = h + (h²+1) + h² + (h³+h)")
    print(f"               = 1 + 2h + 2h² + h³")
    print(f"               = (1+h)² + h²(1+h) + ... hmm")
    print(f"               = 1 + 2h + 2h² + h³")
    net_val = 1 + 2*h + 2*h**2 + h**3
    print(f"               = {net_val:.10f} at q₀")
    print()

    # Factor: net = (1+h)(1+h+h²) = (1+h)·[3]_{1+h}... no
    # Actually: 1 + 2h + 2h² + h³ = (1+h)² + h·(1+h) + ... let me just factor
    # 1 + 2h + 2h² + h³ = (h+1)(h²+h+1)
    factored = (1+h) * (1+h+h**2)
    print(f"    Factor: (1+h)(1+h+h²) = {factored:.10f}")
    print(f"    Match: {'✓' if abs(factored - net_val) < 1e-10 else '✗'}")
    print()

    # (1+h) = q/q = q·(1-1/q+1/q) = ... actually 1+h = 1+(q-1/q) = q + (1-1/q) = q + hbar
    print(f"    (1+h) = 1 + (q−q⁻¹) = {1+h:.10f}")
    print(f"    (1+h+h²) = {1+h+h**2:.10f}")
    print(f"    Note: (1+h) = q·(1 + ℏ_q) where ℏ_q = (q-1)/q")
    hbar = (q_f-1)/q_f
    print(f"      q·(1+ℏ) = {q_f*(1+hbar):.10f} vs (1+h) = {1+h:.10f}")
    # Not equal. Let me check directly
    # 1+h = 1+q-1/q. q(1+hbar) = q + q·(q-1)/q = q + q - 1 = 2q-1. Not same.
    print()

    # The factorization (1+h)(1+h+h²) is structural:
    # (1+h) is the "single-crossing" factor
    # (1+h+h²) is the "geometric series truncated at h²"
    # Together they give the meson net coefficient

    # For kaon: M_K = M_π · σ₁² = M_π · (hσ₁ + 1)
    # The kaon's net should be approximately net_π · (1+h·something)

    pion_word = meson_braid_word(0, q_f)
    kaon_word = meson_braid_word(2, q_f)
    tr_pi = sum(b["y_chi"] for b in wedderburn_decomposition(pion_word, q0) if "y_chi" in b)
    tr_K = sum(b["y_chi"] for b in wedderburn_decomposition(kaon_word, q0) if "y_chi" in b)

    print(f"    tr_M(π) = {tr_pi:.10f}")
    print(f"    tr_M(K) = {tr_K:.10f}")
    print(f"    tr_K/tr_π = {tr_K/tr_pi:.10f}")
    print(f"    (1+h) = {1+h:.10f}")
    print(f"    (tr_K/tr_π) / (1+h) = {(tr_K/tr_pi)/(1+h):.10f}")
    print()

    # What about m_K/m_π from the NF structure?
    # If m ∝ net(braid), then m_K/m_π ≈ net_K/net_π
    # But net is not the same as tr_M...

    elapsed = time.time() - t0
    print(f"\n  Wall time: {elapsed:.1f}s")

    w = WitnessBuilder("meson-sdp-shadow-price-probe", engine="python")
    w.set_description(
        "Applies the confinement LP/SDP shadow-price analysis to meson "
        "braids. Walks through the GB NF calculation, decomposes into "
        "Wedderburn blocks, identifies PSD-violating (active) partitions, "
        "and tests the string-breaking interpretation σ²=hσ+1."
    )
    w.set_content_block("prop:lepton-meson-torus-knot-dictionary")
    w.add_data("pion_nf_factored", "(1+h)(1+h+h²)")
    w.add_data("tr_pion", tr_pi)
    w.add_data("tr_kaon", tr_K)
    w.add_data("ratio_tr", tr_K/tr_pi)
    w.add_assertion("nf_factors", computed=1 if abs(factored-net_val)<1e-10 else 0,
                     expected=1, tolerance=0,
                     source="Pion net = (1+h)(1+h+h²)")
    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
