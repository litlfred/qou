#!/usr/bin/env python3
"""
per_irrep_pole_deuteron_h6.py — Path A verification of the deuteron
shift exponent (multi-nucleon case) in
`prop:per-nucleon-shift-additive-linearity`.

For the deuteron ($Z = 1$, $N = 1$, $A = 2$, $n = 6$) this script:

  1. Loads cached symbolic $y_\\lambda(q)$ for $n = 6$ from
     `y-lambda-wenzl-bridge-symbolic-witness.json` (skips the
     `solve_y_lambda(6)` symbolic bottleneck — `sp.cancel` on
     11 rationals at $n = 6$ takes >5 min from scratch).
  2. Loads (or computes + caches) symbolic $\\chi^\\lambda_q(\\beta_D)$
     for each $\\lambda \\vdash 6$ from
     `chi-deuteron-h6.witness.json`.  First-run cache emission takes
     ~155 s (the 11 chi_lambda_symbolic calls on the 23-crossing
     deuteron word); subsequent runs are <1 s.
  3. For each $\\lambda$, substitutes $q = u^2$ in both factors and
     computes $\\mathrm{ord}_{u=0}(y_\\lambda \\cdot \\chi^\\lambda_q)$
     per-term (avoids the second sp.together bottleneck on the
     11-term sum).
  4. Returns max over $\\lambda$ if uniquely achieved (the
     u-pole of $\\sum_\\lambda y_\\lambda \\chi^\\lambda$ equals
     max per-term pole when the maximizer is unique, since
     lower-order terms cannot cancel a strict maximum).

**Verified result:** $\\mathrm{ord}_{u=0}(\\mathrm{tr}_M(\\beta_D)) = 40$,
matching $\\mathrm{shift}_{\\mathrm{NF}}(\\beta_D) = 18 \\cdot 1 + 21 \\cdot 1 + 1$
from `prop:per-nucleon-shift-additive-linearity`.  Maximizer:
$\\lambda = (4, 1, 1)$ with per-term pole = 40 (uniquely; next-highest
is $(3, 1, 1, 1)$ at 37).

This closes the multi-nucleon case left open by the proton-only
verification in `per_irrep_pole_proton_h3.py`.

Witness: per-irrep-pole-deuteron-h6.witness.json (CI-integrated)
Chi cache: chi-deuteron-h6.witness.json (auto-emit on first run)
Audit doc: docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md

@module folio-assistant/computations/per_irrep_pole_deuteron_h6
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from hoefsmit_symbolic import chi_lambda_symbolic  # noqa: E402
from per_irrep_pole_proton_h3 import negative_q_pole_order  # noqa: E402

Y_LAMBDA_CACHE = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
CHI_CACHE = _pb.witness_path("chi-deuteron-h6.witness.json", HERE)


def parts_of(n: int) -> list[tuple[int, ...]]:
    out = []
    def rec(rem: int, cap: int, acc: list[int]) -> None:
        if rem == 0:
            out.append(tuple(acc))
            return
        for k in range(min(cap, rem), 0, -1):
            rec(rem - k, k, acc + [k])
    rec(n, n, [])
    return out


def load_y_lambda_n6_symbolic(q_sym: sp.Symbol) -> dict[tuple, sp.Expr]:
    """Load cached symbolic y_λ(q) for n=6 from the Wenzl-bridge witness.

    Skips the >5 min `solve_y_lambda(6)` symbolic bottleneck.
    """
    d = json.loads(Y_LAMBDA_CACHE.read_text())
    n6 = d["tables_by_n"]["6"]
    out: dict[tuple, sp.Expr] = {}
    for w in n6["weights"]:
        lam = tuple(w["partition"])
        expr = sp.sympify(w["y_lambda_symbolic"])
        free = expr.free_symbols
        if free:
            other_q = next(iter(free))
            if other_q is not q_sym:
                expr = expr.subs(other_q, q_sym)
        out[lam] = expr
    return out


def load_or_build_chi_deuteron(q_sym: sp.Symbol) -> tuple[dict[tuple, sp.Expr], float]:
    """Load (or compute + cache) symbolic χ^λ_q(β_D) for each λ ⊢ 6."""
    if CHI_CACHE.exists():
        d = json.loads(CHI_CACHE.read_text())
        out: dict[tuple, sp.Expr] = {}
        for entry in d["chi_lambda_symbolic"]:
            lam = tuple(entry["partition"])
            expr = sp.sympify(entry["chi_q_symbolic"])
            free = expr.free_symbols
            if free:
                other_q = next(iter(free))
                if other_q is not q_sym:
                    expr = expr.subs(other_q, q_sym)
            out[lam] = expr
        return out, 0.0
    # First-run: compute + emit cache.
    print(f"  (first run — building chi cache, ~150 s ...)")
    t0 = time.time()
    crossings = atom_canonical_crossings(1, 1)
    out = {}
    cache_entries = []
    for lam in parts_of(6):
        chi = chi_lambda_symbolic(lam, crossings)
        out[lam] = chi
        cache_entries.append({
            "partition": list(lam),
            "chi_q_symbolic": str(chi),
        })
    elapsed = time.time() - t0
    cache_payload = {
        "description": (
            "Symbolic χ^λ_q(β_D) for the deuteron's 23-crossing canonical "
            "braid word at H_6, per partition λ ⊢ 6.  First-run cache "
            "(~155 s); subsequent loads are O(1).  Used by Path A "
            "deuteron pole-order verification in "
            "per_irrep_pole_deuteron_h6.py."
        ),
        "n_partitions": len(cache_entries),
        "compute_time_sec": elapsed,
        "auditOnly": "docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md",
        "chi_lambda_symbolic": cache_entries,
    }
    CHI_CACHE.write_text(json.dumps(cache_payload, indent=2))
    print(f"  chi cache emitted: {CHI_CACHE.name} ({elapsed:.1f}s)")
    return out, elapsed


def main() -> int:
    """Run Path A on the deuteron via the cached y_λ + chi pipeline."""
    from witness_base import WitnessBuilder  # noqa: E402

    q_var = sp.symbols("q", positive=True)
    u_var = sp.symbols("u", positive=True)

    print("=" * 80)
    print("  Per-irrep pole order — deuteron β_D at H_6 (Path A v2)")
    print("=" * 80)
    print()
    print("  Strategy: cached y_λ from witness + per-term pole order")
    print()

    t0 = time.time()
    print("  Loading cached symbolic y_λ(q) for n=6 ...")
    y_lams_q = load_y_lambda_n6_symbolic(q_var)
    print(f"    loaded {len(y_lams_q)} partitions in {time.time() - t0:.2f} s")

    print()
    print("  Loading (or computing) chi_λ(β_D) ...")
    chi_q, build_time = load_or_build_chi_deuteron(q_var)
    if build_time == 0.0:
        print(f"    loaded {len(chi_q)} cached chi_λ values (instant)")
    else:
        print(f"    built + cached {len(chi_q)} chi_λ values in {build_time:.1f} s")

    print()
    print("  Substituting q = u² and computing per-term u-pole orders ...")
    print(f"    {'λ':<22}{'ord_u=0(y_λ · χ^λ)':>24}")
    print("    " + "-" * 46)
    t0 = time.time()
    term_pole_orders: dict[tuple, int] = {}
    for lam in y_lams_q:
        y_u = y_lams_q[lam].subs(q_var, u_var ** 2)
        chi_u = chi_q[lam].subs(q_var, u_var ** 2)
        term = y_u * chi_u
        ord_u = negative_q_pole_order(term, var=u_var)
        term_pole_orders[lam] = ord_u
        print(f"    {str(lam):<22}{ord_u:>24}")
    print(f"    per-term loop: {time.time() - t0:.1f} s")

    max_lam = max(term_pole_orders, key=term_pole_orders.get)
    max_pole = term_pole_orders[max_lam]
    sorted_orders = sorted(term_pole_orders.values(), reverse=True)
    next_highest = sorted_orders[1] if len(sorted_orders) > 1 else -1
    unique_max = max_pole > next_highest
    expected_shift = 18 * 1 + 21 * 1 + 1  # = 40

    print()
    print(f"  Maximizer:    λ = {max_lam}, per-term pole = {max_pole}")
    print(f"  Next-highest pole: {next_highest} (unique max: {unique_max})")
    print(f"  Predicted shift_NF(D) = 18·1 + 21·1 + 1 = {expected_shift}")
    success = unique_max and max_pole == expected_shift
    if success:
        print(f"  ✓ Path A verified for deuteron: ord_{{u=0}}(tr_M(β_D)) "
              f"= {max_pole}, matching prop:per-nucleon-shift-additive-"
              f"linearity exactly.")
        print(f"    The unique-maximum at λ=(4,1,1) is rigorous: lower-")
        print(f"    order terms cannot cancel a strict maximum.")
    else:
        print(f"  ✗ Path A inconclusive at A=2.")

    builder = (
        WitnessBuilder(name="per-irrep-pole-deuteron-h6", engine="sympy")
        .set_description(
            "Path A: per-term symbolic u-pole-order analysis of the "
            "deuteron's tr_M = Σ_λ y_λ(q) · χ^λ_q(β_D) at q = u² (per "
            "the D(u) convention).  Loads cached symbolic y_λ from "
            "y-lambda-wenzl-bridge-symbolic-witness.json (skips "
            "solve_y_lambda(6) bottleneck) and cached chi_λ(β_D) from "
            "chi-deuteron-h6.witness.json (auto-emit on first run, "
            "~155 s).  Per-term ord_{u=0}(y_λ · χ^λ) avoids the "
            "sp.together bottleneck on 11-term sum.  Verifies "
            "shift_NF(β_D) = 40 = 18·1 + 21·1 + 1, matching "
            "prop:per-nucleon-shift-additive-linearity for the "
            "deuteron multi-nucleon case."
        )
        .set_audit_only(
            "docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md"
        )
    )
    per_term = []
    for lam in sorted(term_pole_orders, key=lambda L: -term_pole_orders[L]):
        per_term.append({
            "partition": list(lam),
            "ord_u_eq_0_y_lambda_times_chi": int(term_pole_orders[lam]),
        })
    builder.add_data("per_term_u_pole_orders", per_term)
    builder.add_data("max_term_lambda", {
        "partition": list(max_lam),
        "ord_u_eq_0": int(max_pole),
        "unique_max": bool(unique_max),
        "next_highest": int(next_highest),
    })
    builder.add_data("full_tr_M_u_pole_inferred", {
        "value": int(max_pole),
        "rigorous": bool(unique_max),
        "expected": expected_shift,
        "formula": "shift_NF(β_D) = 18·Z + 21·N + 1 at (Z=1, N=1) = 40",
        "justification": (
            "Unique-max per-term pole equals full-sum pole because "
            "lower-order terms cannot cancel a strict maximum."
        ),
    })
    builder.add_assertion(
        name="deuteron_full_tr_M_u_pole_eq_shift_NF",
        computed=int(max_pole),
        expected=expected_shift,
    )
    builder.add_assertion(
        name="deuteron_per_term_max_unique",
        computed=int(unique_max),
        expected=1,
    )
    out_path = builder.save()
    print(f"\n  Witness emitted: {out_path}")
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
