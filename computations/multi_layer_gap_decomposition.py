"""Per-isotope L1 + L2 + L3 mass-gap decomposition probe.

Per `docs/audits/2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md`,
the +2.89-3.86 % multi-isotope gap decomposes as three layers:

    m_atom(Z, N) = Σ_i m_nucleon_i           (L1: single-knot VolDensity)
                 + Σ_{(i,j)} V_inter(i,j)    (L2: inter-nucleon channels)
                 + V_shell(Z, N)             (L3: nuclear-shell binding)

This probe:

1. Reads the 5-atom mass table (p, n, ²H, ³H, ³He) from
   `low-isotope-mass-table.witness.json`
2. Adds ⁴He's data from PR #1089 (B_AME = 28.296 MeV, prediction = 29.96 MeV)
3. Computes per-isotope ABSOLUTE error (MeV) — disambiguates between
   mass-error (free nucleons) and binding-error (multi-nucleon)
4. Decomposes per-isotope error into L1 + L2 + L3 contributions using
   the cleanest available assumptions
5. Reports the structural Markov × 5/2 improvement projection (PR #1081
   finding: L1 single-knot gap drops from +3.43 % to +1.948 %)

Output: per-isotope decomposition table + summary witness.

Status: EXPLORATORY (per `local/production-vs-exploratory-discipline`).
The L1/L2/L3 layer assignment is conjectural; this probe quantifies
the layers under the reconciliation audit's framing but does NOT
propose production wiring.
"""

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
LOW_ISO_WITNESS = _pb.witness_path("low-isotope-mass-table.witness.json", HERE)

# 4He from PR #1089 (not in low-isotope table; computed via different path)
HE4_PRED_MEV = mpf("29.96")
HE4_AME_MEV = mpf("28.296")

# L1 single-knot mass gap (free p, n): structural Markov × 5/2 improvement
# (PR #1081 Probe 2 finding)
L1_FAMILY_A_GAP_PCT = mpf("3.43")        # Family A linking weight (production)
L1_STRUCTURAL_MARKOV_5_2_PCT = mpf("1.948")  # 5/2 · tr_M(β_Bor) closed form


def n_pairs(A: int) -> int:
    """Number of nucleon pairs in atom: A choose 2 = A·(A-1)/2."""
    return A * (A - 1) // 2


def n_shells(Z: int, N: int) -> int:
    """Number of closed nucleon shells. Naive shell-model:
       - 0 closed shells for A < 4
       - 1 closed shell for A = 4 (alpha particle, 2p + 2n)
       - higher A: more shells (not in scope here)
    """
    A = Z + N
    if A < 4:
        return 0
    elif Z == 2 and N == 2:  # ⁴He α-particle
        return 1
    return 0  # other A ≥ 4 not in scope


def isotope_label(Z: int, N: int) -> str:
    A = Z + N
    if Z == 1 and N == 0:
        return "p"
    if Z == 0 and N == 1:
        return "n"
    if Z == 1 and N == 1:
        return "²H"
    if Z == 1 and N == 2:
        return "³H"
    if Z == 2 and N == 1:
        return "³He"
    if Z == 2 and N == 2:
        return "⁴He"
    return f"({Z},{N})"


def load_isotope_data() -> list:
    """Load low-isotope rows + append ⁴He from PR #1089."""
    with open(LOW_ISO_WITNESS) as f:
        d = json.load(f)
    rows = []
    for r in d["data"]["rows"]:
        rows.append({
            "Z": r["Z"],
            "N": r["N"],
            "A": r["A"],
            "label": isotope_label(r["Z"], r["N"]),
            "pred_MeV": mpf(str(r["prediction_MeV_50dps"])),
            "actual_MeV": mpf(str(r["B_AME_MeV"])),
            "err_pct": mpf(str(r["err_pct"])),
            "is_free_nucleon": (r["A"] == 1),
        })
    # Append ⁴He from PR #1089
    rows.append({
        "Z": 2, "N": 2, "A": 4, "label": "⁴He",
        "pred_MeV": HE4_PRED_MEV,
        "actual_MeV": HE4_AME_MEV,
        "err_pct": (HE4_PRED_MEV - HE4_AME_MEV) / HE4_AME_MEV * 100,
        "is_free_nucleon": False,
    })
    return rows


