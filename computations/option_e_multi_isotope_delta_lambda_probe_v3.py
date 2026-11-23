#!/usr/bin/env python3
"""
Option E v3 — per-knot extension: test content-sum-negated on D, T, ³He,
and probe candidate per-knot corrections f(K).

User insight: f should depend on the knot K (the atomic braid), not just λ.
The canonical Option E Δ_λ(K) has shape
    Δ_λ(K) = -Σ contents(λ) + f(K, λ)
where f may depend on both K and λ but with structural simplicity.

We test:
1. Whether content_sum_negated has consistent shape across D, T, ³He
   (sign + order of magnitude). If yes, leading order is canonical.
2. The residuals per atom (what would f need to provide).
3. Candidate per-knot multipliers from substrate (n_0, A, tr_M, dim_max).

Inputs:
  chi-deuteron-h6-at-q0-50dps.witness.json   (Z=1, N=1, n=6, 11 partitions)
  chi-tritium-h9-at-q0-50dps.witness.json    (Z=1, N=2, n=9, 30 partitions)
  chi-helium-3-h9-at-q0-50dps.witness.json   (Z=2, N=1, n=9, 30 partitions)

Output:
  option-e-multi-isotope-delta-lambda-probe-v3.witness.json
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mpf, mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from codata_constants import AME_B_HE3_MEV_VALIDATION  # noqa: E402  (AME registry)


def young_contents(partition):
    contents = []
    for r, row_len in enumerate(partition):
        for c in range(row_len):
            contents.append(c - r)
    return contents


def load_atom(repo_root, name):
    fn = (
        repo_root
        / "computations"
        / f"chi-{name}-at-q0-50dps.witness.json"
    )
    with fn.open() as f:
        return json.load(f)


def parse_rows(chi_data):
    rows = []
    for entry in chi_data["by_partition"]:
        part = entry["partition"]
        if isinstance(part, str):
            part = eval(part)
        rows.append({
            "partition": part,
            "dim": int(entry["dim"]),
            "y_lambda": mpf(entry["y_lambda"]),
            "chi_lambda": mpf(entry["chi_lambda"]),
            "contribution": mpf(entry["contribution"]),
            "contents": young_contents(part),
        })
    return rows


# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
mp.dps = 50

# AME binding energies (MeV)
AME_MeV = {
    "deuteron":  AME_B_DEUTERON_MEV_VALIDATION,
    "tritium":   AME_B_TRITIUM_MEV_VALIDATION,
    "helium-3":  AME_B_HE3_MEV_VALIDATION,
}

M_E_MEV = mpf("0.51099895069")


def evaluate_rule_per_atom(atom_name, rows, rule_fn):
    """Apply rule_fn(row) → Δ_λ per partition; compute Path-D B_pred."""
    sum_term = mpf(0)
    for row in rows:
        delta = rule_fn(row)
        sum_term += row["contribution"] * delta
    B_pred = M_E_MEV * sum_term
    B_target = AME_MeV[atom_name]
    signed_residual = B_pred + B_target  # closure means ≈ 0
    abs_residual = abs(signed_residual)
    rel_error_pct = 100 * abs_residual / B_target
    closes = abs_residual <= mpf("0.10") * B_target
    return {
        "atom": atom_name,
        "B_pred_MeV": str(B_pred),
        "B_target_MeV": str(B_target),
        "signed_residual_MeV": str(signed_residual),
        "abs_residual_MeV": str(abs_residual),
        "rel_error_pct": str(rel_error_pct),
        "closes_within_10pct": bool(closes),
    }


def main() -> int:
    set_compute_dps()
    repo_root = Path(__file__).resolve().parent.parent

    atom_data = {
        "deuteron": parse_rows(load_atom(repo_root, "deuteron-h6")),
        "tritium":  parse_rows(load_atom(repo_root, "tritium-h9")),
        "helium-3": parse_rows(load_atom(repo_root, "helium-3-h9")),
    }

    # Atom-level substrate data (n_0 = 3A, A = Z+N, tr_M from chi cache,
    # dim_max = largest partition dim)
    atom_substrate = {}
    for name, rows in atom_data.items():
        tr_M_data = load_atom(repo_root, name.replace("helium-3", "helium-3-h9").replace("deuteron", "deuteron-h6").replace("tritium", "tritium-h9"))
        n_0 = tr_M_data.get("n_strands", 6 if name == "deuteron" else 9)
        atom_substrate[name] = {
            "n_0": n_0,
            "A": tr_M_data.get("Z", 1) + tr_M_data.get("N", 1),
            "Z": tr_M_data.get("Z"),
            "N": tr_M_data.get("N"),
            "tr_M": mpf(tr_M_data["tr_M_at_q0"]),
            "n_partitions": tr_M_data["n_partitions"],
            "dim_max": max(int(e["dim"]) for e in tr_M_data["by_partition"]),
        }

    # Rule under test: content_sum_negated, Δ_λ = -Σ contents(λ)
    def rule_content_sum_negated(row):
        return -mpf(sum(row["contents"]))

    # Test the LEADING ORDER on all 3 atoms
    leading_order_results = {}
    for atom_name, rows in atom_data.items():
        leading_order_results[atom_name] = evaluate_rule_per_atom(
            atom_name, rows, rule_content_sum_negated
        )

    # Per-knot residuals. NOT float()-ed: this dict is stringified into the
    # witness as `per_knot_residuals_MeV`, and `leading_order_results` already
    # carries the same numbers at 49 digits. Truncating the duplicate to float64
    # made the two fields of the same witness disagree from the 17th digit.
    per_knot_residuals = {
        atom: leading_order_results[atom]["signed_residual_MeV"]
        for atom in ["deuteron", "tritium", "helium-3"]
    }

    # Try per-knot corrected rules:
    # f(K) candidates - each adds a knot-dependent additive constant
    # to every Δ_λ, scaled by something derivable from substrate

    def make_offset_rule(offset_value):
        """Return a rule that adds `offset_value` to every -Σ contents."""
        def fn(row):
            return -mpf(sum(row["contents"])) + offset_value
        return fn

    # Per-atom offsets derived from substrate (no AME fitting):
    knot_offsets = {}
    for atom in ["deuteron", "tritium", "helium-3"]:
        s = atom_substrate[atom]
        # Candidate offsets — purely from substrate
        knot_offsets[atom] = {
            "negated_n_partitions": -mpf(s["n_partitions"]),  # -p(n_0)
            "negated_tr_M_inverse": -mpf(1) / s["tr_M"],
            "minus_dim_max_over_A": -mpf(s["dim_max"]) / mpf(s["A"]),
            "minus_A_squared": -mpf(s["A"] ** 2),
            "minus_n0_over_2": -mpf(s["n_0"]) / mpf(2),
        }

    # Test each candidate offset universally
    candidate_offset_results = {}
    for offset_name in ["negated_n_partitions", "negated_tr_M_inverse",
                          "minus_dim_max_over_A", "minus_A_squared",
                          "minus_n0_over_2"]:
        per_atom_results = {}
        for atom_name in ["deuteron", "tritium", "helium-3"]:
            offset_value = knot_offsets[atom_name][offset_name]
            corrected_rule = make_offset_rule(offset_value)
            per_atom_results[atom_name] = evaluate_rule_per_atom(
                atom_name, atom_data[atom_name], corrected_rule
            )
        candidate_offset_results[offset_name] = per_atom_results

    # Build witness
    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-multi-isotope-delta-lambda-probe-v3",
        "description": (
            "Option E v3: extends v2's content_sum_negated rule to "
            "T and ³He + tests 5 per-knot offset corrections derived "
            "from substrate data (no AME fitting). User insight: "
            "f should depend on the knot K, not just λ."
        ),
        "scriptFile": "option_e_multi_isotope_delta_lambda_probe_v3.py",
        "precisionMetadata": {"compute_dps": 50, "output_dps": 30},
        "atoms_tested": ["deuteron", "tritium", "helium-3"],
        "atom_substrate": {
            name: {k: str(v) if not isinstance(v, (int, str)) else v for k, v in s.items()}
            for name, s in atom_substrate.items()
        },
        "leading_order_rule": "content_sum_negated",
        "leading_order_results": leading_order_results,
        "per_knot_residuals_MeV": {k: str(v) for k, v in per_knot_residuals.items()},
        "candidate_offsets_tested": list(candidate_offset_results.keys()),
        "candidate_offset_results": candidate_offset_results,
    }

    # Find best offset family (smallest max rel_error across 3 atoms)
    best_offset = None
    best_max_err = float("inf")  # float64-ok: written to the witness as a JSON number
    for offset_name, per_atom in candidate_offset_results.items():
        # a percentage compared against a 10% threshold, then serialised as a
        # JSON number — mpf is not JSON-serialisable there
        max_err = max(float(per_atom[a]["rel_error_pct"]) for a in per_atom)  # float64-ok: JSON number, 2-dp threshold
        if max_err < best_max_err:
            best_max_err = max_err
            best_offset = offset_name

    witness["best_offset"] = {
        "name": best_offset,
        "max_rel_error_pct_across_atoms": best_max_err,
        "uniform_closure_10pct": best_max_err <= 10.0,
    }

    out = (
        repo_root / "computations"
        / "option-e-multi-isotope-delta-lambda-probe-v3.witness.json"
    )
    with out.open("w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)

    # Print summary
    print(f"Wrote {out}\n")
    print("=== Leading order: content_sum_negated (no per-knot correction) ===")
    for atom in ["deuteron", "tritium", "helium-3"]:
        r = leading_order_results[atom]
        # console formatting only; the witness carries the full-precision
        # strings and is untouched by these four conversions
        bp = float(r["B_pred_MeV"])            # float64-ok: console formatting only
        bt = float(r["B_target_MeV"])          # float64-ok: console formatting only
        rs = float(r["signed_residual_MeV"])   # float64-ok: console formatting only
        er = float(r["rel_error_pct"])         # float64-ok: console formatting only
        print(f"  {atom:10s}  B_pred={bp:+8.4f} MeV  target={bt:+8.4f}  "
              f"residual={rs:+8.4f}  err={er:6.2f}%")

    # Check shape consistency
    # float64-ok: `leading_order_results[...]` holds DECIMAL STRINGS, so this is
    # a string parse for a sign test, not an mpf truncation. Dropping the
    # float() here does not tighten precision, it raises TypeError.
    signs = [float(leading_order_results[a]["B_pred_MeV"]) < 0  # float64-ok: sign test on a decimal string
             for a in ["deuteron", "tritium", "helium-3"]]
    targets_neg = all(float(leading_order_results[a]["B_pred_MeV"]) < 0  # float64-ok: sign test on a decimal string
                      for a in ["deuteron", "tritium", "helium-3"])
    print(f"\nShape check: all B_pred negative (correct sign)?  {targets_neg}")

    print("\n=== Per-knot offset candidates ===")
    for offset_name, per_atom in candidate_offset_results.items():
        errs = [float(per_atom[a]["rel_error_pct"])  # float64-ok: console formatting only
                for a in ["deuteron", "tritium", "helium-3"]]
        print(f"  {offset_name:30s}  errs D/T/³He = {errs[0]:6.2f}% / {errs[1]:6.2f}% / {errs[2]:6.2f}%  max={max(errs):6.2f}%")

    print(f"\nBest offset family: {witness['best_offset']['name']}")
    print(f"  max rel error across atoms: {witness['best_offset']['max_rel_error_pct_across_atoms']:.2f}%")
    print(f"  uniform closure 10%? {witness['best_offset']['uniform_closure_10pct']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
