#!/usr/bin/env python3
"""
Probe (3): does the PSD-cone obstruction depth (1 − α*) per atom
correlate with the binding-energy gap |B_pred − B_AME| / B_AME ?

Per the dominant-partition audit (2026-05-25), α* per atom is forced
by a specific Wedderburn block λ* (deuteron: (3,1,1,1); tritium /
³He: (3,2,2,2); ⁴He: (4,4,4)). The depth of PSD violation against
λ* is (1 − α*); the conjecture under test is that this depth tracks
the fractional binding-energy gap, in which case the residual gap is
*concentrated in the dominant-partition channel*.

Falsification rule: if no monotone relationship exists between
(1 − α*) and |err|/B_AME across the 4 atoms with α* data, the
dominant-partition obstruction is NOT the carrier of the binding-
energy gap, and Probes (1)–(2) (project mass formula on (4,4,4),
crystal weight) are likely also weak.

Bound to `conj:atom-braid-exterior-algebra`. Audit-only — no
fitting, no calibration. Reads existing witnesses only.
"""

from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder


def spearman_rho_n4(x: list[float], y: list[float]) -> float:
    """Spearman ρ on n=4 paired samples. Returns 1 if perfectly
    monotone-increasing, −1 if decreasing, 0 if uncorrelated. With
    n=4 the value is exact (24 permutations)."""
    if len(x) != len(y) or len(x) < 2:
        return 0.0

    def ranks(v: list[float]) -> list[float]:
        s = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for rk, i in enumerate(s):
            r[i] = float(rk)
        return r

    rx, ry = ranks(x), ranks(y)
    n = len(x)
    d2 = sum((rx[i] - ry[i]) ** 2 for i in range(n))
    return 1.0 - 6.0 * d2 / (n * (n * n - 1))


