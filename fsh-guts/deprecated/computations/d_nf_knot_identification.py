#!/usr/bin/env python3
"""
Identify named knots in D's NF decomposition from existing witness data.

Uses the 32 NF basis words stored in d-nf-weighted-vol.witness.json
(each basis word's coefficient c_w(q₀) and V_hyp(closure)).  Groups
basis words by Vol, then cross-references with SnapPy's LowDimCensus
to assign named-knot labels.

For each unique Vol that appears in D's NF, we report:
  • the named knot(s) matching that Vol
  • the list of NF basis words that produce it
  • the sum of their c_w(q₀) coefficients
  • the Thurston additive decomposition (basis × Vol)

Output: d-nf-knot-identification.witness.json
"""
from __future__ import annotations

import json
import sys
import warnings
from collections import defaultdict
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import snappy

from witness_base import WitnessBuilder


def census_lookup(vol: float, tol: float = 1e-4) -> list[str]:
    """Return LowDimCensus names with volumes within tol of vol."""
    if vol is None or abs(vol) < 1e-4:
        return []
    matches = []
    # Try up to 7-tetrahedra census (covers all low-crossing hyperbolic pieces)
    for tets_max in [4, 5, 6, 7]:
        try:
            for M in snappy.OrientableCuspedCensus(tets=tets_max):
                try:
                    v = float(M.volume())
                    if abs(v - vol) < tol:
                        matches.append(M.name())
                except Exception:
                    pass
        except Exception:
            pass
    # Try named knot complements too
    for name in ["4_1", "5_2", "6_1", "6_2", "6_3",
                 "7_1", "7_2", "7_3", "7_4", "7_5", "7_6", "7_7",
                 "8_11", "8_12", "8_13", "8_14",
                 "L2a1", "L4a1", "L5a1", "L6a1", "L6a2", "L6a3", "L6a4",
                 "L6a5", "L6n1", "L7a1", "L7a2", "L7a3", "L7a4",
                 "L7a5", "L7a6", "L7a7", "L7n1", "L7n2"]:
        try:
            M = snappy.Manifold(name)
            v = float(M.volume())
            if abs(v - vol) < tol:
                matches.append(name)
        except Exception:
            pass
    # Dedupe
    seen = set()
    out = []
    for m in matches:
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out


def main():
    witness_in = Path(__file__).parent / "d-nf-weighted-vol.witness.json"
    data = json.loads(witness_in.read_text())

    nf_terms = data["nf_terms"]
    print(f"D's NF: {len(nf_terms)} basis words")
    print()

    # Group by V_hyp_float (non-zero only)
    by_vol: dict[float, list] = defaultdict(list)
    for t in nf_terms:
        v = t.get("V_hyp_float")
        if v is None:
            continue
        if abs(v) < 1e-4:
            continue  # trivial / non-hyperbolic
        # Bucket by rounded volume
        key = round(v, 4)
        by_vol[key].append(t)

    # Sort unique volumes
    print(f"{'Vol':>10}  {'# NF words':>10}  {'# comps':>8}  {'named knot match':<40}  "
          f"{'Σ c_w(q₀)':>15}")
    print("-" * 100)
    rows = []
    for vol in sorted(by_vol.keys()):
        terms = by_vol[vol]
        comps_all = sorted({t.get("n_components") for t in terms})
        names = census_lookup(vol)
        sum_cw = sum(float(t["c_w_q0"]) for t in terms)
        basis_list = [t["basis"] for t in terms]
        name_str = ", ".join(names) if names else "(no named match)"
        print(f"{vol:>10.4f}  {len(terms):>10}  {str(comps_all):>8}  "
              f"{name_str:<40}  {sum_cw:>+15.6f}")
        rows.append({
            "V_hyp": vol,
            "n_basis_words": len(terms),
            "basis_words": basis_list,
            "components": comps_all,
            "named_matches": names,
            "sum_c_w_q0": sum_cw,
        })

    # Overall weighted sum check
    overall_sum = sum(float(t["contribution"]) for t in nf_terms)
    print()
    print(f"Overall Σ c_w · V_hyp(ŵ): {overall_sum:+.6f}")
    print(f"Target (B_AME / m_e):    {data['parameters']['target_vol']:+.6f}")
    print(f"Relative error:           {data['relative_error_pct']:+.2f}%")

    # Top NF terms by |contribution|
    print()
    print("Top 5 NF terms by |contribution| = |c_w · V_hyp|:")
    sorted_terms = sorted(nf_terms, key=lambda t: abs(float(t.get("contribution", 0))),
                           reverse=True)
    print(f"{'basis':<24} {'V_hyp':>10}  {'c_w(q₀)':>12}  {'contribution':>14}  knots")
    print("-" * 90)
    for t in sorted_terms[:5]:
        v = t.get("V_hyp_float", 0)
        if v is None:
            v = 0
        names = census_lookup(v) if v > 1e-4 else []
        nm = ", ".join(names) if names else ""
        print(f"{str(t['basis']):<24} {v:>10.4f}  "
              f"{float(t['c_w_q0']):>+12.6f}  "
              f"{float(t['contribution']):>+14.6f}  {nm}")

    w = WitnessBuilder("d-nf-knot-identification", engine="snappy+census")
    w.set_description(
        "Map the 32 NF basis words of D (from d-nf-weighted-vol.witness.json) "
        "to named hyperbolic knots via SnapPy census. Groups by V_hyp; "
        "reports Σ c_w(q₀) per unique volume class and the Thurston-additive "
        "prediction sum."
    )
    w.add_data("nf_volume_classes", rows)
    w.add_data("overall_sum_c_w_V", overall_sum)
    w.add_data("target_vol", data['parameters']['target_vol'])
    w.add_data("relative_error_pct", data['relative_error_pct'])
    w.save()


if __name__ == "__main__":
    main()
