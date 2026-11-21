#!/usr/bin/env python3
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from _precision import set_compute_dps, fmt  # noqa: E402 — raise dps before any mpmath value
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
Compute C_{[3,2,1]} at q_0 — the BW shadow-price coefficient for
the self-conjugate partition (3,2,1) at k = 6.

Per `prop:wigner-2-coefficient`:

    C_{[3,2,1]}  =  [2]_q · [4]_q · [6]_q · h  /  (2 · [3]_q^3 · [5]_q)

where [n]_q = (q^n − q^{−n}) / (q − q^{−1})  and  h = q − q^{−1}.

The proposition gives a clean derivation: C_λ = w_λ · h/2 for any
self-conjugate partition (the trace-per-dim is exactly h/2 for any
self-conjugate λ — Wigner-2 result).

This script:
  1. Evaluates C_{[3,2,1]} at q_0 = 1.1100.
  2. Reports the per-partition shadow price.
  3. Compares to the empirical α_5 fit from the GB-level-5 shell
     diagnostic (witness: higher-a-shell-diagnostic.witness.json).
  4. Notes the SCOPE MISMATCH: Term 7's level-ℓ=5 covers ALL
     height-6 partitions across all A; [3,2,1] is only ONE of those
     (and only contributes at A=2, k=6).

Witness: shadow-price-c-321-q0.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT, Q_MP


def q_int(n, q):
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def c_321_closed_form(q):
    """C_{[3,2,1]} = [2]_q · [4]_q · [6]_q · h / (2 · [3]_q^3 · [5]_q)."""
    h = q - 1 / q
    num = q_int(2, q) * q_int(4, q) * q_int(6, q) * h
    den = 2 * q_int(3, q) ** 3 * q_int(5, q)
    return num / den


def w_lambda_321(q):
    """Schur-Weyl weight w_{[3,2,1]} = dim_q^2 / [6]_q!.

    dim_q([3,2,1]) = [6]_q! / ([5]_q · [3]_q^2)  via hooks {5,3,1,3,1,1}.
    So w = ([6]_q!)^2 / ([5]_q^2 · [3]_q^4) / [6]_q!
        = [6]_q! / ([5]_q^2 · [3]_q^4).
    """
    qf6 = (q_int(1, q) * q_int(2, q) * q_int(3, q)
           * q_int(4, q) * q_int(5, q) * q_int(6, q))
    dim_q = qf6 / (q_int(5, q) * q_int(3, q) ** 2)
    return dim_q ** 2 / qf6


def trace_per_dim_321(q):
    """tr(σ_g) / dim for self-conjugate λ = h/2 (Wigner-2 proposition)."""
    return (q - 1 / q) / 2


# Working precision is raised here and q_0 is read as Q_MP, so the values
# this producer emits carry the full 60-digit output precision. Until
# 2026-11-21 it read q_0 through float(), which capped every result at
# float64 (rel. moves 4e-17..1.2e-16); gate: f64_into_mpmath_audit F64_CAST.
set_compute_dps()

