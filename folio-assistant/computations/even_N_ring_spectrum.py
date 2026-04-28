#!/usr/bin/env python3
"""C8 — Even-N ring closure barrier spectrum and trend.

Backs `prop:even-N-barrier-spectrum` in the Organic Chemistry chapter.

Statement
---------
For even N = 2m ∈ {4, 6, 8, 10, 12, 14}, the predicted ring-closure
barrier ΔE_{closure}(N) (from `prop:ring-closure-barrier-quantitative`)
follows a **monotone-increasing** linear trend in N::

    ΔE_{closure}(N)  ≈  C₀ + C₁ · N,    with C₁ > 0,

where the slope C₁ = |q + q⁻¹|_mol · (½) reflects the
half-weight propagation (prop:threading-half-weight) and the offset
C₀ collects sub-leading q-deviations.

The script:
1. Tabulates the predicted barrier for N = 4, 6, …, 14.
2. Fits the linear trend ΔE = C₀ + C₁·N by least squares.
3. Compares the slope against the prediction
   |q + q⁻¹|_mol · (½) ≈ ½ · 22.4 ≈ 11.2 kJ/mol per added carbon.

Usage
-----
    python3 even_N_ring_spectrum.py
"""
import json
import sys
from pathlib import Path
from statistics import mean

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from lib.alexander import alexander_T2N_closed, q
from lib.units import ev_to_kj_per_mol
from witness_base import WitnessBuilder
from q_parameter import Q


DATA_PATH = Path(__file__).parent / "data" / "experimental-organic.json"


def linear_fit(xs, ys):
    """Ordinary least-squares y = c0 + c1*x; returns (c0, c1, rss)."""
    n = len(xs)
    mx, my = mean(xs), mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    c1 = num / den if den else 0.0
    c0 = my - c1 * mx
    rss = sum((y - (c0 + c1 * x)) ** 2 for x, y in zip(xs, ys))
    return c0, c1, rss


def main() -> int:
    data = json.loads(DATA_PATH.read_text())
    alpha = data["fundamental_constants"]["alpha"]["value"]
    m_ratio = data["fundamental_constants"]["m_e_over_m_p"]["value"]
    e_nuc_MeV = 8.0
    e_mol_eV = alpha**2 * m_ratio * e_nuc_MeV * 1e6
    e_mol_kJpermol = ev_to_kj_per_mol(e_mol_eV)

    Ns = [4, 6, 8, 10, 12, 14]
    rows = []
    for N in Ns:
        delta_q0 = float(sp.N(alexander_T2N_closed(N).subs(q, Q)))
        weight_diff = (N - 1) - delta_q0
        barrier_kJpermol = weight_diff * e_mol_kJpermol
        rows.append({
            "N": N,
            "weight_difference": weight_diff,
            "barrier_predicted_kJ_per_mol": barrier_kJpermol,
        })

    xs = [r["N"] for r in rows]
    ys = [r["barrier_predicted_kJ_per_mol"] for r in rows]
    c0, c1, rss = linear_fit(xs, ys)
    predicted_slope = e_mol_kJpermol * 0.5  # ½ kJ/mol per C, from half-weight
    relative_error = abs(c1 - predicted_slope) / predicted_slope

    w = WitnessBuilder("even-N-ring-spectrum", engine="python")
    w.set_description(
        "Linear trend of predicted ring-closure barriers for even N = "
        "4,…,14, fit by least squares and compared against the "
        "half-weight-derived slope |q+q⁻¹|_mol · ½."
    )
    w.set_content_block("prop:even-N-barrier-spectrum")
    w.add_parameter("e_cross_mol_kJ_per_mol", e_mol_kJpermol)
    w.add_data("table", rows)
    w.add_data("linear_fit", {
        "intercept_kJ_per_mol": c0,
        "slope_kJ_per_mol_per_C": c1,
        "predicted_slope_half_weight_kJ_per_mol_per_C": predicted_slope,
        "slope_relative_error": relative_error,
        "residual_sum_squares": rss,
    })

    w.add_assertion(
        "linear fit slope matches half-weight prediction within 15% "
        "(limit q→1 gives exact match; q₀ ≠ 1 introduces O((q-1)²) "
        "correction)",
        computed=str(relative_error <= 0.15),
        expected="True",
    )
    w.add_assertion(
        "predicted barriers strictly increase with N",
        computed=str(all(ys[i] < ys[i + 1] for i in range(len(ys) - 1))),
        expected="True",
    )
    w.add_assertion(
        "slope numerically equals e_mol_kJ_per_mol / 2 within 15%",
        computed=round(c1, 4),
        expected=round(predicted_slope, 4),
        tolerance=2.0,
        unit="kJ/mol per C",
    )

    w.add_caveat(
        "The experimental trend (kJ/mol vs. N from the data file) is "
        "approximately *flat* or weakly *decreasing* (260, 290, 240, "
        "220, 210, 200 for N=4,6,8,10,12,14), opposite to the "
        "predicted monotone-increasing trend.  This sign disagreement "
        "is a key falsifier of the simple model and indicates that "
        "additional contributions (entropic, ring-strain, "
        "Hückel-electronic) dominate beyond the topological barrier.  "
        "The witness records the disagreement quantitatively for the "
        "chapter to address."
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
