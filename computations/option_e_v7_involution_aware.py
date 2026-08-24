#!/usr/bin/env python3
"""
Option E v7 — involution-aware Δ_λ probe with bar/transpose symmetry.

User question: "are we using involution, bar / skew symmetry appropriately?"

v1-v6 did NOT systematically use partition-transpose involution.
This v7 corrects that by:

  1. Computing partition transpose λᵀ for each block.
  2. Classifying blocks: self-conjugate (λ = λᵀ) vs chiral-pair (λ ≠ λᵀ).
  3. Testing Δ_λ rules that exploit (anti)symmetric combinations:
     - bar-symmetric: (χ_λ + χ_λᵀ) / 2
     - bar-antisymmetric: (χ_λ - χ_λᵀ) / 2
     - self-conj restriction: sum only over λ = λᵀ
  4. Trying multiple scales: m_e, μ₀, m_π = 139.57 MeV, ℏ_q variants

The mirror pair ³H/³He IS an isospin-mirror — the canonical
substrate operation is partition-transpose at the Wedderburn level.
If v7 finds closure under bar-(anti)symmetric Markov-weighting,
that's the structural answer to the cheat-sheet's "2% mirror" claim.

Refs:
  binding_depth_stratified_selfconj.py — self-conjugate restriction
  prop:plancherel-term-7-formulation
  notation-collisions.md (Wenzl bridge: y_λ = w_λ on self-conj stratum)

Output: option-e-v7-involution-aware.witness.json
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mpf, mp, fabs, acos
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
mp.dps = 50


M_E_MEV = mpf("0.51099895069")
M_PI_MEV = mpf("139.57039")  # PDG charged pion mass
# ARCHIVAL: the v9-era substrate literal, 243,000 ppb (0.024 %) from
# both live pins. NOT migrated on purpose — these files ARE the record
# of the v1..v9 progression that docs/coordination/option-e.md tracks
# ("DO NOT REPEAT failed paths"), and option_e_probe1_derive_1plusq_over_2
# exists specifically to show the published 0.11 %% near-match was obtained
# at THIS stale q0. Re-pinning would silently alter a recorded historical
# result and delete that probe's subject. Do not read it as a live pin.
Q_0 = mpf("1.1097090249")

H_Q = 1 - 1 / Q_0
H = Q_0 - 1 / Q_0
MU_0 = M_E_MEV / (mpf(3) * H / mpf(2))

AME_MeV = {"D": mpf("2.224566"), "T": mpf("8.481798"),
           "3He": mpf("7.71806")}
N_STRANDS = {"D": 6, "T": 9, "3He": 9}


def dim_sn(lam):
    lam = list(lam)
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den


def transpose(lam):
    """Partition transpose (conjugate Young diagram)."""
    if not lam:
        return tuple()
    max_part = max(lam)
    transposed = tuple(
        sum(1 for p in lam if p > i)
        for i in range(max_part)
    )
    return transposed


def load_chi_free_atom(repo_root, atom_label):
    fn_map = {"D": "d", "T": "t", "3He": "3he"}
    fn = (repo_root / "computations"
          / f"atom-chi-rust-{fn_map[atom_label]}.witness.json")
    with fn.open() as f:
        data = json.load(f)["data"]
    chi_free, chi_atom = {}, {}
    for cfg, target in [("free", chi_free), ("atom", chi_atom)]:
        for e in data[cfg]["by_partition"]:
            part = e["partition"]
            if isinstance(part, str):
                part = tuple(eval(part))
            else:
                part = tuple(part)
            target[part] = mpf(str(e["chi_lambda"]))
    return chi_free, chi_atom


def load_y_lambda(repo_root, atom_label):
    name_map = {"D": "deuteron-h6", "T": "tritium-h9", "3He": "helium-3-h9"}
    fn = (repo_root / "computations"
          / f"chi-{name_map[atom_label]}-at-q0-50dps.witness.json")
    with fn.open() as f:
        data = json.load(f)
    y = {}
    for e in data["by_partition"]:
        part = e["partition"]
        if isinstance(part, str):
            part = tuple(eval(part))
        else:
            part = tuple(part)
        y[part] = mpf(e["y_lambda"])
    return y


def classify_partitions(parts):
    """Return (self_conj, chiral_pairs) where pairs are unordered."""
    self_conj = []
    chiral_pairs = []
    seen = set()
    for p in parts:
        if p in seen:
            continue
        pt = transpose(p)
        if pt == p:
            self_conj.append(p)
            seen.add(p)
        else:
            if pt in parts and pt not in seen:
                chiral_pairs.append((p, pt))
                seen.add(p)
                seen.add(pt)
    return self_conj, chiral_pairs


def compute_involution_quantities(chi_free, chi_atom, y_lambda):
    """Compute sums over self-conjugate + bar-(anti)symmetric combinations."""
    parts = list(chi_free.keys())
    self_conj, chiral_pairs = classify_partitions(parts)

    # Sums on self-conjugate partitions only
    sc_sum_y_chi_atom = mpf(0)
    sc_sum_y_chi_diff = mpf(0)
    sc_sum_dim = mpf(0)
    for p in self_conj:
        d = mpf(dim_sn(p))
        y = y_lambda.get(p, mpf(0))
        sc_sum_y_chi_atom += y * chi_atom[p]
        sc_sum_y_chi_diff += y * (chi_atom[p] - chi_free[p])
        sc_sum_dim += d

    # Bar-symmetric and -antisymmetric combinations over chiral pairs
    bar_sym_sum_atom = mpf(0)    # Σ pairs y_λ · (χ_λ_atom + χ_λᵀ_atom) / 2
    bar_asym_sum_atom = mpf(0)   # Σ pairs y_λ · (χ_λ_atom - χ_λᵀ_atom) / 2
    bar_sym_sum_diff = mpf(0)    # Σ pairs y_λ · ((χ_λ - χ_λᵀ)_atom - (χ_λ - χ_λᵀ)_free) / 2
    bar_asym_sum_diff = mpf(0)
    pair_phase_sum = mpf(0)
    for (p, pt) in chiral_pairs:
        d = mpf(dim_sn(p))
        y = y_lambda.get(p, mpf(0))
        y_t = y_lambda.get(pt, mpf(0))
        # Use average y (they should be equal by Wenzl symmetry at q_0?)
        y_avg = (y + y_t) / 2
        chi_a_p, chi_a_pt = chi_atom[p], chi_atom[pt]
        chi_f_p, chi_f_pt = chi_free[p], chi_free[pt]
        sym_a = (chi_a_p + chi_a_pt) / 2
        asym_a = (chi_a_p - chi_a_pt) / 2
        sym_f = (chi_f_p + chi_f_pt) / 2
        asym_f = (chi_f_p - chi_f_pt) / 2
        bar_sym_sum_atom += y_avg * sym_a
        bar_asym_sum_atom += y_avg * asym_a
        bar_sym_sum_diff += y_avg * (sym_a - sym_f)
        bar_asym_sum_diff += y_avg * (asym_a - asym_f)
        # Reeb phase using bar-antisymmetric part (the chirality signal)
        r_asym_a = asym_a / d  # might be small
        if fabs(r_asym_a) <= 1:
            pair_phase_sum += y_avg * acos(r_asym_a)

    return {
        "n_self_conj": len(self_conj),
        "n_chiral_pairs": len(chiral_pairs),
        "self_conj_partitions": [str(p) for p in self_conj],
        "chiral_pair_examples": [(str(p), str(pt)) for p, pt in chiral_pairs[:5]],
        "sc_sum_y_chi_atom": sc_sum_y_chi_atom,
        "sc_sum_y_chi_diff": sc_sum_y_chi_diff,
        "sc_sum_dim": sc_sum_dim,
        "bar_sym_sum_atom": bar_sym_sum_atom,
        "bar_asym_sum_atom": bar_asym_sum_atom,
        "bar_sym_sum_diff": bar_sym_sum_diff,
        "bar_asym_sum_diff": bar_asym_sum_diff,
        "pair_phase_sum": pair_phase_sum,
    }


def main() -> int:
    set_compute_dps()
    repo_root = Path(__file__).resolve().parent.parent

    print(f"=== Scales ===")
    print(f"  m_e   = {float(M_E_MEV):.6f}")
    print(f"  μ₀    = {float(MU_0):.6f}")
    print(f"  m_π   = {float(M_PI_MEV):.6f}")
    print(f"  ℏ_q   = {float(H_Q):.6f}")
    print(f"  q_0   = {float(Q_0):.6f}\n")

    # Compute involution quantities per atom
    atom_invol = {}
    for atom in ["D", "T", "3He"]:
        cf, ca = load_chi_free_atom(repo_root, atom)
        y = load_y_lambda(repo_root, atom)
        atom_invol[atom] = compute_involution_quantities(cf, ca, y)

    # Report classification
    print("=== Partition classification ===")
    for atom in ["D", "T", "3He"]:
        r = atom_invol[atom]
        print(f"  {atom}: self_conj = {r['n_self_conj']}, chiral_pairs = {r['n_chiral_pairs']}")
        print(f"    self_conj: {r['self_conj_partitions'][:5]}")
    print()

    # Test candidate formulas — scales × involution sums
    scales = [
        ("m_e", M_E_MEV),
        ("μ₀", MU_0),
        ("μ₀·ℏ_q", MU_0 * H_Q),
        ("m_π", M_PI_MEV),
        ("m_π·ℏ_q", M_PI_MEV * H_Q),
    ]

    inputs = [
        "sc_sum_y_chi_atom",
        "sc_sum_y_chi_diff",
        "bar_sym_sum_atom",
        "bar_asym_sum_atom",
        "bar_sym_sum_diff",
        "bar_asym_sum_diff",
        "pair_phase_sum",
    ]

    print("=== Closure search (scale × involution sum) — D, T, ³He absolute energies ===")
    all_results = {}
    for sname, scale in scales:
        for ikey in inputs:
            row = {}
            for atom in ["D", "T", "3He"]:
                value = scale * atom_invol[atom][ikey]
                target = AME_MeV[atom]
                err = float((value - target) / target * 100)
                row[atom] = {"B_pred": float(value), "err_pct": err}
            # Take max abs err across 3 atoms
            max_err = max(abs(row[a]["err_pct"]) for a in ["D", "T", "3He"])
            row["max_err_pct"] = max_err
            all_results[f"{sname} · {ikey}"] = row

    # Print best 5
    sorted_results = sorted(all_results.items(), key=lambda x: x[1]["max_err_pct"])
    print(f"  {'Formula':45s}  D err     T err     ³He err   max")
    for name, r in sorted_results[:10]:
        marker = "  ✓✓" if r["max_err_pct"] <= 2 else "  ✓" if r["max_err_pct"] <= 10 else "   "
        print(f"{marker} {name:45s}  {r['D']['err_pct']:+7.1f}%  "
              f"{r['T']['err_pct']:+7.1f}%  {r['3He']['err_pct']:+7.1f}%  "
              f"{r['max_err_pct']:5.1f}%")

    # Mirror pair specifically
    print(f"\n=== Mirror pair ³H - ³He difference (target {float(AME_MeV['T'] - AME_MeV['3He']):.4f} MeV) ===")
    diff_target = AME_MeV["T"] - AME_MeV["3He"]
    mirror_results = {}
    for sname, scale in scales:
        for ikey in inputs:
            v_T = scale * atom_invol["T"][ikey]
            v_He = scale * atom_invol["3He"][ikey]
            diff = v_T - v_He
            err = float((diff - diff_target) / diff_target * 100)
            mirror_results[f"{sname} · ({ikey})"] = {
                "diff_MeV": float(diff),
                "err_pct": err,
            }
    sorted_mirror = sorted(mirror_results.items(), key=lambda x: abs(x[1]["err_pct"]))
    print(f"  {'Formula':50s}  diff      err")
    for name, r in sorted_mirror[:10]:
        marker = "  ✓✓" if abs(r["err_pct"]) <= 2 else "  ✓" if abs(r["err_pct"]) <= 10 else "   "
        print(f"{marker} {name:50s}  {r['diff_MeV']:+9.4f}  {r['err_pct']:+8.2f}%")

    # Write witness
    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-v7-involution-aware",
        "description": (
            "Option E v7: involution-aware Δ_λ probe. Tests partition-"
            "transpose λ ↔ λᵀ symmetry (self-conjugate + bar-(anti)symmetric "
            "combinations) with 5 scale candidates (m_e, μ₀, μ₀·ℏ_q, m_π, "
            "m_π·ℏ_q) × 7 involution sums. Addresses user question 'are we "
            "using involution / bar / skew symmetry appropriately?'"
        ),
        "scriptFile": "option_e_v7_involution_aware.py",
        "precisionMetadata": {"compute_dps": 50, "output_dps": 30},
        "scales": {sname: str(s) for sname, s in scales},
        "partition_classification": {
            atom: {
                "n_self_conj": r["n_self_conj"],
                "n_chiral_pairs": r["n_chiral_pairs"],
                "self_conj_partitions": r["self_conj_partitions"],
            }
            for atom, r in atom_invol.items()
        },
        "absolute_energy_results_top10": [
            {"formula": name, **{a: {"B_pred": r[a]["B_pred"], "err_pct": r[a]["err_pct"]}
                                    for a in ["D", "T", "3He"]},
             "max_err_pct": r["max_err_pct"]}
            for name, r in sorted_results[:10]
        ],
        "mirror_pair_results_top10": [
            {"formula": name, "diff_MeV": r["diff_MeV"], "err_pct": r["err_pct"]}
            for name, r in sorted_mirror[:10]
        ],
        "best_absolute": sorted_results[0][0],
        "best_absolute_max_err": sorted_results[0][1]["max_err_pct"],
        "best_mirror": sorted_mirror[0][0],
        "best_mirror_err": sorted_mirror[0][1]["err_pct"],
    }

    out_path = (
        repo_root / "computations"
        / "option-e-v7-involution-aware.witness.json"
    )
    with out_path.open("w") as f:
        json.dump(witness, f, indent=2)
    print(f"\nWrote {out_path}")

    print(f"\n=== Summary ===")
    print(f"  Best absolute closure: {sorted_results[0][0]} (max err {sorted_results[0][1]['max_err_pct']:.1f}%)")
    print(f"  Best mirror closure:   {sorted_mirror[0][0]} (err {sorted_mirror[0][1]['err_pct']:+.2f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
