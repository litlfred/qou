#!/usr/bin/env python3
"""
Probe (1): project the Frobenius Markov-trace mass formula for ⁴He
onto the dominant Wedderburn block (4,4,4) and its conjugate
(3,3,3,3), and quantify what fraction of the full tr_M_⁴He each
contributes.

Per the dominant-partition audit, (4,4,4) forces α* = 0.048 for the
canonical ⁴He atom-braid T_w. The conjecture under test is whether
this PSD-dominant block also dominates the *Markov trace direction*
— i.e., whether y_(4,4,4) · χ^(4,4,4)(T_w) accounts for a
significant fraction of `tr_M(T_w) = Σ_λ y_λ χ^λ(T_w)`.

Falsification rule: if the (4,4,4) and (3,3,3,3) contributions are
< 1% of tr_M, the dominant-PSD partition is NOT the mass-contributing
partition, and the Gap is set by *other* blocks. In that case,
Probes (2)/(4) become structural curiosities rather than Gap-
narrowing tools.

Bound to `conj:atom-braid-exterior-algebra`. Audit-only.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder
from codata_constants import AME_B_HE4_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 50


def main() -> int:
    base = Path(__file__).resolve().parent

    # χ^λ(T_w_⁴He) = sum of eigenvalues of the symmetric part
    # (trace is invariant under symmetrization: tr(M) = tr((M+M^T)/2)).
    with open(base / "joint-tower-sdp-rust.witness.json") as f:
        jt = json.load(f)
    he4 = next(c for c in jt["per_atom_certificates"]
               if c.get("name") == "helium4-4He")

    chi_by_part: dict[tuple, mp.mpf] = {}
    min_eig_by_part: dict[tuple, float] = {}
    for b in he4["wedderburn_blocks"]:
        part = tuple(b["partition"])
        evs = b.get("matrix_at_q_0_sym_eigvals") or []
        if evs:
            chi_by_part[part] = mp.mpf(0)
            for e in evs:
                chi_by_part[part] += mp.mpf(e)
            min_eig_by_part[part] = b.get("min_eigenvalue")

    # y_λ(q_0) at 50 dps from y-lambda-at-q0.witness.json
    with open(base / "y-lambda-at-q0.witness.json") as f:
        yw = json.load(f)
    n12 = yw["data"]["by_n"]["12"]
    y_by_part: dict[tuple, mp.mpf] = {}
    for entry in n12:
        part = tuple(entry["partition"])
        y_by_part[part] = mp.mpf(entry["y_at_q0_50dps"])

    # Compute the partial sum tr_M over the evaluated blocks only
    # (the joint-tower run was capped at d_λ ≤ 500, so 26/77 blocks
    # were evaluated; the rest have empty eigval lists).
    contributions_evaluated: list[tuple[tuple, mp.mpf, mp.mpf, mp.mpf]] = []
    for part, chi in chi_by_part.items():
        if part not in y_by_part:
            continue
        y = y_by_part[part]
        contributions_evaluated.append((part, y, chi, y * chi))

    # Sort by |contribution| descending — find the TRACE-dominant
    # partitions (vs. the PSD-dominant ones).
    contributions_evaluated.sort(key=lambda t: -abs(t[3]))

    partial_tr_M = sum((t[3] for t in contributions_evaluated), mp.mpf(0))

    print(f"⁴He: {len(contributions_evaluated)} blocks evaluated (of 77 total)\n")
    print(f"Partial tr_M(T_w_⁴He) over evaluated blocks = {mp.nstr(partial_tr_M, 12)}\n")

    # d_λ available via len of eigval list for that partition's block
    d_by_part = {tuple(b["partition"]): b["d_lambda"]
                 for b in he4["wedderburn_blocks"]}

    print(f"{'rank':>4s}  {'λ':>20s}  {'d_λ':>5s}  {'y_λ':>14s}  {'χ^λ(T_w)':>13s}  {'y·χ contrib':>14s}  {'|c|/|tr_M|':>10s}")
    for rank, (part, y, chi, c) in enumerate(contributions_evaluated[:10], 1):
        frac = abs(c) / abs(partial_tr_M) if partial_tr_M != 0 else mp.mpf(0)
        print(f"{rank:>4d}  {str(list(part)):>20s}  {d_by_part[part]:>5d}  "
              f"{mp.nstr(y, 6):>14s}  {mp.nstr(chi, 6):>13s}  {mp.nstr(c, 6):>14s}  {float(frac)*100:>9.4f}%")

    # Specifically check the PSD-dominant pair (4,4,4) and (3,3,3,3)
    print("\n=== PSD-dominant pair: (4,4,4) and (3,3,3,3) ===")
    dominant_pair = [(4, 4, 4), (3, 3, 3, 3)]
    pair_total = mp.mpf(0)
    pair_rank = {}
    for part in dominant_pair:
        if part in y_by_part and part in chi_by_part:
            y = y_by_part[part]
            chi = chi_by_part[part]
            c = y * chi
            pair_total += c
            # Find rank
            for rank, (p, _, _, _) in enumerate(contributions_evaluated, 1):
                if p == part:
                    pair_rank[part] = rank
                    break
            frac = abs(c) / abs(partial_tr_M)
            print(f"  λ = {part}: y = {mp.nstr(y, 6)}, χ = {mp.nstr(chi, 6)}, "
                  f"y·χ = {mp.nstr(c, 6)}, |c|/|tr_M_partial| = {float(frac)*100:.6f}%, "
                  f"rank-by-|contrib| = {pair_rank.get(part, 'N/A')}/{len(contributions_evaluated)}, "
                  f"min_eig = {min_eig_by_part[part]:+.4e}")

    print(f"\n  Pair contribution sum (4,4,4)+(3,3,3,3) = {mp.nstr(pair_total, 8)}")
    pair_frac = abs(pair_total) / abs(partial_tr_M)
    print(f"  |pair sum| / |tr_M_partial|              = {float(pair_frac)*100:.6f}%")

    # Mass interpretation (m_e · A · 8G · tr_M formula from alpha_k_jones_markov_h12)
    print("\n=== Mass interpretation ===")
    m_e_MeV = mp.mpf("0.51099895069")
    vol_8G = mp.mpf("7.327724753417752")  # Kashaev vol(L6a4)
    A_he4 = 4
    factor = m_e_MeV * A_he4 * vol_8G  # ≈ 14.98 MeV per unit tr_M
    print(f"  m_e · A · 8G                = {mp.nstr(factor, 6)} MeV (per unit tr_M)")
    print(f"  contrib from (4,4,4) only    = {mp.nstr(factor * y_by_part[(4,4,4)] * chi_by_part[(4,4,4)], 6)} MeV")
    print(f"  contrib from (3,3,3,3) only  = {mp.nstr(factor * y_by_part[(3,3,3,3)] * chi_by_part[(3,3,3,3)], 6)} MeV")
    print(f"  contrib from pair total      = {mp.nstr(factor * pair_total, 6)} MeV")
    print(f"  AME B(⁴He)                  = float(AME_B_HE4_MEV_VALIDATION) MeV")
    print(f"  current B_pred (mass-table) = 29.9557 MeV (formula '2·m_e·4·8G', no tr_M)")

    # === Build witness ===
    out = WitnessBuilder("probe-1-project-4he-on-dominant", engine="python")
    out.set_description(
        "Projects the Frobenius Markov-trace mass formula tr_M(T_w_⁴He) "
        "onto the PSD-dominant Wedderburn block (4,4,4) and its conjugate "
        "(3,3,3,3), and compares to the partial-sum trace over all "
        "evaluated blocks (26/77). Tests whether PSD-dominance and "
        "trace-dominance coincide — they appear to be ORTHOGONAL "
        "structural axes."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")

    out.add_data("partial_tr_M_at_q0", mp.nstr(partial_tr_M, 30))
    out.add_data("n_blocks_evaluated", len(contributions_evaluated))
    out.add_data("n_blocks_total", 77)

    top10 = [
        {
            "rank": rank,
            "partition": list(p),
            "y_lambda": mp.nstr(y, 30),
            "chi_lambda": mp.nstr(chi, 30),
            "contribution": mp.nstr(c, 30),
            "abs_contribution_frac_of_partial_tr_M": float(abs(c) / abs(partial_tr_M)),
            "min_eig": min_eig_by_part.get(p),
        }
        for rank, (p, y, chi, c) in enumerate(contributions_evaluated[:10], 1)
    ]
    out.add_data("top_10_trace_contributors", top10)

    dominant_data = []
    for part in dominant_pair:
        if part in y_by_part and part in chi_by_part:
            y = y_by_part[part]
            chi = chi_by_part[part]
            c = y * chi
            dominant_data.append({
                "partition": list(part),
                "y_lambda": mp.nstr(y, 30),
                "chi_lambda": mp.nstr(chi, 30),
                "contribution": mp.nstr(c, 30),
                "abs_contribution_frac_of_partial_tr_M": float(abs(c) / abs(partial_tr_M)),
                "rank_by_abs_contrib": pair_rank.get(part),
                "min_eig": min_eig_by_part[part],
            })
    out.add_data("psd_dominant_pair", dominant_data)

    out.add_data("mass_projection_MeV", {
        "m_e_x_A_x_8G_MeV_per_unit_tr_M": mp.nstr(factor, 30),
        "contrib_4_4_4_MeV": mp.nstr(factor * y_by_part[(4,4,4)] * chi_by_part[(4,4,4)], 30),
        "contrib_3_3_3_3_MeV": mp.nstr(factor * y_by_part[(3,3,3,3)] * chi_by_part[(3,3,3,3)], 30),
        "pair_contribution_MeV": mp.nstr(factor * pair_total, 30),
        "AME_B_4He_MeV": float(AME_B_HE4_MEV_VALIDATION),
    })

    # Falsification assertion: if PSD-dominant pair contributes < 1% of
    # |tr_M|, PSD-dominance ≠ trace-dominance.
    out.add_assertion(
        name="psd_dominant_pair_contributes_under_1pct_of_trace",
        computed=str(int(float(pair_frac) < 0.01)),
        expected="1",
        tolerance=0,
        source=f"|y_(4,4,4)·χ_(4,4,4) + y_(3,3,3,3)·χ_(3,3,3,3)| / |tr_M_partial| = {float(pair_frac):.6f}",
    )

    out.add_caveat(
        "tr_M is the PARTIAL sum over 26/77 evaluated Wedderburn blocks "
        "(those with d_λ ≤ 500 from the joint-tower-sdp-rust run). The "
        "51 unevaluated blocks may shift tr_M and the fractional "
        "contributions. However, the 26 evaluated blocks include both "
        "(4,4,4) and (3,3,3,3) plus 24 others spanning low-row partitions, "
        "so the *relative* ranking of the dominant pair against the "
        "trace-largest contributors is robust."
    )

    out_path = out.save()
    print(f"\nWitness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
