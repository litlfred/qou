#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical-only graded probe.
"""
Phase 8 of the 1 ppb workplan
([`docs/audits/2026-05-10-1ppb-workplan-update.md`](../../docs/audits/2026-05-10-1ppb-workplan-update.md))
— **graded Hecke energy probe** for the canonical small-A atom set.

Demonstrates the truncation bound proved in
[`prop:graded-hecke-energy-truncation-bound`](../../content/quantum-observable-universe/braids-and-knots/graded-hecke-energy-truncation-bound.md):
the mass-spectrum generating function $P_K(q) = \\sum_d c_d q^d$
has at most $\\ell(K, q_0) + 1$ nonzero grades, where $\\ell(K, q_0)$
is the confinement level.

The probe stratifies the canonical Wenzl-bridge $|\\mathrm{tr}_M(\\beta_K, q_0)|$
contributions per partition $\\lambda$ by the **partition's content
sum** (`n_λ = Σ_x c_x = Σ_x (col(x) - row(x))`), which is the natural
$\\mathbb{Z}$-grade for the principal Schur specialisation
$s_\\lambda(1, Q, Q^2, \\ldots) = Q^{n(\\lambda)} \\cdot \\prod_x (\\ldots)$
underlying the Wenzl-bridge $y_\\lambda$ formula.

For each atom, the probe reports:
- per-partition $\\lambda$: $n(\\lambda)$, $|y_\\lambda(q_0) \\cdot \\chi^\\lambda(\\beta_K, q_0)|$
- the cumulative trace $\\mathrm{tr}_{M, \\leq \\ell}$ as $\\ell$ grows
- the smallest $\\ell$ at which $|tr_{M,\\leq \\ell} - \\mathrm{tr}_M| < \\text{tol}$
  (the **effective confinement level**)

Output: `graded-hecke-energy-probe.witness.json`.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder
from y_lambda_wenzl_bridge import (
    classical_dim,
    n_lambda,
    partitions_of,
    y_lambda_wenzl_bridge_numeric,
)
from q_parameter import Q as Q0_FLOAT


# Canonical |tr_M(β_K, q_0)| values from derivation_chain.TR_M_AT_Q0;
# used as the convergence target for cumulative truncation.
TR_M_TARGETS = {
    "proton":   mp.mpf("1.0653062286131670"),
    "neutron":  mp.mpf("0.9232332971861535"),
    "deuteron": mp.mpf("0.3882864715477132"),
}

# Atom braid encodings (Z, N, include_inter, n_strands) — same as
# `applied_uniqueness_mass_table.py`.
ATOM_BRAID = {
    "proton":   {"Z": 1, "N": 0, "include_inter": False},
    "neutron":  {"Z": 0, "N": 1, "include_inter": False},
    "deuteron": {"Z": 1, "N": 1, "include_inter": True},
}


def stratified_y_lambda_terms(Z: int, N: int, include_inter: bool,
                              q_val: mp.mpf, dps: int = 50) -> list[dict]:
    """Compute the per-partition contributions y_λ(q_0) · χ^λ(β_K, q_0)
    grouped by the partition's content sum n(λ).

    Returns a list of {λ, n_λ, y_λ, chi_λ, term, |term|} sorted by
    n(λ) ascending — the natural graded ordering.
    """
    from canonical_braid_crossings import atom_canonical_crossings as a2c
    from habiro_coefficients_interpolate import chi_lambda_numerical

    A = Z + N
    crossings = a2c(Z, N, include_inter=include_inter)
    parts = partitions_of(3 * A)
    rows: list[dict] = []
    for lam in parts:
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        if abs(y) < mp.mpf(10) ** -(dps - 5):
            continue
        chi, dim = chi_lambda_numerical(lam, q_val, crossings)
        if dim == 0:
            continue
        term = y * chi
        # Convert chi/term to mp.mpc to keep configured `dps` precision
        # rather than downcasting to double-precision Python complex
        # (per Copilot review on PR #631 round 2).  Store real/imag
        # parts as decimal strings so JSON serialisation is lossless.
        chi_mp = mp.mpc(chi)
        term_mp = mp.mpc(term)
        rows.append({
            "partition": lam,
            "n_lambda": n_lambda(lam),
            "classical_dim": classical_dim(lam),
            "y_lambda": str(y),
            "chi_lambda_real": str(chi_mp.real),
            "chi_lambda_imag": str(chi_mp.imag),
            "term_real": str(term_mp.real),
            "term_imag": str(term_mp.imag),
            "term_abs": str(mp.sqrt(term_mp.real ** 2 + term_mp.imag ** 2)),
        })
    rows.sort(key=lambda r: (r["n_lambda"], r["partition"]))
    return rows


def cumulative_by_grade(rows: list[dict]) -> list[dict]:
    """Group per-partition rows by grade n(λ) and emit cumulative
    sum as the grade increases.

    All arithmetic is in mp.mpf / mp.mpc to preserve the configured
    `dps` precision (per Copilot review on PR #631 round 2).
    """
    by_grade: dict[int, list] = {}
    for r in rows:
        by_grade.setdefault(r["n_lambda"], []).append(r)
    cum_sum_real = mp.mpf(0)
    cum_sum_imag = mp.mpf(0)
    out = []
    for grade in sorted(by_grade.keys()):
        grade_terms = by_grade[grade]
        # Sum the per-partition real / imag parts at full mp precision.
        for r in grade_terms:
            cum_sum_real += mp.mpf(r["term_real"])
            cum_sum_imag += mp.mpf(r["term_imag"])
        cum_abs = mp.sqrt(cum_sum_real ** 2 + cum_sum_imag ** 2)
        out.append({
            "grade": grade,
            "num_partitions_at_grade": len(grade_terms),
            "partitions_at_grade": [r["partition"] for r in grade_terms],
            "grade_sum_real": str(cum_sum_real),
            "grade_sum_imag": str(cum_sum_imag),
            "cumulative_abs": str(cum_abs),
        })
    return out


def effective_confinement_level(cumulative: list[dict],
                                 target_abs: mp.mpf,
                                 tol: mp.mpf = mp.mpf("1e-12")) -> int:
    """Smallest grade ℓ at which |cum(≤ℓ) - target| < tol.

    Returns -1 if the cumulative never converges within tol.
    """
    for entry in cumulative:
        cum = mp.mpf(entry["cumulative_abs"])
        if abs(cum - target_abs) < tol:
            return entry["grade"]
    return -1


def main() -> int:
    w = WitnessBuilder("graded-hecke-energy-probe", engine="mpmath")
    w.set_audit_only("docs/audits/2026-05-10-1ppb-workplan-update.md")
    w.set_description(
        "Phase 8 of the 1 ppb workplan — graded Hecke energy probe "
        "demonstrating the truncation bound from "
        "`prop:graded-hecke-energy-truncation-bound`.  Stratifies the "
        "canonical Wenzl-bridge tr_M(β_K, q_0) per partition λ by the "
        "content sum n(λ) (natural ℤ-grade for the principal Schur "
        "specialisation underlying y_λ).  For each atom in {proton, "
        "neutron, deuteron}: per-partition rows sorted by grade, "
        "cumulative trace as grade grows, and the empirical "
        "confinement level (smallest ℓ at which |cum(≤ℓ) - tr_M| < 1e-12)."
    )
    w.set_content_block("prop:graded-hecke-energy-truncation-bound")

    Q_MP = mp.mpf(str(Q0_FLOAT))

    print("=" * 80)
    print("PHASE 8 — GRADED HECKE ENERGY PROBE")
    print("Stratifies tr_M(β_K, q_0) by content-sum grade n(λ)")
    print("=" * 80)
    print()

    results = {}
    for atom, info in ATOM_BRAID.items():
        Z, N = info["Z"], info["N"]
        target = TR_M_TARGETS[atom]
        print(f"── {atom} (Z={Z}, N={N}, A={Z+N}) ──")
        print(f"  Target |tr_M(β_K, q_0)| = {mp.nstr(target, 16)}")
        rows = stratified_y_lambda_terms(
            Z, N, info["include_inter"], Q_MP, dps=50
        )
        cumulative = cumulative_by_grade(rows)

        max_grade = cumulative[-1]["grade"] if cumulative else 0
        eff_level = effective_confinement_level(
            cumulative, target, tol=mp.mpf("1e-12"),
        )
        eff_level_loose = effective_confinement_level(
            cumulative, target, tol=mp.mpf("1e-3"),
        )

        print(f"  Number of partitions:       {len(rows)}")
        print(f"  Number of grades:           {len(cumulative)}")
        print(f"  Max grade n(λ):             {max_grade}")
        print(f"  Effective ℓ (tol=1e-12):    {eff_level}")
        print(f"  Effective ℓ (tol=1e-3):     {eff_level_loose}")
        print()
        print(f"  Cumulative trace by grade:")
        print(f"  {'grade':>5}  {'num_λ':>6}  {'cum_|tr_M|':>20}  "
              f"{'|cum-target|':>16}")
        for entry in cumulative[:12]:  # show first 12 grades
            cum = mp.mpf(entry["cumulative_abs"])
            diff = abs(cum - target)
            print(f"  {entry['grade']:>5}  {entry['num_partitions_at_grade']:>6}  "
                  f"{mp.nstr(cum, 16):>20}  {mp.nstr(diff, 8):>16}")
        if len(cumulative) > 12:
            print(f"  ... ({len(cumulative) - 12} more grades)")
        print()

        results[atom] = {
            "Z": Z, "N": N, "include_inter": info["include_inter"],
            "target_tr_M": str(target),
            "num_partitions": len(rows),
            "num_grades": len(cumulative),
            "max_grade": max_grade,
            "effective_confinement_level_tight": eff_level,
            "effective_confinement_level_loose_1e_minus_3": eff_level_loose,
            "per_grade_cumulative": cumulative,
        }

    w.add_parameter("q_0", float(Q0_FLOAT))
    w.add_parameter("dps", 50)
    w.add_data("results", results)
    w.add_data("phase", "Phase 8 of 1ppb workplan (2026-05-10)")
    w.add_data("workplan_doc", "docs/audits/2026-05-10-1ppb-workplan-update.md")
    w.add_data("truncation_proposition", "prop:graded-hecke-energy-truncation-bound")
    w.add_data("note",
               "Empirical effective confinement level may be higher "
               "than the Lean-side ConfinementLevel.level when the "
               "grading is by partition content-sum n(λ) rather than "
               "the categorical jet/filtration order; the two coincide "
               "modulo the GS-filtration descent (gs-graded-markov-"
               "trace-existence conjecture).")

    # Assertions: cumulative trace at max grade matches target.
    for atom, r in results.items():
        if not r["per_grade_cumulative"]:
            continue
        last_cum = mp.mpf(r["per_grade_cumulative"][-1]["cumulative_abs"])
        target = mp.mpf(r["target_tr_M"])
        w.add_assertion(
            f"cumulative_at_max_grade_matches_target[{atom}]",
            computed=float(last_cum),
            expected=float(target),
            tolerance=1e-10,
        )

    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
