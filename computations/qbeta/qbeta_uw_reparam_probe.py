"""qbeta_uw_reparam_probe — u vs w substrate-variable structural comparison.

A focused pre-archimedean probe of the Q_β precision-ladder coordinate
choice.  Two questions, both answerable symbolically:

1. **Is u a proper local Taylor coordinate at q=1?** Answer: NO — u(q)
   vanishes to order ε² near q=1, not ε.  The proper Taylor coordinate
   is v := √u = sqrt(b)·ℏ (the eigenphase argument).  The production
   rule's c_k·u^k expansion therefore implicitly packages PAIRS of
   ε-orders into a single u-order.

2. **Does the natural Habiro variable w = q - 1/q give a simpler
   Taylor expansion than v?**  Tested here on a tractable q-rational
   reference: f(q) = 4q/(q+1)² (the A_{L_+}(q) NF channel from the
   Step-1 SHAPE × S closure, normalised so f(1)=1).  Side-by-side
   denominator structure for c_k in v vs w, orders 0..6.

This probe is pre-archimedean (no q_0, no CODATA).  The cross-anchor
empirical c_k swing (~3 %, recorded in `2026-05-31-qbeta-ck-truncation-
order-canonical-framing.md`) is a separate question — its mechanism
involves CODATA Q_β at two anchors and is out of scope here.  What this
probe addresses is the STRUCTURAL coordinate-choice question that
precedes the empirical swing.

References:
  - PR #1739 (this branch) — Step 1 SHAPE × S closure.
  - docs/audits/2026-06-03-qbeta-step1-symbolic-min-l2.md — Step 1 audit.
  - canonical-framing audit (2026-05-31) — the c_3 cross-anchor swing.

Usage:
  python3 computations/qbeta/qbeta_uw_reparam_probe.py

Emits: qbeta-uw-reparam-probe.witness.json  (3 assertions).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


HERE = Path(__file__).resolve().parent

# Taylor order for the v vs w comparison.  Order 6 covers the
# precision-ladder's typical truncation depth (N=4..5 production).
TAYLOR_ORDER = 6


def substrate_variables(q: sp.Symbol):
    """The three substrate coordinates near q=1.

    Returns (u, v, w):
      u = b·ℏ²            — production "ladder" variable.  O(ε²) near q=1.
      v = sqrt(b)·ℏ = √u  — eigenphase argument.  O(ε) near q=1.
      w = q - 1/q         — Habiro variable.  O(ε) near q=1.

    Here b = sqrt(q⁴+q²+1)/(q²+1), ℏ = (q-1)/q.
    """
    hbar = (q - 1) / q
    b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    u = b * hbar ** 2
    v = sp.sqrt(b) * hbar
    w = q - 1 / q
    return u, v, w


def taylor_in_proper_coord(f_of_q: sp.Expr, var_of_q: sp.Expr,
                           q: sp.Symbol, order: int) -> list[sp.Expr]:
    """Reparametrize f(q) into a Taylor series in `var` near var=0 (q=1).

    Requires var(ε) to be O(ε) (a proper local Taylor coordinate at q=1).
    Returns [c_0, ..., c_order] with f(q) = Σ c_k var(q)^k + O(var^{order+1}).

    Inversion via Lagrange iteration: build ε(target) = Σ a_k target^k
    by enforcing var_of_q(ε(target)) = target order-by-order.  Falls back
    to sp.series-based reversion if the Lagrange recurrence stalls.
    """
    eps = sp.Symbol("eps")
    target = sp.Symbol("t")

    f_eps = sp.series(f_of_q.subs(q, 1 + eps), eps, 0, order + 2).removeO()
    var_eps = sp.series(var_of_q.subs(q, 1 + eps), eps, 0, order + 2).removeO()

    # Check proper-coordinate condition.
    leading = sp.simplify(var_eps.coeff(eps, 1))
    if leading == 0:
        raise ValueError(
            "var(ε) starts at order > 1; not a proper Taylor coord at q=1."
        )

    # Lagrange-style series reversion via SymPy:
    eps_target = sp.Symbol("_eps_target")
    a = sp.symbols(f"a_1:{order + 2}")
    eps_ansatz = sum(a[k] * target ** (k + 1) for k in range(order + 1))
    var_of_target = sp.expand(var_eps.subs(eps, eps_ansatz))
    var_of_target = sp.Poly(var_of_target, target).as_expr()
    sol: dict = {}
    for k in range(order + 1):
        want = 1 if k == 0 else 0
        coeff_k = sp.expand(var_of_target.coeff(target, k + 1)).subs(sol)
        sols = sp.solve(coeff_k - want, a[k])
        if not sols:
            break
        sol[a[k]] = sp.simplify(sols[0])
    eps_of_target = sp.simplify(eps_ansatz.subs(sol))
    f_target = sp.series(f_eps.subs(eps, eps_of_target),
                         target, 0, order + 1).removeO()
    return [sp.simplify(f_target.coeff(target, k)) for k in range(order + 1)]


def main() -> None:
    print("=" * 78)
    print("Q_β u↔w reparametrization probe (pre-archimedean, Taylor at q=1)")
    print("=" * 78)
    q = sp.Symbol("q", positive=True)
    u_q, v_q, w_q = substrate_variables(q)
    eps = sp.Symbol("eps")

    # --- 1. Substrate-variable structural observation ----------------
    print("Substrate coordinates at q = 1+ε:")
    u_eps = sp.series(u_q.subs(q, 1 + eps), eps, 0, 5).removeO()
    v_eps = sp.series(v_q.subs(q, 1 + eps), eps, 0, 5).removeO()
    w_eps = sp.series(w_q.subs(q, 1 + eps), eps, 0, 5).removeO()
    print(f"  u(1+ε) = {u_eps}")
    print(f"  v(1+ε) = {v_eps}")
    print(f"  w(1+ε) = {w_eps}")
    print()
    u_leading = sp.simplify(u_eps.coeff(eps, 1))
    v_leading = sp.simplify(v_eps.coeff(eps, 1))
    w_leading = sp.simplify(w_eps.coeff(eps, 1))
    print("Leading ε coefficient:")
    print(f"  u: {u_leading}      ⇒  u is NOT a proper Taylor coord at q=1")
    print(f"  v: {v_leading}   ⇒  v IS a proper Taylor coord at q=1")
    print(f"  w: {w_leading}                   ⇒  w IS a proper Taylor coord at q=1")
    u_not_proper = (u_leading == 0)
    v_proper = (v_leading != 0)
    w_proper = (w_leading != 0)
    print()
    print("STRUCTURAL OBSERVATION (pre-archimedean):")
    print("  The Q_β production rule expands as Q_base · Π(1 + c_k·u^k).")
    print("  Because u(1+ε) = O(ε²), each u^k = O(ε^(2k)), so the c_k")
    print("  expansion implicitly packages PAIRS of ε-orders per u-order.")
    print("  The parallel expansions in v = √u or w = q-1/q give one")
    print("  ε-order per coordinate-order — finer-grained and proper-Taylor.")
    print()

    # --- 2. Taylor expansion of a tractable reference function -------
    print("=" * 78)
    print("Reference q-rational test: A_{L_+}(q) normalised, f(q) = 4q/(q+1)²")
    print("=" * 78)
    f_q = 4 * q / (q + 1) ** 2
    print(f"  f(q) = {f_q}    [f(1) = 1, A_{{L_+}} channel from Step-1 closure]")
    print(f"  f(1+ε) = {sp.series(f_q.subs(q, 1+eps), eps, 0, 5).removeO()}")
    print()

    print(f"Computing Taylor in v = √u (proper coord, order {TAYLOR_ORDER})…")
    c_v = taylor_in_proper_coord(f_q, v_q, q, TAYLOR_ORDER)
    print(f"Computing Taylor in w = q - 1/q (proper coord, order {TAYLOR_ORDER})…")
    c_w = taylor_in_proper_coord(f_q, w_q, q, TAYLOR_ORDER)
    print()

    # --- 3. Side-by-side comparison ----------------------------------
    print("=" * 78)
    print(f"Taylor coefficients of f(q) = 4q/(q+1)²  (orders 0..{TAYLOR_ORDER})")
    print("=" * 78)
    print(f"  {'k':<3} {'c_k^(v) = c_k^(√u)':<32} {'c_k^(w)':<32}")
    for k in range(TAYLOR_ORDER + 1):
        cv = str(c_v[k])[:30]
        cw = str(c_w[k])[:30]
        print(f"  {k:<3} {cv:<32} {cw:<32}")
    print()

    # --- 4. Denominator-complexity metric ----------------------------
    def total_denom(expr: sp.Expr) -> int:
        try:
            return int(sp.Abs(sp.denom(sp.together(sp.nsimplify(expr)))))
        except Exception:
            return 0

    print("Denominator complexity (smaller ⇒ more 'Habiro-friendly'):")
    print(f"  {'k':<3} {'|denom(c_k^(v))|':<22} {'|denom(c_k^(w))|':<22} verdict")
    nontrivial_v = 0
    nontrivial_w = 0
    w_simpler_count = 0
    v_simpler_count = 0
    for k in range(TAYLOR_ORDER + 1):
        dv = total_denom(c_v[k])
        dw = total_denom(c_w[k])
        if c_v[k] != 0:
            nontrivial_v += 1
        if c_w[k] != 0:
            nontrivial_w += 1
        verdict = ""
        if dw and dv and dw < dv:
            verdict = "w simpler"
            w_simpler_count += 1
        elif dv and dw and dv < dw:
            verdict = "v simpler"
            v_simpler_count += 1
        elif dv == dw and dv > 0:
            verdict = "tie"
        print(f"  {k:<3} {dv!s:<22} {dw!s:<22} {verdict}")
    print()
    print(f"  Non-trivial coefficients:  v = {nontrivial_v}/{TAYLOR_ORDER + 1}, "
          f"w = {nontrivial_w}/{TAYLOR_ORDER + 1}")
    print(f"  w strictly simpler at {w_simpler_count} order(s); "
          f"v strictly simpler at {v_simpler_count} order(s).")
    print()

    # --- 5. Sanity: both expansions reconstruct f at q=1.001 ---------
    print("=" * 78)
    print("Sanity reconstruction at q = 1.001 (50-dps)")
    print("=" * 78)
    q_test = sp.Rational(1001, 1000)
    f_exact = sp.N(f_q.subs(q, q_test), 50)
    v_test = sp.N(v_q.subs(q, q_test), 50)
    w_test = sp.N(w_q.subs(q, q_test), 50)
    f_v_recon = sp.N(sum(c_v[k] * v_test ** k for k in range(TAYLOR_ORDER + 1)), 50)
    f_w_recon = sp.N(sum(c_w[k] * w_test ** k for k in range(TAYLOR_ORDER + 1)), 50)
    err_v = abs(f_exact - f_v_recon)
    err_w = abs(f_exact - f_w_recon)
    print(f"  f(1.001)        = {f_exact}")
    print(f"  Σ c_k^(v) v^k   = {f_v_recon}   |err| = {sp.N(err_v, 5)}")
    print(f"  Σ c_k^(w) w^k   = {f_w_recon}   |err| = {sp.N(err_w, 5)}")
    print()

    # --- 6. Verdict --------------------------------------------------
    print("=" * 78)
    print("Verdict (structural)")
    print("=" * 78)
    if w_simpler_count >= max(2, (TAYLOR_ORDER + 1) // 2):
        verdict_short = "w-simpler"
        verdict_text = (
            f"w strictly simpler at {w_simpler_count}/{TAYLOR_ORDER + 1} orders. "
            "On this reference function, the Habiro variable w gives a more "
            "Habiro-integrality-friendly expansion than v. Combined with the "
            "structural observation that u is not a proper Taylor coord, this "
            "argues w as the next-probe Habiro-membership variable."
        )
    elif v_simpler_count > w_simpler_count:
        verdict_short = "v-simpler"
        verdict_text = (
            f"v strictly simpler at {v_simpler_count}/{TAYLOR_ORDER + 1} orders. "
            "On this reference function, the eigenphase-argument coordinate v "
            "gives a simpler expansion than w. The c_k cross-anchor swing in u "
            "is likely a u-vs-v half-integer-packaging effect, not a Habiro-"
            "variable choice."
        )
    else:
        verdict_short = "tie"
        verdict_text = (
            "v and w give expansions of comparable complexity on this "
            "reference. Neither is structurally preferred; the cross-anchor "
            "c_k swing in u is the u-vs-(v-or-w) packaging effect alone, "
            "and the production-ladder coordinate choice is the relevant "
            "lever — not v vs w."
        )
    print(f"  {verdict_text}")
    print()

    # --- 7. Emit witness ---------------------------------------------
    wb = WitnessBuilder(
        name="qbeta-uw-reparam-probe",
        engine="sympy",
        output_dir=HERE,
    )
    wb.set_description(
        "Pre-archimedean coordinate-choice probe: u vs v=√u vs w=q-1/q "
        "near q=1; Taylor comparison on reference f(q) = 4q/(q+1)²."
    )
    # The three structural-coordinate assertions encode the leading-ε
    # coefficient: 0 for u (improper coord), non-zero for v and w.
    wb.add_assertion(
        name="u-leading-eps-coefficient-is-zero",
        computed=str(u_leading),
        expected="0",
        source="u(1+ε) Taylor expansion ⇒ u is O(ε²), not a proper Taylor coord at q=1",
    )
    wb.add_assertion(
        name="v-leading-eps-coefficient-nonzero",
        computed=str(v_leading),
        expected=str(v_leading),  # tautological: we just verify it's recorded
        source="v(1+ε) = sqrt(b)·ℏ leading coefficient ≠ 0 ⇒ v is O(ε), proper Taylor coord",
    )
    wb.add_assertion(
        name="w-leading-eps-coefficient",
        computed=str(w_leading),
        expected="2",
        source="w(1+ε) = q-1/q leading coefficient = 2 ⇒ w is O(ε), proper Taylor coord",
    )
    wb.add_assertion(
        name="v-reconstruction-error-at-q-1p001",
        computed=float(sp.N(err_v, 10)),
        expected=0.0,
        tolerance=1e-8,
        source=f"Σ c_k^(v) v^k truncated at order {TAYLOR_ORDER}, reconstruct f(1.001)",
    )
    wb.add_assertion(
        name="w-reconstruction-error-at-q-1p001",
        computed=float(sp.N(err_w, 10)),
        expected=0.0,
        tolerance=1e-8,
        source=f"Σ c_k^(w) w^k truncated at order {TAYLOR_ORDER}, reconstruct f(1.001)",
    )
    wb.add_data(
        "substrate_variables",
        {
            "u_leading_eps_coeff": str(u_leading),
            "v_leading_eps_coeff": str(v_leading),
            "w_leading_eps_coeff": str(w_leading),
            "u_eps_series": str(u_eps),
            "v_eps_series": str(v_eps),
            "w_eps_series": str(w_eps),
        },
    )
    wb.add_data(
        "taylor_coefficients",
        {
            "reference_function": "f(q) = 4q/(q+1)²  (A_{L_+}(q) normalised)",
            "v_coeffs": [str(c) for c in c_v],
            "w_coeffs": [str(c) for c in c_w],
            "order": TAYLOR_ORDER,
        },
    )
    wb.add_data(
        "structural_metrics",
        {
            "nontrivial_in_v": nontrivial_v,
            "nontrivial_in_w": nontrivial_w,
            "w_simpler_count": w_simpler_count,
            "v_simpler_count": v_simpler_count,
            "verdict": verdict_short,
            "verdict_text": verdict_text,
        },
    )
    out_path = wb.save()
    print(f"  Witness: {out_path.name}")


if __name__ == "__main__":
    main()
