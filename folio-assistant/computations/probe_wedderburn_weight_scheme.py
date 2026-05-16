#!/usr/bin/env python3
"""Probe — Wedderburn weight scheme audit (hidden fitting?).

Per user 'review derivation and implementation. hidden fitting?'

The codebase uses TWO different Wedderburn weight schemes for the
Markov-trace expansion. This probe checks whether they agree
numerically, and whether one is "right" for the categorical mass.

Scheme A (mass_endomorphism.py, light_isotope_sweep.py):

  tr_M(T_w) = Σ_λ (dim_q(λ)² / [n]_q!) · χ_λ(T_w) / dim_λ

  with classical dim_λ in the denominator. Weight is the Plancherel
  measure on the q-deformed irreps.

Scheme B (y-lambda-wenzl-witness.json + canonical-mass-table):

  tr_M(T_w) = Σ_λ y_λ(q) · χ_λ(T_w)

  where y_λ is the Wenzl-bridge weight per
  prop:y-lambda-recipe-from-partition / hook-weight-derivation.md.

For the Markov trace on H_n(q) at the standard Markov parameter
z = (q^{1/2} - q^{-1/2})/(q - q^{-1}), Wenzl's theorem gives the
Schur-function expansion. Whether (A) and (B) agree at q_0
requires direct comparison.

If they disagree on χ_λ(T_w(proton)), one (or both) is wrong, and
the +1.84% m_p/m_e residual may live in the WEIGHT CHOICE, not the
formula structure.

NO Vol_hyp.  NO census.  Pure mpmath at 50 dps.

Output: probe-wedderburn-weight-scheme.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder

mp.mp.dps = 50

# q_0 at 50 dps
VOL_FIGURE_EIGHT = mp.mpf("2.029883212819307")
# CAL-2: m_μ/m_e from q_parameter registry (P31-triage Phase A).
from q_parameter import MASS_RATIO_MU_E_STR as _MU_E_STR
MASS_RATIO_MU_E  = mp.mpf(_MU_E_STR)
HBAR_Q_SQ        = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E
HBAR_Q           = mp.sqrt(HBAR_Q_SQ)
Q0               = mp.mpf(1) / (mp.mpf(1) - HBAR_Q)
QI0              = mp.mpf(1) / Q0
HA               = Q0 - QI0


def qint(k):
    if k == 0:
        return mp.mpf(0)
    return (Q0**k - QI0**k) / HA


def q_factorial_mp(n):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(k)
    return r


def classical_dim(part):
    """Hook-length formula (classical dimension)."""
    if not part:
        return 1
    n = sum(part)
    hooks = []
    for i, rl in enumerate(part):
        for j in range(rl):
            arm = rl - j - 1
            leg = sum(1 for r2 in range(i + 1, len(part)) if part[r2] > j)
            hooks.append(arm + leg + 1)
    fact = 1
    for k in range(1, n + 1):
        fact *= k
    h_prod = 1
    for h in hooks:
        h_prod *= h
    return fact // h_prod


def q_dim(part):
    """q-deformed dimension via q-hook formula."""
    if not part:
        return mp.mpf(1)
    n = sum(part)
    qfact = q_factorial_mp(n)
    h_prod = mp.mpf(1)
    for i, rl in enumerate(part):
        for j in range(rl):
            arm = rl - j - 1
            leg = sum(1 for r2 in range(i + 1, len(part)) if part[r2] > j)
            h_prod *= qint(arm + leg + 1)
    return qfact / h_prod


def load_y_lambda_wenzl(n):
    """Load y_λ from y-lambda-wenzl-witness.json at H_n."""
    path = Path(__file__).parent / "y-lambda-wenzl-witness.json"
    with open(path) as f:
        d = json.load(f)
    table = d["tables_by_n"].get(str(n))
    if table is None:
        return {}
    return {tuple(w["partition"]): mp.mpf(w["y_lambda_numeric"])
            for w in table["weights"]}


def main():
    print("=" * 78)
    print("Wedderburn weight-scheme audit (Plancherel-A vs Wenzl-B)")
    print("=" * 78)
    print(f"  q_0 = {mp.nstr(Q0, 30)}")
    print()

    for n in (2, 3, 5):
        print(f"━━ H_{n}: comparing Scheme A vs Scheme B")
        nfac = q_factorial_mp(n)
        wenzl = load_y_lambda_wenzl(n)
        print(f"   {'partition':<14} {'dim_classical':>14} "
              f"{'dim_q':>10} {'A: dim_q²/[n]_q!':>20} "
              f"{'B: Wenzl y_λ':>14} {'B/A':>10}")
        print("   " + "-" * 86)
        # Iterate partitions
        from itertools import chain
        # Generate partitions of n
        def partitions(n):
            if n == 0:
                yield ()
                return
            for first in range(1, n + 1):
                for rest in partitions(n - first):
                    if rest and rest[0] > first:
                        continue
                    yield (first,) + rest
        for shape in sorted(set(partitions(n)), key=lambda x: (-len(x), x), reverse=True):
            d_cls = classical_dim(shape)
            d_q = q_dim(shape)
            scheme_A = d_q ** 2 / nfac
            scheme_B = wenzl.get(shape, None)
            if scheme_B is None:
                ratio = "—"
                B_str = "—"
            else:
                ratio = f"{float(scheme_B / scheme_A):>10.6f}"
                B_str = f"{float(scheme_B):>14.6f}"
            print(f"   {str(list(shape)):<14} {d_cls:>14} "
                  f"{float(d_q):>10.4f} {float(scheme_A):>20.6f} "
                  f"{B_str} {ratio}")
        # Sum check
        sum_A = sum(q_dim(shape) ** 2 / nfac for shape in partitions(n))
        sum_B = sum(wenzl.get(shape, mp.mpf(0)) * classical_dim(shape) for shape in partitions(n))
        print(f"   Σ A · dim_q² (=1 by Plancherel)         = {float(sum_A):.6f}")
        print(f"   Σ B · dim_classical (=1 if normalized)  = {float(sum_B):.6f}")
        print()

    # Build witness
    rows_per_n = []
    for n in (2, 3, 5):
        nfac = q_factorial_mp(n)
        wenzl = load_y_lambda_wenzl(n)
        per_n_rows = []
        def partitions(n):
            if n == 0:
                yield ()
                return
            for first in range(1, n + 1):
                for rest in partitions(n - first):
                    if rest and rest[0] > first:
                        continue
                    yield (first,) + rest
        for shape in sorted(set(partitions(n)), key=lambda x: (-len(x), x), reverse=True):
            d_q = q_dim(shape)
            sA = d_q**2 / nfac
            sB = wenzl.get(shape)
            per_n_rows.append({
                "partition": list(shape),
                "classical_dim": classical_dim(shape),
                "q_dim_at_q_0": float(d_q),
                "scheme_A_plancherel": float(sA),
                "scheme_B_wenzl": float(sB) if sB is not None else None,
                "ratio_B_over_A": float(sB / sA) if sB is not None else None,
            })
        rows_per_n.append({"n": n, "rows": per_n_rows})

    w = (
        WitnessBuilder("probe-wedderburn-weight-scheme", engine="python+mpmath")
        .set_description(
            "Wedderburn weight scheme audit: compares Plancherel "
            "weights (dim_q² / [n]_q!) used in mass_endomorphism.py / "
            "light_isotope_sweep.py against Wenzl-bridge y_λ used in "
            "y-lambda-wenzl-witness.json. If they disagree on χ_λ(T_w) "
            "for non-trivial T_w, one (or both) is wrong, and the "
            "+1.84% m_p/m_e residual may live in the WEIGHT CHOICE."
        )
        .set_content_block("prop:y-lambda-recipe-from-partition")
        .add_parameter("q_0_mpf50", mp.nstr(Q0, 50))
        .add_parameter("mpmath_dps", mp.mp.dps)
        .add_data("comparisons_by_n", rows_per_n)
        .add_caveat(
            "If scheme A and scheme B disagree, check which one is the "
            "STANDARD Markov trace per Wenzl's bridge for the chosen "
            "Markov parameter z = z_M = (q^{1/2}-q^{-1/2}) / (q-q^{-1})."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
