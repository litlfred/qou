#!/usr/bin/env python3
"""Option B probe — H₃ ⊂ H₄ Bratteli induction-restriction test for
deriving the Family-A linking_weight `(3q²+4+3q⁻²)/4`.

Executes the §4 plan in
[`docs/audits/2026-06-04-option-b-h3-h4-bratteli-scoping.md`](../../docs/audits/2026-06-04-option-b-h3-h4-bratteli-scoping.md).

Three sub-hypotheses:

  B1 (uniform). λ_A(q) ?= (1/k) · Σ_{λ⊢3} Σ_{λ⁺⊃λ} dim_q(V_{λ⁺})
       for some constant k. The inner sum is the box-adding diagram
       from H₃ to H₄; the outer sum is over the 3 partitions of 3.
       Tests whether the unweighted box-adding sum from H₃ recovers
       λ_A in any constant ratio.

  B2 (y_λ-weighted). λ_A(q₀) ?= Σ_{λ⊢3} y_λ(q₀) · Σ_{λ⁺⊃λ} dim_q₀(V_{λ⁺}).
       Same box-adding, weighted by the canonical Wenzl-bridge y_λ
       at q₀. The y_λ values for n=3 are loaded from the canonical
       50-dps `y-lambda-at-q0.witness.json`. Tests the Markov-trace
       weighted induction.

  B3 (per-source λ). λ_A(q) ?= (1/k) · Σ_{λ⁺⊃λ_special} dim_q(V_{λ⁺})
       for any single λ_special ⊢ 3. Tests whether one λ⊢3 carries
       the whole sum (i.e. the box-adding induction is from a single
       source, not summed over all 3).

The dim_q is the q-Hecke Wedderburn dimension via the q-hook formula:
  dim_q(V_λ) = [n]_q! / Π_{x∈λ} [h(x)]_q
where [n]_q = (q^n − q^{−n}) / (q − q^{−1}) is the symmetric q-number.

EXPLORATORY — no production code, no Δ_λ-gate ansatz (box-adding is
structural, not a per-partition fit). Witness records the verdict per
sub-hypothesis and the explicit residual polynomial when REFUTED.
"""
from __future__ import annotations

# Path bridge — same pattern as the other probes/ scripts.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import json
from pathlib import Path

# Single path-bridging approach: `_path_bridge` (imported above) puts
# computations/ and every cluster subdir on sys.path, so `_precision`
# and `witness_base` resolve without a second probes/-local insert
# (Copilot review, PR #1841 — consolidated the duplicate mutation).

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402


HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

# Canonical 50-dps q₀ anchor — matches every chi-cache witness header.
Q_0_50DPS = "1.1099785827513808075916690956107688798744991218736"


# ── §1. Young-diagram box-adding (Bratteli induction H_n → H_{n+1}) ──


def partitions_of(n: int) -> list[tuple[int, ...]]:
    """Return partitions of n in descending-parts tuple form."""
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, acc: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(acc))
            return
        for p in range(min(remaining, max_part), 0, -1):
            rec(remaining - p, p, acc + [p])

    rec(n, n, [])
    return out


def outer_corners(lam: tuple[int, ...]) -> list[tuple[int, ...]]:
    """All partitions obtained by adding one box to λ (i.e. all λ⁺ ⊃ λ
    with |λ⁺| = |λ| + 1).

    The legal cells to add are (a) extending an existing row (i, len(lam[i]))
    when row i+1 is strictly shorter, and (b) starting a new row at
    position (len(lam), 0).  Equivalently: a box can be added to row i
    iff i = 0 or lam[i-1] > lam[i] (then-current) or i == len(lam).
    """
    out: list[tuple[int, ...]] = []
    parts = list(lam)
    # Try extending each existing row.
    for i in range(len(parts)):
        if i == 0 or parts[i - 1] > parts[i]:
            new_parts = parts.copy()
            new_parts[i] += 1
            out.append(tuple(new_parts))
    # Try starting a new bottom row of length 1.
    if not parts or parts[-1] >= 1:
        out.append(tuple(parts + [1]))
    return out


# ── §2. q-Hecke Wedderburn dimension via the q-hook formula ──


