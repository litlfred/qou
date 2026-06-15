#!/usr/bin/env python3
"""
Validate the Wenzl-bridge y_λ closed form against three independent
mathematical identities, evaluating at MULTIPLE q values (not just q_0).

Tests:
1. Cross-q validation: at five q probes bracketing q_0 ≈ 1.1097, the
   Wenzl-bridge numeric (50 dps) is compared per-partition against
   either the MPFR witness (at the q_0 probe) or against an independent
   high-precision reference (Wenzl-bridge re-evaluated at 100 dps for
   the other probes).  Pass: max abs diff < 1e-30.

2. Markov-axiom (M3) completeness: Σ_λ y_λ · d_λ = 1.  This is the
   Markov axiom (M3) tr_M(1) = 1 — *not* the Plancherel identity
   Σ_λ d_λ²/n! = 1.  (See docs/audits/2026-05-11-plancherel-usage-audit.md
   Finding D for the disambiguation.)  For n ≤ 4 the symbolic
   Wenzl-bridge form is reduced via sympy and the residue Σ y_λ d_λ - 1
   must be exactly 0.  For n ≥ 5 we verify numerically across all five
   q probes that |Σ y_λ d_λ - 1| < 1e-40 at 50 dps.

3. Markov-trace defining identity: Σ_λ y_λ χ_λ(σ_w_μ) = z^{n-len(μ)}
   for the cycle-type representative σ_w_μ of the extreme conjugacy
   classes μ = (n,) and μ = (1,1,…,1).  Same split as test 2 — symbolic
   for n ≤ 4 (sympy.simplify == 0), numerical for n ≥ 5 (residual
   < 1e-30 at all five probes, 50 dps).

History note (April 2026): the previous version of this script obtained
y_λ via sympy linear-system solve and hit RecursionError for n ≥ 5.
The Wenzl-bridge formula
    y_λ = s_{λ,X}(Q) / Σ_μ d_μ s_{μ,X}(Q),  Q = q², X = q·z/(1-Q+q·z)
gives the closed form directly without solving any linear system.  At
mpmath precision the test scales linearly in #partitions and trivially
extends to n = 12.  See `y_lambda_wenzl_bridge.py` for the formula
derivation and references (Macdonald I.3 ex.1; Wenzl 1988).

The result file (`y-lambda-symbolic-validation.json`) is updated using
the merge-aware load pattern: existing entries for any n not in the
current run are preserved.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
from q_parameter import Q_50_DIGIT_STR
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

sys.path.insert(0, str(Path(__file__).parent))
from y_lambda_wenzl_bridge import (
    chi_lambda_mpmath,
    classical_dim,
    cycle_type_word,
    markov_trace_lhs_numeric,
    markov_trace_target_numeric,
    partitions_of,
    markov_m3_sum_numeric,
    schur_principal,
    y_lambda_wenzl_bridge_numeric,
    y_lambda_wenzl_bridge_symbolic,
)


# ────────────────────────────────────────────────────────────────
# Probes and tolerances
# ────────────────────────────────────────────────────────────────

# Five q probes bracketing q_0 ≈ 1.10998.  The middle probe is q_0 itself
# so test 1 can compare directly to the MPFR witness.  The other four
# bracket q_0 within the physically relevant strip 1.05 ≤ q ≤ 1.20.
Q0_STR = Q_50_DIGIT_STR
PROBES = ["1.05", "1.08", Q0_STR, "1.15", "1.20"]

DPS_TEST = 50      # working precision for tests 1 + 3 (target 1e-30)
DPS_GROUND = 100   # ground-truth precision for cross-q reference (tests 1)
DPS_MARKOV_M3 = 80  # 1e-40 numerical Markov-axiom (M3) target

TOL_CROSS_Q = mp.mpf("1e-30")
TOL_MARKOV = mp.mpf("1e-30")
TOL_MARKOV_M3 = mp.mpf("1e-40")
# Backward-compat alias; remove after downstream callers are updated.
TOL_PLANCHEREL = TOL_MARKOV_M3


# ────────────────────────────────────────────────────────────────
# References — load MPFR witness (q_0 only)
# ────────────────────────────────────────────────────────────────

def load_mpfr_witness() -> dict:
    p = Path(__file__).parent / "y-lambda-mpfr-witness.json"
    with p.open() as f:
        data = json.load(f)
    out = {}
    for n_str, table in data.get("tables_by_n", {}).items():
        out[int(n_str)] = {
            tuple(w["partition"]): mp.mpf(w["y_lambda"])
            for w in table["weights"]
        }
    return out


# ────────────────────────────────────────────────────────────────
# Test 1 — cross-q (Wenzl-bridge numeric vs reference)
# ────────────────────────────────────────────────────────────────

def test_1_cross_q(n: int, mpfr_witness: dict) -> list[tuple]:
    """Returns list of (q_probe_str, max_abs_diff_str, is_pass)."""
    parts = partitions_of(n)
    results = []
    for q_str in PROBES:
        # Compute Wenzl-bridge at the working precision.
        ys_test = {
            tuple(p): y_lambda_wenzl_bridge_numeric(p, q_str, DPS_TEST)
            for p in parts
        }
        # Pick reference: MPFR witness if q_str == q_0 and n in MPFR table,
        # otherwise re-evaluate Wenzl-bridge at higher precision.
        if q_str == Q0_STR and n in mpfr_witness:
            ref = mpfr_witness[n]
            ref_label = "mpfr-witness"
        else:
            ref = {
                tuple(p): y_lambda_wenzl_bridge_numeric(p, q_str, DPS_GROUND)
                for p in parts
            }
            ref_label = f"wenzl-bridge@{DPS_GROUND}dps"
        # Realign tuples (mpfr witness uses tuple keys built above).
        max_diff = mp.mpf(0)
        for p in parts:
            key = tuple(p)
            if key not in ref:
                # MPFR witness for this n exists but the partition list
                # mismatches (shouldn't happen) — fall back to wenzl-bridge.
                ref[key] = y_lambda_wenzl_bridge_numeric(p, q_str, DPS_GROUND)
            d = abs(ys_test[key] - ref[key])
            if d > max_diff:
                max_diff = d
        is_pass = max_diff < TOL_CROSS_Q
        results.append((q_str, str(max_diff), bool(is_pass), ref_label))
    return results


# ────────────────────────────────────────────────────────────────
# Test 2 — Markov-axiom (M3) completeness  Σ_λ y_λ · d_λ = 1
# ────────────────────────────────────────────────────────────────
#
# NOTE: previously named `test_2_plancherel`; that name conflated
# the Markov axiom (M3) tr_M(1)=1 with the genuine Plancherel
# identity Σ_λ d_λ²/n!=1.  See
# docs/audits/2026-05-11-plancherel-usage-audit.md (Finding D).

def test_2_markov_m3(n: int) -> dict:
    """Returns {'mode': 'symbolic'|'numeric', 'pass': bool, 'detail': ...}."""
    if n <= 4:
        # Symbolic — use Wenzl-bridge symbolic forms.
        q = sp.Symbol("q", positive=True)
        m3_sum = sp.Integer(0)
        for p in partitions_of(n):
            y_sym = y_lambda_wenzl_bridge_symbolic(p)
            m3_sum += y_sym * classical_dim(p)
        simp = sp.simplify(m3_sum)
        is_one = sp.simplify(simp - 1) == 0
        return {
            "mode": "symbolic",
            "pass": bool(is_one),
            "result": str(simp),
        }
    # Numeric across all probes.
    probe_results = []
    overall_pass = True
    for q_str in PROBES:
        s = markov_m3_sum_numeric(n, q_str, DPS_MARKOV_M3)
        residual = abs(s - 1)
        ok = residual < TOL_MARKOV_M3
        probe_results.append((q_str, str(residual), bool(ok)))
        if not ok:
            overall_pass = False
    return {
        "mode": "numeric",
        "pass": overall_pass,
        "probes": probe_results,
    }


# Backward-compat alias; remove after downstream callers are updated.
test_2_plancherel = test_2_markov_m3


# ────────────────────────────────────────────────────────────────
# Test 3 — Markov-trace defining identity
# ────────────────────────────────────────────────────────────────

def chi_lambda_symbolic(partition, word, q):
    """Sympy symbolic χ_λ — used only for n ≤ 4."""
    syts, _, contents = _syt_data(partition)
    dim = len(syts)
    if dim == 0:
        return sp.Integer(0)
    h = q - 1 / q
    n = sum(partition)
    sigmas = []
    for k in range(1, n):
        M = sp.zeros(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (1 - q ** (-2 * rho))
            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j = next(
                (jj for jj in range(dim)
                 if jj != i and syts[jj] == swap_map),
                None,
            )
            if j is None:
                M[i, i] = a
                processed.add(i)
            else:
                a_prime = h / (1 - q ** (2 * rho))
                b_sq = sp.cancel(a * a_prime + 1)
                bb = sp.sqrt(b_sq)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = bb
                M[j, i] = bb
                processed.add(i)
                processed.add(j)
        sigmas.append(M)
    M = sp.eye(dim)
    for idx in word:
        M = M * sigmas[idx - 1]
    return sp.trace(M)


def _syt_data(partition):
    from y_lambda_wenzl_bridge import _standard_young_tableaux
    return _standard_young_tableaux(partition)


def test_3_markov(n: int) -> list[dict]:
    """Returns list of per-μ dicts."""
    test_mus = [(n,)]
    if n >= 2:
        test_mus.append(tuple([1] * n))
    out = []
    if n <= 4:
        # Symbolic.
        q = sp.Symbol("q", positive=True)
        z_sym = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
        for mu in test_mus:
            word = cycle_type_word(mu)
            target = z_sym ** (n - len(mu))
            lhs = sp.Integer(0)
            for p in partitions_of(n):
                y_sym = y_lambda_wenzl_bridge_symbolic(p)
                chi = chi_lambda_symbolic(p, word, q)
                lhs += y_sym * chi
            diff = sp.simplify(lhs - target)
            is_zero = sp.simplify(diff) == 0
            out.append({
                "mu": str(mu),
                "mode": "symbolic",
                "pass": bool(is_zero),
                "residual": str(diff),
            })
        return out
    # Numeric across all probes.
    for mu in test_mus:
        probe_results = []
        overall_pass = True
        for q_str in PROBES:
            lhs = markov_trace_lhs_numeric(n, mu, q_str, DPS_TEST)
            rhs = markov_trace_target_numeric(n, mu, q_str, DPS_TEST)
            residual = abs(lhs - rhs)
            ok = residual < TOL_MARKOV
            probe_results.append((q_str, str(residual), bool(ok)))
            if not ok:
                overall_pass = False
        out.append({
            "mu": str(mu),
            "mode": "numeric",
            "pass": overall_pass,
            "probes": probe_results,
        })
    return out


# ────────────────────────────────────────────────────────────────
# Driver
# ────────────────────────────────────────────────────────────────

def main(ns: list[int] | None = None) -> int:
    if ns is None:
        ns = list(range(2, 13))

    out_path = Path(__file__).parent / "y-lambda-symbolic-validation.json"
    # Merge-aware load — preserve entries for n not in this run.
    if out_path.exists():
        try:
            existing = json.loads(out_path.read_text())
        except json.JSONDecodeError:
            print(f"Warning: existing validation file {out_path} is not "
                  "valid JSON; starting fresh.")
            existing = {}
    else:
        existing = {}
    summary_by_n = existing.get("summary_by_n", {})

    mpfr_witness = load_mpfr_witness()
    print(f"MPFR witness: have entries for n in "
          f"{sorted(mpfr_witness.keys())}")

    all_passed = True
    for n in ns:
        parts = partitions_of(n)
        print(f"\n{'='*70}\nn = {n} ({len(parts)} partitions, "
              f"probes {PROBES})\n{'='*70}")

        n_summary = {}

        # Test 1 — cross-q.
        print(f"\n[Test 1] Cross-q Wenzl-bridge vs reference "
              f"(tol < 1e-30)")
        t1 = test_1_cross_q(n, mpfr_witness)
        n_summary["test_1_cross_q"] = [
            {"q": q, "max_abs_diff": d, "pass": ok, "ref": ref}
            for (q, d, ok, ref) in t1
        ]
        for (q, d, ok, ref) in t1:
            tag = "PASS" if ok else "FAIL"
            print(f"  q={q}: max|y_wenzl - {ref}| = {d}  [{tag}]")
            if not ok:
                all_passed = False

        # Test 2 — Markov-axiom (M3): Σ y_λ d_λ = 1.
        print(f"\n[Test 2] Markov-axiom (M3) Σ y_λ d_λ = 1  "
              f"({'symbolic' if n <= 4 else 'numeric < 1e-40'})")
        t2 = test_2_markov_m3(n)
        n_summary["test_2_markov_m3"] = t2
        if t2["mode"] == "symbolic":
            tag = "PASS" if t2["pass"] else "FAIL"
            res_str = t2['result']
            if len(res_str) > 70:
                res_str = res_str[:67] + "..."
            print(f"  symbolic Σ y_λ d_λ = {res_str}  [{tag}]")
            if not t2["pass"]:
                all_passed = False
        else:
            for (q, r, ok) in t2["probes"]:
                tag = "PASS" if ok else "FAIL"
                print(f"  q={q}: |Σ-1| = {r}  [{tag}]")
                if not ok:
                    all_passed = False

        # Test 3 — Markov-trace.
        print(f"\n[Test 3] Markov-trace identity  "
              f"({'symbolic' if n <= 4 else 'numeric < 1e-30'})")
        t3 = test_3_markov(n)
        n_summary["test_3_markov"] = t3
        for entry in t3:
            mu = entry["mu"]
            if entry["mode"] == "symbolic":
                tag = "PASS" if entry["pass"] else "FAIL"
                d = entry["residual"]
                if len(d) > 70:
                    d = d[:67] + "..."
                print(f"  μ={mu}: lhs-rhs = {d}  [{tag}]")
                if not entry["pass"]:
                    all_passed = False
            else:
                for (q, r, ok) in entry["probes"]:
                    tag = "PASS" if ok else "FAIL"
                    print(f"  μ={mu} q={q}: residual = {r}  [{tag}]")
                    if not ok:
                        all_passed = False

        summary_by_n[str(n)] = n_summary
        # Incremental save (preserves prior n entries naturally).
        # Drop stale pre-rename keys so the on-disk schema has a
        # single canonical form (see PR #636 Copilot review).
        for stale in ("dps_plancherel",):
            existing.pop(stale, None)
        # Also drop stale per-n `test_2_plancherel` entries from
        # previous runs that did NOT re-touch that n (otherwise
        # `summary_by_n` keeps both old and new test_2 names).
        for _n_key, _n_summary in summary_by_n.items():
            if isinstance(_n_summary, dict):
                _n_summary.pop("test_2_plancherel", None)
        existing["all_passed"] = all_passed
        existing["probes"] = PROBES
        existing["dps_test"] = DPS_TEST
        existing["dps_ground_truth"] = DPS_GROUND
        existing["dps_markov_m3"] = DPS_MARKOV_M3
        # Overwrite tolerances wholesale so stale keys
        # ("plancherel", "markov") don't survive a merge-aware update.
        existing["tolerances"] = {
            "cross_q": "1e-30",
            "markov_trace_lhs": "1e-30",
            "markov_m3": "1e-40",
        }
        existing["computedAt"] = datetime.now(timezone.utc).isoformat()
        existing["summary_by_n"] = summary_by_n
        out_path.write_text(json.dumps(existing, indent=2))

    print(f"\n{'='*70}")
    print(f"OVERALL: "
          f"{'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    print('=' * 70)
    print(f"Wrote {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        ns = [int(a) for a in args]
    else:
        ns = None
    sys.exit(main(ns))
