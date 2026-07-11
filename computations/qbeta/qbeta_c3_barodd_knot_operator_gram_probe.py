#!/usr/bin/env python3
"""qbeta_c3_barodd_knot_operator_gram_probe.py

The knot-operator / inverse-Gram ALGEBRAIC SHADOW of the c₃ bar-odd S carrier
(owner-directed). Per `thurston-relaxation.md`, the SDP/algebraic solver is the
ℤ[q^{±1/2}]-shadow of the figure-eight shape-parameter geometry. This probe
locates the bar-odd (decay) carrier at the H₃(q) algebra level — the negative-
norm direction of the indefinite Frobenius/Gram form — and shows the figure-eight
knot operator's σ-antisymmetric (decay) projection lands exactly on it.

RESULTS (all computed, none fitted; scope-(a); C14):
  1. β(4₁) = nf(σ₀σ₁⁻¹σ₀σ₁⁻¹) = L₊ + HA·e⁻   (HA = q−q⁻¹) in the NF basis
     {γ, σ₀, σ₁, L₊, L₋, e⁻}.
  2. The FLIP involution (σ₀↔σ₁, L₊↔L₋, e⁻ fixed by the braid relation
     σ₀σ₁σ₀=σ₁σ₀σ₁) is the algebraic bar σ. Its decay projection
     ½(β − flip β) = ½(L₊ − L₋).
  3. The Frobenius/Gram form G_{ij}=tr_M(b_i b_j) is INDEFINITE: signature (5+,1−),
     det G < 0. The UNIQUE negative-norm (ghost) direction is (L₊−L₋)/√2.
  4. ⇒ the figure-eight's decay projection ½(L₊−L₋) lies EXACTLY on the negative-
     norm ghost mode — the algebraic realization of `EkParitySplit.decayProj`
     (σ-antisymmetric = bar-odd = decay). The mass projection ½(L₊+L₋)+HA·e⁻
     lives in the positive-norm (unitary/mass) cone.

So the bar-odd S carrier is pinned, algebraically, to a SINGLE mode — the
negative-signature chirality direction (L₊−L₋). The observable VALUE still needs
the archimedean z(q₀) (Newton on Thurston's gluing equations seeded by the Φ_q
poles, `thurston-relaxation.md` / `def:archimedean-realization-functor`) — the
open eval map — but the carrier is no longer a mystery: it is the Gram ghost.

Companion: docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md;
Lean: QOU.QBeta.EkParitySplit.decayProj.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import pyhecke.gram as G  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# FLIP permutation on NF basis {γ,σ₀,σ₁,L₊,L₋,e⁻}: σ₀↔σ₁, L₊↔L₋, γ,e⁻ fixed.
FLIP = [0, 2, 1, 4, 3, 5]


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — knot-operator / inverse-Gram algebraic shadow (H₃(q))")
    print("=" * 78)

    names = G.NF_NAMES
    gram = np.array(G.G, dtype=float)
    trm = np.array([float(x) for x in G.TR_M], dtype=float)
    ha = float(G.q0 - G.qi)
    print(f"\n  q₀ = {float(G.q0):.10f}   HA = q−q⁻¹ = {ha:.10f}")
    print(f"  NF basis: {names}")

    # ---- 1. figure-eight knot operator in H₃(q) ----
    beta = np.array([float(x) for x in G.nf_of_word([0, -2, 0, -2])], dtype=float)
    print(f"\n[1] β(4₁) = nf(σ₀σ₁⁻¹σ₀σ₁⁻¹) = "
          + " + ".join(f"{c:.4f}·{n}" for c, n in zip(beta, names) if abs(c) > 1e-9))
    # Jones-related closure trace
    trace = float(beta @ trm)
    print(f"    tr_M(β(4₁)) = ⟨β, TR_M⟩ = {trace:.8f}")

    # ---- 2. FLIP (algebraic bar) + decay/mass projections ----
    beta_flip = beta[FLIP]
    decay = (beta - beta_flip) / 2.0     # σ-antisymmetric = bar-ODD (decay)
    mass = (beta + beta_flip) / 2.0      # σ-symmetric = bar-EVEN (mass)
    print(f"\n[2] flip(β) = " + " + ".join(f"{c:.4f}·{n}" for c, n in zip(beta_flip, names) if abs(c) > 1e-9))
    print(f"    decay proj ½(β−flip β) = "
          + " + ".join(f"{c:+.4f}·{n}" for c, n in zip(decay, names) if abs(c) > 1e-9)
          + "   (= ½(L₊−L₋))")
    print(f"    mass  proj ½(β+flip β) = "
          + " + ".join(f"{c:+.4f}·{n}" for c, n in zip(mass, names) if abs(c) > 1e-9))

    # ---- 3. Gram signature + the ghost direction ----
    evals, V = np.linalg.eigh(gram)
    n_neg = int((evals < 0).sum())
    n_pos = int((evals > 0).sum())
    ghost = V[:, int(np.argmin(evals))]
    if ghost[3] < 0:  # sign convention: make it look like (L₊−L₋)
        ghost = -ghost
    print(f"\n[3] Gram G_{{ij}}=tr_M(b_i b_j): det={np.linalg.det(gram):.6f}, "
          f"signature ({n_pos}+,{n_neg}−) — INDEFINITE")
    print(f"    eigenvalues: {np.round(evals,5)}")
    print(f"    ghost (neg-norm) eigenvector = "
          + " + ".join(f"{c:+.4f}·{n}" for c, n in zip(ghost, names) if abs(c) > 1e-6)
          + "   (= (L₊−L₋)/√2)")

    # ---- 4. decay projection lies on the ghost mode ----
    decay_norm2 = float(decay @ gram @ decay)      # Gram norm of the decay proj
    mass_norm2 = float(mass @ gram @ mass)
    # cosine between decay proj and the ghost direction (in ordinary inner product)
    cos = abs(float(decay @ ghost) / (np.linalg.norm(decay) * np.linalg.norm(ghost)))
    print(f"\n[4] decay proj ½(L₊−L₋): Gram-norm² = {decay_norm2:+.6f} (<0 ⇒ GHOST/decay),")
    print(f"    alignment |cos∠(decay, ghost)| = {cos:.8f}  (=1 ⇒ exactly the ghost mode)")
    print(f"    mass proj: Gram-norm² = {mass_norm2:+.6f} (>0 ⇒ unitary/mass cone)")
    print("\n    ⇒ the figure-eight bar-ODD carrier = the UNIQUE negative-signature")
    print("      (ghost) mode of the H₃(q) Gram form = algebraic EkParitySplit.decayProj.")
    print("      Observable VALUE still needs z(q₀) (Newton/gluing, thurston-relaxation).")

    ok = (n_neg == 1 and decay_norm2 < 0 and mass_norm2 > 0 and abs(cos - 1) < 1e-6)

    wb = WitnessBuilder("qbeta-c3-barodd-knot-operator-gram", engine="pyhecke+numpy")
    wb.set_description(
        "Algebraic (knot-operator / inverse-Gram) shadow of the c₃ bar-odd S "
        "carrier. β(4₁)=L₊+HA·e⁻ in H₃(q); the FLIP bar's decay projection "
        "½(L₊−L₋) lands exactly on the UNIQUE negative-norm (ghost) direction of "
        "the indefinite Frobenius/Gram form (signature 5+,1−) — the algebraic "
        "realization of EkParitySplit.decayProj. Observable value still needs the "
        "archimedean z(q₀) (thurston-relaxation Newton map). Scope-(a); C14; no "
        "c_k wired."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("figure_eight_operator", {
        "braid": "sigma0 sigma1^-1 sigma0 sigma1^-1",
        "nf": {n: float(c) for n, c in zip(names, beta) if abs(c) > 1e-9},
        "tr_M": trace})
    wb.add_data("flip_bar_projections", {
        "decay_half_Lplus_minus_Lminus": {n: float(c) for n, c in zip(names, decay) if abs(c) > 1e-9},
        "mass": {n: float(c) for n, c in zip(names, mass) if abs(c) > 1e-9}})
    wb.add_data("gram_signature", {
        "det": float(np.linalg.det(gram)), "n_pos": n_pos, "n_neg": n_neg,
        "eigenvalues": [float(x) for x in evals],
        "ghost_direction": {n: float(c) for n, c in zip(names, ghost) if abs(c) > 1e-6}})
    wb.add_data("carrier_is_ghost_mode", {
        "decay_gram_norm2": decay_norm2, "mass_gram_norm2": mass_norm2,
        "cos_decay_ghost": cos,
        "conclusion": "figure-eight bar-odd carrier = unique negative-signature Gram mode (L+ - L-)",
        "open": "observable S value needs z(q0) = Newton on gluing equations (thurston-relaxation)"})
    wb.add_assertion("gram_indefinite_one_ghost", computed=float(n_neg), expected=1.0,
                     tolerance=0.5, source="tr_M Gram form has signature (5+,1-)")
    wb.add_assertion("decay_proj_is_ghost_mode", computed=abs(cos - 1), expected=0.0,
                     tolerance=1e-6, source="½(L₊−L₋) aligns with the negative-norm eigenvector")
    wb.add_assertion("decay_negative_norm", computed=1.0 if decay_norm2 < 0 else 0.0,
                     expected=1.0, tolerance=0.5, source="decay projection has negative Gram norm (ghost/bar-odd)")
    wb.save()

    print(f"\n  RESULT: {'ALL OK' if ok else 'CHECK'}  (carrier pinned to the Gram ghost; value open)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