def main() -> int:
    base = Path(__file__).resolve().parent

    with open(base / "joint-tower-sdp-rust.witness.json") as f:
        jt = json.load(f)
    with open(base / "ame-2020-binding-energies.witness.json") as f:
        ame = json.load(f)
    with open(base / "mass-table-ppb.witness.json") as f:
        mt = json.load(f)

    # Map atom-cert names → mass-table row sym.
    name_to_sym = {
        "deuteron-canonical-3A": "2H",
        "tritium-canonical-3A": "3H",
        "helium3-canonical-3A": "3He",
        "helium4-4He": "4He",
    }

    # α* per atom from joint-tower witness.
    alphas = {}
    for c in jt.get("per_atom_certificates", []):
        n = c.get("name")
        if n in name_to_sym:
            alphas[n] = c.get("psd_cone_alpha_star")

    # B_AME, B_pred, |err|/B_AME per atom from mass-table-ppb.
    rows_by_sym = {r["sym"]: r for r in mt["data"]["rows"]}

    per_atom = []
    for cert_name, sym in name_to_sym.items():
        if cert_name not in alphas or alphas[cert_name] is None:
            continue
        row = rows_by_sym.get(sym)
        if row is None or row.get("B_pred_MeV") is None:
            continue
        a = alphas[cert_name]
        bame = float(row["B_AME_MeV"])
        bpred = float(row["B_pred_MeV"])
        err = bpred - bame
        per_atom.append({
            "name": cert_name,
            "sym": sym,
            "alpha_star": a,
            "one_minus_alpha_star": 1.0 - a,
            "B_AME_MeV": bame,
            "B_pred_MeV": bpred,
            "err_MeV": err,
            "abs_err_MeV": abs(err),
            "abs_frac_err": abs(err) / bame,
            "signed_frac_err": err / bame,
            "formula": row.get("formula"),
        })

    out = WitnessBuilder("alpha-star-vs-binding-gap", engine="python")
    out.set_description(
        "Tests whether the PSD-cone obstruction depth (1 − α*) per "
        "canonical atom-braid correlates with the fractional binding-"
        "energy gap |B_pred − B_AME| / B_AME. If yes, the residual "
        "binding-energy gap is concentrated in the dominant Wedderburn "
        "block λ* identified in alpha_star_dominant_partitions.py. If "
        "no, the dominant-partition obstruction is structurally distinct "
        "from the binding-energy gap and Probes (1)/(2) are likely weak."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")

    print("=== α* vs binding-energy gap (4 atoms) ===\n")
    print(f"{'sym':>4s} {'α*':>10s} {'1−α*':>8s}   {'B_AME':>10s} {'B_pred':>10s}   {'|err|/B':>10s}  {'err_MeV':>10s}")
    for p in per_atom:
        print(f"{p['sym']:>4s} {p['alpha_star']:10.6f} {p['one_minus_alpha_star']:8.4f}   {p['B_AME_MeV']:10.4f} {p['B_pred_MeV']:10.4f}   {p['abs_frac_err']*100:9.3f}%  {p['err_MeV']:+10.4f}")
    print()

    # Spearman correlations
    x_alpha = [p["alpha_star"] for p in per_atom]
    x_1ma = [p["one_minus_alpha_star"] for p in per_atom]
    y_abs = [p["abs_frac_err"] for p in per_atom]
    y_signed = [p["signed_frac_err"] for p in per_atom]
    y_abs_MeV = [p["abs_err_MeV"] for p in per_atom]

    rho_alpha_vs_abs = spearman_rho_n4(x_alpha, y_abs)
    rho_1ma_vs_abs = spearman_rho_n4(x_1ma, y_abs)
    rho_1ma_vs_signed = spearman_rho_n4(x_1ma, y_signed)
    rho_1ma_vs_absMeV = spearman_rho_n4(x_1ma, y_abs_MeV)

    print(f"Spearman ρ(α*, |err|/B)         = {rho_alpha_vs_abs:+.4f}")
    print(f"Spearman ρ(1−α*, |err|/B)       = {rho_1ma_vs_abs:+.4f}")
    print(f"Spearman ρ(1−α*, err/B signed)  = {rho_1ma_vs_signed:+.4f}")
    print(f"Spearman ρ(1−α*, |err| MeV)     = {rho_1ma_vs_absMeV:+.4f}")
    print()
    print("n=4: |ρ|=1 ⟺ perfect monotone; |ρ|≥0.8 weak-positive; |ρ|<0.5 falsifies monotone.")
    print()

    # ⁴He-specific: how much of |err| could the dominant block carry?
    he4 = next((p for p in per_atom if p["sym"] == "4He"), None)
    if he4 is not None:
        # If the entire (1 − α*) fraction of the binding energy is the
        # missing dominant-block correction, expected gap ≈ (1 − α*) · B_AME
        expected_gap_if_obstruction_eq_gap = he4["one_minus_alpha_star"] * he4["B_AME_MeV"]
        observed_gap = he4["abs_err_MeV"]
        ratio = observed_gap / expected_gap_if_obstruction_eq_gap if expected_gap_if_obstruction_eq_gap else float("inf")
        print(f"⁴He: (1−α*)·B_AME = {expected_gap_if_obstruction_eq_gap:.4f} MeV, observed |err| = {observed_gap:.4f} MeV, ratio = {ratio:.4f}")
        print(f"     (ratio ≈ 1 ⟹ obstruction depth predicts the gap magnitude up to constant)")

    out.add_data("per_atom", per_atom)
    out.add_data("spearman_correlations", {
        "rho_alpha_star_vs_abs_frac_err": rho_alpha_vs_abs,
        "rho_one_minus_alpha_vs_abs_frac_err": rho_1ma_vs_abs,
        "rho_one_minus_alpha_vs_signed_frac_err": rho_1ma_vs_signed,
        "rho_one_minus_alpha_vs_abs_err_MeV": rho_1ma_vs_absMeV,
        "n_samples": len(per_atom),
        "note": "n=4 sample is small; |ρ|=1 is the only convincing signal.",
    })

    # Falsification assertion: if |ρ(1−α*, |err|/B)| < 0.5, the
    # dominant-partition obstruction is NOT the binding-energy gap
    # carrier, and the conjecture is falsified at the empirical level.
    weak_signal = abs(rho_1ma_vs_abs) < 0.5
    # Pass if |ρ| ≥ 0.5 (loose monotone threshold for n=4).
    abs_rho = abs(rho_1ma_vs_abs)
    out.add_assertion(
        name="dominant_partition_obstruction_tracks_binding_gap",
        computed=str(int(abs_rho >= 0.5)),
        expected="1",
        tolerance=0,
        source=f"|Spearman ρ| = {abs_rho:.4f} on 4 atoms (D, T, ³He, ⁴He), threshold 0.5",
    )

    out.add_caveat(
        "Sample size n=4. With only 4 atoms (D, T, ³He, ⁴He), Spearman "
        "ρ has 24 possible permutations; |ρ|=1 corresponds to p≈1/12 "
        "(weak significance). Treat as exploratory diagnostic, not "
        "rigorous statistical evidence. The structural question — "
        "does the dominant Wedderburn block carry the gap — needs "
        "Probe (1) (project mass on (4,4,4)) for direct verification."
    )

    if weak_signal:
        out.add_caveat(
            f"WEAK SIGNAL: |ρ(1−α*, |err|/B)| = {abs(rho_1ma_vs_abs):.4f} < 0.5. "
            "Dominant-partition obstruction depth does NOT monotonically "
            "track binding-energy gap across these 4 atoms. Probes (1)/(2) "
            "may still find structural decomposition, but the simplest "
            "'obstruction = gap' hypothesis is falsified."
        )

    out_path = out.save()
    print(f"\nWitness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
