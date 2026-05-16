#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath numerical evaluation of
# symbolic tr_M at q_0; structural Δ_cat extension across atoms.
"""Extends the magic-shell empirical instantiation Δ_cat table from
the original 4 atoms {D, T, ³He, ⁴He} to additional atoms with
distinct (n_pp, n_pn, n_nn) interface compositions.

Goal: unblock the linear α·n_pp + β·n_nn + γ fit in PR #656 v6 by
providing ≥ 4 distinct (n_pp, n_nn) data points.  Currently the
3-anchor system is trivial (rank 3); with ⁵Li (n_pp=2, n_nn=1) and
⁶Li (n_pp=2, n_nn=2) added, the fit becomes non-trivial and tests
whether (α, β, γ) have clean q-rational closed forms.

⚠ **Convention note on ρ.**  This probe uses `ρ = A − 1` to match
the magic-shell empirical instantiation convention
(`probe_magic_shell_empirical_instantiation.py:55`,
`RHO_MAP = {D: 1, T: 2, ³He: 2, ⁴He: 3}`), so the extended Δ_cat
values are directly comparable to the 4-atom reference bench.

The choice `ρ = A − 1` is **empirical-but-canonically-related-to-
interface-count** (it equals `n_pp + n_pn + n_nn`, the total
inter-nucleon interface count from
`def:canonical-braid-interface-composition`), NOT the
canonically-derived `ρ_K^LO = (Z·m_p + N·m_n) / (m_e·|τ_M|)` from
`atomic_mass_via_rho_k.py`.  Using `ρ_K^LO` here would make Δ_cat
trivially equal to AME(binding) by construction (the LO tautology
documented in `docs/audits/2026-05-09-mass-table-fitting-audit.md`),
eliminating the regression target.

The right long-term substrate-derivation path is the **per-block
binding-fraction** formula `Binding(K) = m_e · Σ_λ y_λ(q) · χ^λ(β_K)
· Δ_λ(K)` (PR #564's open Δ_λ derivation, PRs #602/#603/#613
racing the closure).  This probe is a stepping-stone using the
magic-shell heuristic until Δ_λ are derived.

Atoms added (with AME 2020 binding energies):

  ⁵Li (3, 2)  A=5   B = 26.330 MeV    n_pp=2, n_pn=1, n_nn=1
  ⁶He (2, 4)  A=6   B = 29.268 MeV    n_pp=1, n_pn=1, n_nn=3
  ⁶Li (3, 3)  A=6   B = 31.994 MeV    n_pp=2, n_pn=1, n_nn=2
  ⁶Be (4, 2)  A=6   B = 26.924 MeV    n_pp=3, n_pn=1, n_nn=1

(³He, T, ⁴He, D already in `magic-shell-empirical-instantiation.witness.json`.)

Compute strategy:
  - tr_M_atomic(Z, N, include_inter=True) → symbolic in q
  - .subs(q, q_0_50dps).evalf(50) → 50-dps |τ_M|
  - Categorical mass = m_e · ρ · |τ_M|  with  ρ = A − 1
  - Δ_cat = AME(binding) − categorical

Compute budget (estimates from existing ⁴He=14.8 s scaling):
  ⁵Li (n=15) ~  60 s
  ⁶X  (n=18) ~ 250 s each × 3 = 750 s
  total ≈ 14 min

`auditOnly`: docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md

Witness: `delta-cat-extension.witness.json`

@module folio-assistant/computations/probe_delta_cat_extension
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

from codata_constants import M_E_MEV  # noqa: E402
from interface_composition import interface_composition  # noqa: E402
from markov_peel import tr_M_atomic  # noqa: E402
from q_parameter import HA_MP, Q_MP, Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

# AME 2020 binding energies (MeV).  Source: NUBASE 2020 / AME 2020.
AME_BINDING = {
    "D":   2.224566,
    "T":   8.481798,
    "3He": 7.71806,
    "4He": 28.295674,
    # Extension atoms:
    "5Li": 26.330,      # unbound; resonance-extrapolated value
    "6He": 29.268,      # β-emitter, half-life 0.8 s
    "6Li": 31.994,      # stable
    "6Be": 26.924,      # unbound; AME-2020 extrapolated
}

Z_N = {
    "D":   (1, 1),
    "T":   (1, 2),
    "3He": (2, 1),
    "4He": (2, 2),
    "5Li": (3, 2),
    "6He": (2, 4),
    "6Li": (3, 3),
    "6Be": (4, 2),
}

# ρ = A − 1 per the magic-shell empirical-instantiation convention
# (D: ρ=1, T: ρ=2, ³He: ρ=2, ⁴He: ρ=3 verified in main witness).
def rho_of(Z: int, N: int) -> int:
    return (Z + N) - 1


def main() -> int:
    q_sym = sp.symbols("q", positive=True)
    q_0_sp = sp.Float(Q_50_DIGIT_STR, 50)
    m_e_mp = mpf(str(M_E_MEV))

    builder = (
        WitnessBuilder("delta-cat-extension", engine="sympy+mpmath")
        .set_description(
            "Δ_cat extension to atoms beyond the 4-atom magic-shell "
            "bench.  Computes |τ_M(β(Z, N))| symbolically via "
            "markov_peel + 50-dps mpmath eval at q_0, then "
            "Δ_cat = AME(binding) − m_e · ρ · |τ_M| with ρ = A − 1.  "
            "Provides 4+ new data points for the α·n_pp + β·n_nn + γ "
            "linear fit in PR #656 v6 — distinct (n_pp, n_nn) "
            "combinations beyond the 3-point trivial system."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md"
        )
        .add_parameter("mp_dps", mp.dps)
        .add_parameter("rho_formula", "rho = A - 1")
        .add_parameter("ame_source", "AME 2020 binding energies (MeV)")
    )

    rows = []
    print("=" * 110)
    print("  Δ_cat extension across atoms")
    print("=" * 110)
    print()
    print(f"  {'atom':<5}{'(Z,N)':<8}{'A':>3}{'ρ':>3}"
          f"{'(n_pp,n_pn,n_nn)':>18}{'AME (MeV)':>12}"
          f"{'|τ_M|':>14}{'cat (MeV)':>12}{'Δ_cat (MeV)':>14}{'compute s':>10}")
    print("  " + "-" * 105)

    for atom, (Z, N) in Z_N.items():
        A = Z + N
        rho = rho_of(Z, N)
        n_pp, n_pn, n_nn = interface_composition(Z, N)

        # Skip if AME unknown
        if atom not in AME_BINDING:
            continue
        ame = AME_BINDING[atom]

        t0 = time.time()
        try:
            tr_sym = tr_M_atomic(Z, N, include_inter=True)
            if hasattr(tr_sym, "subs"):
                tr_at = tr_sym.subs(q_sym, q_0_sp).evalf(50)
            else:
                tr_at = sp.sympify(tr_sym).evalf(50)
            abs_tr = abs(mpf(str(tr_at)))
            categorical = m_e_mp * rho * abs_tr
            delta_cat = mpf(str(ame)) - categorical
            elapsed = time.time() - t0
            ok = True
            err = None
        except Exception as e:
            abs_tr = None
            categorical = None
            delta_cat = None
            elapsed = time.time() - t0
            ok = False
            err = str(e)

        row = {
            "atom": atom, "Z": Z, "N": N, "A": A, "rho": rho,
            "interface_composition": {
                "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
            },
            "AME_MeV": ame,
            "compute_time_sec": elapsed,
            "ok": ok,
        }
        if ok:
            row["abs_tr_M_50dps"] = mp.nstr(abs_tr, 50)
            row["abs_tr_M_float"] = float(abs_tr)
            row["categorical_MeV_50dps"] = mp.nstr(categorical, 50)
            row["categorical_MeV_float"] = float(categorical)
            row["delta_cat_MeV_50dps"] = mp.nstr(delta_cat, 50)
            row["delta_cat_MeV_float"] = float(delta_cat)
        else:
            row["error"] = err
        rows.append(row)

        ic_str = f"({n_pp},{n_pn},{n_nn})"
        if ok:
            print(f"  {atom:<5}({Z},{N})  {A:>3}{rho:>3}{ic_str:>18}"
                  f"{ame:>12.4f}{float(abs_tr):>14.8f}"
                  f"{float(categorical):>12.4f}{float(delta_cat):>+14.4f}"
                  f"{elapsed:>10.1f}")
        else:
            print(f"  {atom:<5}({Z},{N})  {A:>3}{rho:>3}{ic_str:>18}"
                  f"{ame:>12.4f}{'FAILED':>14}{'':>12}{err[:14]:>14}"
                  f"{elapsed:>10.1f}")

    builder.add_data("per_atom_extension", rows)

    # ── Linear fit re-run with extended data ──────────────────────
    fit_rows = [r for r in rows if r["ok"]]
    # Build (n_pp, n_pn, n_nn) → Δ_coupling system per the v6 convention.
    # Δ_coupling per-atom anchor:
    #   D (1,1)   : Δ_cat(D)                       (A=2 baseline)
    #   T (1,2)   : Δ_cat(T)   − Δ_cat(D)
    #   ³He (2,1) : Δ_cat(³He) − Δ_cat(D)
    #   ⁴He (2,2) : Δ_cat(⁴He) − 2·Δ_cat(³He)
    # For higher atoms, use the natural extension:
    #   Δ_coupling(Z, N) = Δ_cat(Z, N) − Z·Δ_cat(proton) − N·Δ_cat(neutron)
    # ...but proton/neutron are anchors (B=0 for free nucleon, by def).
    # Simpler: use Δ_cat directly minus the leading-order categorical
    # contribution, i.e. the H7a-residual form already in v6.
    # For the FIT we want residual of Δ_cat from H7a · base.
    import numpy as np

    q0 = Q_MP
    h_q = HA_MP
    log_inv_h = mp.log(1 / h_q)
    E0 = m_e_mp / (q0 * (q0 - 1))
    base = E0 * log_inv_h

    def q_int(n, q):
        if n == 0:
            return mp.mpf(0)
        return (q ** n - q ** (-n)) / (q - 1 / q)

    # Use Δ_cat directly as the regression target (NOT Δ_coupling).
    # The hypothesis becomes:
    #   Δ_cat(Z, N) ≈ [A−2]_q · E_0 · log(1/h) · g(Z, N) +
    #                α·n_pp + β·n_nn + γ
    # Where g(Z, N) is what closes (2,2) to 0.169%.  For the
    # extended fit, fit Δ_cat directly with features (n_pp, n_nn, A−1, 1).
    print()
    print("  Linear regression on extended Δ_cat data:")
    print(f"    target: Δ_cat(Z, N)")
    print(f"    features: (n_pp, n_nn, A−1, intercept)")
    print()

    A_mat = []
    b_vec = []
    labels = []
    for r in fit_rows:
        ic = r["interface_composition"]
        A_mat.append([ic["n_pp"], ic["n_nn"], r["A"] - 1, 1.0])
        b_vec.append(r["delta_cat_MeV_float"])
        labels.append(r["atom"])
    A_mat = np.array(A_mat)
    b_vec = np.array(b_vec)

    fit_summary = {
        "fit_atoms": labels,
        "fit_data_points": len(fit_rows),
    }
    if len(fit_rows) >= 4:
        sol, residuals, rank, sv = np.linalg.lstsq(
            A_mat, b_vec, rcond=None
        )
        alpha, beta, gamma, intercept = sol
        # Per-atom prediction and residual:
        preds = A_mat @ sol
        resids = b_vec - preds
        fit_summary["alpha_per_pp_MeV"] = float(alpha)
        fit_summary["beta_per_nn_MeV"] = float(beta)
        fit_summary["gamma_per_A_minus_1_MeV"] = float(gamma)
        fit_summary["intercept_MeV"] = float(intercept)
        fit_summary["fit_rank"] = int(rank)
        fit_summary["fit_residuals_sum_sq"] = (
            float(residuals[0]) if len(residuals) > 0 else 0.0
        )
        fit_summary["fit_is_trivial"] = rank >= 4 and rank == len(fit_rows)
        fit_summary["per_atom_residuals"] = [
            {"atom": l, "pred": float(p), "actual": float(a),
             "residual": float(a - p)}
            for l, p, a in zip(labels, preds, b_vec)
        ]

        print(f"    α (per pp)        = {alpha:+.4f} MeV")
        print(f"    β (per nn)        = {beta:+.4f} MeV")
        print(f"    γ (per A−1)       = {gamma:+.4f} MeV")
        print(f"    intercept         = {intercept:+.4f} MeV")
        print(f"    rank              = {rank}")
        print(f"    sum-sq residuals  = {fit_summary['fit_residuals_sum_sq']:.6f}")
        print(f"    trivial (rank=n)? = {fit_summary['fit_is_trivial']}")
        print()
        print("    Per-atom predictions:")
        for entry in fit_summary["per_atom_residuals"]:
            print(f"      {entry['atom']:<5} pred={entry['pred']:>10.4f}  "
                  f"actual={entry['actual']:>10.4f}  "
                  f"resid={entry['residual']:>+10.4f}")
    else:
        print(f"    Need ≥ 4 atoms for fit; have {len(fit_rows)}")

    builder.add_data("regression_fit", fit_summary)

    builder.add_assertion(
        name="extended_delta_cat_computed",
        computed=len(fit_rows),
        expected=8,
        tolerance=2.0,
    )

    out = builder.save()
    print(f"\n  Witness emitted: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