def decompose_per_isotope(row: dict) -> dict:
    """Decompose this isotope's error into L1 + L2 + L3 contributions.

    Note: the framework predicts MASS for free nucleons (A=1) and
    BINDING ENERGY for multi-nucleon. These are different physical
    quantities, so per-layer contributions need different treatments:

      - A=1 (free p, n): err is L1 only (no L2, no L3 — no pairs, no shell)
      - A≥2: err is L2+L3 in binding energy (L1's per-nucleon mass
        offset largely cancels in the difference Σm_nuc - m_atom = B,
        because the framework computes B via the inter-nucleon braid
        Markov trace, not via m_atom = m_p + m_n - B).

    So the per-isotope absolute err is attributed to layers as:
      L1_contribution  := A=1 ? full_err : 0
      L2+L3 combined   := A≥2 ? full_err : 0
      L3 specifically  := (A=4, Z=N=2) ? "alpha-binding-shell" : 0
    """
    err_abs_MeV = row["pred_MeV"] - row["actual_MeV"]
    A = row["A"]
    is_free = row["is_free_nucleon"]
    np_pairs = n_pairs(A)
    ns_shells = n_shells(row["Z"], row["N"])

    return {
        "label": row["label"],
        "Z": row["Z"], "N": row["N"], "A": A,
        "pred_MeV": float(row["pred_MeV"]),
        "actual_MeV": float(row["actual_MeV"]),
        "err_MeV": float(err_abs_MeV),
        "err_pct": float(row["err_pct"]),
        "n_pairs": np_pairs,
        "n_shells": ns_shells,
        "L1_contribution_MeV": float(err_abs_MeV) if is_free else 0.0,
        "L2_plus_L3_MeV": float(err_abs_MeV) if not is_free else 0.0,
        "L3_alpha_shell_specific_MeV": (
            float(err_abs_MeV) if (A == 4 and row["Z"] == 2 and row["N"] == 2)
            else 0.0
        ),
        "is_free_nucleon": is_free,
    }


def project_l1_improvement(decomp: dict) -> dict:
    """If we replace Family A's linking weight with structural Markov × 5/2,
    L1 gap drops from +3.43 % to +1.948 % (PR #1081). Project the absolute
    L1 improvement and the resulting err_pct for free nucleons.
    """
    if not decomp["is_free_nucleon"]:
        return {"applies": False}

    # For free p, n: predicted = actual × (1 + L1_gap_pct/100)
    # With L1 Markov × 5/2 improvement: predicted_new = actual × (1 + 1.948/100)
    actual = mpf(str(decomp["actual_MeV"]))
    pred_family_a = mpf(str(decomp["pred_MeV"]))
    pred_markov_5_2 = actual * (1 + L1_STRUCTURAL_MARKOV_5_2_PCT / 100)
    new_err_MeV = pred_markov_5_2 - actual
    new_err_pct = new_err_MeV / actual * 100
    improvement_MeV = float(pred_family_a - pred_markov_5_2)
    return {
        "applies": True,
        "pred_under_family_a_MeV": float(pred_family_a),
        "pred_under_markov_5_2_MeV": float(pred_markov_5_2),
        "improvement_MeV": improvement_MeV,
        "old_err_pct": float(decomp["err_pct"]),
        "new_err_pct": float(new_err_pct),
        "improvement_factor_x": (
            float(decomp["err_pct"]) / float(new_err_pct)
            if new_err_pct != 0 else None
        ),
    }


