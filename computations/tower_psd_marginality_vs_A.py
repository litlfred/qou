#!/usr/bin/env python3
"""Tower adjacent-pair PSD marginality across D / T / ³He / ⁴He.

Owner directive 2026-06-10 next-step 2: "compute the ⁴He adjacent-pair tower
PSD to see if it too is cone-marginal like D."

## What I'm testing (and an honest caveat up front)

`pn_alpha_lp_dual.tower_sdp_dual_at_alpha` found, for the DEUTERON, that the
adjacent-pair PSD blocks `[[V̂_i, x_i],[x_i, V̂_{i+1}]] ⪰ 0` are ALL TIGHT
(`x_i = √(V̂_i V̂_{i+1})`, det = 0) when maximizing Σx_i. CAVEAT: by AM–GM the
PSD bound `x_i ≤ √(V̂_i V̂_{i+1})` is always ≤ the box bound
`(V̂_i+V̂_{i+1})/2`, so *maximizing* couplings saturates the PSD det=0 for ANY
positive V̂ — "all pairs tight" is GENERIC, not a deuteron anomaly. This probe
confirms that across A, and instead reports the MEANINGFUL confinement metric:
how close each generator's `V̂_i` sits to the Φ_q singularity (the deconfine-
ment pole near q₀), i.e. which nucleus is genuinely closest to the cone edge.

Per nucleus: per-generator V̂_i (full), max V̂_i, the pole gap `q₀ − max V̂_i`,
the smallest eigenvalue of the tridiagonal confinement matrix
`M = diag(V̂) + offdiag(√(V̂_iV̂_{i+1}))` (its margin to PSD-singular), and the
adjacent-pair tightness (expected: all tight, generically).

Output: tower-psd-marginality-vs-A.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402
from pn_alpha_lp_dual import atom_per_gen_vols_alpha  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

NUCLEI = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]


def main() -> int:
    t0 = time.time()
    q0 = float(Q0)
    rows = []
    for lab, Z, N in NUCLEI:
        va = atom_per_gen_vols_alpha(Z, N, pn_alpha=0.5)
        Vh = np.array([v["full"] for v in va], dtype=float)
        n = len(Vh)
        # adjacent-pair geometric couplings (the max-Σx PSD optimum)
        sqrt_geom = np.array([(Vh[i] * Vh[i + 1]) ** 0.5 for i in range(n - 1)])
        # all pairs are tight by construction (x_i = sqrt_geom) — generic.
        # tridiagonal confinement matrix M = diag(V) + offdiag(sqrt_geom)
        M = np.diag(Vh)
        for i in range(n - 1):
            M[i, i + 1] = M[i + 1, i] = sqrt_geom[i]
        eig = np.linalg.eigvalsh(M)
        rows.append({
            "nucleus": lab, "Z": Z, "N": N, "A": Z + N, "n_gens": n,
            "V_hat": [round(float(v), 4) for v in Vh],
            "max_V_hat": round(float(Vh.max()), 4),
            "min_V_hat": round(float(Vh.min()), 4),
            "pole_gap_q0_minus_maxV": round(q0 - float(Vh.max()), 4),
            "tridiag_min_eig": round(float(eig.min()), 6),
            "all_pairs_tight": True,  # generic (det=0 by AM-GM, see docstring)
        })

    # Which nucleus is closest to the confinement pole (smallest gap)?
    by_gap = sorted(rows, key=lambda r: r["pole_gap_q0_minus_maxV"])
    closest = by_gap[0]["nucleus"]

    w = WitnessBuilder("tower-psd-marginality-vs-A", engine="python",
                       start_time=t0)
    w.set_description(
        "Adjacent-pair tower PSD across D/T/³He/⁴He. HONEST CORRECTION: the "
        "'all adjacent pairs tight' found for D is GENERIC (maximizing Σx_i "
        "saturates the PSD det=0 for any positive V̂ by AM-GM) — NOT a deuteron "
        "anomaly. The meaningful confinement metric is the gap from max V̂_i to "
        "the Φ_q pole (q₀) and the tridiagonal min-eigenvalue; reports which "
        "nucleus is genuinely closest to the cone edge. So the only real "
        "SDP/PSD distinction across nuclei is the Wedderburn channel migration "
        "(separate probe), not the tower PSD tightness."
    )
    w.add_parameter("q0", q0)
    w.add_data("rows", rows)
    w.add_data("verdict", {
        "all_pairs_tight_is_generic": True,
        "closest_to_pole": closest,
        "pole_gaps": {r["nucleus"]: r["pole_gap_q0_minus_maxV"] for r in rows},
        "tridiag_min_eigs": {r["nucleus"]: r["tridiag_min_eig"] for r in rows},
        "reading": "⁴He is cone-marginal in EXACTLY the same (generic) sense as "
                   "D — adjacent-pair tightness is not a discriminator. The "
                   "honest distinction between nuclei is the Wedderburn weight "
                   "migration, not the tower PSD.",
    })
    out = w.save()

    print("=" * 84)
    print(" Tower adjacent-pair PSD across A  (all-pairs-tight is GENERIC — see caveat)")
    print(f"   q₀ (Φ_q pole) = {q0:.5f}")
    print("=" * 84)
    print(f" {'nuc':>5}{'A':>3}{'n_gens':>7}{'max V̂':>9}{'pole gap':>10}"
          f"{'tridiag min-eig':>17}{'all pairs tight':>16}")
    print(" " + "-" * 82)
    for r in rows:
        print(f" {r['nucleus']:>5}{r['A']:>3}{r['n_gens']:>7}{r['max_V_hat']:>9.4f}"
              f"{r['pole_gap_q0_minus_maxV']:>10.4f}{r['tridiag_min_eig']:>17.6f}"
              f"{'yes (generic)':>16}")
    print(" " + "-" * 82)
    print(f" closest to the Φ_q confinement pole: {closest} "
          f"(gap {by_gap[0]['pole_gap_q0_minus_maxV']:.4f})")
    print(" ⁴He is cone-marginal in the SAME generic sense as D; the real "
          "nucleus distinction is the Wedderburn weight migration, not this PSD.")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
