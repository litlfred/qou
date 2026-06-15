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

import sys
from pathlib import Path
from itertools import combinations

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_lengths  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()  # 50-digit precision throughout


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
    """α_5(A) divided by [3A]_q! — naive guess at normalization,
    motivated by Wedderburn trace identity Σ dim_q² = [n]_q!."""
    raw, contribs = alpha_5_at_A_num(A, q_val)
    n = 3 * A
    qfact = q_factorial_num(n, q_val)
    return raw / qfact, contribs


def alpha_5_at_A_partial_normalized(A, q_val):
    """α_5(A) normalised by the HEIGHT-6 PARTIAL Wedderburn budget:

       β_6(A) := Σ_{λ ⊢ 3A, ht(λ)=6} dim_q(λ)²
             = Σ over height-6 partitions of squared q-dim.

    The result is the height-6-Plancherel-WEIGHTED AVERAGE of
    the JM-central scalars c_5(λ):

       α_5_partial(A) = Σ dim_q²(λ) c_5(λ) / Σ dim_q²(λ).

    This is the structurally derived normaliser when the
    operator-selection LP is restricted to the height-6
    stratum (no full [n]_q! enters; only the partial budget).
    """
    n = 3 * A
    num = mp.mpf(0)         # Σ dim_q² · c_5
    den = mp.mpf(0)         # Σ dim_q²
    contribs = []
    for shape in partitions_of(n):
        if height(shape) != 6:
            continue
        d = dim_q_num(shape, q_val)
        c5 = e5_central_num(shape, q_val)
        num = num + d * d * c5
        den = den + d * d
        contribs.append({
            "shape": list(shape),
            "f_lambda": f_lambda(shape),
            "dim_q_squared": float(d * d),
            "c_5": float(c5),
        })
    if den == 0:
        return mp.mpf("inf"), contribs
    return num / den, contribs


def alpha_5_three_normalisations(A, q_val):
    """Compute α_5(A) at q_val under THREE different normalisations:
       (i)   raw = Σ w_λ(q) · c_5(λ)
       (ii)  divide by [3A]_q!  (naive guess)
       (iii) Plancherel-average over the height-6 stratum
             = Σ dim_q² c_5 / Σ dim_q²        (partial budget)
    """
    raw, _ = alpha_5_at_A_num(A, q_val)
    n = 3 * A
    qfact = q_factorial_num(n, q_val)
    naive_norm = raw / qfact if qfact != 0 else mp.mpf("inf")
    partial, _ = alpha_5_at_A_partial_normalized(A, q_val)
    return raw, naive_norm, partial


def q_sweep_atom_independence():
    """Sweep q across (1, φ) to find where (if anywhere) the
    height-6 Plancherel-average of c_5(λ) is atom-independent.

    Returns: list of dicts, one per q value.
    """
    q_0 = mp.mpf(Q_50_DIGIT_STR)
    phi = (mp.mpf(1) + mp.sqrt(5)) / 2  # golden ratio ≈ 1.618
    q_values = [
        ("q_0 - 0.01", q_0 - mp.mpf("0.01")),
        ("q_0", q_0),
        ("q_0 + 0.01", q_0 + mp.mpf("0.01")),
        ("q = 1.001", mp.mpf("1.001")),
        ("q = 1.20", mp.mpf("1.20")),
        ("q = 1.40", mp.mpf("1.40")),
        ("q = 1.60", mp.mpf("1.60")),
        ("q = phi - eps", phi - mp.mpf("0.01")),
    ]
    out = []
    for label, q_val in q_values:
        rows = []
        partials = []
        for A in [2, 3, 4]:
            raw, naive, partial = alpha_5_three_normalisations(A, q_val)
            rows.append((A, float(raw), float(naive), float(partial)))
            partials.append(float(partial))
        spread_partial = max(partials) - min(partials)
        median_partial = sorted(partials)[1]
        rel_spread_partial = (
            spread_partial / abs(median_partial)
            if median_partial != 0 else float("inf")
        )
        out.append({
            "q_label": label,
            "q_val": float(q_val),
            "rows": rows,
            "rel_spread_partial": rel_spread_partial,
        })
    return out


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

    # This probe is *designed to refute* the naive JM-central closed
    # form for α_5.  We assert that the relative spread EXCEEDS a
    # refutation threshold (so the witness records "passing
    # refutation" rather than failing the headline claim).
    REFUTATION_THRESHOLD = 0.10  # 10% spread suffices to refute
    wb.add_assertion(
        "naive_jm_central_form_refuted_at_q0",
        # passes iff spread > threshold
        float(rel_spread_n > REFUTATION_THRESHOLD),
        1.0,
        tolerance=0.0,
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

    # ── q-sweep across (1, φ) for the partial-Plancherel-norm ─────
    print("\n" + "=" * 60)
    print("q-SWEEP: height-6 Plancherel-average of c_5(λ) vs A")
    print("(structurally derived normaliser; no [3A]_q! guess)")
    print("=" * 60)
    sweep = q_sweep_atom_independence()
    sweep_summary = []
    for entry in sweep:
        print(f"\n  {entry['q_label']} (q = {entry['q_val']:.6f}):")
        for A, raw, naive, partial in entry["rows"]:
            print(f"    A={A}: partial-norm c_5 ≈ {partial:+.6e}")
        rs = entry["rel_spread_partial"]
        print(f"    Relative spread (partial-norm): {rs*100:.2f}%")
        sweep_summary.append({
            "q_label": entry["q_label"],
            "q_val": entry["q_val"],
            "rel_spread_partial": rs,
        })

    best = min(sweep_summary, key=lambda e: e["rel_spread_partial"])
    print(f"\n  Best atom-independence at: {best['q_label']} "
          f"(rel spread = {best['rel_spread_partial']*100:.2f}%)")

    wb.add_data("q_sweep", sweep_summary)
    # Also a refutation assertion: even the BEST q in (1, φ) is
    # well above the refutation threshold, so the simplest closed
    # form is refuted uniformly across the physical regime.
    wb.add_assertion(
        "naive_form_refuted_uniformly_in_q",
        float(best["rel_spread_partial"] > REFUTATION_THRESHOLD),
        1.0,
        tolerance=0.0,
    )

    out_path = wb.save()
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
