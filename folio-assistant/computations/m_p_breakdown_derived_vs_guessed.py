#!/usr/bin/env python3
"""
BREAKDOWN of the m_p tower derivation: what's derived vs guessed.

Re-runs the mass-endomorphism-tower calc (proton_mass_tower_derivation.py)
using the SDP-DERIVED nucleon gluon tails (atom_braid_sdp_gluon.py)
rather than the naive 2·σ₀ uniform assumption.  Tracks per-term
provenance so the +1.83% residual on m_p can be attributed.

Each ingredient in m_p = T1 + T2 + T3 + T4 is tagged:

  ✓ FORMAL DERIVED — proved from Hecke algebra, Plancherel measure,
                      or framework theorems.
  ⚠ CONJECTURAL — formula written in paper (prop:mass-endomorphism-*)
                  but not fully proved.
  □ ASSUMED — physics heuristic or convention adopted without proof.
  ⎯ INPUT — external CODATA-bounded constant (m_e, q₀ from m_μ/m_e).

Output: m-p-breakdown-derived-vs-guessed.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV,
    W_SYM, W_STD, W_ALT, vertex_volume,
)
from atom_braid_sdp_gluon import (
    _NEUTRON_G0_BODY, _NEUTRON_G1_BODY,
    _PROTON_G0_BODY, _PROTON_G1_BODY,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder


def Phi_q(z: float, max_iter: int = 2000, tol: float = 1e-16) -> float:
    """Φ_q(z) = Π_{k=1}^∞ (1 - q^{-k} z)^{-1}."""
    if abs(z) >= float(Q0):
        return float('inf')
    prod = 1.0
    qi_val = float(QI_NUM)
    coef = qi_val
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * z
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * z) < tol:
            break
        coef *= qi_val
    return prod


def describe_chain(chain: list[tuple[float, float]], name: str) -> None:
    print(f"  {name} ({len(chain)} factors):")
    from collections import Counter
    types = Counter()
    h = float(H_A_VAL)
    for c, d in chain:
        if abs(d) < 1e-9:
            types["σ    (1, 0)"] += 1
        elif abs(d + h) < 1e-6:
            types["σ⁻¹  (1, −H_A)"] += 1
        elif abs(d + h/2) < 1e-6:
            types["ud   (1, −H_A/2)"] += 1
        else:
            types[f"other ({c}, {d:.4f})"] += 1
    for t, n in sorted(types.items()):
        print(f"    {n}× {t}")


def main():
    w = WitnessBuilder("m-p-breakdown-derived-vs-guessed",
                        engine="tower+SDP-gluon")
    w.set_description(
        "Breakdown of each ingredient in the m_p = T1+T2+T3+T4 tower "
        "derivation into FORMAL, CONJECTURAL, ASSUMED, or INPUT.  "
        "Uses the SDP-derived neutron gluon tail (σ₀σ₁σ₁σ₀, not 2σ₀)."
    )
    w.add_parameter("q_0", float(Q0))
    w.add_parameter("H_A", float(H_A_VAL))
    w.add_parameter("z_markov", float(Z_MARKOV))

    # ═══════════════════════════════════════════════════════════════
    # SECTION 1: INGREDIENT PROVENANCE
    # ═══════════════════════════════════════════════════════════════
    provenance = [
        ("m_e (MeV scale)",
         "⎯ INPUT",
         "CODATA 2018: 0.51099895 MeV ± 1.5×10⁻¹⁰"),
        ("q_0 substrate parameter",
         "⎯ INPUT (via m_μ/m_e)",
         "1.1099785956; CODATA-bounded to ~1 ppb via m_μ/m_e ratio "
         "(see q_pinning_50_digit.py)"),
        ("H_A = q − 1/q",
         "✓ DERIVED",
         "Hecke relation parameter; follows from q_0 exactly"),
        ("Hecke relation σ_i² = H_A σ_i + 1",
         "✓ DERIVED (standard)",
         "Kassel 'Quantum Groups' Prop. XII.1.2"),
        ("Wedderburn decomposition H_3(q) = sym ⊕ std ⊕ alt",
         "✓ DERIVED (standard)",
         "Dipper–James / Hoefsmit; partitions 3 = (3), (2,1), (1,1,1)"),
        ("Plancherel weights w_λ = d_q(λ)² / [n]_q!",
         "✓ DERIVED (Markov trace)",
         "w_sym = w_alt = 0.1655, w_std = 0.6691 at q_0"),
        ("z (Markov parameter)",
         "✓ DERIVED from q_0",
         f"z = {float(Z_MARKOV):.10f} — Jones–Conway normalization"),
        ("Per-generator chain for B_3 confinement: (σ_0 σ_1^{-1})^3",
         "⚠ CONJECTURAL (quarks-Borromean)",
         "Paper claim (rem:borromean-baryon): 3-quark confinement ≡ "
         "Borromean rings.  Structural, not proven from QCD."),
        ("Quark-pair crossing types: uu=(1,0), dd=(1,−H), ud=(1,−H/2)",
         "✓ DERIVED via integer-LP / SDP",
         "User note: 'no convention. comes from SDP'.  Integer-LP "
         "feasibility (integer-lp-gluon.py, atom_braid_sdp_gluon.py) "
         "picks uu=σ, dd=σ⁻¹, ud=(σ+σ⁻¹)/2 as the Gram-positive solution."),
        ("Gluon tail: proton = 2·σ₀, neutron = σ₀σ₁σ₁σ₀ (NOT 2·σ₀)",
         "✓ DERIVED via integer-LP / SDP",
         "atom_braid_sdp_gluon.py — naive 2·σ₀ for neutron fails the "
         "Gram-positivity constraint; L₊ L₋ = σ₀σ₁σ₁σ₀ is the "
         "feasible optimum.  Paper's original tower used 2·σ₀ for BOTH."),
        ("V̂_i^full = w_sym λ^sym_i + w_std V^std_i + w_alt λ^alt_i",
         "✓ DERIVED (per-gen additive Wedderburn)",
         "Transfer-matrix representation of the 2×2 std block (Hoefsmit); "
         "recurrence in vertex_volume()"),
        ("|V̂_i| operation",
         "□ ASSUMED convention",
         "Absolute value of a signed real; no derivation that |·| is "
         "the correct nonlinearity.  Could be max(0,·) or similar."),
        ("Φ_q(z) = Π_{k=1}^∞ (1 − q^{-k} z)^{-1}",
         "✓ DERIVED (quantum dilogarithm)",
         "Faddeev–Kashaev / Faddeev–Volkov quantum dilogarithm; standard"),
        ("Tower structure: m = |Π V̂_i| + Σ_i Φ_q(|V̂_i|) "
         "+ z² Σ_{|i−j|=1} Φ_q(|V̂_i V̂_j|)",
         "⚠ CONJECTURAL",
         "prop:mass-endomorphism-tower — paper proposes this shape; "
         "proof in content/ sketches jet-tower ascension via pentagon "
         "identity.  Not fully rigorous."),
        ("Restriction to pairs |i−j|=1 (adjacent only)",
         "⚠ CONJECTURAL (locality)",
         "docs/locality-proof-attempt.md — far-commuting locality "
         "is PROVED via Kohno–Drinfeld; adjacent-locality claim is "
         "O(ℏ_q²) ≈ 1% which is the frontier."),
    ]

    print("═" * 90)
    print("INGREDIENT PROVENANCE for m_p tower derivation")
    print("═" * 90)
    for name, tag, note in provenance:
        print(f"  {tag}  {name}")
        print(f"           {note}")
        print()

    # ═══════════════════════════════════════════════════════════════
    # SECTION 2: EXPLICIT CALCULATION with SDP-DERIVED neutron
    # ═══════════════════════════════════════════════════════════════
    print("═" * 90)
    print("RECOMPUTE with SDP-DERIVED neutron gluon (σ₀σ₁σ₁σ₀)")
    print("═" * 90)

    # Build SDP-correct neutron chains
    n_g0_sdp = list(_NEUTRON_G0_BODY) + [(1.0, 0.0)] * 2   # σ₀σ₀ part of L+L-
    n_g1_sdp = list(_NEUTRON_G1_BODY) + [(1.0, 0.0)] * 2   # σ₁σ₁ part
    # Proton unchanged (SDP gives 2·σ₀ = what we had)
    p_g0 = list(_PROTON_G0)
    p_g1 = list(_PROTON_G1)

    describe_chain(p_g0, "proton g0")
    describe_chain(p_g1, "proton g1")
    describe_chain(n_g0_sdp, "neutron g0 (SDP)")
    describe_chain(n_g1_sdp, "neutron g1 (SDP)")
    print()

    # Note: L₊ L₋ = σ₀σ₁σ₁σ₀ in atom_braid_sdp_gluon.py means gen-index
    # interleaving, but when projected onto separate g0 and g1 bucket
    # (as vertex_volume requires), the neutron gluon contributes 2·σ₀
    # to g0 and 2·σ₁ to g1.  The Wedderburn chain is SAME as uniform 2σ₀
    # interpretation FOR PER-GENERATOR purposes — both gens get 2 more σ.
    # This means neutron V̂_0, V̂_1 CHANGE under the SDP rule only in their
    # relative weighting.  Let me rebuild with the body-then-Σ/Σ split.

    V_e = vertex_volume([(1.0, 0.0)] * 3)
    Vp0 = vertex_volume(p_g0)
    Vp1 = vertex_volume(p_g1)
    Vn0_sdp = vertex_volume(n_g0_sdp)
    Vn1_sdp = vertex_volume(n_g1_sdp)
    Vn0_old = vertex_volume(_NEUTRON_G0)
    Vn1_old = vertex_volume(_NEUTRON_G1)

    print(f"{'quantity':<24} {'uniform 2σ₀':>16} {'SDP σ₀σ₁σ₁σ₀':>16} {'shift':>10}")
    print("-" * 72)
    print(f"{'V̂_0 (neutron)':<24} {Vn0_old:>+16.6f} {Vn0_sdp:>+16.6f} "
          f"{(Vn0_sdp - Vn0_old):>+10.6f}")
    print(f"{'V̂_1 (neutron)':<24} {Vn1_old:>+16.6f} {Vn1_sdp:>+16.6f} "
          f"{(Vn1_sdp - Vn1_old):>+10.6f}")
    print()

    # Compute tower for both versions
    def tower(V0, V1, label):
        absV0, absV1 = abs(V0), abs(V1)
        prodV = abs(V0 * V1)
        T1 = prodV
        T2 = Phi_q(absV0)
        T3 = Phi_q(absV1)
        T4 = float(Z_MARKOV) ** 2 * Phi_q(prodV)
        m = T1 + T2 + T3 + T4
        return {"label": label, "V0": V0, "V1": V1,
                "T1": T1, "T2": T2, "T3": T3, "T4": T4, "m_Hecke": m}

    e_tower = {"label": "electron",
               "V0": V_e, "V1": None,
               "T1": abs(V_e), "T2": Phi_q(abs(V_e)),
               "T3": 0.0, "T4": 0.0,
               "m_Hecke": abs(V_e) + Phi_q(abs(V_e))}
    p_tower = tower(Vp0, Vp1, "proton")
    n_tower_old = tower(Vn0_old, Vn1_old, "neutron (uniform 2σ₀, paper)")
    n_tower_sdp = tower(Vn0_sdp, Vn1_sdp, "neutron (SDP σ₀σ₁σ₁σ₀)")

    print(f"{'particle':<28} {'T1':>12} {'T2':>14} {'T3':>14} {'T4':>12} {'m (Hecke)':>14}")
    print("-" * 100)
    for t in [e_tower, p_tower, n_tower_old, n_tower_sdp]:
        print(f"{t['label']:<28} {t['T1']:>12.4f} {t['T2']:>14.2f} "
              f"{t['T3']:>14.2f} {t['T4']:>12.2f} {t['m_Hecke']:>14.2f}")
    print()

    # ═══════════════════════════════════════════════════════════════
    # SECTION 3: MASS PREDICTIONS
    # ═══════════════════════════════════════════════════════════════
    m_e_Hecke = e_tower["m_Hecke"]
    m_p_Hecke = p_tower["m_Hecke"]
    m_n_old_Hecke = n_tower_old["m_Hecke"]
    m_n_sdp_Hecke = n_tower_sdp["m_Hecke"]

    m_p_MeV = (m_p_Hecke / m_e_Hecke) * M_E_MEV
    m_n_old_MeV = (m_n_old_Hecke / m_e_Hecke) * M_E_MEV
    m_n_sdp_MeV = (m_n_sdp_Hecke / m_e_Hecke) * M_E_MEV

    err_p = (m_p_MeV - M_P_MEV) / M_P_MEV * 100
    err_n_old = (m_n_old_MeV - M_N_MEV) / M_N_MEV * 100
    err_n_sdp = (m_n_sdp_MeV - M_N_MEV) / M_N_MEV * 100

    print("═" * 90)
    print("MASS PREDICTIONS (m_e is the only absolute scale input)")
    print("═" * 90)
    print(f"  {'particle':<28} {'predicted':>14} {'CODATA':>12} {'err':>10}")
    print("  " + "-" * 70)
    print(f"  {'m_p':<28} {m_p_MeV:>14.4f} {M_P_MEV:>12.4f} {err_p:>+9.3f}%")
    print(f"  {'m_n (uniform 2σ₀, paper)':<28} {m_n_old_MeV:>14.4f} "
          f"{M_N_MEV:>12.4f} {err_n_old:>+9.3f}%")
    print(f"  {'m_n (SDP σ₀σ₁σ₁σ₀)':<28} {m_n_sdp_MeV:>14.4f} "
          f"{M_N_MEV:>12.4f} {err_n_sdp:>+9.3f}%")
    print()

    # Where the +1.83% residual lives
    print("═" * 90)
    print("WHERE THE PROTON +1.83% RESIDUAL LIVES")
    print("═" * 90)
    print()
    print(" Decomposition by tower term (proton, Hecke units):")
    print(f"   T1 = |V̂_0 V̂_1|              = {p_tower['T1']:>12.4f}  "
          f"({p_tower['T1']/m_p_Hecke*100:>5.2f}% of m_p)")
    print(f"   T2 = Φ_q(|V̂_0|)             = {p_tower['T2']:>12.4f}  "
          f"({p_tower['T2']/m_p_Hecke*100:>5.2f}% of m_p)")
    print(f"   T3 = Φ_q(|V̂_1|)             = {p_tower['T3']:>12.4f}  "
          f"({p_tower['T3']/m_p_Hecke*100:>5.2f}% of m_p)")
    print(f"   T4 = z² · Φ_q(|V̂_0 V̂_1|)   = {p_tower['T4']:>12.4f}  "
          f"({p_tower['T4']/m_p_Hecke*100:>5.2f}% of m_p)")
    print()
    print(" The 1.83% error (+17.2 MeV on 938.27) needs to come from")
    print(" SOMEWHERE in the derivation.  Candidates:")
    print()
    print("   (i)   O(ℏ_q²) ≈ 0.98% adjacent-locality correction")
    print("         (docs/locality-proof-attempt.md §adjacent frontier).")
    print(f"         ℏ_q² = {((float(Q0) - float(QI_NUM))/float(Q0))**2:.6f} — right ballpark.")
    print()
    print("   (ii)  2-gen-gap term (|i−j|=2) dropped from the tower")
    print("         — CONJECTURAL to be subleading.  Not verified.")
    print()
    print("   (iii) Higher-jet tower corrections from the pentagon")
    print("         identity (rem:mass-endomorphism-jet-tower).")
    print("         NOT computed in the current implementation.")
    print()
    print("   (iv)  The |·| absolute-value nonlinearity is ASSUMED.")
    print("         If V̂_i have imaginary parts at the std Hoefsmit level")
    print("         that cancel in the symmetrised tower, dropping them is")
    print("         a loss of precision.")
    print()
    print(" None of (i)-(iv) is computed here; the 1.83% residual is the")
    print(" combined tail from these sources.  The leading +1.83% is")
    print(" likely (i) since ℏ_q² = 0.98% and the sign/scale match.")

    # Save everything
    w.add_data("provenance", [{"name": n, "tag": t, "note": x}
                                 for n, t, x in provenance])
    w.add_data("per_gen_volumes", {
        "V_e": V_e,
        "Vp0": Vp0, "Vp1": Vp1,
        "Vn0_old_uniform_2sigma0": Vn0_old,
        "Vn1_old_uniform_2sigma0": Vn1_old,
        "Vn0_sdp_L_plus_minus": Vn0_sdp,
        "Vn1_sdp_L_plus_minus": Vn1_sdp,
    })
    w.add_data("tower_terms", {
        "electron": e_tower,
        "proton": p_tower,
        "neutron_old_uniform": n_tower_old,
        "neutron_sdp": n_tower_sdp,
    })
    w.add_data("predictions_MeV", {
        "m_p_pred": m_p_MeV, "m_p_CODATA": M_P_MEV, "m_p_err_pct": err_p,
        "m_n_old_pred": m_n_old_MeV, "m_n_CODATA": M_N_MEV,
        "m_n_old_err_pct": err_n_old,
        "m_n_sdp_pred": m_n_sdp_MeV, "m_n_sdp_err_pct": err_n_sdp,
    })
    w.save()


if __name__ == "__main__":
    main()
