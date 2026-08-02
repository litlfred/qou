#!/usr/bin/env python3
"""derived_chi_catalogue_rust_gp_crosscheck.py — port equivalence gate.

Cross-checks the **Rust-backed** symbolic character
`chi_lambda_via_rust_gp` (one `pyhecke_native.chi_q_via_gp` FFI call per
(shape, word), Geck–Pfeiffer engine) against the **pure-Python** Hoefsmit
seminormal matrix product `chi_lambda_via_matrix_product` on the LONG
production braid words — the words the main-script Tests 5–7 delegate to
the Rust path and therefore no longer exercise pure-Python.

Both paths are exact-integer (the character χ^λ(T_β) is an exact Laurent
polynomial in q), so equivalence is **exact**, not merely within a
tolerance:

  1. symbolic delta = `sp.cancel(py_symbolic - rust_symbolic) == 0`, and
  2. numerical agreement at the canonical substrate q₀ (`Q_50_DIGIT_STR`)
     to ≥ 40 decimal digits — the mandated cross-check bar.

Why a separate harness: the main script keeps the pure-Python vs Rust
independent-engine check on the SHORT words (Tests 1–4). This file is the
independent-engine check on the LONG production words (deuteron
`atom_braid_word_3A(1,1)`, 23 crossings; an A=3, n=9 word), so the port's
equivalence claim is machine-verified on exactly the words the main
script optimised.

Precision discipline (compute-author §1): no f64 anywhere. Both sides sum
exact `sp.Integer` Laurent coefficients; the q₀ comparison is done at
55-dps mpmath from the exact sympy value via a decimal-string round-trip.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from derived_chi_catalogue_matrix_m import (  # noqa: E402
    _word_for_braid_word_3a,
    chi_lambda_via_matrix_product,
    chi_lambda_via_rust_gp,
    standard_young_tableaux,
    _shape_partitions_of,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Cross-check digit target and the equivalence guards.
CROSSCHECK_DPS = 40
# Cap the pure-Python matrix dim so the (slow) reference stays bounded;
# the Rust path is fast at any dim, but the pure-Python side scales with
# dim × word-length under sp.cancel. dim ≤ 9 covers every partition of 6
# except (3,2,1)/(2,2,1,1)-class dim-16 shapes and keeps wall ~1–2 min.
MAX_DIM_PY = 9


def _q0_value_exact() -> sp.Rational:
    """Canonical substrate q₀ as an exact rational (no f64)."""
    return sp.Rational(Q_50_DIGIT_STR)


def _mpf_at_q0(expr: sp.Expr, q_sym: sp.Symbol, q0: sp.Rational) -> mp.mpf:
    """Evaluate a symbolic Laurent poly at q₀ as an mpf via an exact
    decimal-string round-trip (compute-author §1.1: no `float(expr)`)."""
    val = sp.nsimplify(expr.subs(q_sym, q0)) if expr.free_symbols else expr
    # sp.N with extra guard digits, serialised as a string, parsed by mpmath.
    return mp.mpf(str(sp.N(expr.subs(q_sym, q0), CROSSCHECK_DPS + 15)))


def crosscheck_word(
    label: str,
    shape: tuple[int, ...],
    word: list[tuple[int, int]],
    q_sym: sp.Symbol,
    q0: sp.Rational,
) -> dict:
    """Return a per-(shape,word) cross-check record."""
    n = sum(shape)
    py = chi_lambda_via_matrix_product(shape, word, q_sym)
    rust = chi_lambda_via_rust_gp(shape, n, word, q_sym)
    symbolic_delta = sp.cancel(py - rust)
    symbolic_match = symbolic_delta == 0

    py_q0 = _mpf_at_q0(py, q_sym, q0)
    rust_q0 = _mpf_at_q0(rust, q_sym, q0)
    if py_q0 == 0 and rust_q0 == 0:
        reldiff = mp.mpf(0)
    elif py_q0 == 0:
        reldiff = abs(rust_q0)
    else:
        reldiff = abs(py_q0 - rust_q0) / abs(py_q0)
    # digits of agreement (∞ when exactly equal)
    digits = mp.inf if reldiff == 0 else -mp.log10(reldiff)
    digits_ok = (digits == mp.inf) or (digits >= CROSSCHECK_DPS)

    return {
        "label": label,
        "shape": list(shape),
        "n_strands": n,
        "word_len": len(word),
        "dim_V_lambda": len(standard_young_tableaux(shape)),
        "symbolic_delta": str(symbolic_delta),
        "symbolic_match": bool(symbolic_match),
        "reldiff_at_q0": mp.nstr(reldiff, 3),
        "digits_agree": ("inf" if digits == mp.inf else mp.nstr(digits, 4)),
        "digits_ok": bool(digits_ok),
        "pass": bool(symbolic_match and digits_ok),
    }


def main() -> int:
    mp.mp.dps = CROSSCHECK_DPS + 25
    q_sym = sp.Symbol("q", positive=True)
    q0 = _q0_value_exact()

    wb = WitnessBuilder(
        "derived-chi-catalogue-rust-gp-crosscheck",
        engine="python",
    )
    wb.set_description(
        "Equivalence gate for the Rust-GP port of the derived-chi "
        "catalogue: pure-Python Hoefsmit matrix product "
        "(chi_lambda_via_matrix_product) vs the Rust Geck–Pfeiffer engine "
        "(chi_lambda_via_rust_gp -> pyhecke_native.chi_q_via_gp) on the "
        "LONG production braid words (deuteron atom_braid_word_3A(1,1), "
        "23 crossings; an A=3 n=9 word). Both paths are exact-integer, so "
        "the two characters agree symbolically (delta = 0) and at q0 to "
        "40+ digits (exactly). Covers the words the main script's "
        "Tests 5-7 delegate to Rust and no longer check pure-Python."
    )

    print("=" * 78)
    print(" Rust-GP port equivalence gate — pure-Python ↔ chi_q_via_gp")
    print("=" * 78)

    records: list[dict] = []

    # ── Production deuteron braid: atom_braid_word_3A(1, 1), 23 crossings ──
    n6, deut_word = _word_for_braid_word_3a(1, 1)
    print(f"\n  Deuteron β = atom_braid_word_3A(1,1)  "
          f"(n={n6}, {len(deut_word)} crossings)")
    print("  " + "─" * 60)
    for shape in _shape_partitions_of(6):
        if len(standard_young_tableaux(shape)) > MAX_DIM_PY:
            continue
        rec = crosscheck_word("deuteron_23", shape, deut_word, q_sym, q0)
        status = "✓" if rec["pass"] else "✗"
        print(f"    {status} λ={rec['shape']} dim={rec['dim_V_lambda']} "
              f"symbolic_delta={rec['symbolic_delta']} "
              f"digits@q0={rec['digits_agree']}")
        records.append(rec)

    # ── A=3 (n=9) word: σ_1..σ_8 ──
    a3_word = [(1, g) for g in (1, 2, 3, 4, 5, 6, 7, 8)]
    print(f"\n  A=3 β = σ_1·…·σ_8  (n=9, {len(a3_word)} crossings)")
    print("  " + "─" * 60)
    for shape in _shape_partitions_of(9):
        if len(standard_young_tableaux(shape)) > MAX_DIM_PY:
            continue
        rec = crosscheck_word("a3_n9", shape, a3_word, q_sym, q0)
        status = "✓" if rec["pass"] else "✗"
        print(f"    {status} λ={rec['shape']} dim={rec['dim_V_lambda']} "
              f"symbolic_delta={rec['symbolic_delta']} "
              f"digits@q0={rec['digits_agree']}")
        records.append(rec)

    n_total = len(records)
    n_pass = sum(1 for r in records if r["pass"])
    n_symbolic = sum(1 for r in records if r["symbolic_match"])
    print("\n  ── Summary ──")
    print(f"    Cross-checks: {n_total}")
    print(f"    Symbolic delta = 0: {n_symbolic}/{n_total}")
    print(f"    q0 agreement ≥ {CROSSCHECK_DPS} digits: "
          f"{sum(1 for r in records if r['digits_ok'])}/{n_total}")
    print(f"    Passed (both): {n_pass}/{n_total}")

    wb.add_assertion(
        "rust_gp_symbolically_identical_to_pure_python_hoefsmit",
        computed=(n_symbolic == n_total),
        expected=True,
        source="Whether chi_lambda_via_rust_gp (Rust chi_q_via_gp, one FFI "
               "call/word) reassembled to a symbolic Laurent poly equals "
               "the pure-Python Hoefsmit matrix product "
               "chi_lambda_via_matrix_product EXACTLY (sp.cancel(py-rust)==0) "
               "on the 23-crossing production deuteron braid and an A=3 n=9 "
               "word, for every partition with dim V_λ ≤ 9. This is the port "
               "equivalence gate: the optimisation moves the character "
               "compute to Rust with zero change to the answer.",
    )
    wb.add_assertion(
        "rust_gp_agrees_at_q0_to_40_digits",
        computed=all(r["digits_ok"] for r in records),
        expected=True,
        source="Whether the Rust-GP and pure-Python characters agree at the "
               "canonical substrate q0 (Q_50_DIGIT_STR) to at least 40 "
               "decimal digits. Because both are exact-integer Laurent "
               "polynomials the agreement is exact (digits = inf); the 40-"
               "digit bar is the compute-author cross-check floor.",
    )
    wb.add_data("crosscheck_dps", CROSSCHECK_DPS)
    wb.add_data("max_dim_pure_python", MAX_DIM_PY)
    wb.add_data("q0_str", Q_50_DIGIT_STR)
    wb.add_data("n_crosschecks", n_total)
    wb.add_data("n_symbolic_match", n_symbolic)
    wb.add_data("n_pass", n_pass)
    wb.add_data("records", records)
    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    print("=" * 78)
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    sys.exit(main())
