#!/usr/bin/env python3
"""
qbeta_habiro_wenzl_tower_zeta_n.py — Level-k SU(2) Verlinde tower at ζ_n
=========================================================================

STRUCTURAL EXTENSION probe for the level-k SU(2) Verlinde tower predicted
by extending the level-2 SU(2) Wenzl witness identified in PR #1625.

CONTEXT (from PR #1625 commit 85bf4f0982)
==========================================

At q = ζ_4 = e^(iπ/2) (equivalently u = √q = ζ_8 = e^(iπ/4)), the Hecke
algebra H_n(q) exhibits the level-2 SU(2) Verlinde truncation via the
Wenzl projector kernel (partitions with first-column ≥ k+2 = 4 are
annihilated). This forces the UNIVERSAL cancellation

    S_M_first_Φ_8(u = ζ_8) = 0   for M = 7

across all atomic-step Habiro elements, where
    S_M(u) = Σ_{m=0..M} Δa_m(u) · (u; u)_m
and (ζ_8; ζ_8)_7 = 8 exactly.

The first-Φ_8 cancellation boundary is
    M_first_Φ_8 = ord(σ_i in H_n(ζ_8 → q=i)) − 1 = 8 − 1 = 7.

PREDICTED TOWER (this probe's hypothesis)
==========================================

For each primitive 2(k+2)-th root of unity ζ_{2(k+2)} in u-coordinates
(equivalently q = ζ_{k+2} in q-coordinates, since u² = q), the
level-k SU(2) Verlinde truncation should force a universal cancellation
at boundary

    M_first_Φ_{2(k+2)} = ord(σ_i in H_n(q = ζ_{k+2})) − 1
                       = 2(k+2) − 1

with the normalisation (ζ; ζ)_{ord(σ)-1} = (ζ_{2(k+2)}; ζ_{2(k+2)})_{2(k+2)-1}
being a non-zero integer.

| u-root      | q-root      | Level k | (u;u)_m=0 first |
|-------------|-------------|---------|------------------|
| ζ_8         | ζ_4 = i     | 2       | m = 8            |
| ζ_12        | ζ_6         | 4       | m = 12           |
| ζ_16        | ζ_8         | 6       | m = 16           |
| ζ_20        | ζ_10        | 8       | m = 20           |

Predicted M_first_Φ = ord(σ_i in H_n(q)) − 1 = 2(k+2) − 1:
    k=2 → M=7  (verified — PR #1625)
    k=4 → M=11 (this probe — testable for all three pairs)
    k=6 → M=15 (this probe — testable for ⁴He−³He only; M_max = 15)
    k=8 → M=19 (INFEASIBLE — exceeds M_max for all available pairs)

FALSIFIABILITY
==============

  - HOLDS at all accessible k → strong validation of the level-k SU(2)
    Wenzl framework as a tower of categorical witnesses.
  - FAILS at any k → either the framework needs refinement (different
    boundary formula) or the k=2 case is special.
  - HOLDS at some k but not others → pin the boundary where the pattern
    breaks; structural pattern.

USAGE
-----
  python3 -u qbeta_habiro_wenzl_tower_zeta_n.py 2>&1 | tee /tmp/wenzl_tower.log

OUTPUTS
-------
  folio-assistant/computations/qbeta-habiro-wenzl-tower-zeta-n.witness.json

Ref:
  docs/audits/2026-06-01-qbeta-habiro-wenzl-tower-zeta-n.md
  docs/audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md
  PR #1625 (level-2 baseline)
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

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ────────────────────── Coefficient loader (reused) ────────────────────────


def parse_coeffs(habiro_entries: list[dict], u: sp.Symbol) -> dict[int, sp.Poly]:
    """Parse {m, a_m, ...} entries into sympy.Poly in u with ℤ coefficients."""
    out: dict[int, sp.Poly] = {}
    for entry in habiro_entries:
        m = int(entry["m"])
        a_str = entry["a_m"]
        out[m] = sp.Poly(sp.sympify(a_str), u, domain="ZZ")
    return out


def load_atomic(u: sp.Symbol) -> dict[str, dict[int, sp.Poly]]:
    path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    log(f"Loading atomic witness: {path.name}")
    data = json.loads(path.read_text())
    return {
        "p": parse_coeffs(
            data["results"]["p (proton, A=1)"]["habiro_coefficients"], u
        ),
        "n": parse_coeffs(
            data["results"]["n (neutron, A=1)"]["habiro_coefficients"], u
        ),
        "D": parse_coeffs(
            data["results"]["D (deuteron, A=2)"]["habiro_coefficients"], u
        ),
    }


def load_helium(u: sp.Symbol) -> dict[str, dict[int, sp.Poly]]:
    """Helium witnesses live on PR #1618 branch; try /tmp first."""
    def _try(p: Path) -> dict | None:
        if p.exists():
            log(f"Loading helium witness: {p}")
            return json.loads(p.read_text())
        return None

    out: dict[str, dict[int, sp.Poly]] = {}
    for label in ("He3", "He4"):
        fname = f"habiro-coefficients-helium-{'3' if label == 'He3' else '4'}.witness.json"
        d = _try(Path(f"/tmp/{'he3.json' if label == 'He3' else 'he4.json'}"))
        if d is None:
            d = _try(HERE / fname)
        if d is None:
            raise FileNotFoundError(f"Cannot find helium witness for {label}")
        out[label] = parse_coeffs(d["habiro_coefficients"], u)
    return out