def hook_lengths(lam: tuple[int, ...]) -> list[int]:
    """Hook lengths of all cells of the Young diagram `lam`."""
    hooks: list[int] = []
    L = len(lam)
    for i in range(L):
        for j in range(lam[i]):
            arm = lam[i] - 1 - j  # cells to the right in same row
            leg = 0
            for k in range(i + 1, L):
                if lam[k] > j:
                    leg += 1
                else:
                    break
            hooks.append(arm + leg + 1)
    return hooks


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    """Symmetric q-number [n]_q = (q^n − q^{−n}) / (q − q^{−1}).

    Returns a Laurent polynomial in q (rationalised so the denominator
    cancels exactly).  For n=0 returns 0.
    """
    if n == 0:
        return sp.Integer(0)
    # (q^n − q^{−n}) / (q − q^{−1}) =
    #   q^{−(n−1)} · (q^{2n} − 1) / (q² − 1) =
    #   q^{−(n−1)} · (1 + q² + q⁴ + … + q^{2(n−1)})
    return sum(q ** (2 * k - (n - 1)) for k in range(n))


def q_factorial_sym(n: int, q: sp.Expr) -> sp.Expr:
    """[n]_q! = [n]_q · [n−1]_q · … · [1]_q."""
    out = sp.Integer(1)
    for k in range(1, n + 1):
        out = sp.expand(out * q_number_sym(k, q))
    return out


def dim_q_sym(lam: tuple[int, ...], q: sp.Expr) -> sp.Expr:
    """q-Hecke Wedderburn dimension via the q-hook formula:

        dim_q(V_λ) = [n]_q! / ∏_{x ∈ λ} [h(x)]_q.
    """
    n = sum(lam)
    num = q_factorial_sym(n, q)
    den = sp.Integer(1)
    for h in hook_lengths(lam):
        den = sp.expand(den * q_number_sym(h, q))
    return sp.cancel(num / den)


# ── §3. Target — Family-A linking_weight (3q² + 4 + 3q⁻²)/4 ──


def linking_weight_family_a_sym(q: sp.Expr) -> sp.Expr:
    """Reproduce the production `linking_weight_family_a(q)` =
    (3q² + 4 + 3q⁻²) / 4 symbolically."""
    return (3 * q ** 2 + 4 + 3 * q ** (-2)) / 4


# ── §4. Sub-hypothesis tests ──


def b1_uniform_inducted_sum_sym(q: sp.Expr) -> sp.Expr:
    """B1: Σ_{λ⊢3} Σ_{λ⁺⊃λ} dim_q(V_{λ⁺}) — unweighted box-adding sum."""
    total = sp.Integer(0)
    for lam in partitions_of(3):
        for lam_plus in outer_corners(lam):
            total = sp.expand(total + dim_q_sym(lam_plus, q))
    return sp.cancel(total)


def b1_verdict(q: sp.Expr) -> dict:
    """B1: does (1/k)·S_B1(q) = λ_A(q) for some constant k?

    Computes S_B1 symbolically, compares the ratio S_B1 / λ_A — if it
    simplifies to a rational constant in q, B1 SUPPORTS; otherwise
    REFUTED with the explicit residual recorded.
    """
    s_b1 = b1_uniform_inducted_sum_sym(q)
    lam_a = linking_weight_family_a_sym(q)
    ratio = sp.cancel(s_b1 / lam_a)
    # If ratio is constant (free of q), then SUPPORTS with k = 1/ratio.
    if sp.diff(ratio, q) == 0:
        return {
            "hypothesis": "B1 (uniform)",
            "verdict": "EXACT-MATCH",
            "constant_ratio_k_inv": str(ratio),
            "s_b1_sym": str(sp.expand(s_b1)),
            "lambda_A_sym": str(sp.expand(lam_a)),
        }
    # Otherwise REFUTED; record residual = S_B1 − k·λ_A for the k that
    # matches at q=1. Keep everything EXACT (SymPy Rational) so the
    # residual reads as e.g. q²/5 − 2/5 + 1/(5q²) rather than the
    # float artefact 0.199999…·q² − 0.4 + … (Copilot review, PR #1841).
    s_at_1 = sp.cancel(s_b1.subs(q, 1))
    lam_at_1 = sp.cancel(lam_a.subs(q, 1))
    k = sp.cancel(s_at_1 / lam_at_1)
    residual = sp.expand(s_b1 - k * lam_a)
    return {
        "hypothesis": "B1 (uniform)",
        "verdict": "REFUTED",
        "s_b1_sym": str(sp.expand(s_b1)),
        "lambda_A_sym": str(sp.expand(lam_a)),
        "s_b1_at_q1": str(s_at_1),
        "lambda_A_at_q1": str(lam_at_1),
        "k_at_q1": str(k),
        "residual_S_minus_k_lambdaA_sym": str(residual),
        "note": (
            "S_B1 / λ_A is q-dependent — no constant rescaling reproduces "
            "λ_A.  Uniform box-adding from H₃ does NOT recover the "
            "Family-A linking_weight."
        ),
    }


