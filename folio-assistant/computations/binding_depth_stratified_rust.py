"""
binding_depth_stratified_rust.py — depth-stratified α_k · Φ_k binding
using the FULL H_{3A} chi witnesses from the Rust kernel (PR #761
cherry-pick). Closes the ⁴He gap (and any A=4-5 atom whose atom-chi
witness is computed via compute_atom_chi_rust.py).

EXTENSION OF binding_depth_stratified.py:
  Reads full atom-chi-rust-{atom}.witness.json (all p(3A) partitions
  at f64 precision via Geck-Pfeiffer + Hoefsmit seminormal Rust kernel)
  for BOTH atom (include_inter=True) and free (include_inter=False)
  configs. Applies the depth-stratified α_k · Φ_k formula at H_{3A}
  with α_{k≥4} = m_e · 8G damping.

CONVOLUTION STRUCTURE: both atom and free chi computed by the SAME
chi_q_atomic Rust function on the SAME H_{3A} braid word — only
toggling whether interface-knot crossings (at gens 3k+2) are
populated. q-shuffle convolution structure, NOT a tensor product.

USAGE:
    python3 compute_atom_chi_rust.py 4He    # generate the witness
    python3 binding_depth_stratified_rust.py   # consume + variance

For atoms beyond cached (6Li, 7Li, etc.), run compute_atom_chi_rust.py
first.

Ref: prop:plancherel-term-7-formulation
Ref: PR #761 (Rust kernel cherry-picked)
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_LI6_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from _precision import set_compute_dps, fmt
from witness_base import WitnessBuilder
from codata_constants import M_E_MEV
from mass_at_3A_proper import dim_q, qfac, E_0_CALIBRATION_MEV
from q_parameter import Q as Q0


B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
    "6Li": AME_B_LI6_MEV_VALIDATION,
    "7Li": mp.mpf("39.2453"),
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
      "6Li": (3, 3), "7Li": (3, 4)}


def alpha_k(k: int) -> mp.mpf:
    """α_0 = α_1 = α_3 = 1; α_2 = z²; α_{k≥4} = m_e · 8G."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G


def phi_k_from_list(by_partition: list, n_strands: int, k: int) -> mp.mpf:
    """Φ_k = Σ_{depth(λ)=k} ~w_λ · log|χ^λ · dim_q λ|."""
    total = mp.mpf(0)
    qfact = qfac(n_strands)
    for p in by_partition:
        shape = tuple(p["partition"])
        if len(shape) - 1 != k:
            continue
        chi = mp.mpf(str(p["chi_lambda"]))
        dq = dim_q(shape)
        magnitude = mp.fabs(chi) * dq
        if magnitude < mp.mpf("1e-30"):
            continue
        weight = mp.mpf(str(dq * dq)) / qfact
        total += weight * mp.log(magnitude)
    return total


def compute_atom_binding_rust(atom: str) -> dict:
    """Read Rust witness for atom + apply depth-stratified formula."""
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True,
                "reason": f"Run compute_atom_chi_rust.py {atom} first"}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]

    delta_phi_total = mp.mpf(0)
    per_depth = {}
    for k in range(n_strands):
        phi_atom = phi_k_from_list(atom_data["by_partition"], n_strands, k)
        phi_free = phi_k_from_list(free_data["by_partition"], n_strands, k)
        delta = phi_free - phi_atom
        ak = alpha_k(k)
        contrib = ak * delta
        if mp.fabs(delta) > mp.mpf("1e-12"):
            per_depth[k] = {
                "alpha_k": fmt(ak),
                "phi_atom": fmt(phi_atom),
                "phi_free": fmt(phi_free),
                "delta_phi": fmt(delta),
                "contrib": fmt(contrib),
            }
        delta_phi_total += contrib

    B_MeV = delta_phi_total
    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "n_partitions": len(atom_data["by_partition"]),
        "per_depth": per_depth,
        "B_MeV": fmt(B_MeV),
        "B_pred_sign": "+" if B_MeV > 0 else "-",
        "engine": "Rust geck_pfeiffer + Hoefsmit seminormal (f64)",
        "canonical_status": "canonical-with-empirical-assignment",
    }


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("binding-depth-stratified-rust")
    builder.set_description(
        "Depth-stratified α_k · Φ_k binding with full H_{3A} chi from "
        "Rust kernel (compute_atom_chi_rust.py). Closes ⁴He H_12 "
        "(53/77 partitions previously missing) via PR #761 cherry-pick."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))

    print(f"{'atom':<6} {'Z':>3} {'N':>3} {'n_str':>6} "
          f"{'B_MeV':>10} {'B_AME':>10} {'ratio':>8} {'n_λ':>5}")

    results = {}
    for atom in ("D", "T", "3He", "4He", "6Li", "7Li"):
        r = compute_atom_binding_rust(atom)
        if r.get("deferred"):
            msg = f"(no Rust witness yet — run compute_atom_chi_rust.py {atom})"
            print(f"  {atom:<6} {msg}")
            results[atom] = r
            continue
        B_pred = mp.mpf(r["B_MeV"])
        B_emp = B_AME.get(atom, mp.mpf(0))
        ratio = B_pred / B_emp if B_emp > 0 else mp.mpf("nan")
        r["B_AME_MeV"] = fmt(B_emp)
        r["ratio_pred_over_AME"] = float(ratio)
        results[atom] = r
        print(f"  {atom:<6} {r['Z']:>3} {r['N']:>3} {r['n_strands']:>6} "
              f"{float(B_pred):>10.4f} {float(B_emp):>10.4f} "
              f"{float(ratio):>8.4f} {r['n_partitions']:>5}")

    builder.add_data("per_atom", results)

    valid = {k: r for k, r in results.items() if not r.get("deferred")}
    ratios = [abs(r["ratio_pred_over_AME"]) for r in valid.values()]
    rmin, rmax = (min(ratios), max(ratios)) if ratios else (0, 0)
    mom = rmax / rmin if rmin > 0 else float("inf")
    signs_correct = all(r["B_pred_sign"] == "+" for r in valid.values())
    builder.add_data("atoms_evaluated", list(valid.keys()))
    builder.add_data("max_over_min_abs", float(mom))
    builder.add_data("all_signs_correct", signs_correct)

    if mom < 1.05 and signs_correct:
        verdict = f"PASS — max/min = {mom:.3f} < 1.05, all signs correct."
    elif mom < 1.5 and signs_correct:
        verdict = f"STRONG — max/min = {mom:.3f}, signs correct."
    elif signs_correct:
        verdict = f"PARTIAL — max/min = {mom:.3f}, signs correct."
    else:
        verdict = (f"max/min = {mom:.3f}, "
                   f"signs_correct = {signs_correct}")
    builder.add_data("verdict", verdict)
    print(f"\n  max/min |ratio| = {mom:.4f}")
    print(f"  All signs +:    {signs_correct}")
    print(f"  Verdict: {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=float(B_AME["D"]),
        expected=2.22456607,
        tolerance=1e-10,
        unit="B(D) MeV",
        source="AME 2020 deuteron binding",
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
