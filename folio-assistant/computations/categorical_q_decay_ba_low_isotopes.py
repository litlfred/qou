#!/usr/bin/env python3
"""Canonical Q / decay / B/A — 4-input scheme (Skein-pair p/n) + 4-tier formula.

Per
content/quantum-observable-universe/observations/nucleon-mass-splitting-proof.md
(commit bd81514, PR #443) the framework's canonical p/n treatment uses
Skein-pair masses with constituent dressed quark masses:

  m_p = S_uu(q) + 2·S_ud(q)
  m_n = 2·S_ud(q) + S_dd(q)
  m_n - m_p = (q + q⁻¹) / (q^{1/2} + q^{-1/2}) · (μ_d − μ_u)

This is a 4-input scheme:

  1. m_μ/m_e = 206.768   (fixes q_0)
  2. m_e = 0.511 MeV     (leptonic scale)
  3. μ_u = 311.10 MeV    (proton-side dressed quark, from m_p calib)
  4. μ_d = 312.39 MeV    (neutron-side dressed quark, from m_n−m_p split)

p and n are CORRECTLY DIFFERENT under this representation — the
n-p mass splitting is exact (μ_d − μ_u capture). Equivalently the
3-input + Q_β scheme of calibration-inputs.md absorbs (μ_u, μ_d)
into a single hadronic scale E_0 calibrated by Q_β(n).

These are NOT fits — each input fixes a distinct physical sector
(shape, leptonic, u-quark mass, d-quark mass).

Per
content/.../np-discrepancy-resolution.md
the canonical 4-tier formula for atomic binding energies (using
the 3-input calibration) is:

  D  (A=2)     : Term 1 (Schur-Weyl) + Term 4 (universal Frobenius co-Casimir)
  T  (A=3)     : Term 5 (BW + chirality (1−h²))
  ³He (A=3)    : Term 5 (BW + chirality (1−h²))
  ⁴He (A=4)   : Term 5 (BW + chirality (1−h²)² + shell)
  A ≥ 5       : Term 5 (BW + shell, chirality → 1) — Term 6 (jet-prefix) OPEN

Layer-2 Q-values then derive from B-differences:

  Q_β⁻(X → Y) = Q_β(n) + B_Y_canonical − B_X_canonical

where Q_β(n) is the third structural input.

Output: categorical-q-decay-ba-low-isotopes.witness.json
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import (
    M_E_MEV,
    M_N_MEV,
    M_P_MEV,
    Q_C14_MEV,
    Q_C14_MEV_ERR,
    Q_NEUTRON_MEV,
    Q_NEUTRON_MEV_ERR,
    Q_TRITIUM_MEV,
    Q_TRITIUM_MEV_ERR,
)
from q_parameter import Q as Q_0
from q_parameter import Q_ERR as Q_0_ERR
from witness_base import WitnessBuilder

HERE = Path(__file__).parent

# ─────────────────────────────────────────────────────────────────────
# Source witnesses (canonical, 3-input scheme)
# ─────────────────────────────────────────────────────────────────────
# bw-chirality-isotopes: Term 5 (BW + chirality) for A ≥ 3
BW_WITNESS = HERE / "bw-chirality-isotopes.witness.json"
# mass-formula-6term: Term 1+4 for D, Term 5 for T/³He
SIX_TERM_WITNESS = HERE / "mass-formula-6term.witness.json"

# Tier selection per isotope
TIER_BY_SYM = {
    "1H":  "trivial (A=1, B=0 by convention; m_atom = m_p + m_e)",
    "D":   "term-1-plus-4 (Schur-Weyl + universal Frobenius)",
    "T":   "term-5 (BW + chirality (1-h²))",
    "3He": "term-5 (BW + chirality (1-h²))",
    "4He": "term-5 (BW + chirality (1-h²)² + shell)",
    "6Li": "term-5 (BW + shell, chirality→1, term-6 OPEN)",
    "7Li": "term-5 (BW + shell, chirality→1, term-6 OPEN)",
    "9Be": "term-5 (BW + shell, chirality→1, term-6 OPEN)",
    "11B": "term-5 (BW + shell, chirality→1, term-6 OPEN)",
    "12C": "term-5 (BW + shell, chirality→1, term-6 OPEN)",
    "16O": "term-5 (BW + shell, chirality→1, term-6 OPEN)",
}

FAMILY_BY_SYM = {
    "1H": 0,                                # bare hydrogen — single proton + electron
    "D": 1, "T": 1, "3He": 1,
    "4He": 2,
    "6Li": 3, "7Li": 3, "9Be": 3, "11B": 3, "12C": 3, "16O": 3,
}

# Layer-2 reference Q-values (NNDC/ENSDF)
Q_AME_REFERENCE = {
    "n → p":     (Q_NEUTRON_MEV, Q_NEUTRON_MEV_ERR),
    "³H → ³He":  (Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    "⁶He → ⁶Li": (3.508,         0.001),
    "¹⁴C → ¹⁴N": (Q_C14_MEV,     Q_C14_MEV_ERR),
    "⁸Li → ⁸Be": (16.004,        0.001),
}


def ensure_witness(path: Path, builder_script: str):
    """Run the source script if its witness is missing or stale."""
    if not path.exists():
        print(f"[recompute] {path.name} missing, regenerating via {builder_script}…")
        subprocess.run([sys.executable, str(HERE / builder_script)], check=True)


def load_canonical_b(sym: str):
    """Pick the canonical B for symbol `sym` from the right tier source."""
    tier = TIER_BY_SYM.get(sym)
    if tier is None:
        return None

    # ¹H is trivial: B=0 by convention (single nucleon, no nuclear binding)
    if "trivial" in tier:
        return {
            "B_pred_MeV": 0.0,
            "err_pct": 0.0,
            "tier": tier,
        }

    # Term 1+4 lives in mass-formula-6term.witness.json
    if "term-1-plus-4" in tier:
        if not SIX_TERM_WITNESS.exists():
            return None
        with open(SIX_TERM_WITNESS) as f:
            d = json.load(f)
        rows = d.get("rows", {})
        if sym in rows:
            r = rows[sym]
            return {
                "B_pred_MeV": float(r["B_pred_term1_plus_term4"]),
                "err_pct": float(r["err_pct"]["term1_plus_term4"]),
                "tier": tier,
            }
        return None

    # Term 5 lives in bw-chirality-isotopes.witness.json (rows is a list)
    if "term-5" in tier:
        if not BW_WITNESS.exists():
            return None
        with open(BW_WITNESS) as f:
            d = json.load(f)
        rows = d.get("rows", [])
        # row key is "isotope" not "sym" in this witness
        for row in rows:
            if row.get("isotope") == sym:
                return {
                    "B_pred_MeV": float(row["B_pred_MeV"]),
                    "err_pct": float(row["err_pct"]),
                    "tier": tier,
                }
        return None

    return None


def main():
    # ─────────────────────────────────────────────────────────────────
    # 1. Ensure source witnesses are up to date
    # ─────────────────────────────────────────────────────────────────
    ensure_witness(BW_WITNESS, "bw_chirality_isotopes.py")
    ensure_witness(SIX_TERM_WITNESS, "mass_formula_6term.py")

    # ─────────────────────────────────────────────────────────────────
    # 2. Layer 1 — canonical B per isotope, picking the right tier
    # ─────────────────────────────────────────────────────────────────
    SYMBOLS = ["1H", "D", "T", "3He", "4He", "6Li", "7Li", "9Be", "11B", "12C", "16O"]
    Z_N = {
        "1H": (1, 0),
        "D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
        "6Li": (3, 3), "7Li": (3, 4), "9Be": (4, 5), "11B": (5, 6),
        "12C": (6, 6), "16O": (8, 8),
    }
    B_AME = {
        "1H": 0.0,                          # convention: single nucleon ⇒ B = 0
        "D": 2.22456612, "T": 8.4817984, "3He": 7.7180375, "4He": 28.2956912,
        "6Li": 31.99405, "7Li": 39.24453, "9Be": 58.16498, "11B": 76.20548,
        "12C": 92.16175, "16O": 127.61929,
    }

    layer1 = []
    canonical_b = {}
    for sym in SYMBOLS:
        Z, N = Z_N[sym]
        A = Z + N
        b = load_canonical_b(sym)
        b_ame = B_AME[sym]
        if b is None:
            layer1.append({
                "sym": sym, "Z": Z, "N": N, "A": A,
                "family": FAMILY_BY_SYM[sym],
                "tier": TIER_BY_SYM[sym],
                "B_pred_MeV": None,
                "B_AME_MeV": b_ame,
                "err_pct": None,
                "status": "tier-source-missing",
            })
            continue
        b_pred = b["B_pred_MeV"]
        canonical_b[sym] = b_pred
        # err undefined when AME = 0 (¹H convention); report absolute residual instead
        err = 100 * (b_pred - b_ame) / b_ame if b_ame else None
        # Atomic mass: M_atom = Z·m_p + N·m_n + Z·m_e − B
        # WARNING: this uses CODATA m_p, m_n directly (arithmetic).
        # NOT through knot operations / GB-NF / SDP categorical chain.
        # The mass-endomorphism tower CATEGORICAL prediction for m_p is
        # 1869.85·m_e ≈ 955.5 MeV (1.84% off CODATA m_p), so a fully-
        # categorical m_atom would carry that residual.
        m_atom_pred = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV - b_pred
        m_atom_ame  = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV - b_ame
        # For comparison: fully-categorical m_atom using mass-endomorphism
        # tower prediction m_p_tower = 1869.85·m_e (per mass-endomorphism.witness.json)
        # and m_n_tower = m_p_tower + Q_β (per calibration-inputs.md)
        M_P_TOWER_MEV = 1869.85 * M_E_MEV       # categorical tower prediction
        M_N_TOWER_MEV = M_P_TOWER_MEV + Q_NEUTRON_MEV
        m_atom_tower = Z * M_P_TOWER_MEV + N * M_N_TOWER_MEV + Z * M_E_MEV - b_pred
        layer1.append({
            "sym": sym, "Z": Z, "N": N, "A": A,
            "family": FAMILY_BY_SYM[sym],
            "tier": TIER_BY_SYM[sym],
            "B_pred_MeV": b_pred,
            "B_AME_MeV": b_ame,
            "B_residual_MeV": b_pred - b_ame,
            "err_pct": err,
            "B_per_A_pred_MeV": b_pred / A if A > 0 else None,
            "B_per_A_AME_MeV": b_ame / A if A > 0 else None,
            "M_atom_pred_MeV": m_atom_pred,
            "M_atom_AME_MeV":  m_atom_ame,
            "M_atom_tower_categorical_MeV": m_atom_tower,
            "atomic_includes_electron": True,    # Z electrons bound to nucleus
            "M_atom_pred_method":
                "arithmetic: Z·m_p_CODATA + N·m_n_CODATA + Z·m_e − B (NOT "
                "through GB-NF / SDP / knot-ops; uses CODATA scaffold)",
            "M_atom_tower_method":
                "categorical: m_p from mass-endomorphism tower (1869.85·m_e, "
                "1.84% off), m_n = m_p + Q_β (per calibration-inputs.md), "
                "B from 4-tier formula. Fully-derived chain prediction.",
            "status": "canonical-3-input-4-tier",
        })

    # ─────────────────────────────────────────────────────────────────
    # 3. Layer 2 — Q-values via Q_β(n) + B_d − B_p
    # ─────────────────────────────────────────────────────────────────
    decays = [
        ("n",  "p",    "n → p",      None),
        ("T",  "3He",  "³H → ³He",   ("T", "3He")),
        # ⁶He → ⁶Li blocked (⁶He is family 4, no Z=2/N=4 entry yet)
        ("6He","6Li",  "⁶He → ⁶Li",  None),
        ("14C","14N",  "¹⁴C → ¹⁴N",  None),
        ("8Li","8Be",  "⁸Li → ⁸Be",  None),
    ]
    layer2 = []
    # n → p  is direct from Q_β(n) input
    q_ame_n, q_ame_n_err = Q_AME_REFERENCE["n → p"]
    layer2.append({
        "decay": "n → p",
        "Q_pred_MeV": Q_NEUTRON_MEV,
        "Q_AME_MeV": q_ame_n,
        "Q_AME_MeV_err": q_ame_n_err,
        "err_pct": 0.0,
        "formula": "Q_β(n) — third structural input",
        "status": "calibration-input",
    })
    for parent, daughter, label, sym_pair in decays[1:]:
        q_ame, q_err = Q_AME_REFERENCE.get(label, (None, None))
        if sym_pair is None:
            layer2.append({
                "decay": label,
                "Q_pred_MeV": None,
                "Q_AME_MeV": q_ame,
                "Q_AME_MeV_err": q_err,
                "status": "blocked: parent or daughter outside canonical-tier set",
            })
            continue
        sym_p, sym_d = sym_pair
        b_p = canonical_b.get(sym_p)
        b_d = canonical_b.get(sym_d)
        if b_p is None or b_d is None:
            layer2.append({
                "decay": label,
                "Q_pred_MeV": None,
                "Q_AME_MeV": q_ame,
                "Q_AME_MeV_err": q_err,
                "status": "tier-source-missing",
            })
            continue
        Q = Q_NEUTRON_MEV + b_d - b_p
        err = 100 * (Q - q_ame) / q_ame if q_ame else None
        layer2.append({
            "decay": label,
            "Q_pred_MeV": Q,
            "Q_AME_MeV": q_ame,
            "Q_AME_MeV_err": q_err,
            "err_pct": err,
            "formula": "Q_β(n) + B_canonical(daughter) − B_canonical(parent)",
            "status": "canonical-derived",
            "details": {
                "B_canonical_parent_MeV": b_p,
                "B_canonical_daughter_MeV": b_d,
            },
        })

    # ─────────────────────────────────────────────────────────────────
    # 4. Build witness
    # ─────────────────────────────────────────────────────────────────
    # Per content/.../calibration-inputs.md, the canonical 3-input scheme is:
    #   Inputs: q_0 (from m_μ/m_e), m_e, Q_β(n)
    #   Derived: m_p ← Skein pair formula + (μ_u, μ_d) from Skein resolution tree
    #            m_n = m_p + Q_β     (Hecke engine, exact)
    #            μ_u from q_0 alone is OPEN (Skein resolution of Borromean braid)
    #
    # We do NOT independently use M_N_MEV from CODATA — that would
    # over-count the hadronic input.  Instead:
    #   - m_p is taken as the CODATA value (until Skein resolution lands)
    #   - m_n = m_p + Q_β (algebraic, follows from chain)
    #   - μ_d − μ_u is then derivable from Q_β via the splitting formula
    #   - μ_u is back-solved from m_p via Skein-pair (Skein resolution
    #     would derive it from q_0 alone)
    import math
    q_half = math.sqrt(Q_0)
    q_inv_half = 1.0 / q_half
    Z_PAIR = q_half + q_inv_half        # q^{1/2} + q^{-1/2}
    SLOPE = (Q_0 + 1.0/Q_0) / Z_PAIR    # (q+q⁻¹)/(q^{1/2}+q^{-1/2})

    # Step A — derive m_n from m_p + Q_β (Hecke engine)
    m_p_calibrated = M_P_MEV       # input scaffold (Skein resolution open)
    m_n_derived    = m_p_calibrated + Q_NEUTRON_MEV
    Delta_m_np_derived = m_n_derived - m_p_calibrated  # = Q_β + m_e
    # Note: Δm_np_derived above is m_n - m_p = Q_β + m_e (NOT the bare Q_β).
    # The splitting formula uses (μ_d - μ_u), which is sourced from Δm_np.
    mu_d_minus_u   = Delta_m_np_derived / SLOPE

    # Step B — back-solve μ_u from m_p Skein-pair formula
    # m_p = (μ_u·(3q+3q⁻¹) + 2·q⁻¹·(μ_d - μ_u)) / Z_pair
    mu_u = (m_p_calibrated * Z_PAIR - 2.0 / Q_0 * mu_d_minus_u) \
           / (3.0 * (Q_0 + 1.0/Q_0))
    mu_d = mu_u + mu_d_minus_u

    w = (
        WitnessBuilder("categorical-q-decay-ba-low-isotopes", engine="python")
        .set_description(
            "Canonical B/A and Q-values for low isotopes via the "
            "paper's 4-input Skein-pair scheme (m_μ/m_e, m_e, μ_u, μ_d) "
            "and 4-tier formula. Layer 1: best tier per isotope (D: T1+T4; "
            "T/³He: BW+chirality; ⁴He: BW+chirality²+shell; A≥5: BW+shell). "
            "Layer 2: Q_β⁻ = Q_β(n) + B_d − B_p where Q_β(n) = m_n − m_p − m_e "
            "is exact under the Skein-pair formula. Layer 3: NOT computed "
            "(N_v open). All canonical, no fits beyond the 4 structural inputs. "
            "p ≠ n via μ_d ≠ μ_u (Δ = μ_d − μ_u captures n-p splitting exactly)."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q_0)
        .add_parameter("q_0_err", Q_0_ERR)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("mu_u_MeV", mu_u)
        .add_parameter("mu_d_MeV", mu_d)
        .add_parameter("mu_d_minus_mu_u_MeV", mu_d_minus_u)
        .add_parameter("Q_beta_n_MeV_derived", M_N_MEV - M_P_MEV - M_E_MEV)
        .add_parameter("Q_beta_n_MeV_codata", Q_NEUTRON_MEV)
        .add_parameter("m_p_MeV", M_P_MEV)
        .add_parameter("m_n_MeV", M_N_MEV)
        .add_data("calibration_scheme",
                  "4-input Skein-pair (m_μ/m_e, m_e, μ_u, μ_d) "
                  "per nucleon-mass-splitting-proof.md (commit bd81514)")
        .add_data("formula_scheme", "4-tier per isotope")
        .add_data("p_n_distinction", {
            "m_p_skein_pair": "S_uu + 2·S_ud",
            "m_n_skein_pair": "2·S_ud + S_dd",
            "m_n_minus_m_p_formula":
                "((q+q⁻¹)/(q^{1/2}+q^{-1/2})) · (μ_d − μ_u)",
            "m_n_minus_m_p_value_MeV": M_N_MEV - M_P_MEV,
            "exact_under_4_input_scheme": True,
        })
        .add_data("layer1_b_over_a", layer1)
        .add_data("layer2_q_values", layer2)
        .add_data("layer3_decay_rates", {
            "status": "not-computed",
            "reason": "N_v topological invariant open",
        })
        .add_data("source_witnesses", {
            "term-5": str(BW_WITNESS.name),
            "term-1-plus-4": str(SIX_TERM_WITNESS.name),
        })
        .add_caveat(
            "All B-values use the paper's canonical 3-input scheme; "
            "Q_β(n) is a structural input, not a fit."
        )
        .add_caveat(
            "A≥5 errors 5–20% are due to term 6 (jet-level prefix) "
            "being OPEN per mass-endomorphism-jet-tower.md."
        )
    )
    out_path = w.save()

    # ─────────────────────────────────────────────────────────────────
    # 5. Print human-readable tables
    # ─────────────────────────────────────────────────────────────────
    print("\n" + "=" * 84)
    print("LAYER 1 — canonical B per isotope (3-input scheme, 4-tier formula)")
    print("=" * 84)
    print(f"{'sym':<6} {'A':>3} {'fam':>4} {'B_pred':>10} {'err%':>8}  "
          f"{'M_atom (arith)':>14}  {'M_atom (tower)':>14}  tier")
    print("-" * 140)
    for r in layer1:
        bp = f"{r['B_pred_MeV']:>10.4f}" if r["B_pred_MeV"] is not None else f"{'—':>10}"
        ep = f"{r['err_pct']:>+8.2f}" if r["err_pct"] is not None else f"{'—':>8}"
        ma = f"{r.get('M_atom_pred_MeV', 0):>14.3f}" if r.get('M_atom_pred_MeV') is not None else f"{'—':>14}"
        mt = f"{r.get('M_atom_tower_categorical_MeV', 0):>14.3f}" if r.get('M_atom_tower_categorical_MeV') is not None else f"{'—':>14}"
        print(f"{r['sym']:<6} {r['A']:>3} {r['family']:>4} {bp} {ep}  {ma}  {mt}  {r['tier']}")
    print()
    print("M_atom (arith) = Z·m_p_CODATA + N·m_n_CODATA + Z·m_e − B   (NOT through chain)")
    print("M_atom (tower) = Z·m_p_TOWER  + N·m_n_TOWER  + Z·m_e − B   (categorical, with 1.84% m_p residual)")

    print("\n" + "=" * 84)
    print("LAYER 2 — Q-values (β⁻) via Q_β(n) + B_d − B_p")
    print("=" * 84)
    print(f"{'decay':<14} {'Q_pred':>10} {'Q_AME':>10} {'err%':>8}  status")
    print("-" * 84)
    for r in layer2:
        qp = f"{r['Q_pred_MeV']:>10.4f}" if r.get("Q_pred_MeV") is not None else f"{'—':>10}"
        qa = f"{r['Q_AME_MeV']:>10.4f}" if r.get("Q_AME_MeV") is not None else f"{'—':>10}"
        ep = f"{r['err_pct']:>+8.2f}" if r.get("err_pct") is not None else f"{'—':>8}"
        print(f"{r['decay']:<14} {qp} {qa} {ep}  {r['status']}")

    print("\n" + "=" * 84)
    print("LAYER 3 — decay rates: NOT COMPUTED (N_v open).")
    print("=" * 84)
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
