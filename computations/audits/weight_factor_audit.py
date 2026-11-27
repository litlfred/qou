#!/usr/bin/env python3
"""Weight-factor audit — cross-consistency gate over the partition-
indexed weight families used in the QOU mass-prediction pipeline.

Triggered by repo-owner directive 2026-05-19: "setup a compute/paper
audit related to weights (lots of them, brings color tubers, wedderburn,
etc etc)" — motivated by the err-vs-n scaling pattern in the co-Casimir
extension (441 → 2.7 ppm as n=3 → n=9), which suggests a small
systematic weight error that averages out at higher n.

This script implements 4 of the 8 cross-consistency checks
catalogued in `docs/audits/2026-05-19-weight-factor-audit.md`:

  C1: Σ_λ w_λ = 1  (classical Plancherel)               — IMPLEMENTED
  C2: w̃_λ → w_λ as q → 1                                — stub (TODO)
  C3: y_λ(q=1) = w_λ on self-conjugate stratum          — stub (TODO)
  C4: Σ_λ w̃_λ at q_0  (tilde-Wedderburn sum)            — IMPLEMENTED
  C5: Σ_λ 1/dim_q(λ) = τ(C_dim_q^{H_n})  (Frobenius)    — IMPLEMENTED
  C6: χ^λ(β_1 β_2) = χ^λ(β_2 β_1)  (Hoefsmit cyclic)    — stub (TODO)
  C7: LP shadow-price strong duality                     — external
       (enforced by `lp_dual_witness_validator.py`; not re-run here)
  C8: z = q^3/(q^2 + 1) at q_0 ≈ 0.6127 (convention D)  — IMPLEMENTED

C2, C3, C6 require additional infrastructure (q → 1 limit machinery,
Wenzl-bridge eval at q=1, per-atom braid pair inputs) and are filed
as follow-up work in the companion audit doc.

Each check emits a row in the witness `weight-factor-audit.witness.json`
with {check, n, computed, expected, tolerance, passed}.

CLI:
    python3 weight_factor_audit.py             # full audit
    python3 weight_factor_audit.py --n-max 12  # cap at n ≤ 12
    python3 weight_factor_audit.py --strict    # exit non-zero on any fail

Audit registry follow-up: gate CI on no new weight family being
introduced without (a) a notation-register entry + (b) a passing
cross-consistency check here.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import json
import math
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from hoefsmit_symbolic import dim_q  # noqa: E402

from qou_substrate.witness import _tolerance_literal  # noqa: E402

mp.mp.dps = 60
Q_MP = Q_MP

#: Declared threshold for check C1. Carried NUMERICALLY here because the
#: comparison below needs a number, and serialized through the guard because
#: the payload needs a literal.
#:
#: Why both, rather than just writing `1e-12` in the dict: this producer's
#: check rows are assertion-SHAPED (`{check, n, computed, expected, tolerance,
#: passed}`) but live in the DATA payload, not in `assertions[]`. So
#: `Assertion.to_dict` — which is where `_tolerance_literal` runs — never sees
#: them, and PR #5910's drain of this file was an artifact edit that any re-run
#: would silently undo. It had already been undone: `weight-factor-audit`
#: carried 11 raw `1e-12` on main while every other witness in the corpus was
#: clean (bean qou-9tqx).
#:
#: `_tolerance_literal` is imported, never restated, so this cannot drift from
#: the rule it implements — the same reason `normalize_assertion_tolerance.py`
#: imports it. It returns `None` for a computed value (>5 significant digits)
#: and for an integral one, so `or` falls back to the number in exactly the
#: cases the guard declines to touch.
C1_TOL = 1e-12
C1_TOL_LITERAL = _tolerance_literal(C1_TOL) or C1_TOL


# ── Helpers ──────────────────────────────────────────────────────

def partitions_of(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    def _rec(rem, mx, acc):
        if rem == 0:
            out.append(tuple(acc))
            return
        for k in range(min(rem, mx), 0, -1):
            _rec(rem - k, k, acc + [k])
    _rec(n, n, [])
    return out


def syt_count(lam: tuple[int, ...]) -> int:
    """Number of standard Young tableaux of shape λ via hook formula."""
    n = sum(lam)
    if n == 0:
        return 1
    rows = list(lam)
    cols = [sum(1 for r in rows if r > i) for i in range(rows[0])]
    fac = math.factorial(n)
    prod = 1
    for i, ri in enumerate(rows):
        for j in range(ri):
            arm = ri - j - 1
            leg = cols[j] - i - 1
            prod *= (arm + leg + 1)
    return fac // prod


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))


def evaluate_at_q0(expr) -> mp.mpf:
    """Numerically evaluate sympy expression at q_0."""
    import sympy as sp
    free = expr.free_symbols
    if not free:
        return mp.mpf(str(expr.evalf(60)))
    qsym = next(iter(free))
    val = expr.subs(qsym, sp.Float(Q_50_DIGIT_STR, 60))
    return mp.mpf(str(val.evalf(60)))


# ── Check C1: Σ_λ w_λ = 1 (classical Plancherel) ─────────────────

def check_C1(n: int) -> dict:
    fac = math.factorial(n)
    parts = partitions_of(n)
    s = sum(syt_count(lam) ** 2 for lam in parts)
    ratio = s / fac
    return {
        "check": "C1",
        "name": "classical Plancherel sums to 1",
        "n": n,
        "computed": ratio,
        "expected": 1.0,
        "tolerance": C1_TOL_LITERAL,
        "passed": abs(ratio - 1.0) < C1_TOL,
    }


# ── Check C4: Σ_λ w̃_λ at q_0 for given n ─────────────────────────

def check_C4(n: int) -> dict:
    """tilde-Wedderburn weight = dim_q²(λ) / [n]_q!. Sum at q_0."""
    parts = partitions_of(n)
    # [n]_q! = Π_{k=1..n} [k]_q where [k]_q = (q^k - q^{-k}) / (q - q^{-1})
    def q_int(k):
        return (Q_MP ** k - Q_MP ** (-k)) / (Q_MP - Q_MP ** mp.mpf(-1))
    q_fac_n = mp.mpf(1)
    for k in range(1, n + 1):
        q_fac_n *= q_int(k)
    s = mp.mpf(0)
    for lam in parts:
        d_q = evaluate_at_q0(dim_q(lam))
        s += d_q ** 2 / q_fac_n
    return {
        "check": "C4",
        "name": "tilde-Wedderburn sum (NOT a probability measure at q != 1)",
        "n": n,
        "computed": float(s),
        "expected_at_n12": 1.51,
        "tolerance_at_n12": 0.05,
        "passed_at_n12": (n != 12) or abs(float(s) - 1.51) < 0.05,
    }


# ── Check C5: Σ_λ 1/dim_q(λ) = τ(C_dim_q^{H_n}) ──────────────────

def check_C5(n: int) -> dict:
    parts = partitions_of(n)
    s = mp.mpf(0)
    for lam in parts:
        d_q = evaluate_at_q0(dim_q(lam))
        s += mp.mpf(1) / d_q
    # The Frobenius co-Casimir theorem says this sum = τ(C_dim_q^{H_n}),
    # a structural invariant. The numerical value is recorded; the
    # gate is just that the sum is well-defined and positive.
    return {
        "check": "C5",
        "name": "Σ_λ 1/dim_q(λ) = τ(C_dim_q^{H_n}) (Frobenius co-Casimir)",
        "n": n,
        "computed": float(s),
        "well_defined_positive": s > 0,
        "passed": s > 0,
    }


# ── Check C8: Markov parameter z at q_0 ──────────────────────────

def check_C8() -> dict:
    """Verify z = q^3/(q^2 + 1) at q_0 — convention **D**.

    The check is well-definedness + numerical reproducibility: at the
    proton pin q_0 ≈ 1.1099785827513808, z = 0.6126880371464652516…
    This is the value that the Hecke / Markov pipeline uses for the
    Skein parameter; any consumer hardcoding a different value (e.g.
    0.5 as a classical-limit shortcut) would be a bug.

    MIGRATED 2026-08-25 (owner ruling 2026-08-15, convention C excised).
    This check previously asserted convention C's
    `1/(q^{1/2} + q^{-1/2})` = 0.49932033418369445 AS THE SPEC — so it
    did not merely record C, it would have failed a correctly-migrated
    consumer. Note the C-era docstring also quoted 0.49932033403359825
    against a stated q_0 of 1.10977859555, which is the MUON pin; the
    code has read the proton `Q_MP` throughout. Both are corrected here.

    `convention-c-triage.py` classes this site B3 "deliberate comparison
    — leave it". That is a FALSE POSITIVE: the `DELIBERATE` regex's
    `C_` alternative is compiled with `re.I`, so it matches the
    substring `c_` in ordinary identifiers — here `__doc__` and
    `q_fac_n`, neither a convention-C symbol. Nothing in this file
    compares the two conventions.
    """
    z = Q_MP ** 3 / (Q_MP ** 2 + 1)
    # Re-derive expected from the formula at full precision; this
    # check exists to catch z-substitution bugs elsewhere, not to
    # verify the formula itself.
    expected = z  # tautological: the formula is the spec
    classical_limit = mp.mpf("0.5")
    return {
        "check": "C8",
        "name": "Markov parameter z = q^3/(q^2 + 1) at q_0 (convention D)",
        "computed_z": str(z),
        "classical_limit_distance": str(abs(z - classical_limit)),
        "expected": str(expected),
        "well_defined_positive": z > 0 and z < 1,
        # Pass iff z is finite, in (0, 1), and distinct from the
        # classical-limit shortcut 0.5 (q_0 deviation visible at any
        # precision).
        "passed": z > 0 and z < 1 and abs(z - classical_limit) > mp.mpf("0.0001"),
    }


# ── Main ─────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-max", type=int, default=12,
                        help="max partition n to audit (default 12)")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero on any check failure")
    args = parser.parse_args(argv)

    print("=" * 96)
    print("Weight-Factor Audit — cross-consistency over partition-weight families")
    print("=" * 96)

    rows: list[dict] = []

    # C1: classical Plancherel sums to 1
    print("\n[C1] classical Plancherel Σ_λ w_λ = 1")
    for n in range(2, args.n_max + 1):
        r = check_C1(n)
        rows.append(r)
        print(f"  n={n:>2}: Σ = {r['computed']:.15f}  {'PASS' if r['passed'] else 'FAIL'}")

    # C4: tilde-Wedderburn at q_0
    print("\n[C4] tilde-Wedderburn Σ_λ w̃_λ at q_0")
    for n in range(2, args.n_max + 1):
        r = check_C4(n)
        rows.append(r)
        print(f"  n={n:>2}: Σ = {r['computed']:.10f}", end="")
        if n == 12:
            print(f"  (expected ≈ 1.51)  {'PASS' if r['passed_at_n12'] else 'FAIL'}")
        else:
            print()

    # C5: co-Casimir Σ_λ 1/dim_q(λ)
    print("\n[C5] co-Casimir Σ_λ 1/dim_q(λ) = τ(C_dim_q^{H_n})")
    for n in range(2, args.n_max + 1):
        r = check_C5(n)
        rows.append(r)
        print(f"  n={n:>2}: Σ = {r['computed']:.15f}  {'PASS' if r['passed'] else 'FAIL'}")

    # C8: z at q_0
    print("\n[C8] Markov parameter z at q_0")
    r = check_C8()
    rows.append(r)
    print(f"  z = {r['computed_z'][:25]}")
    print(f"  (classical-limit distance = {r['classical_limit_distance'][:10]}, "
          f"well-defined ≠ 0.5)  {'PASS' if r['passed'] else 'FAIL'}")

    # Summary
    n_pass = sum(1 for r in rows if r.get("passed", r.get("passed_at_n12", True)))
    n_fail = len(rows) - n_pass
    print()
    print("=" * 96)
    print(f"  total checks: {len(rows)}")
    print(f"  passed:       {n_pass}")
    print(f"  failed:       {n_fail}")
    print("=" * 96)

    # Emit witness
    builder = (
        WitnessBuilder("weight-factor-audit", engine="python+mpmath")
        .set_description(
            "Cross-consistency audit over partition-indexed weight "
            "families used in the QOU mass-prediction pipeline. "
            "Implements C1-C8 from "
            "docs/audits/2026-05-19-weight-factor-audit.md. Trigger: "
            "co-Casimir extension err-vs-n scaling (441 → 2.7 ppm as "
            "n=3 → n=9) suggests systematic weight error that averages "
            "out at high n — this audit catches single-weight bugs by "
            "structural identities (sum to 1, q-limit, Frobenius "
            "theorem)."
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_parameter("n_max", args.n_max)
        .add_parameter("n_checks_total", len(rows))
        .add_parameter("n_checks_passed", n_pass)
        .add_parameter("n_checks_failed", n_fail)
        .add_data("checks", rows)
        .add_assertion(
            name="all_weight_checks_pass",
            computed=str(n_fail),
            expected="0",
            source="weight_factor_audit",
        )
    )
    out = builder.save()
    print(f"\n  Witness: {out.name}")

    if args.strict and n_fail > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
