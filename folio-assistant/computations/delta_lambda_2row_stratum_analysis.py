#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; symbolic
# polynomials live upstream in delta-lambda-empirical-tabulation.witness.json.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Proposal 1 follow-up: 2-row Wedderburn stratum analysis.

The empirical Δ_λ tabulation (delta_lambda_empirical_tabulation) found
that the dominant block per atom always has ≤ 2 rows:

  D    (n=6)  : λ* = (5, 1)
  T    (n=9)  : λ* = (6, 3)
  ³He  (n=9)  : λ* = (6, 3)
  ⁴He  (n=12) : λ* = (9, 3)

Two-row partitions are the only Wedderburn blocks of H_n(q) that
appear in the Schur-Weyl image of V = ℂ² under SU(2) restriction.
This script tests **how much of tr_M is carried by the 2-row sector
vs the > 2-row sector** for each atom, and tests sub-ansätze inside
the 2-row stratum.

Sub-ansätze (within the 2-row stratum):

  (e1) **2-row-only support**: Δ_λ ≠ 0 only for ≤ 2-row λ; pick
       λ* = single 2-row partition, sweep, report min |δ|.
  (e2) **2-row Δ-monotonic**: Δ_λ = α · c(λ) for ≤ 2-row λ only,
       Δ_λ = 0 elsewhere.  Compute α and ‖Δ‖₂ over the 2-row stratum.
  (e3) **2-row Δ-uniform**: Δ_λ = δ on all 2-row λ uniformly, 0
       elsewhere.  Tests whether a single global scalar suffices.
  (e4) **selector hypothesis**: λ*(Z, N) = max(2-row λ)
       under several candidate orderings:
         - max y_λ alone
         - max |χ^λ| alone
         - max y_λ · |χ^λ| (= ansatz a, baseline)
         - max dim_q(λ) (Plancherel-largest)
         - max f^λ (Specht dim)
         - λ closest to (3A − N, N) (the "Z+1, N" hypothesis)