# ───────────────────── q-Pochhammer (u; u)_m ───────────────────────────────


def pochhammer_uu(m: int, u: sp.Symbol) -> sp.Expr:
    """(u; u)_m = Π_{k=1..m} (1 - u^k), expanded."""
    out = sp.Integer(1)
    for k in range(1, m + 1):
        out = sp.expand(out * (1 - u**k))
    return out


def pochhammer_at_value(m: int, zeta_val):
    """Numeric (mpmath) evaluation of (ζ; ζ)_m = Π(1 - ζ^k) at a specific
    complex value ζ. Used to verify (ζ; ζ)_{ord-1} = integer."""
    out = mp.mpc(1)
    for k in range(1, m + 1):
        out *= (1 - zeta_val ** k)
    return out


# ─────────────────── Polynomial divisibility helpers ───────────────────────


def divides_in_u(poly_expr: sp.Expr, divisor_expr: sp.Expr,
                 u: sp.Symbol) -> bool:
    """True iff divisor_expr divides poly_expr over ℚ[u]."""
    if sp.simplify(poly_expr) == 0:
        return True
    q, r = sp.div(sp.expand(poly_expr), sp.expand(divisor_expr), u)
    return sp.simplify(r) == 0


# ───────────────────── Level-k tower probe ─────────────────────────────────


