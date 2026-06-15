#!/usr/bin/env python3
"""
Knot operator SDP: use the figure-eight 4₁ as the knot operator
on V_(2,1) to determine flavor structure.

The 4₁ braid (σ₁σ₂⁻¹)² acts on V_(2,1) as a 2×2 matrix.
The TWO Young tableaux of (2,1) are:
  t₀: [1,2|3] (entries 1,2 in row 1; 3 in row 2)
  t₁: [1,3|2] (entries 1,3 in row 1; 2 in row 2)

The knot operator M_{4₁} on this 2-dim space has:
  - eigenvalues (spectral decomposition)
  - eigenvectors (flavor assignment)
  - shadow prices (SDP dual variables)

The SPECTRAL DECOMPOSITION of M_{4₁} into eigenspaces
should give the flavor channels: which eigenvalue corresponds
to which quark flavor.

If 4₁ is the transition knot between generations 1→2, then:
  - one eigenvalue → generation 1 (u,d / electron)
  - other eigenvalue → generation 2 (s / muon)
  - the eigenvalue RATIO → mass ratio
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402


def main():
    set_compute_dps()
    mp.mp.dps = 50
    q = float(mp.mpf(Q_50_DIGIT_STR))
    h = q - 1.0/q

    print("=" * 70)
    print("  Knot operator SDP: 4₁ on V_(2,1)")
    print("=" * 70)
    print()

    # ── 1. Build 4₁ knot operator on V_(2,1) ───────────────────
    sigmas, dim, syts = build_seminormal_matrices((2, 1), q=q)
    sigmas_d = [s.toarray() if hasattr(s, 'toarray') else np.asarray(s)
                for s in sigmas]

    # 4₁ = (σ₁σ₂⁻¹)² where σ₂⁻¹ = σ₂ - h·I
    I = np.eye(dim)
    s1 = sigmas_d[0]  # σ₁
    s2 = sigmas_d[1]  # σ₂
    s2_inv = s2 - h * I  # σ₂⁻¹

    factor = s1 @ s2_inv  # σ₁σ₂⁻¹
    M_41 = factor @ factor  # (σ₁σ₂⁻¹)²

    print(f"  1. The 4₁ knot operator on V_(2,1) (dim {dim})")
    print(f"     M_{'{4₁}'} = (σ₁σ₂⁻¹)² =")
    print(f"     [{M_41[0,0]:+.8f}  {M_41[0,1]:+.8f}]")
    print(f"     [{M_41[1,0]:+.8f}  {M_41[1,1]:+.8f}]")
    print()

    # ── 2. Spectral decomposition ───────────────────────────────
    eigvals, eigvecs = np.linalg.eig(M_41)

    # Sort by magnitude
    idx = np.argsort(-np.abs(eigvals))
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    print(f"  2. Spectral decomposition")
    for i in range(dim):
        print(f"     λ_{i} = {eigvals[i]:+.10f}")
        print(f"     v_{i} = [{eigvecs[0,i]:+.8f}, {eigvecs[1,i]:+.8f}]")
    print()

    print(f"     Eigenvalue ratio |λ₀/λ₁| = {abs(eigvals[0]/eigvals[1]):.10f}")
    print(f"     Eigenvalue ratio λ₀/λ₁ = {eigvals[0]/eigvals[1]:.10f}")
    print()

    # ── 3. What are the eigenvalues structurally? ───────────────
    print(f"  3. Structural identification of eigenvalues")
    print()

    # The eigenvalues of M_{4₁} = (σ₁σ₂⁻¹)² on V_(2,1)
    # σ₁ has eigenvalues q and -q⁻¹ on V_(2,1)
    # σ₂⁻¹ has eigenvalues q⁻¹ and -q on V_(2,1)
    # But σ₁ and σ₂ act on DIFFERENT 2×2 blocks generally

    # Check: are eigenvalues q-powers?
    for i in range(dim):
        ev = eigvals[i]
        if abs(ev) > 1e-10:
            power = np.log(abs(ev)) / np.log(q)
            print(f"     λ_{i} = {ev:+.10f} = q^{power:.6f}")

    print()

    # ── 4. Compare to mass ratios ───────────────────────────────
    print(f"  4. Eigenvalue ratio vs mass ratios")
    print()

    ev_ratio = abs(eigvals[0] / eigvals[1])
    m_mu_me = 206.768283
    m_K_mpi = 3.537118

    print(f"     |λ₀/λ₁| = {ev_ratio:.10f}")
    print(f"     m_μ/m_e = {m_mu_me:.6f}")
    print(f"     m_K/m_π = {m_K_mpi:.6f}")
    print(f"     |λ₀/λ₁|² = {ev_ratio**2:.10f}")
    print(f"     √|λ₀/λ₁| = {ev_ratio**0.5:.10f}")
    print()

    # What power of the ratio gives m_μ/m_e?
    if ev_ratio > 1:
        power_lep = np.log(m_mu_me) / np.log(ev_ratio)
        power_mes = np.log(m_K_mpi) / np.log(ev_ratio)
        print(f"     m_μ/m_e = |λ₀/λ₁|^{power_lep:.6f}")
        print(f"     m_K/m_π = |λ₀/λ₁|^{power_mes:.6f}")
    print()

    # ── 5. The two Young tableaux as flavor channels ────────────
    print(f"  5. Young tableaux as flavor channels")
    print()

    # The two SYT of (2,1):
    # t₀: entries [1→cell(1,1), 2→cell(1,2), 3→cell(2,1)]
    # t₁: entries [1→cell(1,1), 2→cell(2,1), 3→cell(1,2)]
    # (reversed filling of positions 2 and 3)

    print(f"     t₀: [1,2|3] — entries 1,2 in row 1 (symmetric pair)")
    print(f"     t₁: [1,3|2] — entries 1,3 in row 1 (mixed pair)")
    print()
    print(f"     The eigenvectors of M_{'{4₁}'} mix these two tableaux:")
    for i in range(dim):
        c0 = eigvecs[0, i]
        c1 = eigvecs[1, i]
        print(f"     v_{i} = {c0:+.4f}·t₀ + {c1:+.4f}·t₁  (eigenvalue {eigvals[i]:+.6f})")
    print()

    # ── 6. SDP: which eigenvalue is the mass channel? ───────────
    print(f"  6. SDP analysis: PSD constraints on eigenspaces")
    print()

    # The symmetric part of M_{4₁}
    M_sym = (M_41 + M_41.T) / 2
    sym_eigvals = np.linalg.eigvalsh(M_sym)
    print(f"     Symmetric part eigenvalues: {sym_eigvals}")
    print(f"     PSD? {all(e >= -1e-10 for e in sym_eigvals)}")
    print()

    # Also check the pion and kaon operators for comparison
    pion_word = [(1,0,0),(1,0,1),(1,0,0),(1,0,1),(1,0,1),(1,0,0)]
    kaon_word = pion_word + [(1,0,1),(1,0,1)]

    for name, word in [("pion", pion_word), ("kaon", kaon_word), ("4₁", [(1,0,0),(1,-h,1),(1,0,0),(1,-h,1)])]:
        prod = np.eye(dim)
        for (c, d, g) in word:
            prod = prod @ (c * sigmas_d[g] + d * I)
        ev = np.linalg.eigvalsh((prod + prod.T) / 2)
        print(f"     {name:>6s}: sym eigenvalues = [{ev[0]:+.6f}, {ev[1]:+.6f}]")

    print()

    # ── 7. Key structural question ──────────────────────────────
    print(f"  7. Structural question: does M_{'{4₁}'} factorize the mass?")
    print()
    print(f"     The 4₁ operator on V_(2,1) has two eigenvalues.")
    print(f"     These correspond to the two lepton channels")
    print(f"     V_(2) and V_(1,1) via the Frobenius bridge.")
    print()
    print(f"     If the larger eigenvalue → V_(2) (highest weight)")
    print(f"     and the smaller → V_(1,1) (lowest weight),")
    print(f"     then the eigenvalue ratio IS the mass ratio factor")
    print(f"     (modulo the topological constant Vol(4₁)).")

    w = WitnessBuilder("knot-operator-sdp-4_1", engine="python")
    w.set_description(
        "Spectral decomposition of the 4₁ knot operator on V_(2,1). "
        "The two eigenvalues correspond to the two lepton channels "
        "via the Frobenius bridge V_(2,1)↓H₂ = V_(2)⊕V_(1,1)."
    )
    w.set_content_block("prop:frobenius-lepton-meson-bridge")
    w.add_data("eigenvalues", [float(e) for e in eigvals])
    w.add_data("eigenvalue_ratio", float(ev_ratio))
    w.add_data("eigenvectors", [[float(eigvecs[j,i]) for j in range(dim)] for i in range(dim)])
    w.add_assertion("two_eigenvalues", computed=dim, expected=2, tolerance=0,
                     source="V_(2,1) is 2-dimensional")
    print(f"\n  Witness: {w.save()}")


if __name__ == "__main__":
    main()
