#!/usr/bin/env python3
"""
Cross-check Wenzl-bridge symbolic y_λ against MPFR linear-system y_λ.

For each n that appears in BOTH y-lambda-wenzl-witness.json and
y-lambda-mpfr-witness.json, compute per-partition |y_λ^Wenzl - y_λ^MPFR|
and report the max, ensuring the two independent computations agree
to high precision.

Wenzl-bridge: closed-form principal Schur specialisation
(prop:y-lambda-closed-form-wenzl-bridge).
MPFR witness: linear-system inverse on Hoefsmit characters
(y_lambda_mpfr_witness.py via Rust pyhecke_native kernel).

Output: y-lambda-wenzl-vs-mpfr-cross-check.json
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp


def main() -> None:
    mp.mp.dps = 50
    base = Path(__file__).parent
    wenzl = json.loads((base / "y-lambda-wenzl-witness.json").read_text())
    mpfr = json.loads((base / "y-lambda-mpfr-witness.json").read_text())

    overlap = sorted(
        set(wenzl["tables_by_n"]) & set(mpfr["tables_by_n"]),
        key=int,
    )
    rows = []
    for n_str in overlap:
        wt = wenzl["tables_by_n"][n_str]
        mt = mpfr["tables_by_n"][n_str]
        wmap = {tuple(w["partition"]): mp.mpf(w["y_lambda_numeric"]) for w in wt["weights"]}
        mmap = {tuple(w["partition"]): mp.mpf(w["y_lambda"]) for w in mt["weights"]}
        diffs = []
        for part, yw in wmap.items():
            ym = mmap.get(part)
            if ym is None:
                continue
            diffs.append((part, abs(yw - ym)))
        if not diffs:
            continue
        max_diff = max(d for _, d in diffs)
        worst = max(diffs, key=lambda x: x[1])
        rows.append(
            {
                "n": int(n_str),
                "num_partitions": len(diffs),
                "max_abs_diff": str(max_diff),
                "worst_partition": list(worst[0]),
                "worst_diff": str(worst[1]),
                "within_1e-30": bool(max_diff < mp.mpf("1e-30")),
                "within_1e-40": bool(max_diff < mp.mpf("1e-40")),
            }
        )
        print(
            f"n = {n_str:>2}: {len(diffs):>3} partitions, "
            f"max |Δ| = {mp.nstr(max_diff, 6)}  "
            f"(<1e-30: {max_diff < mp.mpf('1e-30')})"
        )

    out = {
        "description": (
            "Cross-check of Wenzl-bridge symbolic y_λ vs MPFR linear-system "
            "y_λ at every n with overlapping coverage in both witnesses.  "
            "Independent verification at high precision (50 dps comparison)."
        ),
        "references": [
            "prop:y-lambda-closed-form-wenzl-bridge",
            "prop:alpha-k-derivation-procedure",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "comparison_dps": 50,
        "rows": rows,
    }
    out_path = base / "y-lambda-wenzl-vs-mpfr-cross-check.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