def _load_y_lambda_n(n: int) -> dict[tuple, mp.mpf]:
    """Load y_λ(q_0) for partitions of `n` from y-lambda-at-q0."""
    path = COMPUTE_DIR / "y-lambda-at-q0.witness.json"
    raw = json.loads(path.read_text())["data"]["by_n"]
    return {
        tuple(row["partition"]): mp.mpf(row["y_at_q0_50dps"])
        for row in raw[str(n)]
    }


def b2_verdict(q_0: mp.mpf) -> dict:
    """B2: y_λ(q_0)-weighted inducted sum at q_0.

    Computes Σ_{λ⊢3} y_λ(q_0) · Σ_{λ⁺⊃λ} dim_q₀(V_{λ⁺}) numerically
    at q_0, compares to λ_A(q_0).
    """
    y_lams = _load_y_lambda_n(3)
    # B2's verdict depends on having ALL λ⊢3 weights; a silent default
    # of 0 for a missing partition would produce a wrong weighted sum
    # with no failure signal (Copilot review, PR #1841). Fail fast.
    missing_y = [list(lam) for lam in partitions_of(3) if lam not in y_lams]
    if missing_y:
        raise RuntimeError(
            f"B2 cannot run: y-lambda-at-q0 is missing n=3 weights for "
            f"partition(s) {missing_y}. Refresh the y_λ table before "
            f"trusting the B2 verdict."
        )
    # Numerical dim_q at q_0 — substitute symbolic Laurent polynomial.
    q_sym = sp.Symbol("q", positive=True)
    q_0_sp = sp.Float(str(q_0), 50)

    weighted_sum = mp.mpf(0)
    per_source_contributions: list[dict] = []
    for lam in partitions_of(3):
        y = y_lams[lam]
        box_sum_num = mp.mpf(0)
        box_terms: list[dict] = []
        for lam_plus in outer_corners(lam):
            dq_sym = dim_q_sym(lam_plus, q_sym)
            dq_at_q0 = mp.mpf(str(sp.N(dq_sym.subs(q_sym, q_0_sp), 50)))
            box_sum_num += dq_at_q0
            box_terms.append({
                "lambda_plus": list(lam_plus),
                "dim_q_at_q0": str(dq_at_q0),
            })
        weighted_contribution = y * box_sum_num
        weighted_sum += weighted_contribution
        per_source_contributions.append({
            "lambda": list(lam),
            "y_lambda_at_q0": str(y),
            "box_addition_sum": str(box_sum_num),
            "weighted_contribution": str(weighted_contribution),
            "box_additions": box_terms,
        })

    # λ_A at q_0.
    q_sym2 = sp.Symbol("q", positive=True)
    lam_a_sym = linking_weight_family_a_sym(q_sym2)
    lam_a_at_q0 = mp.mpf(
        str(sp.N(lam_a_sym.subs(q_sym2, q_0_sp), 50))
    )
    delta = weighted_sum - lam_a_at_q0
    rel_err = abs(delta) / abs(lam_a_at_q0)

    if rel_err < mp.mpf("1e-40"):
        verdict = "EXACT-MATCH"
    elif rel_err < mp.mpf("1e-3"):
        verdict = "NEAR-MATCH (< 0.1 %)"
    elif rel_err < mp.mpf("1e-1"):
        verdict = "NEAR-MATCH (< 10 %)"
    else:
        verdict = "REFUTED"

    return {
        "hypothesis": "B2 (y_λ-weighted at q_0)",
        "verdict": verdict,
        "weighted_sum_at_q0": str(weighted_sum),
        "lambda_A_at_q0": str(lam_a_at_q0),
        "delta": str(delta),
        "relative_error": str(rel_err),
        "per_source": per_source_contributions,
    }


