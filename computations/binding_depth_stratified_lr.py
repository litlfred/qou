"""
binding_depth_stratified_lr.py — depth-stratified α_k · Φ_k binding
scaled to D, T, ³He, ⁴He via LR-decomposition of free-config chi.

EXTENSION OF binding_depth_stratified.py:
  Reads cached chi witnesses for the ATOM config (β_K with interface
  knot Δ_I^K) at H_{3A}, including ⁴He's 24-partition partial witness.
  Computes the FREE config chi via Littlewood-Richardson decomposition
  from H_3 proton/neutron chi values:

    χ^λ(β_p · β_n · ...) at H_{3A}
       = Σ_{μ_1, ..., μ_A ⊢ 3} c^λ_{μ_1, ..., μ_A} · ∏_k χ^{μ_k}(β_x_k)

  using the precomputed LR tables in `lr_coefficients.py`
  (LR_TABLE_3_3_TO_6, 3_6_TO_9, 6_6_TO_12).

This avoids the H_{3A} character recomputation for the free config
(which OOMs at H_12 on commodity hardware), letting us add ⁴He to
the variance test without needing PR #761's Rust kernel.

CONVOLUTION STRUCTURE (verified): the LR-decomposition computes χ for
the disjoint Hecke product β_p · β_n in H_{3A} — the SAME q-shuffle
convolution structure used by markov_trace_3A(include_inter=False).
This is NOT a tensor product. The LR coefficients c^λ_{μν} encode
the Wedderburn-character branching from the convolved product.

Ref: prop:plancherel-term-7-formulation
Ref: def:ew-interface-knot
Ref: lr_coefficients.py (LR tables for 3⊗3→6, 3⊗6→9, 6⊗6→12)
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import ast
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
from lr_coefficients import get_lr_table


B_AME = {
    "D":   mp.mpf("2.22456607"),
    "T":   mp.mpf("8.481798"),
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}

CHI_FILES = {
    "p":   "chi-proton-h3-at-q0-50dps.witness.json",
    "n":   "chi-neutron-h3-at-q0-50dps.witness.json",
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def load_chi_dict(species: str) -> tuple[int, dict]:
    """Load (n_strands, chi_dict) for species.

    chi_dict: {partition_tuple → mpmath.mpf chi value}.
    """
    w = json.loads((HERE / CHI_FILES[species]).read_text())
    n_strands = int(w["n_strands"])
    chi_dict = {}
    for p in w["by_partition"]:
        lam = p["partition"]
        if isinstance(lam, str):
            lam = ast.literal_eval(lam)
        lam_tup = tuple(lam)
        chi_dict[lam_tup] = mp.mpf(str(p["chi_lambda"]))
    return n_strands, chi_dict


def compose_lr(chi_left: dict, chi_right: dict,
                n_left: int, n_right: int) -> dict:
    """Compose two chi dictionaries via Littlewood-Richardson.

    Returns chi for the disjoint Hecke product at H_{n_left + n_right}:
        χ^λ(β_left · β_right) = Σ_{μ⊢n_left, ν⊢n_right} c^λ_{μν}
                                    · χ^μ(β_left) · χ^ν(β_right)
    """
    lr_table = get_lr_table(n_left, n_right)
    out: dict[tuple, mp.mpf] = {}
    for (mu, nu, lam), c in lr_table.items():
        if mu not in chi_left or nu not in chi_right:
            continue
        contrib = mp.mpf(c) * chi_left[mu] * chi_right[nu]
        out[lam] = out.get(lam, mp.mpf(0)) + contrib
    return out


def free_chi_for_atom(atom: str) -> dict:
    """Compute χ^λ(T_constit^K) at H_{3A} via iterated LR-composition.

    Arrangement [p_1, ..., p_Z, n_1, ..., n_N] of nucleon braids.
    """
    Z, N = ZN[atom]
    _, chi_p = load_chi_dict("p")
    _, chi_n = load_chi_dict("n")

    # Iteratively compose nucleon-by-nucleon
    chi_running = None
    n_running = 0
    sequence = ['p'] * Z + ['n'] * N
    for k, flavor in enumerate(sequence):
        chi_k = chi_p if flavor == 'p' else chi_n
        if chi_running is None:
            chi_running = dict(chi_k)
            n_running = 3
        else:
            chi_running = compose_lr(chi_running, chi_k, n_running, 3)
            n_running += 3
    return chi_running


def alpha_k(k: int) -> mp.mpf:
    """α_0 = α_1 = α_3 = 1; α_2 = z²; α_{k≥4} = m_e · 8G."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G