Output: `delta-lambda-2row-stratum.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import functools
import json
import sys
from datetime import datetime, timezone
from math import factorial
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from q_parameter import Q_MP  # noqa: E402

Q0 = mp.mpf(str(Q_MP))


# ── Reuse partition + atom data from Proposal 1 ────────────────
# Per Copilot PR #619 review: import CAL-3 constants from
# experimental_constants module, not hardcoded.
from experimental_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV_FLOAT,
    M_P_MEV as _M_P_MEV_FLOAT,
    M_N_MEV as _M_N_MEV_FLOAT,
)
M_E_MEV = mp.mpf(str(_M_E_MEV_FLOAT))
M_P_MEV = mp.mpf(str(_M_P_MEV_FLOAT))
M_N_MEV = mp.mpf(str(_M_N_MEV_FLOAT))

ATOMS_CODATA = {
    # Anchors (LO exact by construction; ΔM = 0; included for sector-mass
    # data only — Δ_λ ansätze trivially solve to 0):
    "p":   {"Z": 1, "N": 0, "n": 3,  "M_MeV": "938.27208816"},
    "n":   {"Z": 0, "N": 1, "n": 3,  "M_MeV": "939.56542052"},
    # Compound atoms (binding-energy correction non-trivial):
    "D":   {"Z": 1, "N": 1, "n": 6,  "M_MeV": "1875.61294257"},
    "T":   {"Z": 1, "N": 2, "n": 9,  "M_MeV": "2808.92113298"},
    "3He": {"Z": 2, "N": 1, "n": 9,  "M_MeV": "2808.39160743"},
    "4He": {"Z": 2, "N": 2, "n": 12, "M_MeV": "3727.379378"},
}


from schur_weyl_symbolic import partitions_of, hook_lengths  # noqa: E402


def content_sum(lam: tuple[int, ...]) -> int:
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def is_2row(lam: tuple[int, ...]) -> bool:
    """True iff partition has at most 2 non-zero parts."""
    return len(lam) <= 2


def specht_dim(lam: tuple[int, ...]) -> int:
    """f^λ via hook-length formula."""
    n = sum(lam)
    if n == 0:
        return 1
    prod = 1
    for h in hook_lengths(lam):
        prod *= h
    return factorial(n) // prod


@functools.lru_cache(maxsize=None)
def _nfac_q_at_q0(n: int) -> mp.mpf:
    if n <= 0:
        return mp.mpf(1)
    denom = Q0 - 1 / Q0
    val = mp.mpf(1)
    for k in range(1, n + 1):
        val *= (Q0 ** k - 1 / Q0 ** k) / denom
    return val


@functools.lru_cache(maxsize=None)
def dim_q_at_q0(lam: tuple[int, ...]) -> mp.mpf:
    """dim_q(λ) at q_0 (mpmath end-to-end).  Cached + reuses [n]_q!
    factorial cache (Gemini PR #619 review)."""
    n = sum(lam)
    if n == 0:
        return mp.mpf(1)
    denom = Q0 - 1 / Q0
    nfac_q = _nfac_q_at_q0(n)
    prod_h = mp.mpf(1)
    for h in hook_lengths(lam):
        prod_h *= (Q0 ** h - 1 / Q0 ** h) / denom
    return nfac_q / prod_h


# ── Load the per-atom data from delta_lambda witness ───────────
def load_proposal_1_witness() -> dict:
    """Load the per-atom rows from delta-lambda-empirical-tabulation.witness.json."""
    path = _pb.witness_path("delta-lambda-empirical-tabulation.witness.json", HERE)
    if not path.exists():
        raise FileNotFoundError(f"missing {path} — run "
                                f"delta_lambda_empirical_tabulation.py first")
    return json.loads(path.read_text())


# ── 2-row sector analysis ──────────────────────────────────────
def analyse_2row_sector(atom: str, atom_data: dict) -> dict:
    """For one atom, split contributions by row count and test sub-ansätze."""
    n = atom_data["n"]
    target_signed = mp.mpf(atom_data["target_signed"])
    tr_M = mp.mpf(atom_data["tr_M"])
    abs_tr_M = abs(tr_M)

    # Pull per-partition c_λ data from a_single_block.candidates_top5
    # is incomplete; reconstruct from per-partition tables in the witness.
    # Rebuild via wedderburn_jones_markov to get full data for this atom.
    from wedderburn_jones_markov import global_wedderburn_sum_q_hecke_seminormal
    Z = atom_data["Z"]; N = atom_data["N"]
    # ⁴He: prefer the cached per_partition (instant) over recomputing.
    if atom == "4He":
        cached = json.loads(
            (_pb.witness_path("chi-helium-4-h12-numeric.witness.json", HERE)).read_text())
        terms = cached["per_partition"]
        for t in terms:
            t["y_at_q0"] = float(t["y_at_q0"])
            t["chi_q_at_q0"] = float(t["chi_q_at_q0"])
    else:
        _, terms = global_wedderburn_sum_q_hecke_seminormal(
            Z=Z, N=N, q_val=float(Q_MP)
        )

    # Tabulate: split by row count
    rows_by_count: dict[int, list[dict]] = {}
    sector_mass: dict[int, mp.mpf] = {}  # |Σ_λ y χ| by row count
    contribution_total = mp.mpf(0)
    for t in terms:
        lam = tuple(t["partition"])
        n_rows = len(lam)
        c_l = mp.mpf(t["y_at_q0"]) * mp.mpf(t["chi_q_at_q0"])
        rows_by_count.setdefault(n_rows, []).append({
            "lambda": list(lam),
            "y_at_q0": float(t["y_at_q0"]),
            "chi_q_at_q0": float(t["chi_q_at_q0"]),
            "contribution": float(c_l),
            "abs_contribution": float(abs(c_l)),
            "specht_dim": specht_dim(lam),
            "content_sum": content_sum(lam),
        })
        sector_mass[n_rows] = sector_mass.get(n_rows, mp.mpf(0)) + abs(c_l)
        contribution_total += abs(c_l)

    # 2-row sector total mass + fraction
    mass_2row = sum(sector_mass.get(k, mp.mpf(0)) for k in (1, 2))
    mass_gt_2row = contribution_total - mass_2row
    frac_2row = mass_2row / contribution_total if contribution_total > 0 else mp.mpf(0)

    # 2-row partitions list (sorted by |contribution| desc)
    rows_2row = []
    for k in (1, 2):
        for r in rows_by_count.get(k, []):
            rows_2row.append(r)
    rows_2row.sort(key=lambda r: -r["abs_contribution"])

    # ─── Sub-ansatz (e1) 2-row single-block sweep ───────────────
    e1_candidates = []
    for r in rows_2row:
        c_l = mp.mpf(r["contribution"])
        if abs(c_l) < mp.mpf("1e-30"):
            continue
        delta = target_signed / c_l
        e1_candidates.append({
            "lambda": r["lambda"],
            "delta": float(delta),
            "abs_delta": float(abs(delta)),
        })
    e1_candidates.sort(key=lambda x: x["abs_delta"])

    # ─── Sub-ansatz (e2) Δ-monotonic over 2-row only ────────────
    weighted_sum = mp.mpf(0)
    norm_c2 = mp.mpf(0)
    for r in rows_2row:
        c_l = mp.mpf(r["contribution"])
        cs = r["content_sum"]
        weighted_sum += c_l * cs
        norm_c2 += cs ** 2
    if abs(weighted_sum) > mp.mpf("1e-30"):
        alpha_e2 = target_signed / weighted_sum
        norm_delta_e2 = abs(alpha_e2) * mp.sqrt(norm_c2)
    else:
        alpha_e2 = mp.mpf("nan")
        norm_delta_e2 = mp.mpf("inf")

    # ─── Sub-ansatz (e3) Δ-uniform over 2-row only ──────────────
    sum_c_2row = sum(mp.mpf(r["contribution"]) for r in rows_2row)
    if abs(sum_c_2row) > mp.mpf("1e-30"):
        delta_e3 = target_signed / sum_c_2row
    else:
        delta_e3 = mp.mpf("nan")

    # ─── Sub-ansatz (e4) selector hypotheses ────────────────────
    # Restrict the search to 2-row partitions for each scoring rule.
    selectors = {
        "max_y": max(rows_2row, key=lambda r: r["y_at_q0"]),
        "max_abs_chi": max(rows_2row, key=lambda r: abs(r["chi_q_at_q0"])),
        "max_abs_contribution": max(rows_2row, key=lambda r: r["abs_contribution"]),
        "max_dim_q": max(rows_2row, key=lambda r: float(dim_q_at_q0(tuple(r["lambda"])))),
        "max_specht_dim": max(rows_2row, key=lambda r: r["specht_dim"]),
    }
    # Also test the "(3A - N, N)" canonical hypothesis
    A = Z + N
    canonical_lambda = tuple([3 * A - N, N]) if N <= 3 * A - N else tuple([N, 3 * A - N])
    canonical_match = next(
        (r for r in rows_2row if tuple(r["lambda"]) == canonical_lambda),
        None
    )
    selectors["canonical_3A_minus_N_N"] = canonical_match or {
        "lambda": list(canonical_lambda), "note": "not in 2-row stratum"
    }

    return {
        "atom": atom,
        "n": n,
        "Z": Z,
        "N": N,
        "n_partitions_total": len(terms),
        "n_partitions_2row": len(rows_2row),
        "abs_tr_M": str(abs_tr_M),
        "tr_M_signed": str(tr_M),
        "contribution_total_abs": str(contribution_total),
        "sector_mass_2row": str(mass_2row),
        "sector_mass_gt_2row": str(mass_gt_2row),
        "fraction_in_2row_sector": float(frac_2row),
        "rows_2row_top5": [
            {"lambda": r["lambda"], "y": r["y_at_q0"],
             "chi": r["chi_q_at_q0"], "abs_contrib": r["abs_contribution"]}
            for r in rows_2row[:5]
        ],
        "e1_2row_single_block_top3": e1_candidates[:3],
        "e2_2row_content_monotonic": {
            "alpha": str(alpha_e2),
            "norm_delta_2": str(norm_delta_e2),
        },
        "e3_2row_uniform": {
            "delta": str(delta_e3),
        },
        "e4_selector_hypotheses": {
            name: {"lambda": sel.get("lambda"),
                   "abs_contribution": sel.get("abs_contribution", "n/a")}
            for name, sel in selectors.items()
        },
        "canonical_3A_minus_N_N_predicted": list(canonical_lambda),
    }


def main() -> int:
    # Construct WitnessBuilder up front to capture full durationMs
    # (Copilot PR #619 review).  Engine "python": tier-2 chi data is
    # float64 from wedderburn_jones_markov; per-stratum analysis is
    # mostly mpmath but inherits float64 precision.
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("delta-lambda-2row-stratum", engine="python")
         .set_description(
            "2-row Wedderburn stratum analysis follow-up to Proposal 1's "
            "empirical Δ_λ tabulation. The dominant block per atom always "
            "lands in the 2-row stratum; this script (a) measures what "
            "fraction of |tr_M| the 2-row sector carries vs > 2-row, "
            "(b) restricts the Δ_λ ansätze to the 2-row stratum, and "
            "(c) tests several selector hypotheses inside 2-row to find "
            "the categorical rule that picks (5,1) for D, (6,3) for "
            "T+³He, (9,3) for ⁴He.  Mixed-precision: tier-2 chi data is "
            "float64 (numpy); per-row arithmetic uses mpmath but does "
            "not exceed float64 input precision."
         )
         .set_content_block("prop:rho-k-h3a-refinement"))

    print("=" * 96)
    print("  Δ_λ 2-row Wedderburn stratum analysis (Proposal 1 follow-up)")
    print("=" * 96)
    print(f"\n  q_0 = {Q0}")

    # Load Proposal 1 per-atom data
    p1 = load_proposal_1_witness()
    p1_data = p1.get("data", p1)
    per_atom_p1 = p1_data["per_atom"]

    results: dict[str, dict] = {}
    for atom in ATOMS_CODATA:
        if atom not in per_atom_p1:
            print(f"  WARN: {atom} not in Proposal 1 witness; skipping")
            continue
        print(f"\n  ── {atom} (Z={ATOMS_CODATA[atom]['Z']}, "
              f"N={ATOMS_CODATA[atom]['N']}, n={ATOMS_CODATA[atom]['n']}) ──")
        try:
            r = analyse_2row_sector(atom, per_atom_p1[atom])
        except Exception as exc:
            print(f"    ERROR: {type(exc).__name__}: {exc}")
            continue

        print(f"    n_partitions: total={r['n_partitions_total']}, "
              f"2-row={r['n_partitions_2row']}")
        print(f"    Σ |y χ| (total):    {float(r['contribution_total_abs']):.6f}")
        print(f"    Σ |y χ| (2-row):    {float(r['sector_mass_2row']):.6f}")
        print(f"    Σ |y χ| (>2-row):   {float(r['sector_mass_gt_2row']):.6e}")
        print(f"    fraction in 2-row:  {r['fraction_in_2row_sector']*100:.4f}%")
        print(f"\n    2-row top-5 by |contribution|:")
        for row in r["rows_2row_top5"]:
            print(f"      λ = {str(row['lambda']):<14} "
                  f"y = {row['y']:>10.6f}  χ = {row['chi']:>10.6f}  "
                  f"|y·χ| = {row['abs_contrib']:>10.6f}")

        print(f"\n    Sub-ansätze inside 2-row stratum:")
        print(f"      (e1) single-block min |δ|: {r['e1_2row_single_block_top3'][0]['lambda']} "
              f"|δ|={r['e1_2row_single_block_top3'][0]['abs_delta']:.4f}")
        print(f"      (e2) Δ-monotonic α(c(λ)):  α={r['e2_2row_content_monotonic']['alpha'][:14]} "
              f"‖Δ‖₂={r['e2_2row_content_monotonic']['norm_delta_2'][:14]}")
        print(f"      (e3) Δ-uniform on 2-row:   δ={r['e3_2row_uniform']['delta'][:14]}")

        print(f"\n    (e4) selector hypotheses (which 2-row λ scores highest?):")
        for name, sel in r["e4_selector_hypotheses"].items():
            print(f"      {name:<28} → λ = {sel.get('lambda')}")

        results[atom] = r

    # Cross-atom summary
    print(f"\n  ── Cross-atom 2-row stratum summary ──")
    print(f"  {'atom':<6}{'n':>3}{'frac_2row':>12}{'e1_λ*':>14}{'e1_|δ|':>14}"
          f"{'e3_uniform_δ':>16}")
    print("  " + "-" * 70)
    for atom, r in results.items():
        e1 = r['e1_2row_single_block_top3'][0] if r['e1_2row_single_block_top3'] else {}
        print(f"  {atom:<6}{r['n']:>3}{r['fraction_in_2row_sector']*100:>11.4f}%"
              f"{str(e1.get('lambda', '?')):>14}"
              f"{e1.get('abs_delta', float('nan')):>14.4f}"
              f"{r['e3_2row_uniform']['delta'][:14]:>16}")

    # Test: which selector hypothesis recovers the actual λ* per atom?
    print(f"\n  ── Selector cross-atom validation ──")
    # Actual λ* (from e1 single-block min |δ|)
    actual_lambda = {a: r['e1_2row_single_block_top3'][0]['lambda']
                     for a, r in results.items()
                     if r['e1_2row_single_block_top3']}
    selector_names = ["max_y", "max_abs_chi", "max_abs_contribution",
                      "max_dim_q", "max_specht_dim",
                      "canonical_3A_minus_N_N"]
    print(f"  {'selector':<32} " + " ".join(f"{a:>10}" for a in actual_lambda))
    for sel_name in selector_names:
        row = f"  {sel_name:<32} "
        n_match = 0
        for atom in actual_lambda:
            sel_pred = results[atom]["e4_selector_hypotheses"][sel_name].get("lambda")
            actual = actual_lambda[atom]
            match = sel_pred == actual
            if match:
                n_match += 1
            tag = "✓" if match else "✗"
            row += f"{str(sel_pred)+tag:>10} "
        row += f" [{n_match}/{len(actual_lambda)} match]"
        print(row)

    # WitnessBuilder constructed at start of main(); now populate.
    w.parameters.update({
        "q_0": str(Q0),
        "m_e_MeV": str(M_E_MEV),
        "m_p_MeV": str(M_P_MEV),
        "m_n_MeV": str(M_N_MEV),
    })
    w.add_data("per_atom", results)
    w.add_data("reference_blocks", [
        "prop:rho-k-h3a-refinement",
        "prop:sigma-shell-from-beta-chain-derivation",
        "prop:categorical-mass-markov",
    ])
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
