#!/usr/bin/env python3
"""Categorical Q / decay / B/A — option B (algebraic, pre-Archimedean only).

Per directive: only canonical, no fits. Option B: every B-value comes
from the algebraic Wenzl-Markov trace at q_0,

    B(𝔥) = m_e · ρ · Σ_λ y_λ(q_0) · χ_λ(T_w)

with χ_λ from the joint-tower SDP Wedderburn blocks and y_λ from
y-lambda-wenzl-witness.json. **Vol_hyp(K) is post-Archimedean and is
NOT used.** Therefore mass-table-ppb (which uses Vol_hyp + magic-A
8G + α-cluster Vol(7²_1)) is reclassified as fitted.

Layer 1 (B/A): only family-1 atoms have algebraic predictions today
  (electron, deuteron-2H, tritium-3H, helium3-3He from joint-tower-sdp-rust).
  Family 2, 3, 4 are open in the algebraic regime.

Layer 2 (Q-values): Q_β⁻ = Q_n→p_alg + B_d_alg − B_p_alg, where
  Q_n→p_alg comes from m_n_alg − m_p_alg − m_e_alg via the algebraic
  chain. **Currently zero** because the SDP gives T_w(proton) ≈
  T_w(neutron) ≈ identity, so m_p_alg = m_n_alg = m_e algebraically.
  This is the central open gap of option B.

Layer 3 (decay rates): NOT computed. Bottleneck N_v is open.

Output: categorical-q-decay-ba-low-isotopes.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from q_parameter import Q as Q_0
from witness_base import WitnessBuilder

BYPASS_WITNESS = Path(__file__).parent / "categorical-bypass-volmatch-demo.witness.json"
SDP_WITNESS    = Path(__file__).parent / "joint-tower-sdp-rust.witness.json"
Y_LAMBDA_WITNESS = Path(__file__).parent / "y-lambda-wenzl-witness.json"
MASS_TABLE_PPB   = Path(__file__).parent / "mass-table-ppb.witness.json"

# Algebraic-only family classification (option B).
# Family 1 (D, T, ³He): algebraic via Wenzl-Markov on SDP-derived T_w. **OK.**
# Family 2 (⁴He) magic-A: uses 8G = Vol(Borromean) — POST-ARCHIMEDEAN. fitted.
# Family 3 (⁸Be–⁴⁰Ca) α-cluster: uses 8G + Vol(7²_1) — POST-ARCHIMEDEAN. fitted.
# Family 4 (⁶Li, ⁷Li, ...): no T_w. open.
FAMILY_BY_SYM = {
    "2H": 1, "3H": 1, "3He": 1,
    "4He": 2,
    "8Be": 3, "12C": 3, "16O": 3, "20Ne": 3, "24Mg": 3, "40Ca": 3,
}
LAYER1_STATUS_OPTION_B = {
    1: "algebraic-wenzl-markov-on-sdp-T_w",
    2: "fitted-magic-A-uses-Vol-Borromean",
    3: "fitted-alpha-cluster-uses-Vol-Borromean-and-Vol-7sq1",
    4: "open",
}

# Layer-2 reference Q-values (NNDC/ENSDF — comparison only)
from experimental_constants import (
    Q_C14_MEV,
    Q_C14_MEV_ERR,
    Q_NEUTRON_MEV,
    Q_NEUTRON_MEV_ERR,
    Q_TRITIUM_MEV,
    Q_TRITIUM_MEV_ERR,
)
Q_AME_REFERENCE = {
    "n → p":     (Q_NEUTRON_MEV, Q_NEUTRON_MEV_ERR),
    "³H → ³He":  (Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    "⁶He → ⁶Li": (3.508,         0.001),
    "¹⁴C → ¹⁴N": (Q_C14_MEV,     Q_C14_MEV_ERR),
    "⁸Li → ⁸Be": (16.004,        0.001),
}

DECAY_PAIRS = [
    ("n",   "p",   "n → p"),
    ("3H",  "3He", "³H → ³He"),
    ("6He", "6Li", "⁶He → ⁶Li"),   # blocked: family 4
    ("14C", "14N", "¹⁴C → ¹⁴N"),   # blocked: family 4
    ("8Li", "8Be", "⁸Li → ⁸Be"),   # blocked: family 3-fitted + family 4
]


def load_algebraic_b():
    """Pull B(𝔥) algebraic predictions from the bypass-demo witness."""
    with open(BYPASS_WITNESS) as f:
        d = json.load(f)
    out = {}
    for r in d["data"]["rows"]:
        out[r["sym"]] = {
            "n_native":   r["n_native"],
            "rho":        r["rho"],
            "tr_M":       r["tr_M_direct"],
            "B_pred_MeV": r["B_pred_direct_MeV"],
            "B_AME_MeV":  r["B_AME_MeV"],
            "knot_post_archimedean_label": r["knot"],
        }
    return out


def load_sdp_nucleons():
    """Pull algebraic nucleon predictions: m_p_alg, m_n_alg from the
    joint-tower SDP at H_3."""
    with open(SDP_WITNESS) as f:
        d = json.load(f)
    with open(Y_LAMBDA_WITNESS) as f:
        yd = json.load(f)
    y_n3 = {tuple(w["partition"]): float(w["y_lambda_numeric"])
            for w in yd["tables_by_n"]["3"]["weights"]}
    out = {}
    for e in d["per_atom_certificates"]:
        if e["name"] not in {"proton", "neutron"}:
            continue
        wb = e.get("wedderburn_blocks", [])
        tr_M = 0.0
        for block in wb:
            partition = tuple(block["partition"])
            chi = sum(block["matrix_at_q_0_sym_eigvals"])
            y = y_n3.get(partition)
            if y is not None:
                tr_M += y * chi
        out[e["name"]] = {
            "rho":   e["rho_factor"],
            "tr_M":  tr_M,
            "M_alg": e["rho_factor"] * tr_M,         # M(p) = ρ · tr_M, in m_e units
            "B_alg_MeV": M_E_MEV * e["rho_factor"] * tr_M,
        }
    return out


def main():
    b_alg = load_algebraic_b()
    nucleons = load_sdp_nucleons()

    # ─────────────────────────────────────────────────────────────────
    # Algebraic Q_n→p
    # ─────────────────────────────────────────────────────────────────
    m_p_alg = nucleons["proton"]["B_alg_MeV"]    # = m_e · ρ_p · tr_M(T_w(p))
    m_n_alg = nucleons["neutron"]["B_alg_MeV"]   # same formula for neutron
    Q_N_TO_P_ALG = m_n_alg - m_p_alg - M_E_MEV   # algebraic m_n − m_p − m_e

    # ─────────────────────────────────────────────────────────────────
    # Layer 1: B/A table — algebraic only
    # ─────────────────────────────────────────────────────────────────
    layer1_rows = []
    for sym in ("2H", "3H", "3He"):
        b = b_alg.get(sym)
        if b is None:
            continue
        Z = {"2H": 1, "3H": 1, "3He": 2}[sym]
        N = {"2H": 1, "3H": 2, "3He": 1}[sym]
        A = Z + N
        layer1_rows.append({
            "sym": sym, "Z": Z, "N": N, "A": A,
            "family": 1,
            "B_alg_MeV":   b["B_pred_MeV"],
            "tr_M_alg":    b["tr_M"],
            "rho":         b["rho"],
            "B_AME_MeV":   b["B_AME_MeV"],
            "B_per_A_alg_MeV": b["B_pred_MeV"] / A,
            "ratio_alg_to_AME": b["B_pred_MeV"] / b["B_AME_MeV"]
                              if b["B_AME_MeV"] else None,
            "categorical_status": LAYER1_STATUS_OPTION_B[1],
        })
    # Family 2, 3 atoms: explicitly mark as fitted (no algebraic B today)
    for sym, fam in FAMILY_BY_SYM.items():
        if fam == 1:
            continue
        layer1_rows.append({
            "sym": sym,
            "family": fam,
            "B_alg_MeV": None,
            "B_AME_MeV": None,
            "categorical_status": LAYER1_STATUS_OPTION_B[fam],
            "note": ("mass-table-ppb has a value but it uses Vol_hyp; "
                     "fitted under option B"),
        })

    # ─────────────────────────────────────────────────────────────────
    # Layer 2: Q-values — algebraic only
    # ─────────────────────────────────────────────────────────────────
    layer2_rows = []
    q_ame_n, q_ame_n_err = Q_AME_REFERENCE["n → p"]
    layer2_rows.append({
        "decay": "n → p",
        "Q_alg_MeV": Q_N_TO_P_ALG,
        "Q_AME_MeV": q_ame_n,
        "Q_AME_MeV_err": q_ame_n_err,
        "ratio_alg_to_AME": Q_N_TO_P_ALG / q_ame_n if q_ame_n else None,
        "formula": "Q_n→p = m_n_alg − m_p_alg − m_e",
        "categorical_status": (
            "algebraic-but-degenerate: m_p_alg = m_n_alg = m_e because "
            "SDP gives T_w(p) ≈ T_w(n) ≈ identity → tr_M ≈ 1. "
            "This is the OPEN GAP of option B."
        ),
        "details": {
            "m_p_alg_MeV": m_p_alg,
            "m_n_alg_MeV": m_n_alg,
            "m_p_AME_MeV": 938.272,
            "m_n_AME_MeV": 939.565,
            "scale_gap_factor": 938.272 / m_p_alg if m_p_alg else None,
        },
    })

    # ³H → ³He: both family 1, both algebraic
    Q_3H_3He_alg = Q_N_TO_P_ALG + b_alg["3He"]["B_pred_MeV"] - b_alg["3H"]["B_pred_MeV"]
    q_ame, q_err = Q_AME_REFERENCE["³H → ³He"]
    layer2_rows.append({
        "decay": "³H → ³He",
        "Q_alg_MeV": Q_3H_3He_alg,
        "Q_AME_MeV": q_ame,
        "Q_AME_MeV_err": q_err,
        "ratio_alg_to_AME": Q_3H_3He_alg / q_ame if q_ame else None,
        "formula": "Q_n→p_alg + B(³He)_alg − B(³H)_alg",
        "categorical_status": "algebraic-family-1",
    })

    # Family-4-blocked decays
    for parent, daughter, label in DECAY_PAIRS[2:]:
        q_ame, q_err = Q_AME_REFERENCE.get(label, (None, None))
        layer2_rows.append({
            "decay": label,
            "Q_alg_MeV": None,
            "Q_AME_MeV": q_ame,
            "Q_AME_MeV_err": q_err,
            "categorical_status": (
                "blocked: parent or daughter outside the algebraic-family-1 set"
            ),
        })

    # ─────────────────────────────────────────────────────────────────
    # Build witness
    # ─────────────────────────────────────────────────────────────────
    w = (
        WitnessBuilder(
            "categorical-q-decay-ba-low-isotopes",
            engine="python",
        )
        .set_description(
            "Algebraic-only B/A and Q-values via option B "
            "(pre-Archimedean Wenzl-Markov, no Vol_hyp). "
            "Layer 1: only family-1 atoms (D, T, ³He) have algebraic "
            "predictions today, all 7×–600× smaller than AME. "
            "Layer 2: Q_n→p_alg ≈ −m_e because m_p_alg = m_n_alg "
            "(SDP T_w degenerate at H_3). Layer 3: NOT computed (N_v open). "
            "Open gap: derive nucleon mass scale within ℚ(q)."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q_0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("m_p_alg_MeV", m_p_alg)
        .add_parameter("m_n_alg_MeV", m_n_alg)
        .add_parameter("Q_n_to_p_alg_MeV", Q_N_TO_P_ALG)
        .add_data("layer1_b_over_a", layer1_rows)
        .add_data("layer2_q_values", layer2_rows)
        .add_data("layer3_decay_rates", {
            "status": "not-computed",
            "reason": "N_v topological invariant open",
        })
        .add_data("vol_hyp_witnesses_now_classified_fitted", [
            "mass-table-ppb.witness.json (uses Vol_hyp(K) for family 1, "
            "Vol(Borromean)=8G for family 2 magic-A, Vol(7²_1) for "
            "family 3 c_αα)",
            "low-isotope-mass-table.witness.json",
            "binding-canonical.witness.json",
            "comprehensive-low-isotope-table-v2.witness.json",
        ])
        .add_data("open_gap_central", (
            "Within ℚ(q), what canonical T_w(proton) would yield "
            "tr_M(T_w(p)) ≈ m_p/m_e ≈ 1836? Currently SDP gives "
            "T_w(p) ≈ identity → tr_M ≈ 1. Resolving this is THE central "
            "research question of option B; without it every algebraic "
            "B/A and Q is off by orders of magnitude from AME."
        ))
        .add_caveat(
            "Algebraic B-values are 7×–600× smaller than AME; Q_n→p_alg "
            "is degenerate. This is what option B (pre-Archimedean only) "
            "currently delivers. The gap is real, not a fit-residual."
        )
        .add_caveat(
            "mass-table-ppb has been retroactively reclassified as "
            "fitted under option B because every formula in it uses "
            "Vol_hyp (family 1: Vol(K); family 2: 8G; family 3: 8G + Vol(7²_1))."
        )
    )
    out_path = w.save()

    # Print human-readable summary
    print("\n" + "=" * 78)
    print("LAYER 1 — algebraic B (option B: pre-Archimedean only)")
    print("=" * 78)
    print(f"{'sym':<6} {'A':>3} {'fam':>4} {'B_alg':>9} {'B_AME':>10} "
          f"{'ratio':>7}  status")
    print("-" * 78)
    for r in layer1_rows:
        b_alg_s = f"{r['B_alg_MeV']:>9.4f}" if r.get('B_alg_MeV') is not None else f"{'—':>9}"
        b_ame_s = f"{r['B_AME_MeV']:>10.4f}" if r.get('B_AME_MeV') is not None else f"{'—':>10}"
        ratio = r.get('ratio_alg_to_AME')
        ratio_s = f"{ratio:>7.4f}" if ratio is not None else f"{'—':>7}"
        a_s = f"{r.get('A','—'):>3}"
        print(f"{r['sym']:<6} {a_s} {r['family']:>4} {b_alg_s} {b_ame_s} "
              f"{ratio_s}  {r['categorical_status']}")

    print("\n" + "=" * 78)
    print("LAYER 2 — algebraic Q (option B)")
    print("=" * 78)
    print(f"{'decay':<14} {'Q_alg':>10} {'Q_AME':>10} {'ratio':>9}  status")
    print("-" * 78)
    for r in layer2_rows:
        q_alg = f"{r['Q_alg_MeV']:>10.4f}" if r.get('Q_alg_MeV') is not None else f"{'—':>10}"
        q_ame = f"{r['Q_AME_MeV']:>10.4f}" if r.get('Q_AME_MeV') is not None else f"{'—':>10}"
        ratio = r.get('ratio_alg_to_AME')
        ratio_s = f"{ratio:>9.4f}" if ratio is not None else f"{'—':>9}"
        print(f"{r['decay']:<14} {q_alg} {q_ame} {ratio_s}  {r['categorical_status']}")

    print("\n" + "=" * 78)
    print("CENTRAL OPEN GAP (option B): nucleon mass scale within ℚ(q)")
    print("=" * 78)
    print(f"  m_p_alg = m_e · ρ_p · tr_M(T_w(p))_q_0 = {m_p_alg:.6f} MeV")
    print(f"  m_p_AME = 938.272 MeV  →  scale gap = {938.272/m_p_alg:>9.2f}×")
    print(f"  m_n_alg = m_e · ρ_n · tr_M(T_w(n))_q_0 = {m_n_alg:.6f} MeV")
    print(f"  Q_n→p_alg = m_n − m_p − m_e = {Q_N_TO_P_ALG:.6f} MeV")
    print(f"  Q_n→p_AME = {Q_NEUTRON_MEV:.6f} MeV")
    print()
    print(f"Witness: {out_path.name}")


if __name__ == "__main__":
    main()
