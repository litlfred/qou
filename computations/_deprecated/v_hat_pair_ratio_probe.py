#!/usr/bin/env python3
"""
V-hat-within-level candidate #3: content/scalar pair ratio probe.

The `binding_full_content_pair` probe showed content-weighted V̂_{ij}
over-corrects 5–500x under production calibration.  This module
quantifies the over-correction: compute

    r_{ij} := V̂_{ij}^{content} / (V̂_i · V̂_j)

for every pair (i, j) on the atom braid words of D / T / 3He (free +
atom + inter).  If r_{ij} is (near-)uniform, the over-correction is
homogeneous — a single global scale factor would recover the scalar
path.  If r_{ij} has structure, it pinpoints which pairs SYT-content
correlation affects.

This is the 20-minute research-only step from
`docs/v-hat-within-level-candidates.md` §Candidate 3.

Outputs: `v-hat-pair-ratio.witness.json` with per-pair r_{ij}
statistics per atom.
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone
import statistics

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from content_weighted_pair_probe import content_weighted_pair_term
from hecke_core import atom_per_generator_volumes


def pair_ratios(Z: int, N: int, *, include_inter: bool,
                   m_pp: int = 1, m_pn: int = 1, m_nn: int = 1
                   ) -> list[dict]:
    """For every generator pair (i, j) in the atom braid word,
    compute the scalar product V_i·V_j, the content-weighted
    V̂_{ij}^{content}, and their ratio."""
    vols = atom_per_generator_volumes(
        Z, N, include_inter=include_inter,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
    V = [v["full"] for v in vols]
    n = len(V)
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            v_i, v_j = V[i], V[j]
            v_scalar = v_i * v_j
            v_content = content_weighted_pair_term(
                Z, N, (i, j), include_inter=include_inter,
                m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
            if abs(v_scalar) < 1e-15:
                ratio = float("nan")
            else:
                ratio = v_content / v_scalar
            rows.append({
                "i": i, "j": j, "d": j - i,
                "V_i": v_i, "V_j": v_j,
                "v_scalar": v_scalar,
                "v_content": v_content,
                "ratio": ratio,
                "log_abs_ratio":
                    float("nan") if not np.isfinite(ratio) or ratio == 0
                    else float(np.log10(abs(ratio))),
            })
    return rows


def summarise(rows: list[dict]) -> dict:
    rs = [r["ratio"] for r in rows if np.isfinite(r["ratio"])]
    if not rs:
        return {"n_pairs": len(rows), "n_finite": 0}
    abs_rs = [abs(r) for r in rs]
    log_rs = [np.log10(a) for a in abs_rs if a > 0]
    return {
        "n_pairs": len(rows),
        "n_finite": len(rs),
        "ratio_mean": statistics.mean(rs),
        "ratio_median": statistics.median(rs),
        "abs_ratio_mean": statistics.mean(abs_rs),
        "abs_ratio_median": statistics.median(abs_rs),
        "abs_ratio_stdev": (statistics.stdev(abs_rs)
                               if len(abs_rs) > 1 else 0.0),
        "log_abs_ratio_stdev": (statistics.stdev(log_rs)
                                    if len(log_rs) > 1 else 0.0),
        "abs_ratio_min": min(abs_rs),
        "abs_ratio_max": max(abs_rs),
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
    ]

    print("=" * 110)
    print("V-HAT PAIR-RATIO PROBE — content / scalar per pair")
    print(f"q0 = {Q0:.6f}")
    print("=" * 110)

    results = []
    for name, Z, N in ATOMS:
        for include_inter, label in [(False, "free"), (True, "atom")]:
            t0 = time.time()
            rows = pair_ratios(Z, N, include_inter=include_inter)
            summ = summarise(rows)
            dt = time.time() - t0

            print(f"\n{name}/{label}:  {summ['n_pairs']} pairs, "
                  f"elapsed {dt:.1f}s")
            if summ.get("n_finite"):
                print(f"  ratio: median = {summ['ratio_median']:+.4e}  "
                      f"mean = {summ['ratio_mean']:+.4e}")
                print(f"  |ratio|: min = {summ['abs_ratio_min']:.3e}  "
                      f"max = {summ['abs_ratio_max']:.3e}  "
                      f"stdev = {summ['abs_ratio_stdev']:.3e}")
                print(f"  log10|ratio| spread (stdev): "
                      f"{summ['log_abs_ratio_stdev']:.3f} decades")
                hi = max(rows, key=lambda r: abs(r["ratio"])
                          if np.isfinite(r["ratio"]) else 0)
                lo = min(rows, key=lambda r: abs(r["ratio"])
                          if np.isfinite(r["ratio"]) and r["ratio"] != 0
                          else float("inf"))
                print(f"  largest  |r|: pair ({hi['i']},{hi['j']}) d={hi['d']}  "
                      f"ratio = {hi['ratio']:+.4e}")
                print(f"  smallest |r|: pair ({lo['i']},{lo['j']}) d={lo['d']}  "
                      f"ratio = {lo['ratio']:+.4e}")

            results.append({
                "atom": name, "Z": Z, "N": N,
                "include_inter": include_inter,
                "label": label,
                "summary": summ,
                "pairs": rows,
                "time_sec": dt,
            })

    # Interpretation heuristic: is the over-correction homogeneous?
    print("\n" + "=" * 110)
    print("INTERPRETATION")
    print("=" * 110)
    for r in results:
        atom, label = r["atom"], r["label"]
        s = r["summary"]
        if s.get("n_finite", 0) < 2:
            continue
        spread = s["log_abs_ratio_stdev"]
        verdict = ("HOMOGENEOUS (single-scale-factor fix viable)"
                    if spread < 0.3
                    else "STRUCTURED (per-pair correction needed)"
                    if spread < 1.0
                    else "HEAVILY STRUCTURED (no single-scale fix)")
        print(f"  {atom}/{label}: log10|r| spread = {spread:.3f} decades  "
              f"→ {verdict}")

    witness = {
        "computation": "v-hat-pair-ratio-probe",
        "description": (
            "V-hat-within-level candidate #3: compute r_{ij} = "
            "V̂_{ij}^{content} / (V̂_i · V̂_j) per pair on D / T / 3He "
            "(free + atom).  If the ratio is uniform across pairs, the "
            "over-correction observed in binding_full_content_pair is "
            "homogeneous and a single scale-factor fix recovers "
            "scalar-path accuracy.  If structured, content-weighting "
            "captures genuine per-pair SYT correlation that the scalar "
            "path drops."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0},
        "results": results,
    }
    out = Path(__file__).parent / "v-hat-pair-ratio.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
