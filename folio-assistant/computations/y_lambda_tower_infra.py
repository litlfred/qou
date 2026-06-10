#!/usr/bin/env python3
"""y_λ tower infra — closed-form Markov weights y_λ(q₀) for ANY n (all nuclides).

## The question this answers

"y_λ via trace_weights_n for any n? is it a recursive build? how to optimize?"
— and the planning ask "we need to do all nuclides".

**It is NOT recursive.** The Jones–Markov weight y_λ has a CLOSED FORM via the
hook-content principal specialization of the Schur function (Wenzl bridge):

    s_λ = Q^{n(λ)} · ∏_{x∈λ} (1 − Q^r·Q^{c(x)}) / (1 − Q^{h(x)}) ,   Q = q²,
    y_λ = s_λ / Z ,   Z = Σ_μ s_μ · f^μ   (enforces Σ_λ y_λ f^λ = tr_M(1) = 1)

(`schur_principal_mpmath.y_lambda_at_q0_mpmath`). Each cell of λ is one mpf
multiply + one mpf power, so a whole table H_n is O(Σ_λ |λ|) = O(p(n)·n) mpf
ops — no Wenzl H_n→H_{n-1} recursion, no Rust kernel (which timed out at n=12,
>45 min), no sympy expansion (~30 min at n=13). Measured: n=15 → 0.03 s,
n=18 → 0.09 s, n=30 → 2 s. Verified ≡ the symbolic-sourced canonical witness to
~10⁻⁴⁸ at n=6,9,12 (true 50 dps), so it is the SAME object, just fast.

## What "all nuclides" costs (the honest wall)

The y_λ leg is free for any n we can ENUMERATE partitions of. The hard wall is
p(n) (Hardy–Ramanujan growth):

    A   n=3A   p(n)        y_λ wall (closed form)
    ─   ────   ─────────   ──────────────────────
    5    15        176      ms
    8    24      1 575      ~0.5 s
    12   36     17 977      ~6 s
    16   48    ~1.3e5       ~min
    20   60    ~9.7e5       ~min–hr (enumeration-bound)

So the FULL Wedderburn decomposition (every λ⊢3A) is tractable to A≈15–20. For
heavier nuclei the productive path is NOT brute-force enumeration but the
**operator-selection LP/SDP active set** (the few saturating Wedderburn channels,
`prop:operator-selection-lp` / `nucleus_operator_selection_sdp.py`) plus the
**identical-nucleon symmetrization** (`symmetrized_constituent_general.py`,
h_Z/e_Z via Frobenius) — both of which need only the active λ's y_λ, all of
which this closed form delivers in O(|λ|). The χ_λ(braid word) evaluation (the
matrix-M kernel), not y_λ, is the per-nucleus bottleneck for large A.

## What this module does

Non-destructively EXTENDS the canonical `y-lambda-mpfr-witness.json` `tables_by_n`
to a requested n-range via the closed form, leaving the symbolic-sourced n≤12
entries untouched and gating on a closed-form-≡-symbolic agreement check first.
This unblocks any matrix-M χ consumer (`_load_y_lambda(n)`) at n>12 — e.g.
⁵Li (H₁₅), ⁶Li (H₁₈), ⁷Li (H₂₁), ⁸Be (H₂₄).

Output: updates `y-lambda-mpfr-witness.json` (merge) + `y-lambda-tower-infra.witness.json`.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from schur_principal_mpmath import (  # noqa: E402
    y_lambda_at_q0_mpmath, _f_lambda, partitions_of,
)

CANONICAL = HERE / "y-lambda-mpfr-witness.json"
GATE_TOL = mp.mpf(10) ** -40  # closed-form must match symbolic source this well
SOURCE_TAG = ("schur_principal_mpmath closed-form principal specialization "
              "s_λ=Q^{n(λ)}∏(1−Q^r Q^{c})/(1−Q^{h}); verified ≡ symbolic to ~1e-48")


def _table_entries(n: int, q_val: mp.mpf) -> tuple[list[dict], mp.mpf, float]:
    """Closed-form y_λ table for H_n: (weights list, |Σy·fλ−1| residual, wall)."""
    t0 = time.time()
    y = y_lambda_at_q0_mpmath(n, q_val)
    wall = time.time() - t0
    weights = [{"partition": list(lam), "y_lambda": mp.nstr(y[lam], 50)}
               for lam in partitions_of(n)]
    resid = abs(sum(y[lam] * _f_lambda(lam) for lam in y) - 1)
    return weights, resid, wall


def _gate_against_symbolic(W: dict, q_val: mp.mpf) -> dict:
    """Verify the closed form reproduces every EXISTING (symbolic) n to GATE_TOL."""
    report = {}
    for n_str, tbl in sorted(W["tables_by_n"].items(), key=lambda kv: int(kv[0])):
        ref = {tuple(w["partition"]): mp.mpf(w["y_lambda"]) for w in tbl["weights"]}
        mine = y_lambda_at_q0_mpmath(int(n_str), q_val)
        maxerr = mp.mpf(0)
        for lam, rv in ref.items():
            mv = mine.get(lam, mp.mpf("nan"))
            e = abs(mv - rv) if abs(rv) < mp.mpf("1e-40") else abs(mv - rv) / abs(rv)
            maxerr = max(maxerr, e)
        report[n_str] = float(maxerr)
        if maxerr > GATE_TOL:
            raise AssertionError(
                f"closed-form y_λ disagrees with symbolic source at n={n_str}: "
                f"max_rel_err={float(maxerr):.2e} > gate {float(GATE_TOL):.0e}. "
                f"Convention drift — refusing to extend the canonical witness.")
    return report


def extend_y_lambda_tower(up_to_n: int, witness_path: Path = CANONICAL,
                          q_val: mp.mpf = Q_MP) -> dict:
    """Extend the canonical y_λ witness's tables_by_n to n ≤ up_to_n (closed form).

    Non-destructive: preserves existing n entries; adds missing n only. Gates on
    closed-form ≡ existing (symbolic) agreement before writing. Returns a build
    report (per-n parts / residual / wall / source / added?).
    """
    W = json.loads(witness_path.read_text())
    gate = _gate_against_symbolic(W, q_val)
    existing = set(W["tables_by_n"].keys())
    rows = []
    for n in range(2, up_to_n + 1):
        n_str = str(n)
        if n_str in existing:
            rows.append({"n": n, "num_partitions": len(partitions_of(n)),
                         "added": False, "source": "symbolic (pre-existing)",
                         "gate_rel_err": gate.get(n_str)})
            continue
        weights, resid, wall = _table_entries(n, q_val)
        W["tables_by_n"][n_str] = {
            "n": n, "num_partitions": len(weights), "weights": weights,
            "source": SOURCE_TAG, "norm_residual": mp.nstr(resid, 6),
        }
        rows.append({"n": n, "num_partitions": len(weights), "added": True,
                     "source": "closed-form", "norm_residual": float(resid),
                     "wall_sec": round(wall, 4)})
    # provenance breadcrumb on the canonical file
    W.setdefault("extension", {})
    W["extension"]["closed_form_tower"] = {
        "producer": "y_lambda_tower_infra.py",
        "method": SOURCE_TAG,
        "owns_n": sorted(int(r["n"]) for r in rows if r["added"]),
        "up_to_n": up_to_n,
    }
    witness_path.write_text(json.dumps(W, indent=2) + "\n")
    return {"rows": rows, "gate": gate}


def main() -> int:
    t0 = time.time()
    up_to = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    mp.mp.dps = 50
    print("=" * 84)
    print(f" y_λ tower infra — closed-form principal specialization, extend to n={up_to}")
    print(f"   q₀ = {Q_50_DIGIT_STR[:22]}…   (no recursion; O(p(n)·n) mpf ops)")
    print("=" * 84)
    rep = extend_y_lambda_tower(up_to)
    print(f" {'n':>3}{'A=n/3':>7}{'p(n)':>8}{'added':>7}{'wall(s)':>9}"
          f"{'|Σy·fλ−1|':>14}  source")
    print(" " + "-" * 82)
    for r in rep["rows"]:
        a = f"{r['n']/3:.2f}" if r["n"] % 3 == 0 else "—"
        wall = f"{r.get('wall_sec', 0):.4f}" if r["added"] else ""
        resid = f"{r.get('norm_residual', 0):.2e}" if r["added"] else \
            f"≡sym {r.get('gate_rel_err', 0):.1e}"
        print(f" {r['n']:>3}{a:>7}{r['num_partitions']:>8}"
              f"{('yes' if r['added'] else '·'):>7}{wall:>9}{resid:>14}  "
              f"{'closed-form' if r['added'] else 'symbolic'}")
    print(" " + "-" * 82)
    added = [r["n"] for r in rep["rows"] if r["added"]]
    print(f" extended canonical y-lambda-mpfr-witness.json: added n={added}")
    print(f" gate (closed-form ≡ symbolic, n≤12): max_rel_err="
          f"{max(rep['gate'].values()):.2e} < 1e-40 ✓")

    w = WitnessBuilder("y-lambda-tower-infra", engine="mpmath", start_time=t0)
    w.set_description(
        "Closed-form y_λ(q₀) tower for ANY n (all nuclides). y_λ = s_λ/Z via the "
        "hook-content principal specialization (Wenzl bridge) — NOT recursive, "
        "O(p(n)·n) mpf ops; supersedes the Rust kernel (timed out n=12) and sympy "
        "(~30 min n=13). Verified ≡ the symbolic-sourced canonical witness to "
        "~1e-48 at n=6,9,12; non-destructively extends tables_by_n past n=12 to "
        "unblock matrix-M χ at ⁵Li(H₁₅)/⁶Li(H₁₈)/⁷Li(H₂₁)/⁸Be(H₂₄). The y_λ leg "
        "is free for any enumerable n; the wall for heavy nuclei is p(n) (full "
        "Wedderburn) — for A≳15–20 use the operator-selection LP active set + "
        "Frobenius symmetrization, both of which need only the active λ's y_λ."
    )
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("up_to_n", up_to)
    w.add_data("rows", rep["rows"])
    w.add_data("gate_closed_form_vs_symbolic", rep["gate"])
    w.add_data("added_n", added)
    w.add_assertion(
        name="closed_form_matches_symbolic_source",
        computed=float(max(rep["gate"].values())), expected=0.0, tolerance=1e-40,
        source="max rel err of closed-form y_λ vs the symbolic-sourced canonical "
               "witness over all pre-existing n (≤12) — confirms the tower "
               "extension is the same object, just non-recursive/fast.",
    )
    # every newly-added table must satisfy the tr_M(1)=1 normalization
    new_resid = [r["norm_residual"] for r in rep["rows"] if r["added"]]
    if new_resid:
        w.add_assertion(
            name="extended_tables_normalized",
            computed=float(max(new_resid)), expected=0.0, tolerance=1e-45,
            source="max |Σ_λ y_λ f^λ − 1| over the newly-added n — the Jones "
                   "Markov trace normalization tr_M(1)=1 holds at true 50 dps.",
        )
    out = w.save()
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
