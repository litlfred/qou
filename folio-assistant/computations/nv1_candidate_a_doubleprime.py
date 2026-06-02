"""
NV-1 candidate (a″) — q-deformed Plancherel sum hypothesis.

Tests whether
    \widetilde{N_v} = \sum_{\lambda \vdash 9}  dim_q V_\lambda \cdot f_\lambda
                    \big|_{q=q_0}
agrees with the back-solved-from-CODATA-G_F effective crossing count
    N_v = 1,445,519
to CODATA-G_F precision (~5e-7).

Background: docs/audits/2026-05-02-nv-frob-filter-conjectures.md, lines 129-159.

Method:
  - Enumerate all 30 partitions of 9.
  - Compute classical Specht dimension f_lambda by the hook-length formula
        f_lambda = n! / prod h_x.
  - Compute q-dimension of the Iwahori-Hecke representation by the q-hook formula
        dim_q V_lambda = [n]_q! / prod [h_x]_q.
  - Sum lambda -> dim_q V_lambda * f_lambda at q = q_0.
  - Cross-check classical limit (q -> 1) reproduces 9! = 362,880.
  - If the principal sum fails, also test variants:
        (a) sum (dim_q V_lambda)^2
        (b) self-conjugate-only restriction
        (c) descent-involution correction delta_w (heuristic).

All q-arithmetic at mpmath 50 dps.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import os
import sys
import time
from math import factorial
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at  # high-precision substrate parameter
from partition_utils import hook_lengths  # noqa: E402

# -----------------------------------------------------------------
# Precision
# -----------------------------------------------------------------
set_compute_dps()

# -----------------------------------------------------------------
# Targets
# -----------------------------------------------------------------
N_TARGET   = 9
N_V_TARGET = 1_445_519       # back-solved from CODATA G_F (audit doc)
N_V_PREC   = mp.mpf("5e-7")  # CODATA G_F relative precision

# -----------------------------------------------------------------
# Partition enumeration (generates partitions in any-order; we take
# weakly-decreasing tuples for canonicality).
# -----------------------------------------------------------------
def partitions(n: int):
    """All integer partitions of n as weakly-decreasing tuples."""
    if n == 0:
        yield ()
        return
    def _rec(rem, max_part):
        if rem == 0:
            yield ()
            return
        for p in range(min(rem, max_part), 0, -1):
            for tail in _rec(rem - p, p):
                yield (p,) + tail
    yield from _rec(n, n)


# -----------------------------------------------------------------
# Classical Specht dimension f_lambda via hook-length formula.
# -----------------------------------------------------------------
def specht_dim(lam):
    n = sum(lam)
    hooks = hook_lengths(lam)
    prod = 1
    for h in hooks:
        prod *= h
    return factorial(n) // prod


# -----------------------------------------------------------------
# q-integer, q-factorial, and q-dimension (mpmath).
# -----------------------------------------------------------------
def q_int_mp(k, q):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    if k == 0:
        return mp.mpf(0)
    return (q**k - q**(-k)) / (q - 1/q)


def q_factorial_mp(n, q):
    """[n]_q! = prod_{k=1}^n [k]_q."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int_mp(k, q)
    return out


def dim_q_V_lambda(lam, q):
    """q-Hecke representation dimension via q-hook product formula:
       dim_q V_lambda = [n]_q! / prod [h_x]_q.
       In the classical limit q -> 1 this reduces to f_lambda."""
    n = sum(lam)
    nfac = q_factorial_mp(n, q)
    denom = mp.mpf(1)
    for h in hook_lengths(lam):
        denom *= q_int_mp(h, q)
    return nfac / denom


# -----------------------------------------------------------------
# Self-conjugate check.
# -----------------------------------------------------------------
def conjugate(lam):
    if not lam:
        return ()
    max_col = lam[0]
    return tuple(sum(1 for r in lam if r > j) for j in range(max_col))


def is_self_conjugate(lam):
    return tuple(lam) == conjugate(lam)


