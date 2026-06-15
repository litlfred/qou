#!/usr/bin/env python3
"""EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).

Option-3 falsification probe for the PR #1570 ("v9") isospin-mirror claim.

This script is exploratory hypothesis-generation; the finding it surfaces is
NOT for production. It tests whether the v9 structure

    scale · (1+q)/2 · Σ_λ y_λ · χ^λ(atom)

that hit the ³H/³He binding-energy *difference* to 0.11 % (PR #1570) ALSO
reproduces the individual *absolute* binding energies of D, T, ³He.

Discipline logic (multiple-comparisons / overfitting):
  If (1+q)/2 is a genuine substrate factor it must help the absolute
  energies too. If it ONLY helps the mirror difference (where it was
  back-solved as correction_target = diff_target / base_v8), then 0.11 %
  was specific to the difference — the classic overfitting tell.

The witness asserts the REFUTATION (assert no-generalize) so allPassed
stays true on the expected-negative outcome (discipline §Step 6).

Precision note: uses Python `decimal` at 40 digits. The inputs (y_λ, χ^λ)
are read from the existing 50-dps witnesses; this probe only compares at
the ~0.1 %–% level, so 40-digit decimal is far more than adequate and no
new high-precision compute is introduced.

Output: probe-isospin-mirror-v9-generalization.witness.json
"""

import ast
import json
import sys
from datetime import datetime, timezone
from decimal import Decimal as D, getcontext
from pathlib import Path

getcontext().prec = 40

M_E_MEV = D("0.51099895069")
M_PI_MEV = D("139.57039")
Q_0 = D("1.1097090249")
H_Q = 1 - 1 / Q_0
H = Q_0 - 1 / Q_0
MU_0 = M_E_MEV / (D(3) * H / D(2))

# AME2020 binding energies (MeV), same source as v7/v8/v9.
AME_MeV = {"D": D("2.224566"), "T": D("8.481798"), "3He": D("7.71806")}


def load_chi_atom(repo_root, atom_label):
    fn_map = {"D": "d", "T": "t", "3He": "3he"}
    fn = (repo_root / "folio-assistant" / "computations"
          / f"atom-chi-rust-{fn_map[atom_label]}.witness.json")
    with fn.open() as f:
        data = json.load(f)["data"]
    chi_atom = {}
    for e in data["atom"]["by_partition"]:
        part = e["partition"]
        part = tuple(ast.literal_eval(part)) if isinstance(part, str) else tuple(part)
        chi_atom[part] = D(str(e["chi_lambda"]))
    return chi_atom


def load_y(repo_root, atom_label):
    name_map = {"D": "deuteron-h6", "T": "tritium-h9", "3He": "helium-3-h9"}
    fn = (repo_root / "folio-assistant" / "computations"
          / f"chi-{name_map[atom_label]}-at-q0-50dps.witness.json")
    with fn.open() as f:
        data = json.load(f)
    y = {}
    for e in data["by_partition"]:
        part = e["partition"]
        part = tuple(ast.literal_eval(part)) if isinstance(part, str) else tuple(part)
        y[part] = D(e["y_lambda"])
    return y


