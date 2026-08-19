#!/usr/bin/env python3
"""EXPLORATORY shape-probe — q-6j / JM-spectrum per-block volume for Δ_λ.

Follow-up to `probe_volume_wedderburn_delta_lambda.py` (which refuted the
cheap content/hook-angle Vol_λ proxies). This probe upgrades Vol_λ to the
**Jucys–Murphy spectral** version — the genuine q-6j-symbol volume
mechanism: at a root of unity q = e^{iπ/r}, the block's JM content
eigenvalues become roots of unity, and the volume conjecture for the
6j-symbol assigns each an ideal-tetrahedron volume via the Bloch–Wigner
dilogarithm D(z) = Im Li_2(z) (z on the unit circle ⇒ D = Cl_2(arg z)).

    Vol_λ(r) = Σ_{cells, content c} D(e^{2πi·c/r})       (q-6j saddle proxy)

scanned over root-of-unity order r, with the framework-natural choices
r ∈ {n, n+1, …, 2n} flagged. Tested zero-parameter on D / T / ³He / ⁴He
with the SAME rule, no per-isotope refit.

It also reports the **T/³He differential diagnostic** — T and ³He share
n=9 (same 30 partitions, same y_λ), so the ONLY source of B_T ≠ B_³He is
Σ_λ Vol_λ y_λ (χ^λ(β_T) − χ^λ(β_³He)) = (B_T − B_³He)/m_e. Any universal
Vol_λ rule must reproduce that single number; this is the sharpest test.

EXPLORATORY (per production-vs-exploratory-discipline): asserts the
refutation (expected-negative ⇒ CI-safe). Touches no production. Δ_λ open.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
HERE = Path(__file__).parent

M_E_MEV = mp.mpf("0.51099895069")
AME_B = {
    "deuteron": mp.mpf("2.2245662"),
    "tritium": mp.mpf("8.4818"),
    "helium-3": mp.mpf("7.7180"),
    "helium-4": mp.mpf("28.29566"),
}
CHI_CACHE = {
    "deuteron": "chi-deuteron-h6-at-q0-50dps.witness.json",
    "tritium": "chi-tritium-h9-at-q0-50dps.witness.json",
    "helium-3": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "helium-4": "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def bloch_wigner_unit(theta: mp.mpf) -> mp.mpf:
    """D(e^{iθ}) = Im Li_2(e^{iθ}) = Cl_2(θ) — ideal-tetrahedron volume."""
    return mp.im(mp.polylog(2, mp.e ** (1j * theta)))


def partition_cells(part: list[int]):
    for i, row in enumerate(part):
        for j in range(row):
            yield i, j


def vol_jm_spectral(part: list[int], r: int) -> mp.mpf:
    """Σ_cells |D(e^{2πi·content/r})| — JM-spectral q-6j volume at order r."""
    return sum(abs(bloch_wigner_unit(2 * mp.pi * (j - i) / r))
               for i, j in partition_cells(part))


def load_blocks(fname: str):
    d = json.load(open(HERE / fname))
    blocks = [{"part": list(r["partition"]), "y": mp.mpf(r["y_lambda"]),
               "chi": mp.mpf(r["chi_lambda"])} for r in d["by_partition"]]
    return blocks, d["n_strands"]


def main() -> int:
    iso = {}
    for atom, fname in CHI_CACHE.items():
        if (HERE / fname).exists():
            blocks, n = load_blocks(fname)
            iso[atom] = (blocks, n, AME_B[atom])
    print(f"Loaded {len(iso)} isotopes: {', '.join(iso)}\n")

    TOL = mp.mpf("0.05")
    results = {}
    any_closes_all = False
    best = None  # (worst_err, r)

    # Scan root-of-unity order r. Each isotope uses ITS OWN n for the
    # natural band, but Vol_λ(r) is a fixed function of (λ, r); for a
    # single universal rule we use the SAME r across all isotopes.
    for r in range(4, 31):
        S = {a: sum(b["y"] * b["chi"] * vol_jm_spectral(b["part"], r)
                    for b in blk) for a, (blk, n, _B) in iso.items()}
        # zero-parameter: volume units, scale = 1 (m_e is the only scale)
        per = {}
        worst = mp.mpf(0)
        for a, (blk, n, B) in iso.items():
            B_pred = M_E_MEV * S[a]
            err = (B_pred - B) / B
            per[a] = {"B_pred_MeV": float(B_pred), "rel_err": float(err)}
            worst = max(worst, abs(err))
        closes = worst <= TOL
        any_closes_all = any_closes_all or closes
        results[f"r={r}"] = {"worst_rel_err": float(worst),
                             "closes_all": bool(closes), "per_isotope": per}
        if best is None or worst < best[0]:
            best = (worst, r, per)

    bw, br, bper = best
    print(f"Best universal r = {br}: worst |err| = {float(bw)*100:.1f}%")
    for a in iso:
        print(f"    {a:<10} B_pred={bper[a]['B_pred_MeV']:8.4f}  "
              f"AME={float(AME_B[a]):8.4f}  err={bper[a]['rel_err']*100:+8.1f}%")

    # ── T/³He same-n differential diagnostic ──
    diff_report = None
    if "tritium" in iso and "helium-3" in iso:
        blkT, nT, _ = iso["tritium"]
        blkH, nH, _ = iso["helium-3"]
        target_diff = float((AME_B["tritium"] - AME_B["helium-3"]) / M_E_MEV)
        # map partition→chi for each
        chiT = {tuple(b["part"]): b["chi"] for b in blkT}
        yT = {tuple(b["part"]): b["y"] for b in blkT}
        chiH = {tuple(b["part"]): b["chi"] for b in blkH}
        print(f"\n── T/³He differential (same n=9): "
              f"target (B_T−B_³He)/m_e = {target_diff:+.4f}")
        dr = {}
        for r in range(4, 31):
            d = sum(vol_jm_spectral(list(p), r) * yT[p] * (chiT[p] - chiH[p])
                    for p in chiT)
            dr[f"r={r}"] = float(d)
        # closest r
        best_r = min(dr, key=lambda k: abs(dr[k] - target_diff))
        print(f"    best r for differential: {best_r} → "
              f"Σ Vol·y·Δχ = {dr[best_r]:+.4f} (target {target_diff:+.4f})")
        diff_report = {"target_diff": target_diff, "by_r": dr,
                       "best_r": best_r, "best_value": dr[best_r]}

    w = WitnessBuilder("probe-q6j-jm-spectral-delta-lambda", engine="mpmath")
    w.set_description(
        "EXPLORATORY: q-6j / Jucys–Murphy-spectral per-block volume "
        "Vol_λ(r) = Σ_cells |D(e^{2πi·content/r})| as a Δ_λ closure "
        "candidate, scanned over root-of-unity order r, zero-parameter on "
        "D/T/³He/⁴He. Includes the T/³He same-n differential diagnostic. "
        "Δ_λ remains open (GAP-A-3/A-4)."
    )
    w.add_parameter("tolerance_pct", 5.0)
    w.add_parameter("r_scan", "4..30")
    w.add_data("by_r", results)
    w.add_data("best_universal_r", br)
    w.add_data("best_worst_rel_err", float(bw))
    if diff_report:
        w.add_data("t_he3_differential", diff_report)
    w.add_data("any_r_closes_all_within_5pct", any_closes_all)
    w.add_assertion(
        name="no_jm_spectral_r_closes_all_four",
        computed=str(int(not any_closes_all)),
        expected="1",
        tolerance=0,
        source=(f"EXPECTED NEGATIVE: best universal r={br} still misses "
                f"(worst |err| {float(bw)*100:.0f}%); JM-spectral content "
                "volume insufficient — genuine closure needs the full "
                "Turaev–Viro state-sum on the knot-complement triangulation."),
    )
    out = w.save()
    print(f"\nWitness: {out}")
    print(f"any r closes all 4 within 5%: {any_closes_all}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
