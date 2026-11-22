#!/usr/bin/env python3
"""
Derivation of D's Frobenius packing density ρ_F(D) = 1·m_e.

Master formula from docs/path-to-1ppb-04-plan.md:

    B(Z, N; q_0) = Σ_{P ∈ JSJ(K_{Z,N})} ρ_F(P, q_0) · Vol_hyp(P, q_0)

    ρ_F(P, q_0) = m_e(q_0) · n_chir(P)

    n_chir(P) ∈ {1, 2} = # of active chirality blocks (sym/alt) of
                          H_{n_P}(q_0) populated by β_P's support.

For D (single inter-nucleon JSJ piece, census-matched to 6_2), we
compute n_chir from the Wedderburn decomposition of the full atom
braid word β_D ∈ H_6(q_0) and the framework rule:

    n_chir = 2  iff alt ∈ Λ(β_D)  and  alt carries independent weight
             1  otherwise  (alt-suppressed / single-chirality)

The "alt ∈ Λ(β_D)" criterion has two readings in the manuscript:

    (I) character criterion:  χ_alt(β_D) ≠ 0
    (II) weight criterion:    contribution of alt to the Plancherel
                              sum of β_D is of the SAME ORDER as sym

This script computes both readings for β_D explicitly, using the
CLOSED-FORM characters derived in docs/chi-sym-alt-theorem.md (no
matrix machinery needed).

Output: d-density-derivation.witness.json

Status:
  • Hecke characters χ_sym, χ_alt — DERIVED (closed form)
  • The rule "ρ_F = m_e · n_chir" itself — CONJECTURE
    (see conj:mass-volume-factorization and
     rem:frobenius-packing-density)
  • Reading (I) vs (II) — ambiguous in the manuscript
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=UserWarning)
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import h as H_A_VAL
from mass_at_3A_proper import atom_braid_word_3A
from hecke_core import w_sym, w_std, w_alt
from q_parameter import Q_MP as Q0, HA_MP
import mpmath as mp
from _precision import set_compute_dps, fmt
set_compute_dps()
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder


def count_factor_types(word):
    c = {"pure_sigma": 0, "pure_sigma_inv": 0, "ud": 0}
    for cc, dd, _g in word:
        if abs(cc - 1.0) > 1e-12:
            c[f"other({cc},{dd})"] = c.get(f"other({cc},{dd})", 0) + 1
            continue
        if abs(dd) < 1e-12:
            c["pure_sigma"] += 1
        elif abs(dd - (-H_A_VAL)) < 1e-12:
            c["pure_sigma_inv"] += 1
        elif abs(dd - (-H_A_VAL / 2)) < 1e-12:
            c["ud"] += 1
    return c


def chi_sym_closed_form(n_sigma: int, n_sigma_inv: int, n_ud: int,
                          q: float, H_A: float) -> float:
    """χ_sym(β) = q^(n_σ − n_σ⁻¹) · ([2]_q/2)^n_ud.

    Ref: docs/chi-sym-alt-theorem.md §Individual closed forms.
    """
    two_q = q + 1 / q
    return (q ** (n_sigma - n_sigma_inv)) * (two_q / 2) ** n_ud


def chi_alt_closed_form(n_sigma: int, n_sigma_inv: int, n_ud: int,
                          q: float, H_A: float) -> float:
    """χ_alt(β) = (−1)^#(β) · q^(n_σ⁻¹ − n_σ) · ([2]_q/2)^n_ud.

    Ref: docs/chi-sym-alt-theorem.md §Individual closed forms.
    """
    two_q = q + 1 / q
    sign = -1 if (n_sigma + n_sigma_inv + n_ud) % 2 else 1
    return sign * (q ** (n_sigma_inv - n_sigma)) * (two_q / 2) ** n_ud


def main():
    w = WitnessBuilder("d-density-derivation", engine="closed-form")
    w.set_description(
        "Derivation of Deuterium's Frobenius packing density ρ_F(D) from "
        "n_chir(β_D), using the closed-form χ_sym/χ_alt characters from "
        "docs/chi-sym-alt-theorem.md. Both the character-criterion (I) "
        "and the Plancherel-weight-criterion (II) readings of 'alt ∈ Λ' "
        "are computed."
    )
    w.set_content_block("conj:mass-volume-factorization")
    w.add_parameter("q_0", fmt(Q0))
    w.add_parameter("H_A", fmt(HA_MP))
    w.add_parameter("m_e_MeV", float(M_E_MEV))
    w.add_caveat(
        "The rule ρ_F(P) = m_e · n_chir(P) is a conjecture "
        "(conj:mass-volume-factorization). The criterion for 'alt ∈ Λ' "
        "is ambiguous in the manuscript between character non-vanishing "
        "and Plancherel-weight order. Both readings are reported."
    )

    Z, N = 1, 1
    A = Z + N
    word = atom_braid_word_3A(Z, N)
    counts = count_factor_types(word)
    n_sigma = counts["pure_sigma"]
    n_sigma_inv = counts["pure_sigma_inv"]
    n_ud = counts["ud"]
    word_len = n_sigma + n_sigma_inv + n_ud

    # q₀ and H_A as 70-digit mpf. Until 2026-11-21 both entered as float64
    # (q_parameter.Q, hecke_core.h), capping every character below at float64
    # (f64_into_mpmath_audit F64_CAST).
    H_A_sq_4 = 1 + HA_MP * HA_MP / 4
    chi_sym = chi_sym_closed_form(n_sigma, n_sigma_inv, n_ud, Q0, HA_MP)
    chi_alt = chi_alt_closed_form(n_sigma, n_sigma_inv, n_ud, Q0, HA_MP)
    chi_product = chi_sym * chi_alt
    chi_product_closed = -(H_A_sq_4 ** n_ud)

    print("=" * 78)
    print("DERIVATION OF ρ_F(D) = 1 · m_e")
    print("=" * 78)
    print(f"  Z = {Z}, N = {N}, A = {A}")
    print(f"  q_0 = {float(Q0):.10f}")
    print(f"  H_A = q_0 - 1/q_0 = {float(H_A_VAL):.10f}")
    print(f"  [2]_q/2 = (q + 1/q)/2 = {(Q0 + 1/Q0)/2:.10f}")
    print()

    print("Step 1. Count factor types in atom_braid_word_3A(1, 1):")
    print(f"  n_σ    = {n_sigma}    (pure positive crossings)")
    print(f"  n_σ⁻¹  = {n_sigma_inv}    (pure negative crossings)")
    print(f"  n_ud   = {n_ud}    (quark-pair ud-half crossings; = 2A+1 = {2*A+1})")
    print(f"  #(β_D) = {word_len}")
    print()

    print("Step 2. Closed-form characters "
           "(docs/chi-sym-alt-theorem.md):")
    print(f"  χ_sym(β_D) = q^{n_sigma - n_sigma_inv} · ([2]_q/2)^{n_ud}")
    print(f"            = {chi_sym:+.6f}")
    print(f"  χ_alt(β_D) = (-1)^{word_len} · q^{n_sigma_inv - n_sigma} · ([2]_q/2)^{n_ud}")
    print(f"            = {chi_alt:+.6f}")
    print(f"  χ_s·χ_a    = -(1 + H_A²/4)^{n_ud} = {chi_product:+.6f}")
    print(f"             (cross-check vs closed form {chi_product_closed:+.6f})")
    print()

    # Reading (I): character criterion
    chi_alt_nonzero = abs(chi_alt) > 1e-10
    reading_I = "alt ∈ Λ (character non-vanishing)" if chi_alt_nonzero \
                else "alt ∉ Λ (χ_alt = 0)"
    n_chir_I = 2 if chi_alt_nonzero else 1
    rho_F_I = n_chir_I * M_E_MEV

    print("Reading (I) — character criterion:")
    print(f"  alt ∈ Λ  iff  χ_alt(β_D) ≠ 0")
    print(f"  χ_alt(β_D) = {chi_alt:+.6f}  →  {reading_I}")
    print(f"  n_chir = {n_chir_I}")
    print(f"  ρ_F = n_chir · m_e = {rho_F_I:.6f} MeV")
    print()

    # Reading (II): weight criterion.
    # Compare the Plancherel-weighted contributions of sym and alt.
    # Wedderburn-Artin weights of H_3(q), same closed form as
    # pyhecke.gram.W_SYM / W_ALT (q²/(q⁴+4q²+1)), evaluated in mpf.
    _q2 = Q0 ** 2
    w_sym_f = _q2 / (_q2 ** 2 + 4 * _q2 + 1)
    w_alt_f = w_sym_f
    assert abs(w_sym_f - float(w_sym)) < 1e-15 and abs(w_alt_f - float(w_alt)) < 1e-15
    contrib_sym = w_sym_f * chi_sym
    contrib_alt = w_alt_f * chi_alt
    ratio_alt_over_sym = (abs(contrib_alt) / abs(contrib_sym)
                           if abs(contrib_sym) > 1e-30 else float("inf"))
    alt_saturated = ratio_alt_over_sym > 0.5
    reading_II = ("alt ∈ Λ (weights comparable)" if alt_saturated
                  else "alt ∉ Λ (weight suppressed vs sym)")
    n_chir_II = 2 if alt_saturated else 1
    rho_F_II = n_chir_II * M_E_MEV

    print("Reading (II) — Plancherel-weight criterion:")
    print(f"  w_sym · χ_sym = {w_sym_f:.6f} · {chi_sym:+.6f} = {contrib_sym:+.6f}")
    print(f"  w_alt · χ_alt = {w_alt_f:.6f} · {chi_alt:+.6f} = {contrib_alt:+.6f}")
    print(f"  |alt / sym|   = {ratio_alt_over_sym:.4f}")
    print(f"  → {reading_II}")
    print(f"  n_chir = {n_chir_II}")
    print(f"  ρ_F = n_chir · m_e = {rho_F_II:.6f} MeV")
    print()

    # Paper's claim
    paper_rho_F = 1 * M_E_MEV
    print("Paper's claim:")
    print(f"  rem:frobenius-packing-density §'topological triggers':")
    print("    'Two-body links (e.g. 6_2 representing deuterium) have only")
    print("    mutual linking of two components; the alt block remains")
    print("    suppressed and ρ_F = m_e.'")
    print(f"  → paper asserts n_chir = 1,  ρ_F = m_e = {paper_rho_F:.6f} MeV")
    print()

    # Verdict
    print("=" * 78)
    print("VERDICT")
    print("=" * 78)
    if rho_F_II == paper_rho_F:
        print("  Reading (II) agrees with paper: ρ_F(D) = m_e.")
        print("  Both sym and alt are Plancherel-supported, but at q_0 the")
        print("  alt CONTRIBUTION is comparable in magnitude to sym — NOT")
        print("  'saturated' at O(1) relative weight with an extra factor.")
    if rho_F_I != paper_rho_F:
        print(f"  Reading (I) disagrees with paper: gives ρ_F = {rho_F_I:.4f}.")
        print("  χ_alt(β_D) ≠ 0, so by character non-vanishing the alt block")
        print("  IS populated.  Paper's 'alt suppressed' claim is not")
        print("  justifiable under reading (I).")
    print()
    print("  Conclusion: the paper's ρ_F = m_e for D is consistent with a")
    print("  WEIGHT-based reading of 'alt suppression', NOT a character-")
    print("  based reading.  Since the rule is a conjecture, this is the")
    print("  current best interpretation — but it leaves the +1.09% residual")
    print("  unexplained by a discrete {1, 2} switch: the correction needed")
    print("  is δρ = -0.0108 · m_e, which is continuous, not discrete.")

    w.add_data("factor_counts", {
        "n_sigma": n_sigma,
        "n_sigma_inv": n_sigma_inv,
        "n_ud": n_ud,
        "expected_n_ud": 2 * A + 1,
        "word_length": word_len,
    })
    w.add_data("characters_closed_form", {
        "chi_sym": fmt(chi_sym),
        "chi_alt": fmt(chi_alt),
        "chi_sym_times_chi_alt": fmt(chi_product),
    })
    w.add_data("reading_I_character", {
        "chi_alt_nonzero": bool(chi_alt_nonzero),
        "n_chir": n_chir_I,
        "rho_F_MeV": float(rho_F_I),
        "verdict": reading_I,
    })
    w.add_data("reading_II_weight", {
        "w_sym": fmt(w_sym_f),
        "w_alt": fmt(w_alt_f),
        "contribution_sym": fmt(contrib_sym),
        "contribution_alt": fmt(contrib_alt),
        "ratio_alt_over_sym": fmt(ratio_alt_over_sym),
        "alt_saturated": bool(alt_saturated),
        "n_chir": n_chir_II,
        "rho_F_MeV": float(rho_F_II),
        "verdict": reading_II,
    })
    w.add_data("paper_claim", {
        "rho_F_MeV": paper_rho_F,
        "n_chir": 1,
        "source": "rem:frobenius-packing-density §topological triggers",
    })
    w.add_assertion(
        "ρ_F(D) from weight criterion matches paper (ρ_F = m_e)",
        computed=float(rho_F_II),
        expected=float(paper_rho_F),
        tolerance=1e-12,
        source="Plancherel-weighted χ contributions",
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    w.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "folio/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    w.save()


if __name__ == "__main__":
    main()