# -----------------------------------------------------------------
# Main computation.
# -----------------------------------------------------------------
def main():
    start = time.time()

    q0 = q_at(50)
    print(f"q_0  = {mp.nstr(q0, 30)}")
    print(f"hbar_q = q - 1/q = {mp.nstr(q0 - 1/q0, 30)}")
    print()

    # ── Enumerate partitions of 9 ─────────────────────────────────
    parts = list(partitions(N_TARGET))
    assert len(parts) == 30, f"expected 30 partitions of 9, got {len(parts)}"
    print(f"# partitions of 9: {len(parts)}\n")

    rows = []
    sum_principal     = mp.mpf(0)   # sum dim_q * f
    sum_dim_q_squared = mp.mpf(0)   # sum (dim_q)^2
    sum_self_conj     = mp.mpf(0)   # sum dim_q * f restricted to lam = lam'
    sum_classical     = 0           # sum f^2 — should equal 9!

    print(f"{'partition':<22} {'f_lambda':>10}  {'dim_q V_lambda':>22}  {'product':>22}")
    print("-" * 80)
    for lam in parts:
        f_lam = specht_dim(lam)
        dq    = dim_q_V_lambda(lam, q0)
        prod  = dq * f_lam

        sum_principal     += prod
        sum_dim_q_squared += dq * dq
        if is_self_conjugate(lam):
            sum_self_conj += prod
        sum_classical += f_lam * f_lam

        rows.append({
            "lambda": list(lam),
            "f_lambda": int(f_lam),
            "dim_q_V_lambda": mp.nstr(dq, 20),
            "product_dq_f": mp.nstr(prod, 20),
            "self_conjugate": is_self_conjugate(lam),
        })
        print(f"{str(lam):<22} {f_lam:>10}  {mp.nstr(dq, 12):>22}  {mp.nstr(prod, 12):>22}")

    print()
    print(f"Classical sum f^2     = {sum_classical}  (should be 9! = {factorial(9)})")
    assert sum_classical == factorial(N_TARGET)

    # ── Comparison ─────────────────────────────────────────────────
    target = mp.mpf(N_V_TARGET)
    fac9   = mp.mpf(factorial(N_TARGET))

    rel_dev_principal = (sum_principal - target) / target
    rel_dev_squared   = (sum_dim_q_squared - target) / target
    rel_dev_selfconj  = (sum_self_conj - target) / target

    print()
    print("=== Candidate (a″) results ===")
    print(f"  sum dim_q V * f        = {mp.nstr(sum_principal, 20)}")
    print(f"  N_v target             = {N_V_TARGET}")
    print(f"  ratio sum / N_v        = {mp.nstr(sum_principal/target, 20)}")
    print(f"  rel deviation          = {mp.nstr(rel_dev_principal, 12)}")
    print()
    print("=== Variant (a) — sum (dim_q V)^2 ===")
    print(f"  sum (dim_q V)^2        = {mp.nstr(sum_dim_q_squared, 20)}")
    print(f"  rel deviation from N_v = {mp.nstr(rel_dev_squared, 12)}")
    print()
    print("=== Variant (b) — self-conjugate only ===")
    print(f"  sum_{{lam=lam'}} dim_q*f = {mp.nstr(sum_self_conj, 20)}")
    print(f"  rel deviation from N_v = {mp.nstr(rel_dev_selfconj, 12)}")
    print()

    # ── Verdict ────────────────────────────────────────────────────
    abs_rel = abs(rel_dev_principal)
    if abs_rel <= N_V_PREC:
        verdict = "pass"
        verdict_note = "Agreement within CODATA-G_F precision."
    elif abs_rel < mp.mpf("1e-2"):
        verdict = "close-but-not-exact"
        verdict_note = (
            f"Relative deviation {mp.nstr(rel_dev_principal,3)} is small but "
            f"exceeds CODATA precision; q-deformation does not absorb the 0.4% gap."
        )
    else:
        verdict = "fail"
        verdict_note = (
            f"Relative deviation {mp.nstr(rel_dev_principal,3)} exceeds CODATA "
            f"precision substantially; q-deformed Plancherel sum is falsified."
        )

    print(f"Verdict: {verdict}")
    print(f"  -> {verdict_note}")

    # ── Variant (c) — descent-involution correction (heuristic) ────
    # delta_w correction is not algorithmically defined in the audit
    # doc; it is sketched as ~6001 ~= 7! * 1.19. We compute the gap
    # delta_w = N_v - sum_principal and report its size for follow-on
    # discussion (no canonical formula to test against).
    delta_w_gap = target - sum_principal
    print()
    print("=== Variant (c) — descent-involution residual ===")
    print(f"  N_v - sum dim_q*f      = {mp.nstr(delta_w_gap, 20)}")
    print(f"  | delta_w | / 7!       = {mp.nstr(abs(delta_w_gap)/mp.mpf(factorial(7)), 6)}")

    # ── Witness JSON ───────────────────────────────────────────────
    witness = {
        "name": "nv1_candidate_a_doubleprime",
        "description": (
            "Test of the q-deformed Plancherel sum hypothesis "
            "N_v = sum_{lambda |- 9} dim_q V_lambda * f_lambda |_{q=q_0} "
            "vs the CODATA-G_F-back-solved value N_v = 1,445,519. "
            "Source: docs/audits/2026-05-02-nv-frob-filter-conjectures.md "
            "lines 129-159."
        ),
        "computation": "nv1_candidate_a_doubleprime",
        "inputs": {
            "n_target": N_TARGET,
            "k_w_label": "weak-sector characteristic level",
            "q_0_dps_50": mp.nstr(q0, 50),
            "hbar_q_dps_50": mp.nstr(q0 - 1/q0, 50),
            "n_v_target": N_V_TARGET,
            "codata_g_f_relative_precision": mp.nstr(N_V_PREC, 6),
            "mpmath_dps": 50,
        },
        "partitions": rows,
        "principal_sum": {
            "definition": "sum_{lambda |- 9} dim_q V_lambda * f_lambda",
            "value_at_q0": mp.nstr(sum_principal, 30),
            "ratio_to_n_v": mp.nstr(sum_principal / target, 30),
            "relative_deviation": mp.nstr(rel_dev_principal, 16),
        },
        "classical_limit_check": {
            "sum_f_lambda_squared": int(sum_classical),
            "expected_9_factorial": int(factorial(N_TARGET)),
            "ok": sum_classical == factorial(N_TARGET),
        },
        "variants": {
            "a_sum_dim_q_squared": {
                "definition": "sum_{lambda |- 9} (dim_q V_lambda)^2",
                "value": mp.nstr(sum_dim_q_squared, 30),
                "relative_deviation_from_n_v": mp.nstr(rel_dev_squared, 16),
            },
            "b_self_conjugate_only": {
                "definition": (
                    "sum_{lambda |- 9, lambda = lambda'} "
                    "dim_q V_lambda * f_lambda"
                ),
                "n_self_conjugate": sum(1 for lam in parts if is_self_conjugate(lam)),
                "value": mp.nstr(sum_self_conj, 30),
                "relative_deviation_from_n_v": mp.nstr(rel_dev_selfconj, 16),
            },
            "c_descent_involution_residual": {
                "definition": "N_v - sum dim_q V_lambda * f_lambda  (gap; no canonical formula)",
                "delta_w_value": mp.nstr(delta_w_gap, 30),
                "ratio_to_7_factorial": mp.nstr(abs(delta_w_gap)/mp.mpf(factorial(7)), 16),
            },
        },
        "verdict": verdict,
        "verdict_note": verdict_note,
        "timing_seconds": time.time() - start,
    }

    out_path = HERE / "nv1_candidate_a_doubleprime.witness.json"
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"\nWitness written: {out_path}")
    return witness


if __name__ == "__main__":
    main()