def sum_y_chi(y, chi_atom):
    """Plain Σ_λ y_λ · χ^λ(atom) — the per-atom analogue of the v8 base."""
    s = D(0)
    for p, chi in chi_atom.items():
        s += y.get(p, D(0)) * chi
    return s


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent.parent

    base = {}
    for atom in ["D", "T", "3He"]:
        chi = load_chi_atom(repo_root, atom)
        y = load_y(repo_root, atom)
        base[atom] = sum_y_chi(y, chi)

    # Candidate scales (same family the v7/v8/v9 saga used).
    scales = {
        "m_pi*hbar_q": M_PI_MEV * H_Q,
        "m_pi*hbar_q*(1+q)/2": M_PI_MEV * H_Q * (1 + Q_0) / 2,
        "mu_0": MU_0,
        "mu_0*(1+q)/2": MU_0 * (1 + Q_0) / 2,
    }

    print("=== Option-3: does v9 structure generalize to ABSOLUTE B(D,T,3He)? ===\n")
    print(f"  Per-atom base Sigma y_lambda chi^lambda(atom):")
    for atom in ["D", "T", "3He"]:
        print(f"    {atom:4s}: base={float(base[atom]):+.6f}  AME B={float(AME_MeV[atom]):.4f} MeV")
    print()

    abs_results = {}
    for sname, scale in scales.items():
        row = {}
        for atom in ["D", "T", "3He"]:
            pred = scale * base[atom]
            err = (pred - AME_MeV[atom]) / AME_MeV[atom] * 100
            row[atom] = {"pred_MeV": float(pred), "err_pct": float(err)}
        row["max_abs_err_pct"] = max(abs(row[a]["err_pct"]) for a in ["D", "T", "3He"])
        abs_results[sname] = row
        print(f"  scale = {sname}")
        for atom in ["D", "T", "3He"]:
            print(f"    {atom:4s}: pred={row[atom]['pred_MeV']:+9.4f}  err={row[atom]['err_pct']:+8.2f}%")
        print(f"    -> max abs err = {row['max_abs_err_pct']:.2f}%\n")

    # The key falsification test: compare the (1+q)/2 multiplier's effect on
    # the mirror DIFFERENCE (where it was tuned, ~0.11%) vs on the ABSOLUTE
    # energies (where it was not). If absolute errors stay huge, (1+q)/2 did
    # NOT generalize -> the 0.11% was specific to the difference.
    best_abs_with_factor = abs_results["m_pi*hbar_q*(1+q)/2"]["max_abs_err_pct"]
    best_abs_without = abs_results["m_pi*hbar_q"]["max_abs_err_pct"]

    # "generalizes" would mean the (1+q)/2 family gets absolute energies to a
    # comparable (<~2%) accuracy as it got the difference. Define refutation:
    GENERALIZE_THRESHOLD_PCT = 2.0
    generalizes = best_abs_with_factor <= GENERALIZE_THRESHOLD_PCT
    refuted = int(not generalizes)

    print("=== Verdict ===")
    print(f"  mirror DIFFERENCE err with (1+q)/2 (PR #1570): 0.11%")
    print(f"  ABSOLUTE B max err with same (1+q)/2 family:   {best_abs_with_factor:.2f}%")
    print(f"  ABSOLUTE B max err WITHOUT (1+q)/2:            {best_abs_without:.2f}%")
    print(f"  generalizes (<= {GENERALIZE_THRESHOLD_PCT}% absolute)? {generalizes}")
    print(f"  => {'OVERFIT CONFIRMED: 0.11% was specific to the difference' if refuted else 'generalizes'}")

    witness = {
        "engine": "python-decimal",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "probe-isospin-mirror-v9-generalization",
        "exploratory": True,
        "description": (
            "EXPLORATORY falsification probe (Option 3 of the PR #1570 "
            "discipline gate). Tests whether the v9 scale*(1+q)/2*Sigma "
            "y_lambda chi^lambda(atom) structure that hit the 3H/3He binding "
            "DIFFERENCE to 0.11% also reproduces the ABSOLUTE binding "
            "energies of D, T, 3He. If absolute errors stay large, the "
            "(1+q)/2 factor did not generalize -> 0.11% was specific to the "
            "back-solved difference (overfitting tell)."
        ),
        "scriptFile": "probe_isospin_mirror_v9_generalization.py",
        "precisionMetadata": {"compute": "decimal-40", "note": "coarse %-level comparison; inputs from 50-dps witnesses"},
        "per_atom_base_sum_y_chi": {a: str(base[a]) for a in base},
        "AME_MeV": {a: str(AME_MeV[a]) for a in AME_MeV},
        "absolute_energy_results": abs_results,
        "mirror_difference_err_pct_PR1570": 0.1131772975,
        "absolute_max_err_with_1plusq_over_2_pct": best_abs_with_factor,
        "absolute_max_err_without_factor_pct": best_abs_without,
        "generalize_threshold_pct": GENERALIZE_THRESHOLD_PCT,
        "assertions": [
            {
                "name": "v9_structure_does_not_generalize_to_absolute_energies",
                "computed": refuted,
                "expected": 1,
                "tolerance": None,
                "source": "Option-3 falsification: (1+q)/2 was back-solved for the difference; it does not reproduce absolute B(D,T,3He).",
            }
        ],
        "allPassed": bool(refuted),
    }
    out = (repo_root / "folio-assistant" / "computations"
           / "probe-isospin-mirror-v9-generalization.witness.json")
    with out.open("w") as f:
        json.dump(witness, f, indent=2)
    print(f"\nWrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
