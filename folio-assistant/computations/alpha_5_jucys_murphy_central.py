"""α_5 derivation via Jucys–Murphy central elements at the crystal limit.

Per the dual-statement / FSC / center analysis (chat thread,
2026-05-09):

  α_5 = m_e · tr_M(P_5) / [3A]_q!  with  P_5 = e_5(J_1, ..., J_n)|_{ht=6}

where:
  - J_k are q-deformed Jucys–Murphy elements: J_k acts on a
    seminormal-basis vector |T⟩ (T a standard Young tableau) by
    multiplication by q^{2 c(□_k)}, with c(□_k) the cell-content
    of the cell containing k in T.
  - e_5(...) is the 5th elementary symmetric polynomial in the J_k.
  - The "ht=6 restriction" projects to height-6 partitions only.

By Murphy 1992, e_k(J_1, ..., J_n) ∈ Z(H_n(q)) — central, hence
a scalar c_k(λ) on each Wedderburn block V_λ. The scalar is

  c_k(λ) = e_k({q^{2c(□)} : □ ∈ λ})

— the elementary symmetric polynomial in q^{2·content} over the
cells of λ.

THE FUNDAMENTAL CLAIM:

  α_5 = m_e · Σ_{λ ⊢ 3A, ht(λ)=6} w_λ(q) · c_5(λ) / [3A]_q!

If atom-independent (constant across A=2, 3, 4, ...), then α_5 is
DERIVED — no AME calibration needed.

NUMERICAL STRATEGY.  To avoid sympy's exponential expansion blow-up
on partitions of 3·4 = 12, this version evaluates EVERYTHING
numerically at q_0 (and at q=1 as a sanity check) using Python's
mpmath with 50-digit precision.  No symbolic q is used.

Computes for A ∈ {2, 3, 4} and tests atom-independence.
"""
from __future__ import annotations
import sys
from pathlib import Path
from itertools import combinations

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50  # 50-digit precision throughout


def partitions_of(n):
    if n == 0:
        return [()]
    out = []

    def gen(rem, cap, cur):
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
    out = []
    for r, length in enumerate(shape):
        for c in range(length):
            out.append(c - r)
    return out


def hook_lengths(shape):
    rows = list(shape)
    cols_count = [0] * (rows[0] if rows else 0)
    for length in rows:
        for c in range(length):
            cols_count[c] += 1
    out = []
    for r, length in enumerate(rows):
        for c in range(length):
            arm = length - c - 1
            leg = cols_count[c] - r - 1
            out.append(arm + leg + 1)
    return out


def q_int_num(n, q_val):
    """[n]_q at numeric q.  Uses (q^n - q^{-n}) / (q - q^{-1}) form
    for stability away from q=1; reverts to balanced sum at q=1."""
    if n == 0:
        return mp.mpf(0)
    if n < 0:
        return -q_int_num(-n, q_val)
    if abs(q_val - 1) < mp.mpf("1e-30"):
        return mp.mpf(n)
    qn = q_val ** n
    qmn = q_val ** (-n)
    qd = q_val - q_val ** (-1)
    return (qn - qmn) / qd


def q_factorial_num(n, q_val):
    res = mp.mpf(1)
    for k in range(1, n + 1):
        res = res * q_int_num(k, q_val)
    return res


def dim_q_num(shape, q_val):
    n = sum(shape)
    num = q_factorial_num(n, q_val)
    den = mp.mpf(1)
    for h in hook_lengths(shape):
        den = den * q_int_num(h, q_val)
    return num / den


def w_lambda_num(shape, q_val):
    n = sum(shape)
    return dim_q_num(shape, q_val) ** 2 / q_factorial_num(n, q_val)


def e5_central_num(shape, q_val):
    """5th elementary symmetric polynomial in {q^{2c(□)} : □ ∈ λ},
    evaluated numerically at q_val."""
    cells = cell_contents(shape)
    if len(cells) < 5:
        return mp.mpf(0)
    eigenvalues = [q_val ** (2 * c) for c in cells]
    total = mp.mpf(0)
    for subset in combinations(eigenvalues, 5):
        prod = mp.mpf(1)
        for v in subset:
            prod = prod * v
        total = total + prod
    return total


def height(shape):
    return len(shape)


def f_lambda(shape):
    """Classical Specht dim f^λ via hook formula (integer)."""
    n = sum(shape)
    fact = mp.factorial(n)
    den = mp.mpf(1)
    for h in hook_lengths(shape):
        den = den * h
    return int(fact / den)


def alpha_5_at_A_num(A, q_val):
    """α_5(A) at numeric q_val.

    Returns:
        (alpha_5_value, contributions_list)
        alpha_5_value is the unnormalized sum
            Σ_{λ ⊢ 3A, ht=6} w_λ(q) · c_5(λ)
        (the m_e and 1/[3A]_q! prefactors are A-independent in the
        atom-independence comparison so we test on this sum alone).
    """
    n = 3 * A
    total = mp.mpf(0)
    contributions = []
    for shape in partitions_of(n):
        if height(shape) != 6:
            continue
        w = w_lambda_num(shape, q_val)
        c5 = e5_central_num(shape, q_val)
        prod = w * c5
        total = total + prod
        contributions.append({
            "shape": list(shape),
            "f_lambda": f_lambda(shape),
            "w_lambda": float(w),
            "c_5": float(c5),
            "contribution": float(prod),
        })
    return total, contributions


def alpha_5_at_A_normalized(A, q_val):
    """α_5(A) divided by [3A]_q! — the actual scaling-corrected
    quantity that should be atom-independent if the JM-central
    derivation is correct."""
    raw, contribs = alpha_5_at_A_num(A, q_val)
    n = 3 * A
    qfact = q_factorial_num(n, q_val)
    return raw / qfact, contribs