def probe_level_k(
    delta_a: dict[int, sp.Poly],
    pair_label: str,
    level_k: int,
    u: sp.Symbol,
) -> dict:
    """For a single (pair, level_k), test the Verlinde-tower prediction.

    - n := 2(k+2): cyclotomic order in u-coords (since u² = q).
    - Φ_n(u): the cyclotomic polynomial that should first divide S_M.
    - Predicted M_first = n − 1.
    - Tests:
        * Verify S_{M-1}(u) is NOT divisible by Φ_n(u) (no premature cancel).
        * Verify S_M(u) IS divisible by Φ_n(u) (predicted cancellation).
        * Verify S_M(ζ_n) = 0 numerically at high precision.
        * Compute (ζ_n; ζ_n)_{M} = integer (normalization check).
    """
    n = 2 * (level_k + 2)
    expected_M = n - 1
    phi_n = sp.cyclotomic_poly(n, u)

    ms = sorted(delta_a.keys())
    M_max = max(ms)

    # Feasibility check
    if expected_M > M_max:
        return {
            "pair": pair_label,
            "level_k": level_k,
            "n_cyclotomic_index": n,
            "predicted_M_first": expected_M,
            "M_max_available": M_max,
            "feasible": False,
            "reason": (
                f"Expected M_first = {expected_M} exceeds M_max = {M_max} "
                f"for pair {pair_label} — pair's Δa_m polynomials only "
                f"go to m = {M_max}, insufficient data."
            ),
        }

    log("-" * 78)
    log(f"  Pair: {pair_label} | Level k = {level_k} | n = {n} | "
        f"Φ_{n}(u) = {phi_n} | predicted M_first = {expected_M}")
    log("-" * 78)

    # Build S_M for M = expected_M - 1 and M = expected_M
    pochs: dict[int, sp.Expr] = {}
    terms: dict[int, sp.Expr] = {}
    partial: dict[int, sp.Expr] = {}
    running = sp.Integer(0)
    for m in ms:
        pochs[m] = pochhammer_uu(m, u)
        am = delta_a[m].as_expr()
        terms[m] = sp.expand(am * pochs[m])
        running = sp.expand(running + terms[m])
        partial[m] = running

    # Strict tests at M = expected_M and M = expected_M - 1
    S_pre = partial[expected_M - 1]    # should NOT be divisible by Φ_n
    S_at = partial[expected_M]         # should BE divisible by Φ_n

    pre_divisible = divides_in_u(S_pre, phi_n, u)
    at_divisible = divides_in_u(S_at, phi_n, u)

    log(f"  S_{expected_M-1} divisible by Φ_{n}? {pre_divisible} (expect False)")
    log(f"  S_{expected_M}   divisible by Φ_{n}? {at_divisible}   (expect True)")

    # Numeric verification at u = ζ_n
    mp.mp.dps = 50
    zeta_n = mp.exp(mp.mpc(0, 1) * mp.pi / n)  # e^(iπ/n) for primitive 2n-th root
    # Actually we need primitive n-th root: ζ_n = e^(2πi/n)
    zeta_n = mp.exp(mp.mpc(0, 1) * 2 * mp.pi / n)
    # numeric S_at(ζ_n)
    S_at_at_zeta = mp.mpc(0)
    for m_ in ms:
        if m_ > expected_M:
            break
        am_val = mp.mpc(0)
        # evaluate Δa_m(ζ_n) using sympy symbolic → mpmath complex
        # Use sp.Poly's all_coeffs (Δa_m is ℤ-polynomial)
        coefs = delta_a[m_].all_coeffs()
        # all_coeffs returns high-to-low; reverse for low-to-high
        coefs_lh = list(reversed(coefs))
        for j, c in enumerate(coefs_lh):
            am_val += mp.mpf(int(c)) * zeta_n ** j
        S_at_at_zeta += am_val * pochhammer_at_value(m_, zeta_n)
    S_at_at_zeta_abs = mp.fabs(S_at_at_zeta)
    log(f"  |S_{expected_M}(ζ_{n})| = {mp.nstr(S_at_at_zeta_abs, 6)} "
        f"(expect ~ 0 at 50 dps)")

    # Same for S_pre
    S_pre_at_zeta = mp.mpc(0)
    for m_ in ms:
        if m_ > expected_M - 1:
            break
        am_val = mp.mpc(0)
        coefs_lh = list(reversed(delta_a[m_].all_coeffs()))
        for j, c in enumerate(coefs_lh):
            am_val += mp.mpf(int(c)) * zeta_n ** j
        S_pre_at_zeta += am_val * pochhammer_at_value(m_, zeta_n)
    S_pre_at_zeta_abs = mp.fabs(S_pre_at_zeta)
    log(f"  |S_{expected_M-1}(ζ_{n})| = {mp.nstr(S_pre_at_zeta_abs, 6)} "
        f"(expect ≠ 0)")

    # Normalisation: (ζ_n; ζ_n)_{expected_M} numerically
    poch_at_zeta = pochhammer_at_value(expected_M, zeta_n)
    poch_at_zeta_abs = mp.fabs(poch_at_zeta)
    # If this is an integer, the imaginary part should be ~0 and the real
    # part should be close to a rational integer.
    poch_real = float(mp.re(poch_at_zeta))
    poch_imag = float(mp.im(poch_at_zeta))
    poch_round = round(poch_real)
    poch_integer_match = (abs(poch_imag) < 1e-30 and
                          abs(poch_real - poch_round) < 1e-30)
    log(f"  (ζ_{n}; ζ_{n})_{expected_M} numeric = "
        f"{mp.nstr(poch_at_zeta, 8)}, |·| = {mp.nstr(poch_at_zeta_abs, 6)}")
    log(f"    nearest integer: {poch_round} (integer match: {poch_integer_match})")

    # Symbolic check via sympy: substitute u → ζ_n exactly and simplify
    zeta_n_sym = sp.exp(sp.I * 2 * sp.pi / n)
    poch_at_zeta_sym = sp.simplify(pochs[expected_M].subs(u, zeta_n_sym))
    poch_at_zeta_sym_str = str(poch_at_zeta_sym)
    log(f"  sympy: (ζ_{n};ζ_{n})_{expected_M} = {poch_at_zeta_sym_str[:120]}")

    # Verdict per-(pair,level):
    held = (not pre_divisible) and at_divisible
    log(f"  → Verdict for (pair={pair_label}, k={level_k}): "
        f"{'HOLD' if held else 'FAIL'}")

    return {
        "pair": pair_label,
        "level_k": level_k,
        "n_cyclotomic_index": n,
        "phi_n_polynomial": str(phi_n),
        "predicted_M_first": expected_M,
        "M_max_available": M_max,
        "feasible": True,
        "S_pre_divisible_by_phi_n": pre_divisible,
        "S_at_divisible_by_phi_n": at_divisible,
        "S_at_zeta_n_numeric_abs": mp.nstr(S_at_at_zeta_abs, 12),
        "S_pre_zeta_n_numeric_abs": mp.nstr(S_pre_at_zeta_abs, 12),
        "pochhammer_zeta_n_ord_minus_1_numeric_abs": mp.nstr(poch_at_zeta_abs, 12),
        "pochhammer_zeta_n_real": str(poch_real),
        "pochhammer_zeta_n_imag": str(poch_imag),
        "pochhammer_integer_match": poch_integer_match,
        "pochhammer_integer_value": int(poch_round) if poch_integer_match else None,
        "pochhammer_symbolic": poch_at_zeta_sym_str[:400],
        "verdict_per_pair_level": "HOLD" if held else "FAIL",
    }


