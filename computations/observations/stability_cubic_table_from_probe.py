"""Render `tbl:stability-cubic-plot-table-data` from the neutron-prediction probe.

The table previously carried a predicted-neutron column that no formula in the
corpus reproduces (bean `qou-opjb`, 2026-10-11): its N_pred equalled N_obs in
10 of 14 rows, and no normalisation of the stability line gave N = 20 for Ca.

This script makes no new computation. It reads the committed witness of
`neutron_prediction_comparison_probe.py` -- the prediction
A* = p(2 + c A*^{2/3}) of `prop:beta-stability` at c = lambda_C/(2 a_asym)
(owner decision 1b), and the observation rule stated there (most abundant
isotope per NUBASE2020 `IS=`, else longest-lived ground state) -- and prints
the 14 rows the stability-cubic block displays, so the table and the probe
cannot drift apart.

Usage:  python3 computations/observations/stability_cubic_table_from_probe.py
        (prints markdown; redirect into the table-data .md)
"""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WITNESS = ROOT / "computations" / "observations" / "neutron_prediction_comparison_probe.witness.json"
P_SHOWN = [1, 2, 6, 8, 14, 20, 26, 28, 36, 50, 56, 74, 82, 92]


def main() -> None:
    rows = {r["p"]: r for r in json.loads(WITNESS.read_text())["data"]["rows"]}
    print("| $p$ | $N_{\\mathrm{pred}}$ | $N_{\\mathrm{obs}}$ | Atom | $N_{\\mathrm{pred}}/p$ | $\\Delta N$ |")
    print("|----:|----:|----:|--------|------:|---:|")
    for p in P_SHOWN:
        r = rows[p]
        npred, nobs = r["n_pred_new"], r["n_obs"]
        ratio = Fraction(npred, p)
        # exact rational, rounded half-up to 2 decimals for display only
        disp = (ratio * 100 + Fraction(1, 2)).__floor__()
        print(f"| {p} | {npred} | {nobs} | {r['symbol']} | {disp // 100}.{disp % 100:02d} | {abs(npred - nobs)} |")


if __name__ == "__main__":
    main()