def main() -> int:
    q_0 = mp.mpf(Q_50_DIGIT_STR)

    print("α_5 derivation via Jucys–Murphy central elements")
    print(f"  q_0 ≈ {float(q_0):.10f}")
    print()

    wb = (
        WitnessBuilder("alpha-5-jucys-murphy-central", engine="mpmath")
        .set_description(
            "α_5 derivation probe via the Jucys–Murphy central element "
            "P_5 := e_5(J_1, ..., J_n) restricted to height-6 partitions. "
            "By Murphy 1992, e_5(J_1..J_n) ∈ Z(H_n(q)) — central — so "
            "α_5(A) := Σ_{λ ⊢ 3A, ht=6} w_λ · c_5(λ) is computable as a "
            "finite combinatorial sum in q-rationals.  Tests "
            "atom-independence across A = 2..4: if the sum normalised "
            "by [3A]_q! is constant, α_5 is DERIVED."
        )
        .set_content_block("prop:mass-formula-iterative-lp-dual")
        .add_parameter("q_0", str(q_0))
        .add_parameter("alpha_5_AME_fit_MeV", -4.2e5)
    )

    results = {}
    for A in [2, 3, 4]:
        print(f"=== A = {A} (n = {3*A}) ===")
        raw_q0, contribs_q0 = alpha_5_at_A_num(A, q_0)
        norm_q0, _ = alpha_5_at_A_normalized(A, q_0)

        # q→1 limit (use 1+epsilon to avoid the apparent singularity
        # in our q_int_num form at q=1).
        q_eps = mp.mpf("1") + mp.mpf("1e-25")
        raw_q1, contribs_q1 = alpha_5_at_A_num(A, q_eps)
        norm_q1, _ = alpha_5_at_A_normalized(A, q_eps)

        print(f"  # height-6 partitions of {3*A}: {len(contribs_q0)}")
        print(f"  α_5(A={A}) raw at q_0 ≈ {float(raw_q0):+.6e}")
        print(f"  α_5(A={A}) /[3A]_q! at q_0 ≈ {float(norm_q0):+.6e}")
        print(f"  α_5(A={A}) raw at q→1  ≈ {float(raw_q1):+.6e}")
        print(f"  α_5(A={A}) /[3A]_q! at q→1  ≈ {float(norm_q1):+.6e}")

        for c in contribs_q0[:3]:
            print(
                f"    λ = {tuple(c['shape'])}, f^λ = {c['f_lambda']}, "
                f"contribution = {c['contribution']:+.4e}"
            )

        results[A] = {
            "alpha_5_raw_q0": float(raw_q0),
            "alpha_5_normalized_q0": float(norm_q0),
            "alpha_5_raw_q1": float(raw_q1),
            "alpha_5_normalized_q1": float(norm_q1),
            "n_height_6_partitions": len(contribs_q0),
            "top_contributions_q0": contribs_q0[:5],
        }

    # Atom-independence test on the NORMALIZED quantity
    print()
    print("Atom-independence test (NORMALIZED by [3A]_q!):")
    vals_q0_norm = [results[A]["alpha_5_normalized_q0"] for A in [2, 3, 4]]
    spread_n = max(vals_q0_norm) - min(vals_q0_norm)
    median_n = sorted(vals_q0_norm)[len(vals_q0_norm) // 2]
    rel_spread_n = spread_n / abs(median_n) if median_n != 0 else float("inf")
    print(f"  α_5(2)/[6]!, α_5(3)/[9]!, α_5(4)/[12]! at q_0:")
    for A in [2, 3, 4]:
        print(f"    A={A}: {results[A]['alpha_5_normalized_q0']:+.6e}")
    print(f"  Range: {spread_n:.4e}, median: {median_n:.4e}")
    print(f"  Relative spread: {rel_spread_n:.6f} ({rel_spread_n*100:.2f}%)")

    # Also test on raw (no normalization)
    print()
    print("Atom-independence test (RAW, no [3A]_q! normalization):")
    vals_q0_raw = [results[A]["alpha_5_raw_q0"] for A in [2, 3, 4]]
    spread_r = max(vals_q0_raw) - min(vals_q0_raw)
    median_r = sorted(vals_q0_raw)[len(vals_q0_raw) // 2]
    rel_spread_r = spread_r / abs(median_r) if median_r != 0 else float("inf")
    for A in [2, 3, 4]:
        print(f"    A={A}: {results[A]['alpha_5_raw_q0']:+.6e}")
    print(f"  Range: {spread_r:.4e}, median: {median_r:.4e}")
    print(f"  Relative spread: {rel_spread_r:.6f}")

    wb.add_assertion(
        "alpha_5_atom_independent_normalized",
        float(rel_spread_n),
        0.0,
        tolerance=0.05,
    )
    wb.add_assertion(
        "alpha_5_normalized_finite",
        1.0 if all(abs(v) < 1e30 for v in vals_q0_norm) else 0.0,
        1.0,
        tolerance=1e-6,
    )

    if rel_spread_n < 0.01:
        verdict = "atom-independent (α_5 derived)"
    elif rel_spread_n < 0.10:
        verdict = "weakly atom-dependent (curvature in connection)"
    else:
        verdict = "strongly atom-dependent (mechanism orthogonal to JM-central)"
    print(f"\nVERDICT: {verdict}")

    wb.add_data("results", results)
    wb.add_data("verdict", verdict)
    wb.add_data("relative_spread_normalized", float(rel_spread_n))
    wb.add_data("relative_spread_raw", float(rel_spread_r))
    out_path = wb.save()
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
