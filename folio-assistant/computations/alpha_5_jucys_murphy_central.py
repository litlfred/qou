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

By Murphy 1981, e_k(J_1, ..., J_n) ∈ Z(H_n(q)) — central, hence
a scalar c_k(λ) on each Wedderburn block V_λ. The scalar is

  c_k(λ) = e_k({q^{2c(□)} : □ ∈ λ})

— the elementary symmetric polynomial in q^{2·content} over the
cells of λ.

THE FUNDAMENTAL CLAIM:

  α_5 = m_e · Σ_{λ ⊢ 3A, ht(λ)=6} w_λ(q) · c_5(λ) / [3A]_q!

If atom-independent (constant across A=2, 3, 4, ...), then α_5 is
DERIVED — no AME calibration needed.

Computes for A ∈ {2, 3, 4} and tests atom-independence.
"""
from __future__ import annotations
import sys
from pathlib import Path

import sympy as sp
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


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
    """List of contents c(□) = j - i for cells (i, j) of partition shape."""
    out = []
    for r, length in enumerate(shape):
        for c in range(length):
            out.append(c - r)
    return out


def hook_lengths(shape):
    """Standard hook lengths for the partition."""
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


def q_int(n, q):
    if n == 0:
        return sp.Integer(0)
    if n < 0:
        return -q_int(-n, q)
    return sum(q ** (n - 1 - 2 * k) for k in range(n))


def q_factorial(n, q):
    res = sp.Integer(1)
    for k in range(1, n + 1):
        res = sp.expand(res * q_int(k, q))
    return res


def dim_q(shape, q):
    """q-Specht dimension via hook-length formula."""
    n = sum(shape)
    num = q_factorial(n, q)
    den = sp.Integer(1)
    for h in hook_lengths(shape):
        den = sp.expand(den * q_int(h, q))
    return sp.cancel(num / den)


def w_lambda(shape, q):
    """Wedderburn weight w_λ = (dim_q λ)² / [n]_q!."""
    n = sum(shape)
    return sp.cancel(dim_q(shape, q) ** 2 / q_factorial(n, q))


def e5_central(shape, q):
    """5th elementary symmetric polynomial in {q^{2c(□)} : □ ∈ λ}."""
    cells = cell_contents(shape)
    if len(cells) < 5:
        return sp.Integer(0)
    eigenvalues = [q ** (2 * c) for c in cells]
    # e_5 = Σ over 5-element subsets, product
    total = sp.Integer(0)
    for subset in combinations(eigenvalues, 5):
        prod = sp.Integer(1)
        for v in subset:
            prod = prod * v
        total = total + prod
    return sp.expand(total)


def height(shape):
    return len(shape)


def alpha_5_at_A(A, q):
    """Compute α_5(A) := Σ_{λ ⊢ 3A, ht(λ) = 6} w_λ · e_5_central(λ).

    (Without the m_e and 1/[3A]_q! prefactors — those are A-independent
    in the comparison, so the atom-independence test is on the
    weighted sum alone.)
    """
    n = 3 * A
    total = sp.Integer(0)
    contributions = []
    for shape in partitions_of(n):
        if height(shape) != 6:
            continue
        w = w_lambda(shape, q)
        c5 = e5_central(shape, q)
        prod = sp.cancel(w * c5)
        total = sp.expand(total + prod)
        contributions.append({
            "shape": list(shape),
            "f_lambda_classical": int(_f_lambda(shape)),
            "c_5_at_q1": float(c5.subs(q, 1)),
        })
    return sp.cancel(total), contributions


def _f_lambda(shape):
    """Classical Specht dimension f^λ via hook formula."""
    n = sum(shape)
    fact = sp.factorial(n)
    den = sp.Integer(1)
    for h in hook_lengths(shape):
        den = den * h
    return fact // den


def main() -> int:
    q = sp.Symbol("q", positive=True)
    q_0 = sp.Float(Q_50_DIGIT_STR, 50)

    print("α_5 derivation via Jucys–Murphy central elements")
    print(f"  q_0 ≈ {float(q_0):.10f}")
    print()

    wb = (
        WitnessBuilder("alpha-5-jucys-murphy-central", engine="sympy")
        .set_description(
            "α_5 derivation probe via the Jucys–Murphy central element "
            "P_5 := e_5(J_1, ..., J_n) restricted to height-6 partitions. "
            "By Murphy 1981, e_5(J_1..J_n) ∈ Z(H_n(q)) — central — so "
            "α_5(A) := Σ_{λ ⊢ 3A, ht=6} w_λ · c_5(λ) is computable as a "
            "finite combinatorial sum in q-rationals.  Tests "
            "atom-independence across A = 2..4: if constant, α_5 is "
            "DERIVED."
        )
        .set_content_block("prop:term7-shell-correction")
        .add_parameter("q_0", str(q_0))
        .add_parameter("alpha_5_AME_fit_MeV", -4.2e5)
    )

    results = {}
    for A in [2, 3, 4]:
        print(f"=== A = {A} (n = {3*A}) ===")
        alpha_5, contribs = alpha_5_at_A(A, q)
        # Numerical at q_0
        alpha_5_num = float(alpha_5.subs(q, q_0))
        # At q = 1 (classical / crystal limit pull-back)
        try:
            alpha_5_q1 = float(sp.limit(alpha_5, q, 1))
        except Exception:
            alpha_5_q1 = None

        print(f"  # height-6 partitions: {len(contribs)}")
        print(f"  α_5(A={A}) at q_0 ≈ {alpha_5_num:.6e}")
        print(f"  α_5(A={A}) at q→1 ≈ {alpha_5_q1}")

        # Show top 3 contributions per partition
        for c in contribs[:3]:
            print(f"    λ = {tuple(c['shape'])}, f^λ_classical = {c['f_lambda_classical']}, "
                  f"c_5(λ)|_{{q=1}} = {c['c_5_at_q1']}")

        results[A] = {
            "alpha_5_at_q0": alpha_5_num,
            "alpha_5_at_q1": alpha_5_q1,
            "n_height_6_partitions": len(contribs),
            "contributions": contribs,
        }

    # Atom-independence test
    print()
    print("Atom-independence test:")
    if len(results) >= 2:
        vals_q0 = [results[A]["alpha_5_at_q0"] for A in [2, 3, 4]]
        spread = max(vals_q0) - min(vals_q0)
        median = sorted(vals_q0)[len(vals_q0) // 2]
        rel_spread = spread / abs(median) if median != 0 else float("inf")
        print(f"  α_5(2), α_5(3), α_5(4) at q_0:")
        for A in [2, 3, 4]:
            print(f"    A={A}: {results[A]['alpha_5_at_q0']:+.6e}")
        print(f"  Range: {spread:.4e}, median: {median:.4e}")
        print(f"  Relative spread: {rel_spread:.4f} ({rel_spread*100:.1f}%)")

        wb.add_assertion(
            "alpha_5_atom_independent",
            float(rel_spread),
            0.0,
            tolerance=0.05,
        )

        if rel_spread < 0.01:
            verdict = "atom-independent (α_5 derived)"
        elif rel_spread < 0.10:
            verdict = "weakly atom-dependent (curvature in connection)"
        else:
            verdict = "strongly atom-dependent (mechanism orthogonal to JM-central)"
        print(f"\nVERDICT: {verdict}")

    wb.add_data("results", results)
    wb.add_data("verdict", verdict if 'verdict' in dir() else "single_atom_only")
    out_path = wb.save()
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