def main() -> None:
    print("Per-isotope L1 + L2 + L3 mass-gap decomposition")
    print(f"50-dps mpmath; data from low-isotope-mass-table.witness.json + ⁴He from PR #1089")
    print("=" * 80)

    rows = load_isotope_data()
    decompositions = []
    l1_projections = []

    for row in rows:
        d = decompose_per_isotope(row)
        decompositions.append(d)
        if d["is_free_nucleon"]:
            l1p = project_l1_improvement(d)
            l1_projections.append({**d, **l1p})

    # Print decomposition table
    print(f"\n{'atom':<6} {'Z,N,A':<8} {'pred (MeV)':>12} {'actual (MeV)':>14} "
          f"{'err (MeV)':>11} {'err %':>9} {'pairs':>6} {'shells':>7}")
    print("-" * 80)
    for d in decompositions:
        print(f"{d['label']:<6} "
              f"{d['Z']},{d['N']},{d['A']}    "
              f"{d['pred_MeV']:>12.4f} {d['actual_MeV']:>14.4f} "
              f"{d['err_MeV']:>+11.4f} {d['err_pct']:>+9.3f}  "
              f"{d['n_pairs']:>5} {d['n_shells']:>6}")

    # Per-layer attribution summary
    print("\n" + "=" * 80)
    print("PER-LAYER ATTRIBUTION (absolute errors)")
    print("=" * 80)
    print(f"{'atom':<6} {'L1 (MeV)':>10} {'L2+L3 (MeV)':>13} {'L3-alpha (MeV)':>16}")
    print("-" * 50)
    total_l1 = mpf(0)
    total_l2_l3 = mpf(0)
    total_l3 = mpf(0)
    for d in decompositions:
        print(f"{d['label']:<6} {d['L1_contribution_MeV']:>+10.4f} "
              f"{d['L2_plus_L3_MeV']:>+13.4f} {d['L3_alpha_shell_specific_MeV']:>+16.4f}")
        total_l1 += mpf(d['L1_contribution_MeV'])
        total_l2_l3 += mpf(d['L2_plus_L3_MeV'])
        total_l3 += mpf(d['L3_alpha_shell_specific_MeV'])

    print("-" * 50)
    print(f"{'TOTAL':<6} {float(total_l1):>+10.4f} {float(total_l2_l3):>+13.4f} "
          f"{float(total_l3):>+16.4f}")

    # L1 structural-Markov projection
    print("\n" + "=" * 80)
    print("L1 PROJECTION: replacing Family A → structural Markov × 5/2 (PR #1081)")
    print("=" * 80)
    print(f"{'atom':<6} {'err FA (%)':>12} {'err M5/2 (%)':>14} {'Δ (MeV)':>10} {'x improvement':>16}")
    print("-" * 65)
    for p in l1_projections:
        print(f"{p['label']:<6} {p['old_err_pct']:>+12.3f}  "
              f"{p['new_err_pct']:>+14.3f}  "
              f"{p['improvement_MeV']:>+10.4f}  "
              f"{(p['improvement_factor_x'] or 0):>15.2f}x")

    # L2+L3 sign-flip evidence
    print("\n" + "=" * 80)
    print("L2+L3 SIGN-FLIP EVIDENCE (multi-nucleon residual signs)")
    print("=" * 80)
    for d in decompositions:
        if d["is_free_nucleon"]:
            continue
        sign = "+" if d['L2_plus_L3_MeV'] >= 0 else "−"
        explain = ""
        if d["A"] == 4 and d["Z"] == 2 and d["N"] == 2:
            explain = " ← α-particle shell binding (L3 dominant)"
        elif d["A"] == 3 and d["L2_plus_L3_MeV"] < 0:
            explain = " ← inter-nucleon channel binding (L2 dominant)"
        elif d["A"] == 2:
            explain = " ← deuteron pn pair (L2 only, sign +)"
        print(f"  {d['label']}: err = {d['L2_plus_L3_MeV']:+.4f} MeV "
              f"({sign} sign){explain}")

    # Write witness
    witness = {
        "compute": "multi_layer_gap_decomposition",
        "description": (
            "Per-isotope L1 + L2 + L3 decomposition of the +2.89-3.86 % "
            "multi-isotope mass gap. Implements the three-layer framing "
            "from docs/audits/2026-05-24-single-knot-vs-multi-nucleon-"
            "reconciliation.md. Quantifies which layer dominates each "
            "isotope's error and projects the structural Markov × 5/2 "
            "improvement (PR #1081) on L1 free-nucleon predictions."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "L1_family_a_gap_pct": float(L1_FAMILY_A_GAP_PCT),
            "L1_structural_markov_5_2_pct": float(L1_STRUCTURAL_MARKOV_5_2_PCT),
        },
        "decompositions": decompositions,
        "l1_projections": l1_projections,
        "summary": {
            "total_L1_MeV": float(total_l1),
            "total_L2_plus_L3_MeV": float(total_l2_l3),
            "total_L3_alpha_shell_MeV": float(total_l3),
            "n_isotopes": len(decompositions),
            "interpretation": (
                "L1 dominates free-nucleon errors (+27 MeV per nucleon on "
                "p, n via Family A linking weight). L2+L3 dominates "
                "multi-nucleon binding-energy errors (sign-varying, max "
                "+1.66 MeV on ⁴He). The α-particle shell (⁴He) carries "
                "the entire L3-specific contribution at this scope. "
                "Structural Markov × 5/2 (PR #1081 Probe 2) closes "
                "~14.5 MeV of L1 per free nucleon — a 1.5× gap closure "
                "at L1 scope. L2 + L3 closures remain open structural "
                "questions (channel-weight derivation + per-shell Geom "
                "evaluation respectively)."
            ),
        },
        "cross_references": [
            "docs/audits/2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md",
            "docs/audits/2026-05-24-family-a-gap-audit.md",
            "docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md",
            "folio-assistant/computations/vol_density_borromean_h4_probe.py",
            "folio-assistant/computations/low-isotope-mass-table.witness.json",
            "PR #1089 (open) — multi-nucleon sign-flip diagnostic",
        ],
        "status": "exploratory",
        "tags": [
            "multi-layer-decomposition",
            "L1",
            "L2",
            "L3",
            "borromean",
            "alpha-shell",
            "sign-flip",
            "structural-markov-5-2",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }

    out_path = HERE / "multi-layer-gap-decomposition.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