if __name__ == "__main__":
    print("BW SHADOW PRICE C_{[3,2,1]} AT q_0")
    print("=" * 80)
    q0 = Q_MP  # was mp.mpf(str(float(Q0_FLOAT))): float64 cap (f64_into_mpmath_audit F64_CAST)
    print(f"q_0 = {float(q0):.6f}")

    # Numerical at q_0
    c_q0 = c_321_closed_form(q0)
    w_q0 = w_lambda_321(q0)
    h_q0 = q0 - 1 / q0
    tr_per_dim = trace_per_dim_321(q0)

    print(f"\nIngredients at q_0:")
    print(f"  h = q - q⁻¹            = {float(h_q0):.6f}")
    print(f"  [2]_q                  = {float(q_int(2, q0)):.6f}")
    print(f"  [3]_q                  = {float(q_int(3, q0)):.6f}")
    print(f"  [4]_q                  = {float(q_int(4, q0)):.6f}")
    print(f"  [5]_q                  = {float(q_int(5, q0)):.6f}")
    print(f"  [6]_q                  = {float(q_int(6, q0)):.6f}")
    print(f"  w_{{[3,2,1]}}              = {float(w_q0):.6e}")
    print(f"  tr(σ_g)/dim = h/2      = {float(tr_per_dim):.6f}")
    print()
    print(f"C_{{[3,2,1]}} (Hecke units)  = {float(c_q0):.6e}")

    # Symbolic identity check
    print(f"\nSymbolic identity check:  C = w · (h/2) ?")
    c_check = w_q0 * tr_per_dim
    print(f"  closed-form C           = {float(c_q0):.6e}")
    print(f"  w · (h/2)               = {float(c_check):.6e}")
    print(f"  ratio                   = {float(c_q0 / c_check):.10f}")
    if abs(float(c_q0 / c_check) - 1.0) < 1e-9:
        print(f"  ✓ identity holds (Wigner-2 corollary)")
    else:
        print(f"  ✗ MISMATCH — check formula")

    # Compare to empirical α_5 fit
    print(f"\n── Comparison to empirical α_5 fit ──")
    diag_path = (Path(__file__).parent
                  / "higher-a-shell-diagnostic.witness.json")
    if diag_path.exists():
        diag = json.loads(diag_path.read_text())
        per_lvl = diag.get("per_level_fits", {})
        if "5" in per_lvl:
            fit = per_lvl["5"]
            alpha_5_fit_mev = float(fit["alpha"])
            print(f"  empirical α_5 fit (MeV)  = {alpha_5_fit_mev:+.3e}")
            print(f"    (single-feature fit of CODATA−|S|≤2 residual vs")
            print(f"     ℓ=5 sum-of-w·χ across A=1–4 isotopes; RMSE = "
                  f"{fit['rmse']:.2f} MeV)")

    print(f"\n── SCOPE MISMATCH NOTE ──")
    print(f"  C_{{[3,2,1]}} is the shadow-price coefficient for ONE specific")
    print(f"  partition at k = 6 (i.e., A = 2 = deuteron).")
    print()
    print(f"  My session's 'GB level ℓ = 5' (Term 7 conjecture) covers ALL")
    print(f"  partitions of height 6 = ℓ+1, across ALL atomic-braid sizes")
    print(f"  k = 3A for A = 2, 3, 4, ...:")
    print(f"    A = 2  (k=6):  height-6 partitions = {{(3,2,1)}} (1 partition)")
    print(f"    A = 3  (k=9):  height-6 partitions  = 3 partitions")
    print(f"    A = 4  (k=12): height-6 partitions = 11 (per atom-level witness)")
    print()
    print(f"  At A = 2, my level-5 = {{[3,2,1]}} exactly, so C_{{[3,2,1]}} IS")
    print(f"  the shadow price.  At A ≥ 3 the level-5 fit aggregates over")
    print(f"  multiple partitions, each with its own C_λ.  Direct comparison")
    print(f"  requires per-partition decomposition (Item 4).")

    witness = {
        "computation": "shadow-price-c-321-q0",
        "engine": "python",
        # Downstream-added field, now emitted by the producer so a re-run
        # does not delete it (AGENTS.md "Bare producers").
        "auditOnly": "docs/audits/2026-05-02-lp-dual-infra-scope.md",
        "description": (
            "Numerical evaluation of the BW shadow-price coefficient "
            "C_{[3,2,1]} at q_0 via the closed form from "
            "prop:wigner-2-coefficient.  Uses [n]_q · h / [3]_q^3 · "
            "[5]_q closed form; cross-checks via Wigner-2 corollary "
            "C = w · h/2."
        ),
        "reference_blocks": [
            "prop:wigner-2-coefficient",
            "prop:mass-coefficient-shadow-price",
            "conj:shell-correction-term-seven",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": fmt(q0),
        },
        "results": {
            "C_321_at_q0": fmt(c_q0),
            "w_321_at_q0": fmt(w_q0),
            "h_at_q0": fmt(h_q0),
            "trace_per_dim_at_q0": fmt(tr_per_dim),
            "wigner_2_identity_check": (abs(float(c_q0 / c_check) - 1.0)
                                          < 1e-9),
        },
        "scope_note": (
            "C_{[3,2,1]} is the SINGLE-PARTITION shadow price at k=6 "
            "(A=2 only).  The empirical α_5 fit from the higher-A shell "
            "diagnostic aggregates over ALL height-6 partitions across "
            "A=1..4.  Direct numerical comparison requires per-partition "
            "decomposition (see paper_six_term_isotope_sweep refactor)."
        ),
    }
    out = Path(__file__).parent / "shadow-price-c-321-q0.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
