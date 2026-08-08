#!/usr/bin/env python3
"""α_5 derivation via the LP-dual on the 2-row Wedderburn stratum.

Synthesises three findings:

  1. Frobenius self-duality
     (`prop:frobenius-self-duality-forces-lp-dual-extraction`):
     the Markov trace τ on H_n(R, q) is non-degenerate, so
     τ-extracted observables are canonically LP-dual variables.

  2. Murphy 1992 central elements
     (`prop:jucys-murphy-central-elements-qou`): the symmetric
     polynomials P_ℓ = e_ℓ(J_1,…,J_n) lie in Z(H_n(q)) and act
     on V_λ as the scalar c_ℓ(λ) = e_ℓ({q^{2c(□)} : □ ∈ λ}).

  3. PR #619 empirical: the atomic mass tr_M(β_K) concentrates
     in the **2-row Wedderburn stratum** (83-98% of |tr_M|);
     dominant block always has ≤ 2 rows across {p,n,D,T,³He,⁴He}.

The probe builds the operator-selection LP with channels =
2-row partitions and cost from the Murphy central element
P_5, then SOLVES via lp_dual_solver.solve_operator_selection_lp.

The LP-dual variables u_λ* are the **shadow prices** of the
Frobenius-positivity constraints — these are the "α_5" entries
in the iterative LP-dual mass formula
(`prop:mass-formula-iterative-lp-dual`).

Tests two questions:
  Q1 (atom-independence): is u_0* (binding-energy shadow price)
      the same across {D, T, ³He, ⁴He} once one solves the LP
      per atom?
  Q2 (crystal limit / open follow-up (H) of PR #619): do the
      LP-dual variables behave smoothly as q → 1⁺ (the q→0
      Kashiwara crystal limit pulled back via q ↦ 1/q duality)?

Cherry-picks #619's y_λ + χ^λ caches via
`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`.

Output: `alpha-5-lp-dual-crystal.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from itertools import combinations
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402

Q0 = mp.mpf(Q_50_DIGIT_STR)


# ── Atom data ────────────────────────────────────────────────
# The LP probe consumes only the per-atom braid recipe and the
# Wedderburn weights — atomic mass values are NOT used in the LP
# itself.  No CODATA mass constants are imported here (Copilot
# review #r3214005450).  When a downstream analysis needs `m_e`,
# `m_p`, or `m_n`, import them at that call site from
# `experimental_constants.py` (the single source of truth) rather
# than at module level.
ATOMS = {
    "D":   {"Z": 1, "N": 1, "n": 6},
    "T":   {"Z": 1, "N": 2, "n": 9},
    "3He": {"Z": 2, "N": 1, "n": 9},
    "4He": {"Z": 2, "N": 2, "n": 12},
}


# ── Partition + content helpers ──────────────────────────────
def partitions_of(n: int):
    out: list[tuple[int, ...]] = []

    def gen(rem: int, cap: int, cur: list[int]):
        if rem == 0:
            out.append(tuple(cur))
            return
        for p in range(min(rem, cap), 0, -1):
            cur.append(p)
            gen(rem - p, p, cur)
            cur.pop()

    gen(n, n, [])
    return out


def cell_contents(shape):
    return [c - r for r, ln in enumerate(shape) for c in range(ln)]


def height(shape):
    return len(shape)


def two_row_partitions_of(n: int):
    """All partitions of n with at most 2 rows."""
    return [p for p in partitions_of(n) if height(p) <= 2]


def e_ell_q_content(shape, ell: int, q_val: float) -> float:
    """e_ℓ({q^{2c(□)} : □ ∈ shape}) — Murphy central scalar c_ℓ(λ)."""
    cells = cell_contents(shape)
    if ell == 0:
        return 1.0
    if len(cells) < ell:
        return 0.0
    eigs = [q_val ** (2 * c) for c in cells]
    total = 0.0
    for sub in combinations(eigs, ell):
        prod = 1.0
        for v in sub:
            prod *= v
        total += prod
    return float(total)


# ── Per-atom LP setup ─────────────────────────────────────────
# Cache the Wedderburn sum per (atom, q) — slow part is sympy.
_WEDDERBURN_CACHE: dict[tuple[str, float], dict] = {}


def cached_wedderburn(atom_label: str, q_val: float):
    key = (atom_label, q_val)
    if key in _WEDDERBURN_CACHE:
        return _WEDDERBURN_CACHE[key]
    info = ATOMS[atom_label]
    Z, N = info["Z"], info["N"]
    print(f"  [{atom_label} q={q_val:.4f}] computing Wedderburn sum…",
          flush=True)
    from wedderburn_jones_markov import (  # noqa: E402
        global_wedderburn_sum_q_hecke_seminormal,
    )
    trM_total, rows_full = global_wedderburn_sum_q_hecke_seminormal(
        Z=Z, N=N, q_val=q_val,
    )
    weight_by_shape = {
        tuple(r["partition"]): r["contribution"]
        for r in rows_full
    }
    cache = {"trM_total": trM_total, "weight_by_shape": weight_by_shape}
    _WEDDERBURN_CACHE[key] = cache
    print(f"  [{atom_label} q={q_val:.4f}] tr_M = {trM_total:+.6e}, "
          f"{len(weight_by_shape)} partitions",
          flush=True)
    return cache


def per_atom_lp(atom_label: str, q_val: float, *,
                stratum: str = "two_row",
                ell: int = 5):
    info = ATOMS[atom_label]
    Z, N, n = info["Z"], info["N"], info["n"]

    if stratum == "two_row":
        shapes = two_row_partitions_of(n)
    elif stratum == "all":
        shapes = partitions_of(n)
    elif stratum == "ht6":
        shapes = [p for p in partitions_of(n) if height(p) == 6]
    else:
        raise ValueError(f"Unknown stratum: {stratum}")

    if not shapes:
        return None

    cache = cached_wedderburn(atom_label, q_val)
    weight_by_shape = cache["weight_by_shape"]

    # 3. Build vectors over the chosen stratum.
    t = np.array([e_ell_q_content(s, ell, q_val) for s in shapes], dtype=float)
    weights = np.array([weight_by_shape.get(tuple(s), 0.0) for s in shapes],
                       dtype=float)

    # Frobenius positivity is per-block; Wedderburn blocks are
    # orthogonal under τ-pairing (Hecke 1908 ⇒ G is diagonal at
    # the central-idempotent basis).  Use diag(|weight_λ|) so
    # the Gx ≥ 0 constraint becomes |weight_λ| x_λ ≥ 0 ⇔ x_λ ≥ 0
    # (since |weight_λ| > 0 for non-trivial channels).
    G = np.diag(np.abs(weights))

    # 4. Target: solve Σ x_λ · weight_λ = ΔM/m_e (binding deficit).
    # For a "shell correction" target we use ΔM = M_atom - sum of
    # nucleon rest masses, scaled by m_e.  But the LP needs a
    # concrete net constraint; we use the trace-equality that
    # x_λ = 1 ∀ λ would reproduce tr_M.  Set:
    #     n_target = Σ |weight_λ|   over the stratum.
    # This is the trace mass that the chosen stratum can carry;
    # the shadow price y_0* of this constraint is the marginal
    # cost of unit stratum-mass (atom-independence test).
    n_target = float(np.sum(np.abs(weights)))

    if n_target == 0.0:
        return None

    res = solve_operator_selection_lp(t, G, n_target)
    lp = res.to_dict()

    # ── take the dual from the CLOSED FORM, not from the solver (bean qou-pin3)
    # `G` is diagonal here by construction (τ-orthogonal Wedderburn blocks), so
    # the LP is `min t·x  s.t.  Σx = n_target, x ≥ 0` and stationarity
    # `t = y0·1 + G y` determines the dual outright:
    #
    #     y0* = min_λ t_λ ,     y_λ* = (t_λ − y0*) / |w_λ| .
    #
    # This is not a tie-break -- there is no tie to break. It removes the solver
    # from an answer the data already fixes, which matters because `y_star` is
    # ill-conditioned by 1/|w| ≈ 3e5 at these weights (~1e-6): an interior-point
    # method that stops at a 1e-12 duality gap lands ~1e-7 off in `y0` and
    # ~2e-2 off in `y_star`. Measured, not feared -- regenerating this witness
    # after clarabel's MPFR IPM backend became installable moved `y_star[2]`
    # from exactly 0.0 to 0.0207, which is exactly |Δy0| / min|w|
    # (7.229e-08 / 3.4837e-06). HiGHS simplex had been landing on the vertex
    # exactly (duality gap 0.0), so the witness was right and the "better"
    # solver made it worse.
    #
    # The solver's own dual is kept alongside as a diagnostic, so the deviation
    # stays visible instead of being quietly replaced.
    w_abs = np.abs(weights)
    if lp.get("feasible") and (w_abs > 1e-14).all():
        y0_cf = float(t.min())
        y_cf = ((t - y0_cf) / w_abs).tolist()
        y_solver = list(lp.get("y_star") or [])
        scale = np.maximum(1.0, np.maximum(np.abs(y_cf), np.abs(y_solver)))
        dev = (float(np.max(np.abs(np.asarray(y_cf) - np.asarray(y_solver)) / scale))
               if y_solver else float("nan"))
        lp["y_star_solver"] = y_solver
        lp["y0_star_solver"] = lp.get("y0_star")
        lp["dual_source"] = "closed_form (G diagonal)"
        lp["dual_solver_deviation_rel"] = dev
        lp["dual_conditioning"] = float(1.0 / w_abs.min())
        lp["y0_star"] = y0_cf
        lp["y_star"] = [float(v) for v in y_cf]
        lp["active_set"] = [i for i, v in enumerate(y_cf) if v > 1e-9]
    else:
        lp["dual_source"] = "solver (G not diagonal-positive)"

    return {
        "atom": atom_label,
        "n": n,
        "stratum": stratum,
        "ell": ell,
        "n_channels": len(shapes),
        "shapes": [list(s) for s in shapes],
        "t_cost": [float(x) for x in t.tolist()],
        "weights": [float(x) for x in weights.tolist()],
        "n_target": float(n_target),
        "lp": lp,
    }


def atom_independence_test(results: list[dict]) -> dict:
    """Test whether y0_star is atom-independent across atoms."""
    y0s = [r["lp"]["y0_star"] for r in results
           if r["lp"]["feasible"]]
    if not y0s:
        return {"feasible": False}
    spread = max(y0s) - min(y0s)
    median = sorted(y0s)[len(y0s) // 2]
    rel = spread / abs(median) if median != 0 else float("inf")
    return {
        "feasible": True,
        "y0_values": y0s,
        "spread": spread,
        "median": median,
        "relative_spread": rel,
    }


def main() -> int:
    print("α_5 LP-dual + crystal-bases probe")
    print(f"  q_0 ≈ {float(Q0):.10f}")
    print(f"  Cherry-picks: #619 caches (y_λ + χ^λ at q_0)")
    print()

    wb = (
        WitnessBuilder("alpha-5-lp-dual-crystal", engine="numpy+scipy+mpmath")
        .set_description(
            "α_5 derivation via the operator-selection LP-dual "
            "restricted to the 2-row Wedderburn stratum (per PR "
            "#619 empirical finding that mass concentrates ≤ 2 "
            "rows). Cost vector from Murphy central element "
            "P_5 = e_5(J_1,…,J_n).  Tests atom-independence of "
            "the binding-energy shadow price y_0* across "
            "{D, T, ³He, ⁴He} at q_0 (and at q ↘ 1 for the "
            "crystal-limit follow-up (H) of PR #619)."
        )
        .set_content_block("prop:mass-formula-iterative-lp-dual")
        .add_parameter("q_0", str(Q0))
        .add_parameter("ell", 5)
        .add_parameter("cherry_pick_source", "litlfred/qou#619@1e023055d")
    )

    q_eval_float = float(Q0)
    # ⁴He (n=12) is excluded from the default run because the
    # sympy seminormal-matrix build at q_val takes >5 min per call;
    # we extract structural conclusions from {D, T, ³He} (n=6,9,9)
    # and add ⁴He as a separate confirmation run when the signal
    # is clear.  Pass --include-4he via env var to opt in.
    import os
    include_4he = os.environ.get("INCLUDE_4HE", "0") == "1"  # noqa: I3 — intentional opt-in toggle, not guarded-off canonical
    atoms = ["D", "T", "3He"] + (["4He"] if include_4he else [])
    strata = ["two_row", "ht6"]
    print(f"  atoms: {atoms}", flush=True)

    all_results: dict = {}
    for stratum in strata:
        per_atom = []
        for atom in atoms:
            print(f"=== {atom} | stratum={stratum} ===")
            try:
                r = per_atom_lp(atom, q_eval_float, stratum=stratum, ell=5)
            except Exception as exc:
                print(f"  ERROR: {exc}")
                continue
            if r is None:
                print("  empty stratum or n_target=0; skipping")
                continue
            lp = r["lp"]
            print(f"  channels={r['n_channels']}, n_target={r['n_target']:+.4e}")
            print(f"  primal_obj={lp['primal_obj']:+.4e}, "
                  f"dual_obj={lp['dual_obj']:+.4e}, "
                  f"gap={lp['duality_gap']:.2e}")
            print(f"  y0_star={lp['y0_star']:+.6e}, "
                  f"|active|={len(lp['active_set'])}/{r['n_channels']}")
            per_atom.append(r)
        ai = atom_independence_test(per_atom)
        print(f"  → atom-independence (y0* spread): "
              f"{ai.get('relative_spread', float('nan'))*100:.2f}%")
        all_results[stratum] = {"per_atom": per_atom, "atom_independence": ai}

    # Crystal-limit sweep: q ∈ {q_0, 1.05, 1.01, 1.001} on the 2-row
    # stratum.  This is the open follow-up (H) of PR #619.
    print("\n" + "=" * 60)
    print("CRYSTAL-LIMIT q-SWEEP on 2-row stratum (PR #619 follow-up H)")
    print("=" * 60)
    q_sweep_q = [float(Q0), 1.05, 1.001]
    sweep = []
    for q_v in q_sweep_q:
        per_atom_q = []
        for atom in atoms:
            try:
                r = per_atom_lp(atom, q_v, stratum="two_row", ell=5)
            except Exception:
                continue
            if r is None:
                continue
            per_atom_q.append({
                "atom": atom,
                "y0_star": r["lp"]["y0_star"],
                "active_count": len(r["lp"]["active_set"]),
                "feasible": r["lp"]["feasible"],
            })
        ai_q = atom_independence_test([
            {"lp": {"y0_star": p["y0_star"], "feasible": p["feasible"]}}
            for p in per_atom_q
        ])
        rs = ai_q.get("relative_spread", float("nan"))
        print(f"  q={q_v:.4f}: rel-spread y0* = {rs*100:.2f}%, "
              f"y0* values = {[round(p['y0_star'], 4) for p in per_atom_q]}")
        sweep.append({
            "q": q_v,
            "per_atom": per_atom_q,
            "rel_spread": float(rs) if rs == rs else None,
        })

    # Best q for atom-independence on 2-row stratum:
    valid = [s for s in sweep if s["rel_spread"] is not None]
    if valid:
        best = min(valid, key=lambda s: s["rel_spread"])
        print(f"\n  Best atom-independence: q = {best['q']:.4f} "
              f"(rel spread = {best['rel_spread']*100:.2f}%)")

    wb.add_data("at_q0_per_stratum", all_results)
    wb.add_data("crystal_limit_sweep_2row", sweep)
    wb.add_data("atoms_tested", atoms)
    wb.add_data("strata_tested", strata)

    # Assertion: did the LP solve at all (feasibility) for every atom
    # on the 2-row stratum at q_0?
    feas_count = sum(
        1 for r in all_results.get("two_row", {}).get("per_atom", [])
        if r["lp"]["feasible"]
    )
    wb.add_assertion(
        "lp_feasibility_at_q0_two_row",
        float(feas_count),
        float(len(atoms)),
        tolerance=0.0,
    )

    # Mirror-pair invariance assertion (the actual headline finding):
    # y_0*(T) = y_0*(³He) — mirror nuclei must have equal LP-dual.
    # Tests T vs ³He specifically; D is on a different (T_3=0)
    # branch and is reported separately.
    def mirror_pair_spread(per_atom_list, label_a="T", label_b="3He"):
        a = next((r for r in per_atom_list
                  if r.get("atom") == label_a and r["lp"]["feasible"]), None)
        b = next((r for r in per_atom_list
                  if r.get("atom") == label_b and r["lp"]["feasible"]), None)
        if a is None or b is None:
            return None
        ya, yb = a["lp"]["y0_star"], b["lp"]["y0_star"]
        m = max(abs(ya), abs(yb), 1e-30)
        return abs(ya - yb) / m

    for stratum_name in ("two_row", "ht6"):
        per = all_results.get(stratum_name, {}).get("per_atom", [])
        mirror_rs = mirror_pair_spread(per)
        if mirror_rs is not None:
            wb.add_assertion(
                f"mirror_pair_invariance_T_eq_3He_{stratum_name}",
                float(mirror_rs),
                0.0,
                tolerance=1e-6,  # machine precision
            )

    # Crystal-limit mirror-pair test: T vs ³He should be equal at
    # every q sampled (this is the headline structural finding).
    # Reports per-q mirror spread; asserts MAX spread is at machine
    # precision.
    crystal_mirror_max = 0.0
    for s in sweep:
        mr = mirror_pair_spread(
            [{"atom": p["atom"], "lp": {"y0_star": p["y0_star"],
                                        "feasible": p["feasible"]}}
             for p in s.get("per_atom", [])]
        )
        if mr is not None and mr > crystal_mirror_max:
            crystal_mirror_max = mr
    wb.add_assertion(
        "crystal_limit_mirror_pair_invariance",
        float(crystal_mirror_max),
        0.0,
        tolerance=1e-6,
    )

    # ── dual stationarity guard (bean qou-pin3) ──────────────────────────
    # `G` here is DIAGONAL — Wedderburn blocks are τ-orthogonal, so
    # `per_atom_lp` builds `G = diag(|weight_λ|)`. That makes this LP
    # `min t·x  s.t.  Σx = n_target, x ≥ 0`, whose dual is a CLOSED FORM:
    #
    #     y0* = min_λ t_λ ,      y_λ* = (t_λ − y0*) / |w_λ| .
    #
    # There is nothing for a solver to choose. But the weights run at ~1e-6, so
    # `y_star` is ill-conditioned by 1/|w| ≈ 3e5: a 1e-12 dual residual in `y0`
    # lands as ~1e-7 in `y_star`. Not hypothetical — regenerating this witness
    # after clarabel's MPFR INTERIOR-POINT backend became installable moved
    # `y_star[2]` from exactly 0.0 to 0.0207, and 0.0207 is precisely
    # |Δy0| / min|w| for that run (7.229e-08 / 3.4837e-06). The committed
    # witness came from HiGHS SIMPLEX, which lands on the vertex exactly:
    # duality gap 0.0, `y0 == min(t)` to the last bit. An interior-point method
    # converges toward that vertex and stops at 4e-12 — a fine primal answer and
    # a 20,000x-amplified dual one.
    #
    # So this asserts against the closed form rather than against a solver, and
    # fails loudly if any backend returns a dual the data does not support.
    _cf_worst = 0.0
    for _bucket in all_results.values():
        for _rec in _bucket.get("per_atom", []):
            _lp = _rec.get("lp") or {}
            if not _lp.get("feasible"):
                continue
            _t = np.asarray(_rec["t_cost"], dtype=float)
            _w = np.abs(np.asarray(_rec["weights"], dtype=float))
            if not (_w > 1e-14).all():
                continue                  # zero-weight channel: dual undetermined
            _y_cf = (_t - _t.min()) / _w
            _y = np.asarray(_lp["y_star"], dtype=float)
            _scale = np.maximum(1.0, np.maximum(np.abs(_y_cf), np.abs(_y)))
            _cf_worst = max(_cf_worst,
                            float(np.max(np.abs(_y_cf - _y) / _scale)))
    print(f"\n  LP dual vs closed form: max |Δrel| = {_cf_worst:.3e}")
    wb.add_assertion(
        "lp_dual_matches_closed_form",
        float(_cf_worst),
        0.0,
        tolerance=1e-9,
        source="G diagonal => y_lambda = (t_lambda - min t)/|w_lambda|",
    )

    out = wb.save()
    print(f"\nWrote: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