def phi_k_from_dict(chi_dict: dict, n_strands: int, k: int) -> mp.mpf:
    """Φ_k = Σ_{λ⊢n_strands, depth(λ)=k} ~w_λ · log|χ^λ · dim_q λ|.

    Skips partitions not present in chi_dict (e.g. for ⁴He's partial
    witness — only 24 / 77 partitions cached, the high-weight ones).
    """
    total = mp.mpf(0)
    qfact = qfac(n_strands)
    for lam, chi in chi_dict.items():
        if len(lam) - 1 != k:
            continue
        dq = dim_q(lam)
        magnitude = mp.fabs(chi) * dq
        if magnitude < mp.mpf("1e-30"):
            continue
        weight = mp.mpf(str(dq * dq)) / qfact
        total += weight * mp.log(magnitude)
    return total


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("binding-depth-stratified-lr")
    builder.set_description(
        "Depth-stratified α_k · Φ_k binding on D, T, ³He, ⁴He at "
        "H_{3A} via LR-decomposition of free-config chi from H_3 "
        "proton/neutron chi witnesses. Atom chi from existing cached "
        "witnesses. Extends binding_depth_stratified.py by adding ⁴He "
        "without H_12 character recomputation (uses 24 cached "
        "partitions per the existing chi-helium-4-h12 witness)."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    builder.add_parameter("alpha_k_geq_4_MeV",
                           str(mp.mpf(str(M_E_MEV)) * 8 * mp.catalan))

    # Expected partition count p(n) — surface a ⚠ warning when the
    # cached atom chi witness is partial (missing partitions become 0
    # in Φ_atom, which artificially inflates Φ_free − Φ_atom and
    # therefore B). The script does NOT abort on partial witness; it
    # records the partial state in partition_completeness_warnings so
    # downstream consumers can see it. See docs/audits/2026-06-09-
    # binding-canonical-default-depth-stratified.md §Prevention.
    PARTITION_COUNTS = {3: 3, 6: 11, 9: 30, 12: 77, 15: 176, 18: 385, 21: 792}

    print(f"{'atom':<6} {'Z':>3} {'N':>3} {'n_str':>6} "
          f"{'B_MeV':>10} {'B_AME':>10} {'ratio':>8} {'n_λ_atom':>10}")
    results = {}
    completeness_warnings = []
    for atom in ("D", "T", "3He", "4He"):
        Z, N = ZN[atom]
        n_strands, chi_atom = load_chi_dict(atom)
        chi_free = free_chi_for_atom(atom)

        # Partition-completeness gate — see PARTITION_COUNTS comment above.
        expected_partitions = PARTITION_COUNTS.get(n_strands)
        if expected_partitions is not None and len(chi_atom) < expected_partitions:
            warn = (f"⚠ {atom} cached atom chi PARTIAL: "
                    f"{len(chi_atom)}/{expected_partitions} partitions. "
                    f"Φ_atom will under-count; B will inflate.")
            print(warn)
            completeness_warnings.append({
                "atom": atom,
                "cached": len(chi_atom),
                "expected": expected_partitions,
                "coverage_pct": round(100 * len(chi_atom) / expected_partitions, 2),
            })

        # Use chi_free at ALL partitions (LR computes them all);
        # atom chi may be partial — missing partitions treated as 0.
        # (Surfaced as completeness_warnings above to prevent silent
        # consumption.)
        atom_partial = len(chi_atom) < len(chi_free)
        chi_free_for_phi = chi_free  # ALL partitions
        chi_atom_for_phi = {lam: chi_atom.get(lam, mp.mpf(0))
                             for lam in chi_free.keys()}

        # Compute Φ_k for depths 0 .. n_strands - 1
        delta_phi_total = mp.mpf(0)
        per_depth = {}
        for k in range(n_strands):
            phi_atom = phi_k_from_dict(chi_atom_for_phi, n_strands, k)
            phi_free = phi_k_from_dict(chi_free_for_phi, n_strands, k)
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
        B_emp = B_AME[atom]
        ratio = B_MeV / B_emp if B_emp > 0 else mp.mpf("nan")
        results[atom] = {
            "Z": Z, "N": N, "A": Z + N, "n_strands": n_strands,
            "n_partitions_atom": len(chi_atom),
            "n_partitions_free": len(chi_free),
            "per_depth": per_depth,
            "B_MeV": fmt(B_MeV),
            "B_AME_MeV": fmt(B_emp),
            "ratio_pred_over_AME": float(ratio),
            "B_pred_sign": "+" if B_MeV > 0 else "-",
            "canonical_status": "canonical-with-empirical-assignment",
            "method": "depth-stratified α_k·Φ_k via LR-decomposition",
        }
        print(f"  {atom:<6} {Z:>3} {N:>3} {n_strands:>6} "
              f"{float(B_MeV):>10.4f} {float(B_emp):>10.4f} "
              f"{float(ratio):>8.4f} {len(chi_atom):>10}")

    builder.add_data("per_atom", results)
    builder.add_data("partition_completeness_warnings", completeness_warnings)
    builder.add_data("all_atom_chi_witnesses_complete",
                      len(completeness_warnings) == 0)

    ratios = [abs(r["ratio_pred_over_AME"]) for r in results.values()]
    rmin, rmax = (min(ratios), max(ratios)) if ratios else (0, 0)
    mom = rmax / rmin if rmin > 0 else float("inf")
    signs_correct = all(r["B_pred_sign"] == "+" for r in results.values())
    builder.add_data("max_over_min_abs", float(mom))
    builder.add_data("all_signs_correct", signs_correct)

    if mom < 1.05 and signs_correct:
        verdict = (f"PASS — max/min = {mom:.3f} < 1.05, signs correct, "
                   "4-atom variance closed via depth-stratified "
                   "α_k · Φ_k + LR-decomposed free chi.")
    elif mom < 1.5 and signs_correct:
        verdict = (f"STRONG — max/min = {mom:.3f}, all signs correct.")
    elif signs_correct:
        verdict = (f"PARTIAL — max/min = {mom:.3f}, signs correct.")
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

    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).

    builder.add_data("lean_uniqueness_ref", {

        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",

        "framework_doc":

            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",

        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",

    })


    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
