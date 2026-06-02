"""
delta_lambda_two_factor_phase2.py — Phase 2 of the closed-forms workplan.

Tests the **two-factor closure form**

    Δ_λ(K) := V(K) · c_λ

(separable per-knot × per-partition) against empirical Δ_λ data for
the deuteron, tritium, ³He, and ⁴He. Phase 1b's negative result on
the single-factor closure surfaced two structural constraints:

  - T (Z=1, N=2) and ³He (Z=2, N=1) at the same n=9 give different
    best-single-block Δ values (366.3 vs 211.0 — ratio 1.74 ≈ √3).
    The per-knot factor V(K) must distinguish these two.
  - Per-partition c_λ should be expressible from the 3 Galois-orbit
    residues identified in the discriminant-factorisation analysis.

Strategy:

  1. Build the empirical Δ_λ(K) table (best-single-block from
     delta-lambda-empirical-tabulation.witness.json).
  2. For each candidate V(K) form, compute the residual per-partition
     c_λ(K) = Δ_λ(K) / V(K) and test whether c_λ depends on K
     (closure form requires c_λ to be K-independent).
  3. Report the best V(K) form and its K-independent residue.

Candidate V(K) forms (categorically motivated):

  V1: V(K) = |tr_M(β_K)|                  — Markov-trace magnitude
  V2: V(K) = ℏ_q^{n - 1}                   — substrate-tower depth
  V3: V(K) = Vol_hyp(K) (when knownan)     — JSJ hyperbolic volume
  V4: V(K) = √3 · |tr_M|^{-1/2}             — empirical √3 motif
  V5: V(K) = Z·N · ℏ_q^{n-1}                — flavour-aware
  V6: V(K) = (Z²+N²) · ℏ_q^{n-1}            — flavour-symmetric

  Ref: [manuscript] conj:delta-lambda-categorical-closure
  Ref: [manuscript] docs/audits/2026-05-19-delta-lambda-exploration-findings.md
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from codata_constants import M_E_MEV
from q_parameter import Q as Q0, HBAR_Q


def load_empirical_atoms() -> dict:
    """Per-atom empirical best-single-block Δ data."""
    w = json.loads(
        (_pb.witness_path("delta-lambda-empirical-tabulation.witness.json", HERE)).read_text()
    )
    out = {}
    for atom in ("D", "T", "3He", "4He"):
        a = w["data"]["per_atom"][atom]
        sb = a["a_single_block"]
        out[atom] = {
            "Z": a["Z"],
            "N": a["N"],
            "n": a["n"],
            "n_partitions": a["n_partitions"],
            "tr_M": mp.mpf(a["tr_M"]),
            "abs_tr_M": mp.mpf(a["abs_tr_M"]),
            "B_AME": -mp.mpf(a["delta_M_MeV"]),   # positive binding
            "delta_M_signed": mp.mpf(a["delta_M_MeV"]),
            "best_lambda": tuple(sb["best_lambda"]),
            "best_delta_signed": mp.mpf(sb["best_delta"]),
            "best_abs_delta": mp.mpf(sb["best_abs_delta"]),
        }
    return out


def candidate_V(atom_data: dict, form: str) -> mp.mpf:
    """Categorical candidates for the per-knot factor V(K)."""
    Z, N, n = atom_data["Z"], atom_data["N"], atom_data["n"]
    abs_tr_M = atom_data["abs_tr_M"]
    if form == "V1_abs_tr_M":
        return abs_tr_M
    elif form == "V2_hbar_q_tower":
        return HBAR_Q ** (n - 1)
    elif form == "V3_inv_abs_tr_M":
        return 1 / abs_tr_M
    elif form == "V4_sqrt_inv_tr_M":
        return mp.sqrt(1 / abs_tr_M)
    elif form == "V5_ZN_hbar_q_tower":
        return mp.mpf(Z) * mp.mpf(N) * HBAR_Q ** (n - 1)
    elif form == "V6_Z2N2_hbar_q":
        return (mp.mpf(Z) ** 2 + mp.mpf(N) ** 2) * HBAR_Q ** (n - 1)
    elif form == "V7_n_inv_tr_M":
        return mp.mpf(n) / abs_tr_M
    elif form == "V8_hbar_inv_squared":
        return 1 / HBAR_Q ** 2
    else:
        raise ValueError(f"Unknown V form: {form}")


def test_two_factor(atoms: dict, V_form: str) -> dict:
    """Test if Δ_λ*(K) / V(K) is approximately K-independent (= c_λ*)."""
    # Compute the empirical ratio Δ*/V for each atom and the
    # variance across atoms (low variance = good separability).
    ratios = {}
    for atom, a in atoms.items():
        V = candidate_V(a, V_form)
        ratio = a["best_abs_delta"] / V if V > 1e-50 else mp.mpf("nan")
        ratios[atom] = float(ratio)
    # Statistics: mean, std/mean, max/min
    values = [r for r in ratios.values() if not mp.isnan(mp.mpf(r))]
    if not values:
        return {"V_form": V_form, "ratios": ratios, "consistency": "NaN"}
    mean = sum(values) / len(values)
    var = sum((r - mean) ** 2 for r in values) / len(values)
    std = mp.sqrt(mp.mpf(var))
    max_min_ratio = max(values) / min(values) if min(values) != 0 else float('inf')
    return {
        "V_form": V_form,
        "ratios": ratios,
        "mean": float(mean),
        "rel_std": float(std / mp.mpf(mean)) if mean != 0 else float('inf'),
        "max_over_min": float(max_min_ratio),
    }


def main() -> int:
    builder = WitnessBuilder("delta-lambda-two-factor-phase2")
    builder.set_description(
        "Phase 2 of the closed-forms-first-principles workplan: tests "
        "the two-factor closure form Δ_λ(K) = V(K) · c_λ across "
        "8 candidate per-knot factors V(K), looking for K-independent "
        "residue c_λ. Atoms: D, T, ³He, ⁴He."
    )

    atoms = load_empirical_atoms()
    builder.add_parameter("q0", str(Q0))
    builder.add_parameter("hbar_q", str(HBAR_Q))
    builder.add_parameter(
        "atoms",
        [
            f"{a}: Z={d['Z']}, N={d['N']}, n={d['n']}, λ*={d['best_lambda']}"
            for a, d in atoms.items()
        ],
    )

    # Per-atom |Δ*| reference (best-single-block from empirical tabulation)
    builder.add_data("empirical_best_delta", {
        a: {
            "lambda_star": str(d["best_lambda"]),
            "abs_delta": str(d["best_abs_delta"]),
            "B_AME_MeV": str(d["B_AME"]),
            "abs_tr_M": str(d["abs_tr_M"]),
            "n": d["n"],
        }
        for a, d in atoms.items()
    })

    # Test each candidate V(K) form
    forms = [
        "V1_abs_tr_M",
        "V2_hbar_q_tower",
        "V3_inv_abs_tr_M",
        "V4_sqrt_inv_tr_M",
        "V5_ZN_hbar_q_tower",
        "V6_Z2N2_hbar_q",
        "V7_n_inv_tr_M",
        "V8_hbar_inv_squared",
    ]
    results = [test_two_factor(atoms, f) for f in forms]
    builder.add_data("V_form_tests", results)

    # Find best form by lowest rel_std (closest to K-independent)
    valid_results = [r for r in results if r.get("rel_std") is not None]
    if valid_results:
        best = min(valid_results, key=lambda r: r["rel_std"])
        builder.add_data("best_form", best["V_form"])
        builder.add_data("best_form_rel_std", best["rel_std"])
        builder.add_data("best_form_residue_c_lambda", best["mean"])

    # Verdict
    if valid_results and best["rel_std"] < 0.05:
        verdict = f"GOOD ({best['V_form']} → c_λ K-independent at < 5%)"
    elif valid_results and best["rel_std"] < 0.5:
        verdict = f"PARTIAL ({best['V_form']} → c_λ varies by < 50%)"
    else:
        verdict = "MISS — no candidate V(K) form gives K-independent c_λ"
    builder.add_data("verdict", verdict)

    builder.add_assertion(
        "tr_M_data_loaded",
        computed=float(atoms["D"]["abs_tr_M"]),
        expected=0.3882864240747888,
        tolerance=1e-10,
        unit="tr_M(D) at q_0",
        source="delta-lambda-empirical-tabulation.witness.json",
    )

    builder.save()

    # Console summary
    print("=" * 78)
    print("  Phase 2 — two-factor Δ_λ closure form across D, T, ³He, ⁴He")
    print("=" * 78)
    print(f"\n  Atoms (empirical best-single-block):")
    for a, d in atoms.items():
        print(f"    {a:<6} (Z={d['Z']}, N={d['N']}, n={d['n']}, λ*={d['best_lambda']}) "
              f"|Δ*| = {float(d['best_abs_delta']):>10.4f}, "
              f"B = {float(d['B_AME']):>8.4f} MeV")
    print()

    print(f"  {'V form':<28} {'D':>10} {'T':>10} {'³He':>10} {'⁴He':>10}  "
          f"{'rel_std':>10} {'max/min':>10}")
    for r in results:
        if "ratios" in r and "rel_std" in r:
            row = (r["ratios"].get("D", float("nan")),
                   r["ratios"].get("T", float("nan")),
                   r["ratios"].get("3He", float("nan")),
                   r["ratios"].get("4He", float("nan")))
            print(f"  {r['V_form']:<28} {row[0]:>10.4f} {row[1]:>10.4f} "
                  f"{row[2]:>10.4f} {row[3]:>10.4f}  "
                  f"{r['rel_std']:>10.4f} {r['max_over_min']:>10.4f}")
    print()
    print(f"  Verdict: {verdict}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
