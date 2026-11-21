#!/usr/bin/env python3
"""
Phase 1c: exact symbolic decomposition of the proton Borromean
Markov trace tr_M(β_Bor, q) at H₃ into per-partition rational
functions of q.

H₃ has 3 partitions: (3), (2,1), (1,1,1) with d_λ = 1, 2, 1.
The Borromean braid β_Bor = (σ₁σ₂⁻¹)³ gives the proton mass
via the substrate identity.

Computes the EXACT rational function y_λ(q) · χ^λ(β_Bor)(q) for
each partition, then:
1. h-expands to identify per-partition h² coefficients
2. Sums to verify tr_M = y_(3)·χ^(3) + y_(2,1)·χ^(2,1) + y_(1,1,1)·χ^(1,1,1)
3. Cross-checks against the Lean-proved closed form:
   |tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

The per-partition decomposition shows WHERE the Borromean trace's
structure comes from — essential for understanding the Reading-A
gap at the proton level.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
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
import time
from pathlib import Path

import sympy as sp
from sympy import Symbol, sqrt, cancel, series, Rational, simplify, factor

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder
from _precision import set_compute_dps  # noqa: E402


q = Symbol("q", positive=True)
h = q - 1/q


# ── Hoefsmit seminormal matrices for H₃ ────────────────────────

def build_h3_symbolic():
    """Build σ₁, σ₂ symbolically for each partition of 3.

    Returns dict: shape → (list of σ matrices, dim).
    """
    result = {}

    # (3): d=1, single SYT [1,2,3] all in row 1
    # σ₁ swaps 1,2: both in row 1, content diff = 1. Eigenvalue: q
    # σ₂ swaps 2,3: both in row 1, content diff = 1. Eigenvalue: q
    # Actually: a_ρ = h/(1 - q^{-2ρ}) with ρ = c(2) - c(1) = 1
    # a₁ = h/(1 - q⁻²) = h·q²/(q² - 1) = (q-q⁻¹)·q²/(q²-1) = q²(q-q⁻¹)/(q-1)(q+1) = q²·(q-1/q)/((q-1)(q+1))
    # = q²·(q²-1)/(q·(q²-1)) = q. Yes: a₁ = q for ρ=1.
    s1_3 = sp.Matrix([[q]])
    s2_3 = sp.Matrix([[q]])
    result[(3,)] = ([s1_3, s2_3], 1)

    # (1,1,1): d=1, single SYT [1,2,3] all in column 1
    # σ₁: ρ = c(2)-c(1) = -1. a_{-1} = h/(1-q²) = -q⁻¹
    # σ₂: ρ = c(3)-c(2) = -1. a_{-1} = -q⁻¹
    s1_111 = sp.Matrix([[-1/q]])
    s2_111 = sp.Matrix([[-1/q]])
    result[(1, 1, 1)] = ([s1_111, s2_111], 1)

    # (2,1): d=2, two SYT:
    #   t₀: 1,2 in row 1; 3 in row 2  → assignments [0,0,1]
    #   t₁: 1,3 in row 1; 2 in row 2  → assignments [0,1,0]
    #
    # For σ₁ (swaps entries 1 and 2):
    #   t₀: entries 1,2 both in row 1 → content diff c(2)-c(1) = 1
    #        1×1 block with eigenvalue a₁ = q
    #   t₁: entry 1 in row 1 (content 0), entry 2 in row 2 (content -1)
    #        → ρ = -1. 1×1 block with eigenvalue a_{-1} = -q⁻¹
    #   BUT WAIT: can swapping 1↔2 in t₁ give t₀?
    #   t₁ has: 1→cell(1,1), 2→cell(2,1), 3→cell(1,2)
    #   Swap 1↔2: 1→cell(2,1), 2→cell(1,1), 3→cell(1,2)
    #   This is: row 1 has [2,3], row 2 has [1] → valid SYT? NO!
    #   Entry 1 must come before 2 in each column. 1 in row 2, 2 in row 1:
    #   column 1 has [2,1] which is NOT increasing. So NOT a valid SYT.
    #   → 1×1 blocks for both t₀ and t₁ under σ₁.
    #   σ₁: diag(q, -1/q)

    # For σ₂ (swaps entries 2 and 3):
    #   t₀: entry 2 in row 1 col 2 (content 1), entry 3 in row 2 col 1 (content -1)
    #        ρ = c(3)-c(2) = -1 - 1 = -2
    #        Can we swap 2↔3? t₀ has 2→(1,2), 3→(2,1). Swap: 2→(2,1), 3→(1,2).
    #        New tableau: row 1=[1,3], row 2=[2]. This is t₁!
    #        → 2×2 block coupling t₀ and t₁.
    #   ρ = -2 for (t₀, t₁): a_{-2} = h/(1-q⁴), a₂ = h/(1-q⁻⁴)
    #   b² = a_{-2}·a₂ + 1

    a_neg2 = h / (1 - q**4)
    a_pos2 = h / (1 - q**(-4))
    b_sq = cancel(a_neg2 * a_pos2 + 1)
    b = sqrt(b_sq)

    s1_21 = sp.Matrix([[q, 0], [0, -1/q]])
    s2_21 = sp.Matrix([[a_neg2, b], [b, a_pos2]])
    result[(2, 1)] = ([s1_21, s2_21], 2)

    return result


def borromean_braid_character(sigmas, dim):
    """Compute χ^λ(β_Bor) where β_Bor = (σ₁σ₂⁻¹)³.

    σ₂⁻¹ = σ₂ − h·I (from Hecke relation σ² = h·σ + 1 → σ⁻¹ = σ − h).
    """
    I = sp.eye(dim)
    s1 = sigmas[0]
    s2 = sigmas[1]
    s2_inv = s2 - h * I  # σ₂⁻¹ via Hecke relation

    factor = s1 * s2_inv  # σ₁σ₂⁻¹
    product = factor * factor * factor  # (σ₁σ₂⁻¹)³

    # Simplify
    product = product.applyfunc(cancel)
    return cancel(product.trace())


def main():
    t0 = time.time()
    print("=" * 70)
    print("  Phase 1c: exact symbolic proton Borromean trace decomposition")
    print("=" * 70)
    print()

    reps = build_h3_symbolic()

    # Load symbolic y_λ for n=3
    import json
    witness_path = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
    y_sym_map = {}
    if witness_path.exists():
        doc = json.load(open(witness_path))
        tables = doc.get("tables_by_n", doc.get("data", {}).get("tables_by_n", {}))
        n3 = tables.get("3", {})
        for w in n3.get("weights", []):
            part = tuple(w["partition"])
            y_sym_map[part] = sp.sympify(w["y_lambda_symbolic"], locals={"q": q})

    # Compute per-partition
    shapes = [(3,), (2, 1), (1, 1, 1)]
    results = {}
    total_tr = sp.Integer(0)

    for shape in shapes:
        sigmas, dim = reps[shape]

        chi = borromean_braid_character(sigmas, dim)
        print(f"  λ = {list(shape)}, d = {dim}")
        print(f"    χ^λ(β_Bor) = {chi}")

        y = y_sym_map.get(shape)
        if y is not None:
            product = cancel(y * chi)
            print(f"    y_λ         = {y}")
            print(f"    y·χ         = {product}")

            # h-expand
            h_sym = Symbol("h_var")
            q_of_h = (h_sym + sqrt(h_sym**2 + 4)) / 2
            sub = product.subs(q, q_of_h)
            ser = sp.series(sub, h_sym, 0, 7)
            print(f"    h-expansion:")
            for k in range(7):
                ck = cancel(ser.coeff(h_sym, k))
                ck_float = float(ck.evalf()) if ck != 0 else 0.0
                marker = " ◄" if k == 2 else ""
                print(f"      h^{k}: {ck} ≈ {ck_float:.8e}{marker}")

            results[shape] = {
                "chi": chi,
                "y": y,
                "product": product,
                "h2_coeff": cancel(ser.coeff(h_sym, 2)),
            }
            total_tr += product
        else:
            print(f"    WARNING: no symbolic y_λ")
        print()

    # Total trace
    total_tr = cancel(total_tr)
    print("=" * 70)
    print("  TOTAL: tr_M(β_Bor) = Σ y_λ · χ^λ")
    print("=" * 70)
    print(f"  tr_M(β_Bor) = {total_tr}")
    print()

    # Compare to Lean-proved form
    lean_form = (4 + h**2 - 3*h**4 - h**6) / (h**2 + 4)
    lean_expanded = cancel(lean_form)
    diff = cancel(total_tr - lean_expanded)
    print(f"  Lean form: (4 + h² − 3h⁴ − h⁶) / (h² + 4) = {lean_expanded}")
    print(f"  Difference: {diff}")
    print(f"  Match: {'YES ✓' if diff == 0 else 'NO — checking numerically...'}")

    if diff != 0:
        # Try numerical check
        import mpmath as mp
        set_compute_dps()
        # Was:
        #   q0 = mp.mpf(Q_50_DIGIT_STR) if 'Q_50_DIGIT_STR' in dir() \
        #        else mp.mpf("1.1097785955541805")
        #
        # THREE compounding defects, all in one line:
        #  1. `dir()` with no argument returns the LOCAL namespace. This line
        #     is inside `main()`, so a module-level name could never appear
        #     there — the guard is unsatisfiable.
        #  2. `Q_50_DIGIT_STR` is imported at line ~282, AFTER `main()`, so it
        #     was never a local of `main()` under any circumstance. The guard
        #     was therefore ALWAYS False and the fallback ALWAYS taken.
        #  3. The fallback literal `1.1097785955541805` is a DIGIT-TRANSPOSED
        #     muon pin — `1.10977…` for `1.10997…` — which is 0.018 % off,
        #     roughly 15,600x the ~11.5 ppb μ–p substrate tension.
        #
        # Reached only when the symbolic comparison above fails (`diff != 0`),
        # so it is a rarely-executed path rather than a live wrong number in
        # every run. Import it properly and let an ImportError be loud.
        from q_parameter import Q_50_DIGIT_STR as _Q0_STR
        q0 = mp.mpf(_Q0_STR)
        tr_num = float(total_tr.subs(q, float(q0)).evalf())
        lean_num = float(lean_expanded.subs(q, float(q0)).evalf())
        print(f"  Numerical at q₀: tr_M = {tr_num:.15e}, lean = {lean_num:.15e}")
        print(f"  Difference: {abs(tr_num - lean_num):.3e}")

    # Per-partition h² summary
    print(f"\n  Per-partition h² coefficients:")
    h2_sum = sp.Integer(0)
    for shape in shapes:
        if shape in results:
            c2 = results[shape]["h2_coeff"]
            h2_sum += c2
            print(f"    {str(list(shape)):>12s}: {c2}")
    print(f"    {'Sum':>12s}: {h2_sum}")

    # h-expand the TOTAL
    print(f"\n  Total tr_M h-expansion:")
    h_sym = Symbol("h_var")
    q_of_h = (h_sym + sqrt(h_sym**2 + 4)) / 2
    total_sub = total_tr.subs(q, q_of_h)
    total_ser = sp.series(total_sub, h_sym, 0, 9)
    for k in range(9):
        ck = cancel(total_ser.coeff(h_sym, k))
        print(f"    h^{k}: {ck}")

    elapsed = time.time() - t0
    print(f"\n  Wall time: {elapsed:.1f}s")

    # Witness
    w = WitnessBuilder("phase1c-proton-h3-symbolic-decomposition", engine="sympy")
    w.set_description(
        "Exact symbolic per-partition decomposition of the proton "
        "Borromean Markov trace at H₃. Computes y_λ · χ^λ(β_Bor) "
        "as rational functions of q for all 3 partitions: (3), (2,1), "
        "(1,1,1). Cross-checks against Lean-proved closed form."
    )
    w.set_content_block("conj:proton-mass-substrate-identity")
    w.set_audit_only("docs/audits/2026-05-26-phase1c-proton-h3-decomposition.md")

    for shape in shapes:
        if shape in results:
            w.add_data(f"partition_{shape}", {
                "chi": str(results[shape]["chi"]),
                "y_lambda": str(results[shape]["y"]),
                "product": str(results[shape]["product"]),
                "h2_coefficient": str(results[shape]["h2_coeff"]),
            })
    w.add_data("total_tr_M", str(total_tr))
    w.add_data("lean_form_matches", diff == 0)

    w.add_assertion(
        name="lean_form_match",
        computed=1 if diff == 0 else 0,
        expected=1,
        tolerance=0,
        source="Sum of per-partition contributions must equal Lean-proved form"
    )
    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    from q_parameter import Q_50_DIGIT_STR  # noqa: F401
    main()