def b3_verdict(q: sp.Expr) -> dict:
    """B3: per-source λ — does any single λ⊢3 give a constant rescaling
    of λ_A from its box-additions alone?"""
    lam_a = linking_weight_family_a_sym(q)
    per_source: list[dict] = []
    any_match = False
    for lam in partitions_of(3):
        s_lam = sp.Integer(0)
        for lam_plus in outer_corners(lam):
            s_lam = sp.expand(s_lam + dim_q_sym(lam_plus, q))
        s_lam = sp.cancel(s_lam)
        ratio = sp.cancel(s_lam / lam_a)
        if sp.diff(ratio, q) == 0:
            any_match = True
            per_source.append({
                "lambda": list(lam),
                "verdict_for_source": "EXACT-MATCH",
                "s_lambda_sym": str(s_lam),
                "constant_ratio_k_inv": str(ratio),
            })
        else:
            # Exact SymPy throughout (matches b1_verdict; no float
            # downcast — Copilot review, PR #1841).
            s_at_1 = sp.cancel(s_lam.subs(q, 1))
            lam_at_1 = sp.cancel(lam_a.subs(q, 1))
            per_source.append({
                "lambda": list(lam),
                "verdict_for_source": "REFUTED",
                "s_lambda_sym": str(sp.expand(s_lam)),
                "s_at_q1": str(s_at_1),
                "lambda_A_at_q1": str(lam_at_1),
                "k_at_q1": str(sp.cancel(s_at_1 / lam_at_1)),
            })
    return {
        "hypothesis": "B3 (per-source λ)",
        "verdict": "EXACT-MATCH" if any_match else "REFUTED",
        "per_source": per_source,
        "note": (
            "No single λ⊢3 reproduces λ_A under any constant rescaling."
            if not any_match
            else "At least one λ⊢3 gives a constant rescaling of λ_A."
        ),
    }


