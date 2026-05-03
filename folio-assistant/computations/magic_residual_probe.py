#!/usr/bin/env python3
"""
Magic-shell enhancement residual probe.

The Term6/A³ normalization fit (gs_term6_normalization.py) gave:

    binding/nucleon ≈ 342.5 · (Term6 / A³) + 1.20

with R² = 0.70 and a +2.5 MeV residual at 4He. This script
extracts the per-atom residuals and correlates them with
self-conjugate-partition saturation density to test whether
the magic-enhancement hypothesis is supported.

Hypotheses for what drives the residual:

  H1: |N - Z| asymmetry (SEMF asymmetry leftover)
  H2: # self-conjugate partitions of 3A (BB-saturation density)
  H3: # κ=0 partitions (categorical-neutrality saturation)
  H4: shell-distance min(d(Z,N) to magic pair)
  H5: parity (even-even vs odd-odd vs odd-A)

For each, compute correlation with the fit residual.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from enumerate_self_conjugate_partitions import (
    all_self_conjugate_partitions, content_sum,
)

MAGIC = (2, 8, 20, 28, 50, 82, 126)


def shell_distance(Z: int, N: int) -> int:
    return min(abs(Z - mz) + abs(N - mn) for mz in MAGIC for mn in MAGIC)


def parity_class(Z: int, N: int) -> int:
    """+1 ee, -1 oo, 0 oa."""
    pZ, pN = Z % 2, N % 2
    if pZ == 0 and pN == 0: return +1
    if pZ == 1 and pN == 1: return -1
    return 0


def main():
    print("=" * 88)
    print("Magic-residual probe: extract residuals from Term6/A³ fit")
    print("=" * 88)

    p = (Path(__file__).parent.parent.parent
         / "docs/audits/2026-05-02-Term6-normalization.witness.json")
    d = json.loads(p.read_text())
    best = d["best_fit"]
    slope = best["slope"]
    intercept = best["intercept"]
    print(f"  Fit: B/A ≈ {slope:.4e} · (Term6/A³) + {intercept:.4f}")
    print()

    # Load Term6 atoms
    p_t6 = (Path(__file__).parent.parent.parent
            / "docs/audits/2026-05-02-gs-filtration-E2-probe.witness.json")
    t6_data = json.loads(p_t6.read_text())["atoms"]

    rows = []
    print(f"  {'atom':>5} {'A':>3} {'B/A':>10} {'pred':>10} {'residual':>10} "
          f"{'|N-Z|':>5} {'#sc':>4} {'#κ=0':>5} {'shell_d':>7} {'parity':>6}")
    print("  " + "-" * 95)
    for r in t6_data:
        A = r["A"]
        if A < 3 or r["term6_z3_sum_PhiQ"] == 0:
            continue
        Z, N = r["Z"], r["N"]
        T6 = r["term6_z3_sum_PhiQ"]
        bn = r["binding_per_nucleon"]
        norm = T6 / A ** 3
        pred = slope * norm + intercept
        residual = bn - pred

        # Structural variables
        n3A = 3 * A
        sc_parts = all_self_conjugate_partitions(n3A)
        n_sc = len(sc_parts)
        n_k0 = sum(1 for lam in sc_parts if content_sum(lam) == 0)
        sd = shell_distance(Z, N)
        pc = parity_class(Z, N)

        rows.append({
            "atom": r["atom"], "Z": Z, "N": N, "A": A,
            "B_over_A": bn,
            "predicted": pred,
            "residual": residual,
            "abs_NZ": abs(N - Z),
            "n_self_conj": n_sc,
            "n_kappa_0": n_k0,
            "shell_distance": sd,
            "parity_class": pc,
            "Term6": T6,
        })
        print(f"  {r['atom']:>5} {A:>3} {bn:>10.4f} {pred:>10.4f} "
              f"{residual:>+10.4f} {abs(N-Z):>5} {n_sc:>4} {n_k0:>5} "
              f"{sd:>7} {pc:>+6}")

    # Compute correlations of residual against each candidate variable
    if len(rows) > 2:
        residuals = np.array([r["residual"] for r in rows])
        print()
        print(f"  {'variable':<20} {'correlation w/ residual':>26}")
        print("  " + "-" * 50)
        for var in ["abs_NZ", "n_self_conj", "n_kappa_0", "shell_distance",
                    "parity_class"]:
            x = np.array([r[var] for r in rows])
            if x.std() > 0:
                corr = np.corrcoef(x, residuals)[0, 1]
                print(f"  {var:<20} {corr:>+26.4f}")
            else:
                print(f"  {var:<20} {'(constant)':>26}")
        # Special: shell_distance == 0 indicator (1 at magic, 0 elsewhere)
        magic_indicator = np.array([1.0 if r["shell_distance"] == 0 else 0.0
                                     for r in rows])
        if magic_indicator.std() > 0:
            corr = np.corrcoef(magic_indicator, residuals)[0, 1]
            print(f"  {'is_magic_pair':<20} {corr:>+26.4f}")

    out = {
        "computation": "magic-residual-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "fit_used": {"slope": slope, "intercept": intercept,
                     "form": "B/A = slope · (Term6/A³) + intercept"},
        "atoms": rows,
        "correlations": {
            var: float(np.corrcoef(
                np.array([r[var] for r in rows]),
                np.array([r["residual"] for r in rows]),
            )[0, 1]) if len({r[var] for r in rows}) > 1 else None
            for var in ["abs_NZ", "n_self_conj", "n_kappa_0",
                         "shell_distance", "parity_class"]
        },
        "interpretation": (
            "Tests which structural variable explains the (B/A − fit) "
            "residual from the Term6/A³ normalization. The +2.5 MeV "
            "outlier at 4He suggests magic-shell enhancement; this "
            "probe identifies which categorical variable correlates "
            "with the residual structure."
        ),
    }
    p_out = (Path(__file__).parent.parent.parent
             / "docs/audits/2026-05-02-magic-residual.witness.json")
    p_out.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
