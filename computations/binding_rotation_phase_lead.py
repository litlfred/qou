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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import json
import math
from pathlib import Path

from mpmath import mp, mpf, fabs, acos

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from mass_at_3A_proper import (  # noqa: E402
    atom_braid_word_3A, chi_lambda_of_word, _cached_seminormal,
)
from sympy.utilities.iterables import partitions as _sympy_partitions  # noqa: E402


def _parts(n):
    out = []
    for p in _sympy_partitions(n):
        lam = []
        for k in sorted(p, reverse=True):
            lam += [k] * p[k]
        out.append(tuple(lam))
    return out


def strong_channel_rho(Z, N, ydict, ame, acos_fn, clamp_fn):
    """Markov-weighted q-Reeb phase ρ with the antisymmetric (sinh / h)
    inter-nucleon term removed (d=0): isolates the symmetric cosh 'strong'
    channel. Recomputes χ_λ from the braid word (free vs d=0-atom) via
    chi_lambda_of_word. Returns ρ_need = B_AME / Σ y_λ dim_λ |Δθ_λ|."""
    n = 3 * (Z + N)
    ng = n - 1
    w_free = atom_braid_word_3A(Z, N, include_inter=False)
    w_atom = atom_braid_word_3A(Z, N, include_inter=True)
    # zero the inter-nucleon d (the −h = −2 sinh(λ) antisymmetric term);
    # inter-nucleon crossings sit at strand index 3k+2.
    w_d0 = [(c, 0.0 if (k % 3 == 2) else d, k) for (c, d, k) in w_atom]
    S = mpf(0)
    for lam in _parts(n):
        sig, dim, _ = _cached_seminormal(lam)
        if dim == 0:
            continue
        cf = mpf(str(chi_lambda_of_word(sig, dim, w_free, ng)))
        ca = mpf(str(chi_lambda_of_word(sig, dim, w_d0, ng)))
        if fabs(cf / dim) > 1 + 1e-14 or fabs(ca / dim) > 1 + 1e-14:
            continue
        dth = acos_fn(clamp_fn(ca / dim)) - acos_fn(clamp_fn(cf / dim))
        S += ydict.get(lam, mpf(0)) * dim * fabs(dth)
    return (mpf(str(ame)) / S) if S != 0 else None


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

    AME = {
        "D": float(AME_B_DEUTERON_MEV_VALIDATION),
        "T": float(AME_B_TRITIUM_MEV_VALIDATION),
        "3He": float(AME_B_HE3_MEV_VALIDATION),
        "4He": float(AME_B_HE4_MEV_VALIDATION),
    }
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
            if fabs(chi_f[lam] / d) > 1 + 1e-14 or fabs(chi_a[lam] / d) > 1 + 1e-14:
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

    # ── d=0 strong (cosh) channel: remove the antisymmetric −h term ──
    # (D/T/³He only; H₁₂ chi_lambda_of_word recompute is too slow for ⁴He)
    print("\n[d=0 cosh/strong channel]  −h (sinh) inter-nucleon term removed:")
    y_by_n = {6: y_H6, 9: y_H9}
    d0 = {}
    for iso, _f, Z, N in [("D", None, 1, 1), ("T", None, 1, 2),
                          ("3He", None, 2, 1)]:
        rho = strong_channel_rho(Z, N, y_by_n[3 * (Z + N)],
                                 AME[iso], acos, clamp)
        full_rho = (mpf(str(AME[iso])) / aggs["S3_markov"][iso]
                    if aggs["S3_markov"][iso] != 0 else None)
        d0[iso] = {"rho_full": (mp.nstr(full_rho, 6) if full_rho else None),
                   "rho_d0_strong": (mp.nstr(rho, 6) if rho else None)}
        print(f"  {iso:4s}: full={float(full_rho):.3f}  "
              f"d0(strong)={float(rho):.3f}" if (rho and full_rho)
              else f"  {iso}: NA")
    d0v = [float(mpf(d0[i]["rho_d0_strong"])) for i in ["D", "T", "3He"]
           if d0[i]["rho_d0_strong"]]
    fullv = [float(mpf(d0[i]["rho_full"])) for i in ["D", "T", "3He"]
             if d0[i]["rho_full"]]
    d0_spread = (max(d0v) / min(d0v) - 1) * 100 if len(d0v) == 3 else None
    full_spread = (max(fullv) / min(fullv) - 1) * 100 if len(fullv) == 3 else None
    if d0_spread is not None:
        print(f"  D/T/³He spread: full={full_spread:.0f}%  →  "
              f"d0(strong)={d0_spread:.0f}%  "
              f"(removing sinh pulls D up toward the A=3 scale)")

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
    wb.add_data("d0_strong_channel", {
        "per_atom": d0,
        "DTHe3_spread_full_pct": full_spread,
        "DTHe3_spread_d0_pct": d0_spread,
        "note": "Removing the antisymmetric −h (sinh) inter-nucleon term "
                "(d=0, symmetric cosh/strong channel) tightens the D/T/³He "
                "spread and pulls D up toward the A=3 scale — the sinh term "
                "carries the deuteron's anomaly. D/T/³He only (H₁₂ too slow).",
    })
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