def main() -> int:
    w = WitnessBuilder("option-b-h3-h4-bratteli-probe", engine="sympy+mpmath")
    w.set_audit_only("docs/audits/2026-06-04-option-b-h3-h4-bratteli-scoping.md")
    w.set_description(
        "Option B probe (PR #1762 §5 / sibling #1816 Option A): H₃ ⊂ H₄ "
        "Bratteli induction-restriction test for deriving Family-A "
        "linking_weight (3q²+4+3q⁻²)/4. Three sub-hypotheses (B1 "
        "uniform / B2 y_λ-weighted / B3 per-source λ) tested "
        "symbolically in q (B1, B3) and numerically at q_0 (B2) "
        "against the production closed-form. EXPLORATORY — no "
        "production code, content blocks, or witnesses changed."
    )

    print("=" * 78)
    print("Option B probe — H₃ ⊂ H₄ Bratteli induction-restriction")
    print("=" * 78)

    # ── Setup ──
    q = sp.Symbol("q", positive=True)
    q_0 = mp.mpf(Q_0_50DPS)

    # ── Bratteli structure summary ──
    parts3 = partitions_of(3)
    parts4 = partitions_of(4)
    box_additions: list[dict] = []
    for lam in parts3:
        for lam_plus in outer_corners(lam):
            box_additions.append({
                "lambda": list(lam),
                "lambda_plus": list(lam_plus),
            })
    print(f"\n  Partitions of 3: {parts3}")
    print(f"  Partitions of 4: {parts4}")
    print(f"  Box additions H₃ → H₄: {len(box_additions)} edges")
    print(f"  (Expect 7 — matches §2 of the scoping doc)")

    w.add_data("bratteli_structure", {
        "partitions_of_3": [list(p) for p in parts3],
        "partitions_of_4": [list(p) for p in parts4],
        "box_additions_count": len(box_additions),
        "box_additions": box_additions,
    })

    # Enforce the structural sanity check (was print-only): 7 box
    # additions from the 3 partitions of 3 to the 5 partitions of 4.
    # A regression in outer_corners() or partitions_of() now surfaces
    # as a failed assertion, not just a console line (Copilot review,
    # PR #1841).
    w.add_assertion(
        "h3_h4_box_additions_count_is_7",
        computed=len(box_additions),
        expected=7,
        tolerance=0,
    )

    # ── Sanity: target closed-form at q=1 ──
    lam_a = linking_weight_family_a_sym(q)
    print(f"\n  λ_A(q) = (3q²+4+3q⁻²)/4")
    print(f"  λ_A(1) = {float(lam_a.subs(q, 1))}  (expect 5/2 = 2.5)")
    print(f"  λ_A(q₀) ≈ {float(sp.N(lam_a.subs(q, sp.Float(str(q_0), 30)), 30)):.6f}")

    # ── Sanity: Σ_{λ⊢4} dim_q(V_λ) should be 3q² + 4 + 3q⁻² ──
    sigma_4 = sp.Integer(0)
    for lam in parts4:
        sigma_4 = sp.expand(sigma_4 + dim_q_sym(lam, q))
    sigma_4 = sp.cancel(sigma_4)
    expected_sigma_4 = 3 * q ** 2 + 4 + 3 * q ** (-2)
    delta_sigma_4 = sp.simplify(sp.cancel(sigma_4 - expected_sigma_4))
    print(
        f"\n  Σ_{{λ⊢4}} dim_q(V_λ) = {sp.expand(sigma_4)}  "
        f"(expected 3q²+4+3q⁻²; Δ = {delta_sigma_4})"
    )
    w.add_assertion(
        "sigma_over_4_matches_3q2_plus_4_plus_3qinv2",
        computed=float(sp.N(sigma_4.subs(q, 1), 20)),
        expected=10.0,
        tolerance=1e-12,
    )

    # ── B1, B2, B3 ──
    b1 = b1_verdict(q)
    b2 = b2_verdict(q_0)
    b3 = b3_verdict(q)
    print("\n" + "-" * 78)
    print(f"  B1 (uniform):      {b1['verdict']}")
    if b1["verdict"] == "REFUTED":
        # k_at_q1 is now an exact SymPy Rational string (e.g. "32/5").
        print(f"      S_B1(q=1)={b1['s_b1_at_q1']}  k(q=1)={b1['k_at_q1']}")
        print(f"      residual: {b1['residual_S_minus_k_lambdaA_sym']}")
    print(f"  B2 (y_λ-weighted): {b2['verdict']}")
    print(
        f"      Σ y_λ·(Σ dim_q) at q₀ = {float(mp.mpf(b2['weighted_sum_at_q0'])):.6f}  "
        f"vs λ_A(q₀) = {float(mp.mpf(b2['lambda_A_at_q0'])):.6f}  "
        f"rel err = {float(mp.mpf(b2['relative_error'])):.3e}"
    )
    print(f"  B3 (per-source λ): {b3['verdict']}")
    for src in b3["per_source"]:
        print(
            f"      λ={src['lambda']}  → {src['verdict_for_source']}"
            + (f"  k(q=1)={src['k_at_q1']}"
               if src["verdict_for_source"] == "REFUTED" else "")
        )
    print("-" * 78)

    w.add_data("b1_uniform", b1)
    w.add_data("b2_y_lambda_weighted", b2)
    w.add_data("b3_per_source_lambda", b3)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data(
        "scoping_doc",
        "docs/audits/2026-06-04-option-b-h3-h4-bratteli-scoping.md",
    )

    # ── Final verdict synthesis ──
    matches = [
        b1["verdict"] == "EXACT-MATCH",
        "MATCH" in b2["verdict"],
        b3["verdict"] == "EXACT-MATCH",
    ]
    if any(matches):
        synthesis = (
            "At least one sub-hypothesis recovers Family-A linking_weight "
            "from the H₃ Bratteli induction step — H₃→H₄ jump derivable."
        )
    else:
        synthesis = (
            "All three sub-hypotheses REFUTED at the closed-form level. "
            "The box-adding Bratteli induction axis does not derive the "
            "Family-A linking_weight by any of {uniform, y_λ-weighted, "
            "per-source}. The H₃→H₄ jump must come from a different "
            "structural mechanism (e.g. Markov-stabilization analog at "
            "the trace level, not the algebra-tower level — PR #1808 "
            "Option E literature-import flagged this as the next axis)."
        )
    w.add_data("synthesis_verdict", synthesis)
    print(f"\n  SYNTHESIS:")
    for line in synthesis.split(". "):
        print(f"    {line.strip()}")

    out_path = w.save()
    repo_root = COMPUTE_DIR.parent.parent
    try:
        rel = out_path.relative_to(repo_root)
    except ValueError:
        rel = out_path
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
