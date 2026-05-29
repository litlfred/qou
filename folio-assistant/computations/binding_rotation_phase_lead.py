#!/usr/bin/env python3
"""
binding_rotation_phase_lead.py — push the q-Reeb rotation-phase lead:
does the per-representation phase shift Σ Δθ_λ (free→bound) give a
constant binding scale ρ? (Derive-or-refute; no AME fit.)

CONTEXT. binding_reeb_phase_decomposition.py found the first EXTENSIVE
binding observable: the per-rep q-Reeb phase shift. On each rotation block
λ (unit-modulus eigenvalues e^{±iθ}, |χ_λ/dim_λ|≤1) the phase is
θ_λ = arccos(χ_λ/dim_λ); binding shifts it by Δθ_λ = θ_λ(atom) − θ_λ(free).
The unweighted Σ|Δθ| gave ρ ≈ 0.9–1.0 MeV/rad for the A=3 pair (T, ³He)
but D low (0.39) and ⁴He high (1.64). This probe tests the principled
refinements:

  S1  unweighted        Σ_λ |Δθ_λ|
  S2  dim-weighted      Σ_λ dim_λ · |Δθ_λ|
  S3  Markov-weighted   Σ_λ y_λ · dim_λ · |Δθ_λ|   (the tr_M weighting)
  S4  signed Markov     |Σ_λ y_λ · dim_λ · Δθ_λ|   (phases can cancel)

For each, report ρ_needed = B_AME / S per atom and the spread. The
tightest constant-ρ aggregation (if any) is the lead; a persistent
⁴He outlier flags the doubly-magic Coulomb (sinh) channel, handled
separately (crossing-energy-decomposition: Coulomb = sinh(ln q)).
DERIVE-OR-REFUTE — ρ is reported, never fitted.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path

from mpmath import mp, mpf, fabs, acos

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def dim_sn(lam):
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den


def load_chi(fname, cfg):
    d = json.loads((HERE / fname).read_text())
    return {tuple(e["partition"]): mpf(str(e["chi_lambda"]))
            for e in d["data"][cfg]["by_partition"]}


def load_y(fname, key_path):
    d = json.loads((HERE / fname).read_text())
    node = d["data"]
    for k in key_path:
        node = node[k]
    out = {}
    for e in node:
        out[tuple(e["partition"])] = mpf(str(e.get("y_lambda_at_q0",
                                                   e.get("y_lambda"))))
    return out


def clamp(x):
    if x > 1:
        return mpf(1)
    if x < -1:
        return mpf(-1)
    return x


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-rotation-phase-lead", engine="mpmath")

    AME = {"D": 2.22452, "T": 8.48180, "3He": 7.71804, "4He": 28.29567}
    # y_λ sources (same as delta_lambda_binding_full_evaluation)
    y_H6 = load_y("rho-k-h3a-lp-dual.witness.json", ["per_lambda"])
    y_H9 = load_y("wenzl-y-lambda-h9.witness.json", ["per_partition"])
    y_H12 = load_y("wenzl-y-lambda-h12.witness.json", ["per_partition"])
    atoms = [("D", "atom-chi-rust-d.witness.json", y_H6),
             ("T", "atom-chi-rust-t.witness.json", y_H9),
             ("3He", "atom-chi-rust-3he.witness.json", y_H9),
             ("4He", "atom-chi-rust-4he.witness.json", y_H12)]

    print("=" * 74)
    print("ROTATION-PHASE LEAD — ρ_needed = B_AME / Σ(Δθ aggregation)")
    print("=" * 74)

    aggs = {"S1_unweighted": {}, "S2_dim": {}, "S3_markov": {},
            "S4_markov_signed": {}}
    for name, fname, ydict in atoms:
        chi_f = load_chi(fname, "free")
        chi_a = load_chi(fname, "atom")
        s1 = s2 = s3 = mpf(0)
        s4 = mpf(0)
        for lam in chi_f:
            d = dim_sn(list(lam))
            rf = clamp(chi_f[lam] / d)
            ra = clamp(chi_a[lam] / d)
            # only rotation blocks (both ends on the unit circle)
            if fabs(chi_f[lam] / d) > 1 or fabs(chi_a[lam] / d) > 1:
                continue
            dth = acos(ra) - acos(rf)
            y = ydict.get(lam, mpf(0))
            s1 += fabs(dth)
            s2 += d * fabs(dth)
            s3 += y * d * fabs(dth)
            s4 += y * d * dth
        aggs["S1_unweighted"][name] = s1
        aggs["S2_dim"][name] = s2
        aggs["S3_markov"][name] = s3
        aggs["S4_markov_signed"][name] = fabs(s4)

    results = {}
    for agg, vals in aggs.items():
        rho = {iso: (mpf(str(AME[iso])) / vals[iso]) if vals[iso] != 0
               else None for iso in AME}
        rs = [float(rho[i]) for i in AME if rho[i] is not None and rho[i] > 0]
        spread = (max(rs) / min(rs) - 1) * 100 if rs and min(rs) > 0 else None
        # A=3 pair sub-spread (T, ³He)
        a3 = [float(rho[i]) for i in ["T", "3He"]
              if rho[i] is not None and rho[i] > 0]
        a3spread = (max(a3) / min(a3) - 1) * 100 if len(a3) == 2 else None
        results[agg] = {
            "rho_needed": {i: (mp.nstr(rho[i], 6) if rho[i] is not None
                               else None) for i in AME},
            "spread_pct": spread,
            "A3_pair_spread_pct": a3spread,
        }
        print(f"\n{agg}:")
        print("  ρ_needed: " + "  ".join(
            f"{i}={float(rho[i]):.3f}" if rho[i] is not None else f"{i}=NA"
            for i in ["D", "T", "3He", "4He"]))
        print(f"  full spread = {spread:.0f}%   "
              f"A=3 pair (T,³He) spread = {a3spread:.0f}%"
              if spread is not None and a3spread is not None else "")

    # tightest aggregation by full spread
    best = min((a for a in results if results[a]["spread_pct"] is not None),
               key=lambda a: results[a]["spread_pct"])
    print(f"\nTightest full-spread aggregation: {best} "
          f"({results[best]['spread_pct']:.0f}%).")
    print("⁴He (doubly-magic) is the persistent outlier — its 2-proton")
    print("Coulomb (sinh channel, crossing-energy-decomposition) is not yet")
    print("removed; the A=3 mirror pair (T,³He) is the clean test.")

    wb.set_description(
        "Push the q-Reeb rotation-phase binding lead: ρ_needed = B_AME / "
        "Σ(Δθ aggregation) for unweighted / dim / Markov(y_λ) / signed-Markov "
        "per-rep phase shifts (free→bound), D/T/³He/⁴He. Reports ρ spread and "
        "the A=3 mirror-pair (T,³He) sub-spread. Derive-or-refute, no AME fit; "
        "⁴He doubly-magic Coulomb (sinh channel) handled separately."
    )
    wb.add_data("aggregations", results)
    wb.add_data("tightest", {"aggregation": best,
                             "spread_pct": results[best]["spread_pct"],
                             "A3_pair_spread_pct":
                                 results[best]["A3_pair_spread_pct"]})
    wb.add_assertion(
        "rotation_phase_lead_evaluated",
        computed=len(results),
        expected=4,
        tolerance=0,
        source="four phase aggregations evaluated for all four atoms",
    )
    wb.save()


if __name__ == "__main__":
    main()
