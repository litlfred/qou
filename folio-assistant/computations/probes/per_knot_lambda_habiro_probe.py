"""Per-knot λ(K) via the Habiro element — first computational step of the
§6.8 experiment in
[`docs/audits/2026-06-03-1ppq-roadmap-reanalysis-and-geom-full-bridge-gap.md`].

GOAL (the Geom_full bridge derivation gap).  Production uses
`linking_weight_family_a(q) = (1/4)·Σ_{λ⊢4} dim_q(V_λ) = 5/2 + (3/4)h²`
as the proton's mass-formula multiplier — even though the proton braid
lives in H_3, not H_4.  The lit review (G-S-W-Z 2024, arXiv:2412.04241)
says the canonical per-knot object is a **Habiro-ring element Φ_K(h)**
whose perturbative expansion around q=1 should reproduce Family-A as its
leading terms, with the higher h^{2k} coefficients fixed by the K_3(K)
grading (rigid — no fit).

This probe does the parts that are **computable inside the framework
right now** (no external G-Z tables, no SnapPy) and HONESTLY marks the
parts that need external data:

  Part 1 — verify the Family-A identity symbolically (sympy):
           (1/4)·Σ_{λ⊢4} dim_q(V_λ) ?= 5/2 + (3/4)h².
  Part 2 — map the Σ_{λ⊢n} dim_q(V_λ) family for n=3..6, expressed in
           h = q − q⁻¹, as the candidate "comparison target" for Φ_K.
  Part 3 — the figure-eight (4_1 = muon, linking_weight = 1) Habiro
           element J(4_1) = Σ_n (q;q)_n (q⁻¹;q⁻¹)_n at the REAL anchor
           q₀ ≈ 1.110: demonstrate that the NAIVE series DIVERGES
           (same q>1 q-Pochhammer growth that killed the α_r ansatz),
           so the framework's FINITE 5/2 + (3/4)h² must be the
           PERTURBATIVE / asymptotic series, not the convergent Habiro
           sum.  This is the key structural distinction.
  Part 4 — honest gap statement: what external data (Garoufalidis–Zagier
           Φ_K perturbative coefficients) is needed to finish §6.8.

ZERO fit.  All numbers are either symbolic identities or AME/CODATA
comparisons.  EXPLORATORY per production-vs-exploratory-discipline:
touches no production compute path.

q-usage discipline (CLAUDE.md §7c, §q-usage).  q₀ ≈ 1.110 is the real
archimedean substrate anchor (Im = 0).  The Habiro element is a FIBRE-
level object (formal q); its perturbative h-series has real coefficients
that get evaluated at the real q₀.  We compute the fibre-level series
symbolically and only realise at q₀ (real) — never at |q| = 1.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401, E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


# ── Symbolic q-dimension machinery (sympy, symmetric q-integers) ──────

def _partitions(n: int) -> list[tuple[int, ...]]:
    """All partitions of n, descending parts."""
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, maxpart: int, acc: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(acc))
            return
        for p in range(min(remaining, maxpart), 0, -1):
            rec(remaining - p, p, acc + [p])

    rec(n, n, [])
    return out


def _q_int_sym(k: int, q: sp.Symbol) -> sp.Expr:
    """Symmetric q-integer [k]_q = (q^k − q^{-k})/(q − q^{-1}).

    Invariant under q ↦ q^{-1} — this is why every Σ dim_q below is a
    symmetric Laurent polynomial (a polynomial in h² = (q−q⁻¹)²).
    """
    if k == 0:
        return sp.Integer(0)
    return (q**k - q**(-k)) / (q - q**(-1))


def _q_factorial_sym(n: int, q: sp.Symbol) -> sp.Expr:
    out = sp.Integer(1)
    for k in range(1, n + 1):
        out *= _q_int_sym(k, q)
    return sp.together(out)


def _q_hook_product_sym(lam: tuple[int, ...], q: sp.Symbol) -> sp.Expr:
    """∏_{x∈λ} [hook_x]_q (symmetric)."""
    width = lam[0]
    conj = [sum(1 for p in lam if p > j) for j in range(width)]
    H = sp.Integer(1)
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = conj[j] - i - 1
            H *= _q_int_sym(arm + leg + 1, q)
    return sp.together(H)


def _q_dimension_sym(lam: tuple[int, ...], q: sp.Symbol) -> sp.Expr:
    """d_q(λ) = [n]_q! / H_q(λ), simplified to a Laurent polynomial."""
    n = sum(lam)
    if n == 0:
        return sp.Integer(1)
    d = sp.cancel(_q_factorial_sym(n, q) / _q_hook_product_sym(lam, q))
    return d


def part1_verify_family_a() -> dict:
    """(1/4)·Σ_{λ⊢4} dim_q(V_λ) ?= 5/2 + (3/4)h²."""
    q, h = sp.symbols("q h", positive=True)
    parts4 = _partitions(4)
    dims = {lam: _q_dimension_sym(lam, q) for lam in parts4}
    total = sp.cancel(sum(dims.values()))
    lw = sp.cancel(total / 4)
    # Family-A claim in q: (3q² + 4 + 3q⁻²)/4
    claim_q = (3 * q**2 + 4 + 3 * q**(-2)) / 4
    diff = sp.simplify(lw - claim_q)
    # Also express as 5/2 + (3/4)h² with h = q - 1/q:
    lw_in_h = sp.simplify(lw.subs(q, (h + sp.sqrt(h**2 + 4)) / 2))
    family_a_h = sp.Rational(5, 2) + sp.Rational(3, 4) * h**2
    diff_h = sp.simplify(lw_in_h - family_a_h)
    return {
        "partitions_of_4": [list(p) for p in parts4],
        "q_dimensions": {str(list(k)): str(v) for k, v in dims.items()},
        "sum_dim_q": str(total),
        "linking_weight_(1/4)sum": str(sp.simplify(lw)),
        "family_a_claim_q": str(sp.simplify(claim_q)),
        "diff_vs_claim_q": str(diff),
        "matches_q_form": diff == 0,
        "family_a_in_h": "5/2 + (3/4)h^2",
        "diff_vs_h_form": str(diff_h),
        "matches_h_form": diff_h == 0,
    }


def part2_map_dim_q_family() -> dict:
    """Σ_{λ⊢n} dim_q(V_λ) for n=3..6, in h, and various normalizations."""
    q, h = sp.symbols("q h", positive=True)
    rows = []
    for n in (3, 4, 5, 6):
        parts = _partitions(n)
        total = sp.cancel(sum(_q_dimension_sym(lam, q) for lam in parts))
        # classical dim sum (q→1) = number of SYT = Σ (f^λ); for the
        # FULL sum of dims it's Σ d_λ, the dimension of the regular-ish
        # rep restricted... just evaluate at q=1.
        total_at_1 = sp.simplify(sp.limit(total, q, 1))
        # express in h via the x = log q series
        x = sp.symbols("x", real=True)
        ser = sp.series(sp.simplify(total).subs(q, sp.exp(x)),
                        x, 0, 8).removeO()
        ser = sp.expand(ser)
        # h² = 4 sinh²(x) = 4x² + (4/3)x⁴ + ... ; invert to get poly in h²
        # leading: total = a0 + a1·x² + ... ; a0 = total_at_1
        a0 = sp.simplify(total_at_1)
        # coefficient of x² in ser:
        c_x2 = ser.coeff(x, 2)
        # h² = 4x² + O(x⁴) ⇒ x² = h²/4 + O(h⁴) ⇒ coeff of h² ≈ c_x2/4
        h2_coeff_leading = sp.simplify(c_x2 / 4)
        rows.append({
            "n": n,
            "n_partitions": len(parts),
            "sum_dim_q_at_q1": str(a0),
            "(1/n)·sum_at_q1": str(sp.nsimplify(a0 / n)),
            "leading_h2_coeff_of_sum": str(h2_coeff_leading),
            # Normalized leading h² coeff under the selection-rule 1/(c+1)
            # = 1/n normalization (Copilot review PR #1765): for n=4 this
            # is the Family-A 3/4, NOT the raw 3 — recorded alongside the
            # raw coeff to avoid misreading the witness.
            "leading_h2_coeff_normalized_1_over_n": str(
                sp.simplify(h2_coeff_leading / n)),
            "sum_dim_q_symbolic": str(sp.simplify(total)),
        })
    return {
        "note": ("Family-A uses n=4 with normalization 1/4: "
                 "(1/4)Σ_{λ⊢4} = 5/2 + (3/4)h². The table below maps "
                 "the analogous Σ_{λ⊢n} for n=3..6 so the per-knot "
                 "selection rule (which n, which normalization) can be "
                 "compared against Φ_K once external coefficients land."),
        "rows": rows,
    }


def part3_figure_eight_habiro_at_q0(dps: int = 50) -> dict:
    """Figure-eight (4_1 = muon, linking_weight = 1) Habiro element

        J(4_1; q) = Σ_{n≥0} (q;q)_n · (q^{-1};q^{-1})_n
                  = Σ_{n≥0} ∏_{j=1}^{n} (1 − q^j)(1 − q^{-j})

    evaluated at the REAL substrate anchor q₀ ≈ 1.110.  This is the
    canonical Habiro-ring element of the figure-eight (Habiro 2008,
    Masbaum).  At a root of unity it terminates; at real q₀ > 1 we test
    naive convergence.
    """
    with mp.workdps(dps):
        q = mp.mpf(Q_50_DIGIT_STR)
        partials = []
        terms = [mp.mpf(1)]  # n=0 term = empty product = 1
        sums = [mp.mpf(1)]
        term = mp.mpf(1)
        total = mp.mpf(1)
        partials.append((0, mp.nstr(total, 14), mp.nstr(term, 14)))
        for n in range(1, 61):
            factor = (1 - q**n) * (1 - q**(-n))
            term *= factor
            total += term
            terms.append(term)
            sums.append(total)
            if n <= 14 or n % 5 == 0:
                partials.append(
                    (n, mp.nstr(total, 14), mp.nstr(term, 14)))
        # OPTIMAL TRUNCATION (asymptotic-series superasymptotics): the
        # best estimate of the Borel sum is the partial sum at the index
        # where |term_n| is minimal (just before the series starts to
        # diverge). This is the canonical "least-term" truncation.
        abs_terms = [abs(t) for t in terms]
        n_opt = min(range(len(abs_terms)), key=lambda i: abs_terms[i] if i > 0 else mp.inf)  # noqa: E501
        S_opt = sums[n_opt]
        min_term = abs_terms[n_opt]
        last_term_mag = abs_terms[-1]
        # Divergence test (Copilot review PR #1765): base it on the
        # least-term location + subsequent GROWTH rather than a fixed
        # cutoff at a fixed n, so it stays correct if q₀ or the loop
        # bound changes.  "Diverges" ⇔ the terms grow by a large factor
        # after n_opt (the asymptotic-series turnaround).
        diverges = (n_opt < len(abs_terms) - 1
                    and min_term > 0
                    and last_term_mag / min_term > mp.mpf("1e6"))
        # Compare optimally-truncated value to the muon's linking_weight=1
        lw_muon = mp.mpf(1)
        rel_to_lw1 = (S_opt - lw_muon) / lw_muon
        return {
            "knot": "4_1 (figure-eight = muon)",
            "linking_weight_target": 1,
            "habiro_element": "J(4_1;q) = Σ_n (q;q)_n (q⁻¹;q⁻¹)_n",
            "q0": mp.nstr(q, 20),
            "partial_sums_(n, S_n, term_n)": partials,
            "optimal_truncation_index": n_opt,
            "min_term_magnitude": mp.nstr(min_term, 6),
            "S_optimal_truncation": mp.nstr(S_opt, 20),
            "muon_linking_weight": 1,
            "S_opt_rel_to_lw1": mp.nstr(rel_to_lw1, 6),
            "S_opt_vs_lw1_pct": mp.nstr(rel_to_lw1 * 100, 6),
            "final_term_magnitude_n60": mp.nstr(last_term_mag, 6),
            "naive_series_diverges_at_q0": bool(diverges),
            "divergence_mechanism": (
                "|(1−q^j)(1−q^{-j})| = q^j + q^{-j} − 2 ~ q^j for q>1, so "
                "∏_{j=1}^n ~ q^{n(n+1)/2} — super-exponential, the SAME "
                "growth that refuted the α_r single-rank q-Pochhammer "
                "ansatz (docs/audits/...alpha-r...). The naive Habiro sum "
                "is NOT summable at real q₀>1 — but it is an ASYMPTOTIC "
                "series: least-term truncation at n_opt gives a finite "
                "Borel-sum estimate."),
            "implication": (
                "The framework's FINITE linking_weight (5/2 + 3h²/4) "
                "cannot be the convergent Habiro sum at q₀. It must be "
                "the PERTURBATIVE / asymptotic series of the Habiro "
                "element around q=1 (the Garoufalidis–Zagier Φ_K(h) "
                "formal series), evaluated as a truncated polynomial in "
                "h. The G-S-W-Z 2024 resummation (Borel / K_3-graded) is "
                "what assigns a finite value to the divergent sum — "
                "exactly the resurgence content the §6.8 experiment needs."),
        }


def part3b_control_torus_trefoil(dps: int = 50) -> dict:
    """CONTROL: trefoil 3_1 is a TORUS knot (NOT hyperbolic, Vol=0).

    Its Habiro element should behave qualitatively differently from the
    hyperbolic figure-eight — no geometric saddle, so no Vol-driven
    optimal-truncation plateau. Tests whether the part-3 figure-eight
    plateau is a hyperbolic-geometry signal vs an artefact of the
    (q)_n(q⁻¹)_n form.

    Element used (matches the implementation below): the trefoil
    cyclotomic / Habiro form

        J(3_1; q) = Σ_n (−1)^n q^{−n(n+3)/2} (q;q)_n ,

    i.e. a SINGLE Pochhammer (q;q)_n with the alternating sign and the
    q^{−n(n+3)/2} twist — NOT the symmetric (q)_n(q⁻¹)_n of Part 3.
    This is the (near-)canonical torus-knot form (a CONTROL: the point
    is only that a non-hyperbolic knot lacks the figure-eight's
    Vol-driven least-term plateau, not to reproduce a specific
    normalization).
    """
    with mp.workdps(dps):
        q = mp.mpf(Q_50_DIGIT_STR)
        # Trefoil cyclotomic form J(3_1) = Σ (−1)^n q^{−n(n+3)/2} (q;q)_n
        # (single Pochhammer + twist; matches the docstring). The trefoil
        # has Vol=0, so a Vol-driven plateau interpretation predicts NO
        # meaningful least-term plateau here, unlike the figure-eight.
        terms = [mp.mpf(1)]
        total = mp.mpf(1)
        term = mp.mpf(1)
        for n in range(1, 61):
            # trefoil twist q^{-n(n+3)/2} times (q)_n (canonical-ish)
            factor = -(1 - q**n)  # (q;q)_n single Pochhammer, alternating
            term *= factor
            twist = q ** (-mp.mpf(n) * (n + 3) / 2)
            total += term * twist
            terms.append(term * twist)
        abs_terms = [abs(t) for t in terms]
        n_opt = min(range(len(abs_terms)),
                    key=lambda i: abs_terms[i] if i > 0 else mp.inf)
        return {
            "knot": "3_1 (trefoil, TORUS — Vol=0, non-hyperbolic CONTROL)",
            "Vol": 0,
            "optimal_truncation_index": n_opt,
            "S_optimal_truncation": mp.nstr(total if n_opt >= len(terms)-1
                                            else sum(terms[:n_opt+1]), 12),
            "note": ("Non-hyperbolic control. A Vol-driven plateau "
                     "interpretation of the figure-eight Part-3 result "
                     "predicts qualitatively different behaviour here "
                     "(no geometric saddle)."),
        }


def part4_gap_statement() -> dict:
    """What external data is needed to finish §6.8."""
    return {
        "computable_now (this probe)": [
            "Family-A identity (1/4)Σ_{λ⊢4} dim_q = 5/2+3h²/4 (Part 1)",
            "Σ_{λ⊢n} dim_q family n=3..6 (Part 2) — comparison target",
            "Figure-eight Habiro element diverges at real q₀ (Part 3)",
        ],
        "needs_external_data": [
            "Garoufalidis–Zagier Φ_K(h) perturbative coefficients for "
            "K ∈ {4_1, 6_2, Borromean} from arXiv:2111.06645 tables "
            "(the asymptotic series around the geometric saddle).",
            "OR: SnapPy to compute the A-polynomial + Borot–Eynard "
            "topological-recursion coefficients S_0, S_1, S_2 (§6.6).",
            "Both give the SAME perturbative h-series; the test is "
            "whether its h² coefficient matches Family-A's 3/4 (knots) "
            "or the per-link analog (Borromean).",
        ],
        "decisive_test": (
            "Φ_{4_1}(h)/Vol(4_1) should give linking_weight=1 + O(h²) "
            "for the muon (a KNOT, lw=1); Φ_{Borromean}(h)/[stuff] "
            "should give 5/2 + (3/4)h² for the proton (a 3-LINK). If "
            "the h² coefficients match — the Geom_full bridge is DERIVED "
            "from the Habiro element, not fit. K_3 grading makes the "
            "coefficients rigid (no free params)."),
        "next_branch": "this branch — add Part 5 once Φ_K data is sourced",
    }


def main() -> int:
    set_compute_dps()
    t0 = time.time()
    print("=" * 72)
    print(" Per-knot λ(K) via Habiro element — §6.8 experiment, step 1")
    print("=" * 72)

    p1 = part1_verify_family_a()
    print("\n── Part 1: Family-A identity ──")
    print(f"  Σ_{{λ⊢4}} dim_q = {p1['sum_dim_q']}")
    print(f"  (1/4)·sum     = {p1['linking_weight_(1/4)sum']}")
    print(f"  matches (3q²+4+3q⁻²)/4 : {p1['matches_q_form']}")
    print(f"  matches 5/2 + (3/4)h²  : {p1['matches_h_form']}")

    p2 = part2_map_dim_q_family()
    print("\n── Part 2: Σ_{λ⊢n} dim_q family ──")
    print(f"  {'n':>2} {'#λ':>4} {'Σdim@q=1':>10} {'(1/n)Σ@1':>10} "
          f"{'lead h² coeff':>16}")
    for r in p2["rows"]:
        print(f"  {r['n']:>2} {r['n_partitions']:>4} "
              f"{r['sum_dim_q_at_q1']:>10} {r['(1/n)·sum_at_q1']:>10} "
              f"{r['leading_h2_coeff_of_sum']:>16}")

    p3 = part3_figure_eight_habiro_at_q0()
    print("\n── Part 3: figure-eight Habiro element at real q₀ ──")
    print(f"  J(4_1) partial sums (n, S_n, term_n):")
    for n, sn, tn in p3["partial_sums_(n, S_n, term_n)"][:8]:
        print(f"    n={n:>2}  S={sn:>18}  term={tn:>18}")
    print(f"  optimal-truncation index n_opt = "
          f"{p3['optimal_truncation_index']}  "
          f"(min |term| = {p3['min_term_magnitude']})")
    print(f"  S* (least-term truncation)     = "
          f"{p3['S_optimal_truncation']}")
    print(f"  muon linking_weight target     = 1")
    print(f"  S* vs lw=1                     = "
          f"{p3['S_opt_vs_lw1_pct']} %")
    print(f"  |term| at n=60 = {p3['final_term_magnitude_n60']}  "
          f"(diverges: {p3['naive_series_diverges_at_q0']})")

    p3b = part3b_control_torus_trefoil()
    print("\n── Part 3b: trefoil (non-hyperbolic CONTROL) ──")
    print(f"  n_opt = {p3b['optimal_truncation_index']}  "
          f"S* = {p3b['S_optimal_truncation']}")

    p4 = part4_gap_statement()
    print("\n── Part 4: decisive test (needs external Φ_K data) ──")
    print(f"  {p4['decisive_test']}")

    out = {
        "computation": "per-knot-lambda-habiro-probe",
        "description": (
            "Step 1 of the §6.8 Habiro experiment: verifies Family-A "
            "q-dim identity, maps the Σ_{λ⊢n} dim_q family, and shows "
            "the figure-eight Habiro element diverges at real q₀ (so "
            "Family-A must be the PERTURBATIVE Habiro series, not the "
            "convergent sum). EXPLORATORY; no production path touched."),
        "part1_family_a": p1,
        "part2_dim_q_family": p2,
        "part3_figure_eight_habiro": p3,
        "part3b_trefoil_control": p3b,
        "part4_gap_statement": p4,
    }
    out_path = HERE.parent / "per-knot-lambda-habiro-probe.witness.json"
    out_path.write_text(json.dumps(out, indent=2))
    # compute_time_sec is printed to stdout only (NOT persisted) so the
    # committed witness stays deterministic across machines/runs
    # (Copilot review PR #1765).
    print(f"\nWitness: {out_path.name}  "
          f"(compute_time {round(time.time() - t0, 2)}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
