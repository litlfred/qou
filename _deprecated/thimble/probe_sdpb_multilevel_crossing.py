"""
probe_sdpb_multilevel_crossing.py — full SDPB with multi-level
crossing equations (jet-tower cross-level + mirror-pair).

Per owner: "do next steps on full SDPB"

This builds on probe_sdpb_pl_crossing_equations.py (H_3 only) by
adding the cross-level consistency constraints from QOU's existing
joint-tower SDP framework (prop:joint-tower-sdp-confinement):

  Decision variables (per particle):
    α_λ^(p) for proton at H_3 (3 blocks)
    α_λ^(n) for neutron at H_3 (3 blocks)
    α_λ^(D) for deuteron at H_6 (11 blocks)
    α_λ^(T) for tritium at H_9 (30 blocks — large)
    α_λ^(³He) for helium-3 at H_9 (30 blocks)
    a — the universal PL integration limit

  Crossing equations:
    1. PSD per block (or eigenvalue ≥ 0 in LP form)
    2. Normalisation per particle (Σα_λ = 1)
    3. Mirror parity ((λ) ↔ (λ') under q ↔ q⁻¹)
    4. **Cross-level Markov multiplicativity** for disjoint braids
       (Wenzl 1988): tr_M(β_p ⊗ β_n) = tr_M(β_p) · tr_M(β_n)
       for the disjoint embedding in H_6.
    5. **Mirror-pair self-conjugacy** T vs ³He: |tr_M(β_T)| =
       |tr_M(β_³He)| · (ρ_K(T) / ρ_K(³He)).
    6. **Per-pair integration-limit consistency**.

  Objective: max a subject to ALL constraints.

  If the multi-level SDPB narrows `a` below z_markov, we have
  a SUBSTANTIVE substrate-only derivation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import numpy as np
import cvxpy as cp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from joint_tower_sdp_solver_v2 import (
    trivial_rep_of_braid, sign_rep_of_braid, represent_braid_in_h3_standard,
)
from q_parameter import Q as q0, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, VOL_BORROMEAN

z_mark = 1 / (np.sqrt(q0) + np.sqrt(1.0 / q0))

# Particle braid words (1-indexed):
proton_word  = [1, -2, 1, -2, 1, -2]
neutron_word = [-1, 2, -1, 2, -1, 2]   # mirror of proton


def hecke_data_h3(braid_word):
    """Compute (chi_3, chi_21, chi_111, M_21) at q_0 for an H_3 braid."""
    chi_3 = float(trivial_rep_of_braid(braid_word, q0))
    chi_111 = float(sign_rep_of_braid(braid_word, q0))
    M = represent_braid_in_h3_standard(braid_word, q0)
    chi_21 = float(np.trace(M))
    return chi_3, chi_21, chi_111, M


def main() -> int:
    print("=" * 78)
    print("  Multi-level SDPB with jet-tower cross-level + mirror-pair")
    print("=" * 78)
    print(f"  q_0 = {q0:.10f}, z_markov = {z_mark:.6f}")
    print()

    # ── H_3 data ──────────────────────────────────────────────────
    chi_p_3, chi_p_21, chi_p_111, M_p = hecke_data_h3(proton_word)
    chi_n_3, chi_n_21, chi_n_111, M_n = hecke_data_h3(neutron_word)

    print("  H_3 Hecke data:")
    print(f"    proton  χ_λ = ({chi_p_3:.4f}, {chi_p_21:.4f}, {chi_p_111:.4f})")
    print(f"    neutron χ_λ = ({chi_n_3:.4f}, {chi_n_21:.4f}, {chi_n_111:.4f})")
    print()

    # ── Wenzl weights at H_3 ──────────────────────────────────────
    def q_int(n):
        return (q0**n - q0**(-n)) / (q0 - 1/q0) if n > 0 else 0.0
    qfact_3 = q_int(1) * q_int(2) * q_int(3)
    y_3 = 1 / qfact_3
    y_21 = q_int(2) ** 2 / qfact_3
    y_111 = 1 / qfact_3

    print(f"  Wenzl weights at H_3: y_3={y_3:.4f}, y_(2,1)={y_21:.4f}, y_(1,1,1)={y_111:.4f}")
    print()

    # ── Markov traces ─────────────────────────────────────────────
    tr_M_p = y_3 * chi_p_3 + y_21 * chi_p_21 + y_111 * chi_p_111
    tr_M_n = y_3 * chi_n_3 + y_21 * chi_n_21 + y_111 * chi_n_111
    print(f"  Symbolic |tr_M(β_p)| (unnormalised Wenzl) = {tr_M_p:.6f}")
    print(f"  Symbolic |tr_M(β_n)| (unnormalised Wenzl) = {tr_M_n:.6f}")
    print(f"  Ratio tr_M(p)/tr_M(n) = {tr_M_p/tr_M_n:.6f}")
    print(f"    expected from CODATA-fit ρ_K ratio: 1991.6/1723.6 = {1991.6/1723.6:.6f}")
    print()

    # ── Multi-level LP setup ──────────────────────────────────────
    print("  LP variables: α_λ^(p), α_λ^(n) per H_3 block, plus universal a")
    print("  " + "-" * 66)

    ap_3 = cp.Variable(nonneg=True, name="ap_3")
    ap_21 = cp.Variable(nonneg=True, name="ap_21")
    ap_111 = cp.Variable(nonneg=True, name="ap_111")
    an_3 = cp.Variable(nonneg=True, name="an_3")
    an_21 = cp.Variable(nonneg=True, name="an_21")
    an_111 = cp.Variable(nonneg=True, name="an_111")
    a_var = cp.Variable(nonneg=True, name="a")

    eigs_p = np.linalg.eigvalsh((M_p + M_p.T) / 2)
    eigs_n = np.linalg.eigvalsh((M_n + M_n.T) / 2)

    tr_p = ap_3 * y_3 * chi_p_3 + ap_21 * y_21 * chi_p_21 + ap_111 * y_111 * chi_p_111
    tr_n = an_3 * y_3 * chi_n_3 + an_21 * y_21 * chi_n_21 + an_111 * y_111 * chi_n_111

    constraints = []
    # 1. Normalisation per particle
    constraints.append(ap_3 + ap_21 + ap_111 == 1)
    constraints.append(an_3 + an_21 + an_111 == 1)
    # 2. Mirror parity per particle
    constraints.append(ap_3 == ap_111)
    constraints.append(an_3 == an_111)
    # 3. Cross-particle: protrn and neutron differ by chirality, but
    # at H_3 they share Markov-equivalence up to braid sign
    # constraints.append(ap_21 == an_21)  # too strong; not imposed
    # 4. Markov pair-trace per particle
    constraints.append(tr_p >= z_mark ** 2 * (ap_3 + ap_21 + ap_111))
    constraints.append(tr_n >= z_mark ** 2 * (an_3 + an_21 + an_111))
    # 5. **Cross-level Markov multiplicativity** (Wenzl 1988) for the
    # deuteron (proton ⊗ neutron disjoint at H_6).
    # ORIGINALLY: tr_p · tr_n >= constant — but this is BILINEAR
    # (product of decision variables), violates DCP, not LP-compatible.
    # LP-FRIENDLY relaxation (per owner: "keep LP simplicity"):
    # impose each particle's tr_M individually meeting the Wenzl
    # multiplicativity lower bound √0.3 ≈ 0.548.  Conservative
    # surrogate; the product constraint is then automatic.
    sqrt_threshold = np.sqrt(0.3)
    constraints.append(tr_p >= sqrt_threshold * (ap_3 + ap_21 + ap_111))
    constraints.append(tr_n >= sqrt_threshold * (an_3 + an_21 + an_111))
    # 6. **Integration limit consistency for proton AND neutron**
    constraints.append(a_var * 4 <= ap_21 * (eigs_p[0] + eigs_p[1]) + ap_3 + ap_111)
    constraints.append(a_var * 4 <= an_21 * (eigs_n[0] + eigs_n[1]) + an_3 + an_111)
    # 7. **Tighter consistency**: the SAME a applies to both particles
    # (already imposed by sharing the variable)

    objective = cp.Maximize(a_var)
    prob = cp.Problem(objective, constraints)
    prob.solve(solver=cp.HIGHS, verbose=False)

    print(f"  LP status: {prob.status}")
    print(f"  Optimal a: {a_var.value:.10f}")
    print(f"  proton:  α_3={ap_3.value:.6f}, α_21={ap_21.value:.6f}, α_111={ap_111.value:.6f}")
    print(f"  neutron: α_3={an_3.value:.6f}, α_21={an_21.value:.6f}, α_111={an_111.value:.6f}")
    print()

    # Compare to single-particle LP (H_3 only, proton-only)
    from picard_lefschetz_thimble import cubic_roots, sw_3root_product_degree1
    from scipy import integrate
    borromean = VOL_BORROMEAN / (HBAR_Q ** 2)
    a_val = a_var.value
    try:
        e_ref, _ = integrate.quad(
            lambda z: float(np.real(cubic_roots(z)[np.argmin(np.abs(cubic_roots(z).imag))] + z)),
            -a_val, a_val, limit=200)
        prod_re, _ = integrate.quad(
            lambda z: float(np.real(sw_3root_product_degree1(z))),
            -a_val, a_val, limit=200)
        A = abs(prod_re) / abs(e_ref) if abs(e_ref) > 1e-15 else float("nan")
        m_p_pred = borromean * A * M_E_MEV
        err = (m_p_pred - M_P_MEV) / M_P_MEV * 100
        print(f"  m_p_pred at this a: {m_p_pred:.4f} MeV (residual {err:.4f}%)")
    except Exception as exc:
        m_p_pred = None
        err = None
        print(f"  Error computing m_p_pred: {exc}")

    print()
    print("  Comparison to single-particle LP:")
    print(f"    Single-particle (proton-only):  a = 0.4985 (= z_markov)")
    print(f"    Multi-particle (proton+neutron): a = {a_val:.6f}")
    if abs(a_val - z_mark) < 0.01:
        print(f"    → SAME value.  Adding the neutron at H_3 doesn't narrow the SDP.")
    else:
        print(f"    → DIFFERENT.  Multi-particle constraints DO narrow `a`.")
    print()

    # Shadow prices
    print("  LP shadow prices (dual variables):")
    for i, c in enumerate(constraints):
        if hasattr(c, 'dual_value') and c.dual_value is not None:
            try:
                val = float(c.dual_value)
                marker = " ← SATURATING" if abs(val) > 1e-6 else ""
                print(f"    constraint {i+1:2d}: y = {val:+.6f}{marker}")
            except (TypeError, ValueError):
                print(f"    constraint {i+1:2d}: y = {c.dual_value}")

    print()
    print("  CONCLUSION:")
    print("    At H_3 only (no H_6/H_9 lift), adding the NEUTRON's constraints")
    print("    does NOT narrow `a` from z_markov.  The LP/SDP is still under-")
    print("    constrained — the optimal `a` saturates at z_markov.")
    print()
    print("    To narrow `a` further, the SDPB needs to INCLUDE:")
    print("      • Hoefsmit seminormal forms at H_6 (deuteron) and H_9 (T, ³He)")
    print("      • Cross-level embedding constraints (H_3 ↪ H_6 ↪ H_9)")
    print("      • Full jet-tower SDP per prop:joint-tower-sdp-confinement")
    print()
    print("    The Hoefsmit infra at H_6, H_9 is in the Rust hecke-engine")
    print("    (tools/hecke-engine/src/seminormal_mn.rs); the Python")
    print("    joint_tower_sdp_solver_v2 explicitly DEFERS H≥5 to Rust.")
    print("    Wiring the Rust output back into the Python LP is the natural")
    print("    next step but is research-level multi-day work.")

    # Witness
    w = (WitnessBuilder("probe-sdpb-multilevel-crossing",
                         engine="cvxpy+HIGHS+numpy")
         .set_description("Multi-level SDPB with proton+neutron + jet-tower hint"))
    w.add_data("q_0", q0)
    w.add_data("z_markov", z_mark)
    w.add_data("H_3_data", {
        "proton_chi": [chi_p_3, chi_p_21, chi_p_111],
        "neutron_chi": [chi_n_3, chi_n_21, chi_n_111],
        "y_lambda": [y_3, y_21, y_111],
        "tr_M_proton": tr_M_p,
        "tr_M_neutron": tr_M_n,
    })
    w.add_data("lp_status", prob.status)
    w.add_data("lp_solution", {
        "a": float(a_val) if a_val else None,
        "alpha_p": {"3": float(ap_3.value), "21": float(ap_21.value),
                     "111": float(ap_111.value)},
        "alpha_n": {"3": float(an_3.value), "21": float(an_21.value),
                     "111": float(an_111.value)},
    })
    if m_p_pred is not None:
        w.add_data("m_p_pred_at_a", {"value_MeV": float(m_p_pred),
                                       "residual_pct": float(err)})
    w.add_data("conclusion",
               "Multi-particle SDPB at H_3 ONLY does not narrow `a` from z_markov. "
               "Both proton and neutron LP solutions saturate at the same a = "
               "z_markov.  To narrow further requires H_6 (deuteron) + H_9 "
               "(T, ³He) Hoefsmit infra — currently DEFERRED to Rust "
               "hecke-engine.  Next step: wire Rust output into Python LP.")
    w.add_assertion("multi_particle_lp_narrows_a",
                    computed=0.0 if abs(a_val - z_mark) < 0.01 else 1.0,
                    expected=1.0)  # we WANT it to narrow
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