# ──────────────────────────── main ─────────────────────────────────────────


def main() -> int:
    u = sp.Symbol("u")
    t0 = time.perf_counter()

    builder = WitnessBuilder(
        "qbeta-habiro-wenzl-tower-zeta-n",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Level-k SU(2) Verlinde tower probe: for k = 2, 4, 6, 8, "
        "test whether the universal cancellation S_M(u = ζ_{2(k+2)}) = 0 "
        "holds at the predicted boundary M = 2(k+2) − 1 for each "
        "atomic-step pair (D−n), (³He−D), (⁴He−³He). The level-2 case "
        "(k=2, ζ_8, M=7) is already verified in PR #1625; this probe "
        "extends to ζ_{12}, ζ_{16}, ζ_{20} where data permits, and "
        "checks (ζ; ζ)_{2(k+2)-1} integer normalization."
    )
    builder.set_content_block("prop:full-pole-structure-mass-trace")

    atomic = load_atomic(u)
    helium = load_helium(u)

    def make_delta(X: dict[int, sp.Poly],
                   Y: dict[int, sp.Poly]) -> dict[int, sp.Poly]:
        ms = sorted(set(X) | set(Y))
        out: dict[int, sp.Poly] = {}
        for m in ms:
            a_x = X.get(m, sp.Poly(0, u, domain="ZZ"))
            a_y = Y.get(m, sp.Poly(0, u, domain="ZZ"))
            delta = sp.Poly(a_x.as_expr() - a_y.as_expr(), u, domain="ZZ")
            out[m] = delta
        return out

    pairs = {
        "D_minus_n": make_delta(atomic["D"], atomic["n"]),
        "He3_minus_D": make_delta(helium["He3"], atomic["D"]),
        "He4_minus_He3": make_delta(helium["He4"], helium["He3"]),
    }

    levels = [2, 4, 6, 8]  # full tower; k=2 is the verification baseline.

    all_results: dict[str, dict] = {}
    cross_level_summary: dict[int, dict] = {}
    for level_k in levels:
        log("=" * 78)
        log(f"  LEVEL k = {level_k}  ⟹  n = 2(k+2) = {2*(level_k+2)}, "
            f"predicted M = {2*(level_k+2) - 1}")
        log("=" * 78)
        per_pair = {}
        feasible_pairs = []
        held_pairs = []
        for pair_label, delta_a in pairs.items():
            r = probe_level_k(delta_a, pair_label, level_k, u)
            per_pair[pair_label] = r
            if r.get("feasible", False):
                feasible_pairs.append(pair_label)
                if r.get("verdict_per_pair_level") == "HOLD":
                    held_pairs.append(pair_label)

        all_held = (
            len(feasible_pairs) > 0
            and len(held_pairs) == len(feasible_pairs)
        )
        universal = all_held and len(feasible_pairs) >= 2
        if len(feasible_pairs) == 0:
            level_verdict = "INFEASIBLE"
        elif all_held:
            if universal:
                level_verdict = "CONFIRMED (universal across pairs)"
            else:
                level_verdict = "PARTIAL (only one pair feasible, but holds)"
        else:
            level_verdict = "FALSIFIED (at least one pair fails)"
        log(f"\n  Level k = {level_k} verdict: {level_verdict}")
        log(f"    feasible pairs: {feasible_pairs}")
        log(f"    held pairs:     {held_pairs}")

        cross_level_summary[level_k] = {
            "n_cyclotomic_index": 2 * (level_k + 2),
            "predicted_M_first": 2 * (level_k + 2) - 1,
            "feasible_pairs": feasible_pairs,
            "held_pairs": held_pairs,
            "all_held": all_held,
            "universal_across_pairs": universal,
            "verdict": level_verdict,
        }
        all_results[f"level_{level_k}"] = {
            "per_pair": per_pair,
            "summary": cross_level_summary[level_k],
        }

    for key, val in all_results.items():
        builder.add_data(key, val)
    builder.add_data("cross_level_summary", cross_level_summary)

    # Final tower verdict
    confirmed_levels = [
        k for k, s in cross_level_summary.items()
        if s["verdict"].startswith("CONFIRMED")
    ]
    partial_levels = [
        k for k, s in cross_level_summary.items()
        if s["verdict"].startswith("PARTIAL")
    ]
    failed_levels = [
        k for k, s in cross_level_summary.items()
        if s["verdict"].startswith("FALSIFIED")
    ]
    infeasible_levels = [
        k for k, s in cross_level_summary.items()
        if s["verdict"] == "INFEASIBLE"
    ]

    log("\n" + "=" * 78)
    log("  TOWER VERDICT")
    log("=" * 78)
    log(f"  Confirmed (universal):  levels {confirmed_levels}")
    log(f"  Partial (1 pair):       levels {partial_levels}")
    log(f"  Falsified:              levels {failed_levels}")
    log(f"  Infeasible (no data):   levels {infeasible_levels}")

    if not failed_levels and (confirmed_levels or partial_levels):
        if infeasible_levels:
            tower_verdict = (
                f"PARTIAL — tower CONFIRMED at levels {confirmed_levels} "
                f"+ {partial_levels}, INFEASIBLE at {infeasible_levels}; "
                f"no falsification"
            )
        else:
            tower_verdict = f"CONFIRMED at all tested levels: {confirmed_levels}"
    elif failed_levels:
        tower_verdict = (
            f"FALSIFIED at levels {failed_levels}; confirmed at "
            f"{confirmed_levels + partial_levels}; infeasible at "
            f"{infeasible_levels}"
        )
    else:
        tower_verdict = "NO DATA"
    log(f"\n  TOWER VERDICT: {tower_verdict}")
    builder.add_data("tower_verdict", tower_verdict)

    # Assertions: level-2 verification (sanity), level-4 prediction
    if 2 in cross_level_summary:
        builder.add_assertion(
            "level_2_baseline_universal_at_M_7",
            computed=int(cross_level_summary[2]["universal_across_pairs"]),
            expected=1,
            tolerance=0,
            source="PR #1625 commit 85bf4f0982 (level-2 SU(2) Wenzl baseline).",
        )
    if 4 in cross_level_summary:
        builder.add_assertion(
            "level_4_tower_holds_at_M_11",
            computed=int(cross_level_summary[4]["all_held"]),
            expected=1,
            tolerance=0,
            source=(
                "Tower-extension prediction: SU(2) level-4 Verlinde at "
                "q = ζ_6 (u = ζ_12) should force S_11 = 0 across pairs."
            ),
        )

    builder.save()
    log("\n  ✓ Witness saved: qbeta-habiro-wenzl-tower-zeta-n.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
