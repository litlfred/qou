#!/usr/bin/env python3
"""Plan H — extend ρ-from-Wedderburn-multiplicity probe to all 4
census atoms (²H, ³H, ³He, ⁴He).

The single-atom probe in `rho_3he_wedderburn_experiment.py` showed
that no simple Wedderburn integer reproduces ³He's "true ρ" of
2.062 — the residual δρ ≈ 0.062 has no obvious closed form.

Question: with 4 data points (²H, ³H, ³He, ⁴He) is there a UNIFORM
δρ pattern across the census?

Setup at q_0 = 1.1099785955541805 (50 dps):

  atom    knot      hand-pick ρ   M_err_ppm    Vol_hyp        B_AME
  ²H      6_2       1·m_e         -12.92       4.40083 (8_11) 2.22458 MeV
  ³H      8_11      2·m_e          +4.70       8.28631        8.4818  MeV
  ³He     L_6a4     2·m_e         +81.57       7.32772 (=8G)  7.71800 MeV
  ⁴He    α-cluster ρ=2 magic-A    +0.00       n/a            28.29566 MeV

For each atom, compute:
  1. χ_λ(atom-braid) at q_0 for each Wedderburn block λ
  2. y_λ(q_0) from the canonical witness at native strand count
  3. tr_M(atom-braid)|_{q=q_0}
  4. "true ρ" = B_AME / (m_e · Vol_hyp)
  5. δρ = true_ρ − hand_pick_ρ  (residual after removing structural integer)
  6. δρ candidates as functions of q_0 / Wedderburn data

Refs:
  - docs/plans/H-rho-from-wedderburn-multiplicity.md
  - PR #512 single-atom probe finding
  - low-isotope-mass-table.witness.json
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 50

Q_0 = 1.1099785955541805
M_E = 0.51099895
G_CATALAN = float(mp.catalan)


# ─── Census data (from low-isotope-mass-table.witness.json) ────────
CENSUS = [
    {
        "name": "2H", "Z": 1, "N": 1, "A": 2,
        "B_AME": 2.22458,
        "knot": "6_2",
        "vol_hyp": 4.40083,
        "rho_handpick": 1,
        "native_n": 3,    # 6_2 in B_3
        "braid": [1, -2, 1, 1, 1, -2],
        "M_err_ppm_handpick": -12.92,
        "M_AME": 1876.124,  # total mass MeV
    },
    {
        "name": "3H", "Z": 1, "N": 2, "A": 3,
        "B_AME": 8.4818,
        "knot": "8_11",
        "vol_hyp": 8.28631,
        "rho_handpick": 2,
        "native_n": 5,    # 8_11 in B_5
        "braid": [-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2],
        "M_err_ppm_handpick": +4.70,
        "M_AME": 2809.432,
    },
    {
        "name": "3He", "Z": 2, "N": 1, "A": 3,
        "B_AME": 7.7180,
        "knot": "L_6a4",
        "vol_hyp": 8 * G_CATALAN,  # exactly 8G ≈ 7.32772
        "rho_handpick": 2,
        "native_n": 3,    # Borromean in B_3
        "braid": [-1, 2, -1, 2, -1, 2],
        "M_err_ppm_handpick": +81.57,
        "M_AME": 2809.413,
    },
    {
        "name": "4He", "Z": 2, "N": 2, "A": 4,
        "B_AME": 28.29566,
        "knot": "magic-A",
        "vol_hyp": float('nan'),  # not a single hyperbolic knot
        "rho_handpick": 2,
        "native_n": None,   # magic-A formula
        "braid": None,
        "M_err_ppm_handpick": +0.00,
        "M_AME": 3727.379,
    },
]


def hoefsmit_h3_at_q(q: float):
    T_1 = np.array([[q, 0.0], [0.0, -1.0 / q]])
    denom = q * q + 1.0
    a = -1.0 / (q * denom)
    d = (q ** 3) / denom
    c = (q ** 4 + q * q + 1.0) / (denom * denom)
    T_2 = np.array([[a, 1.0], [c, d]])
    h = q - 1.0 / q
    T_2_inv = T_2 - h * np.eye(2)
    return T_1, T_2, T_2_inv


def chi_h3_braid(braid_word, q):
    """χ_λ(braid) for each λ ⊢ 3 at q (numerical)."""
    chi = {}
    chi["(3)"] = 1.0  # trivial
    chi["(1,1,1)"] = 1.0  # sign
    for k in braid_word:
        if k > 0:
            chi["(3)"] *= q
            chi["(1,1,1)"] *= -1.0 / q
        else:
            chi["(3)"] *= 1.0 / q
            chi["(1,1,1)"] *= -q
    # standard (2,1) — explicit Hoefsmit
    T_1, T_2, T_2_inv = hoefsmit_h3_at_q(q)
    M = np.eye(2)
    for k in braid_word:
        if k == 1:
            M = M @ T_1
        elif k == -1:
            M = M @ (T_1 - (q - 1.0 / q) * np.eye(2))
        elif k == 2:
            M = M @ T_2
        elif k == -2:
            M = M @ T_2_inv
        else:
            return None  # only H_3
    chi["(2,1)"] = float(np.trace(M))
    return chi


def _load_h3_y_lambda(base: Path) -> dict:
    """Load the H_3 Jones–Markov y_λ table once at start of run."""
    with open(base / "y-lambda-jones-markov-witness.json") as f:
        W = json.load(f)
    h3 = W["tables_by_n"]["3"]
    y = {}
    for w in h3["weights"]:
        if w["partition"] == [3]:
            y["(3)"] = w["y_lambda"]
        elif w["partition"] == [2, 1]:
            y["(2,1)"] = w["y_lambda"]
        elif w["partition"] == [1, 1, 1]:
            y["(1,1,1)"] = w["y_lambda"]
    return y


def main():
    base = Path(__file__).parent
    print("══════════════════════════════════════════════════════════════════════")
    print("  Plan H — full-census Wedderburn-multiplicity probe (4 atoms)")
    print(f"  q_0 = {Q_0}, m_e = {M_E} MeV")
    print("══════════════════════════════════════════════════════════════════════\n")

    # Load the H_3 y_λ table once outside the per-atom loop.
    h3_y = _load_h3_y_lambda(base)

    rows = []
    for atom in CENSUS:
        name = atom["name"]
        rho_hp = atom["rho_handpick"]
        B_AME = atom["B_AME"]
        vol_hyp = atom["vol_hyp"]

        if atom["knot"] == "magic-A":
            # ⁴He: not a single knot; use the magic-A formula directly
            B_pred_handpick = 2 * M_E * 4 * 8 * G_CATALAN  # 2·m_e·A·8G with A=4
            true_rho = B_AME / (M_E * 4 * 8 * G_CATALAN)
            delta_rho = true_rho - rho_hp
            tr_M = float('nan')
            chi = {"(magic-A)": "n/a"}
        else:
            B_pred_handpick = rho_hp * M_E * vol_hyp
            true_rho = B_AME / (M_E * vol_hyp)
            delta_rho = true_rho - rho_hp
            if atom["native_n"] == 3:
                chi = chi_h3_braid(atom["braid"], Q_0)
                tr_M = sum(h3_y[k] * chi[k] for k in h3_y)
            else:
                chi = {"(see-witness)": "deferred"}
                tr_M = float('nan')

        err_pct = (B_pred_handpick - B_AME) / B_AME * 100
        M_err_ppm = (B_pred_handpick - B_AME) / atom["M_AME"] * 1e6

        print(f"──── {name} ({atom['knot']}) ────")
        print(f"  Vol_hyp           = {vol_hyp:.6f}" if not np.isnan(vol_hyp) else f"  Vol_hyp           = n/a (magic-A)")
        print(f"  hand-pick ρ       = {rho_hp}")
        print(f"  B_pred_handpick   = {B_pred_handpick:.6f} MeV")
        print(f"  B_AME             = {B_AME:.6f} MeV")
        print(f"  err on B          = {err_pct:+.4f}%")
        print(f"  M_err on total    = {M_err_ppm:+.2f} ppm  (witness: {atom['M_err_ppm_handpick']:+.2f})")
        print(f"  'true ρ'          = {true_rho:.6f}")
        print(f"  δρ = true − hp    = {delta_rho:+.6f}")
        if not np.isnan(tr_M):
            print(f"  tr_M(braid)|_{{q_0}} = {tr_M:.6f}")
        print()

        rows.append({
            "name": name, "Z": atom["Z"], "N": atom["N"], "A": atom["A"],
            "knot": atom["knot"], "vol_hyp": vol_hyp,
            "B_AME": B_AME, "rho_handpick": rho_hp,
            "B_pred_handpick": B_pred_handpick,
            "true_rho": true_rho, "delta_rho": delta_rho,
            "M_err_ppm_predicted": M_err_ppm,
            "tr_M_at_q0": tr_M if not np.isnan(tr_M) else None,
            "chi": {k: (float(v) if isinstance(v, (int, float)) else v) for k, v in chi.items()},
        })

    # Pattern analysis
    print("══════════════════════════════════════════════════════════════════════")
    print("  Pattern analysis — δρ across census")
    print("══════════════════════════════════════════════════════════════════════\n")
    print(f"  {'atom':<5} {'true ρ':>10} {'hp ρ':>6} {'δρ':>10} {'δρ/ρ_hp':>10}")
    for r in rows:
        ratio = r['delta_rho'] / r['rho_handpick'] if r['rho_handpick'] else float('nan')
        print(f"  {r['name']:<5} {r['true_rho']:>10.6f} {r['rho_handpick']:>6} "
              f"{r['delta_rho']:>+10.6f} {ratio:>+10.6f}")

    # Quick test: is δρ/ρ_hp universal?
    deltas = [r['delta_rho'] / r['rho_handpick'] for r in rows[:3] if r['rho_handpick']]
    print(f"\n  δρ/ρ_hp values for ²H, ³H, ³He: "
          f"{deltas[0]:+.6f}, {deltas[1]:+.6f}, {deltas[2]:+.6f}")
    if max(deltas) - min(deltas) < 0.005:
        print(f"  → UNIFORM at ~{sum(deltas)/len(deltas):+.6f} ⇒ δρ proportional to ρ_hp!")
    else:
        print(f"  → non-uniform; δρ/ρ_hp varies by {(max(deltas)-min(deltas))*1e6:.0f} ppm")

    # Try: is δρ proportional to (q-1)?
    q_minus_1 = Q_0 - 1
    print(f"\n  q-1 = {q_minus_1:.6f}")
    print(f"  candidate: δρ = (q-1) · ρ_hp?")
    for r in rows[:3]:
        pred = q_minus_1 * r['rho_handpick']
        actual = r['delta_rho']
        print(f"    {r['name']:<5}: pred {pred:+.6f}  actual {actual:+.6f}  err {(actual-pred)/actual*100 if actual else 0:+.2f}%")

    print(f"\n  candidate: δρ = (q-1)/2 · ρ_hp²?  (genus-like quadratic)")
    for r in rows[:3]:
        pred = q_minus_1 / 2 * r['rho_handpick'] ** 2
        actual = r['delta_rho']
        print(f"    {r['name']:<5}: pred {pred:+.6f}  actual {actual:+.6f}")

    # Witness
    out_path = base / "rho-census-wedderburn-experiment.witness.json"
    witness = {
        "computation": "rho-census-wedderburn-experiment",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Plan H extension: compute δρ = (B_AME/(m_e·Vol_hyp)) − ρ_hp for "
            "all 4 census atoms (²H, ³H, ³He, ⁴He) and look for a universal "
            "δρ pattern (e.g., proportional to ρ_hp, to (q-1), or some "
            "Wedderburn data)."
        ),
        "q_0": Q_0,
        "rows": rows,
        "delta_rho_summary": {
            "2H":  rows[0]["delta_rho"],
            "3H":  rows[1]["delta_rho"],
            "3He": rows[2]["delta_rho"],
            "4He": rows[3]["delta_rho"],
        },
    }
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\n→ wrote {out_path}")


if __name__ == "__main__":
    main()
