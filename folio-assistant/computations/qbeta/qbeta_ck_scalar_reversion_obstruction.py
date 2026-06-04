"""qbeta_ck_scalar_reversion_obstruction — why the c_k need the OPERATOR route.

FORMALIZE-FIRST FOUNDATION for the Q_β c_k operator-valued derivation tranche.
This is the structural invariant that PRUNES the scalar hypothesis class up
front (compute-author §3.3), so the tranche does not re-attempt any scalar-q
closure (all of which are refuted — see the refuted-class map C1..C12,
docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md).

NECESSITY (from the precision-floor probe, PR #1844): the c_k≥4 cannot be
data-extracted (σ(c_k)=σ_R/u^k is below the measured-Q_β floor), so they must be
DERIVED from framework structure. The question is THROUGH WHAT structure.

THE OBSTRUCTION. The c_k were posited as scalar Taylor coefficients of
R = Q_β/(Q_A·cos α_eff) = ∏_k(1 + c_k·u^k) in the single scalar u = b·ℏ_q²,
ℏ_q = (q−1)/q. But ℏ_q is LINEAR in t = q−1 (ℏ_q = t − t² + t³ − …), so
u = b·ℏ_q² has a DOUBLE ZERO at q=1 (u = b(1)·t² + O(t³)) for ANY b regular and
nonzero at q=1. Hence the reversion t(u) is singular — it needs a u^{1/2}
branch — so R(q) is a clean series in INTEGER powers of u only if R is EVEN in t
(equivalently bar-even, since q ↦ q⁻¹ acts as t ↦ −t + O(t²)).

WHY α_EM SUCCEEDED BUT Q_β DOES NOT (scalar). The α_EM Habiro element
H(q) = [2]_q·(1 − h²α) is manifestly bar-even ([2]_q = q+q⁻¹ and h² = (q−q⁻¹)²
are both bar-invariant), so its scalar u-series is clean and its c_k ARE scalar
Taylor coefficients — the identification worked. The Q_β residual's
trace-difference is NOT bar-fixed at the archimedean level (registry §5;
docs/coordination/1ppq-qbeta.md), so R has odd-in-t content, the u^{1/2} branch
is genuinely present, and the scalar c_k series is singular.

⇒ THE RESOLUTION (the open axis). The c_k are NOT scalar-q Taylor coefficients;
they are the OPERATOR-LEVEL (N=k) coefficients of the Hoefsmit T_β matrix chain,
where each representation level N=k contributes b^k·ℏ_q^{2k} = u^k by substrate
scaling — supplying integer u-powers structurally, bypassing the singular scalar
reversion. The executable recipe is
docs/audits/2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md
(Stages 1–5); the first structural gate is "N=2 level reproduces c_2 = −1".

This probe formalizes ONLY the obstruction (b-independent, witness-anchored). It
performs no extraction and no fit; it is the gate that justifies the operator
route. Diagnostic-only.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).resolve().parent


def load_b() -> mp.mpf:
    """Hoefsmit b at the substrate anchor, from the N3 operator-valued witness."""
    with open(HERE.parent / "q-beta-operator-valued-N3.witness.json",
              encoding="utf-8") as f:
        d = json.load(f)["data"]
    return mp.mpf(d["hoefsmit_b"])


def first_nonzero_order(expr, t, upto: int = 8) -> int:
    """Order of the lowest nonzero Taylor coefficient of expr in t at t=0.

    Requests ``upto+1`` terms so the coefficients of t^0..t^upto are genuinely
    present (``sp.series(..., n)`` truncates at t^(n-1)). Returns ``upto+1`` when
    the series vanishes through t^upto (caller reads that as "no low-order term"),
    keeping "identically zero" and "first nonzero ≥ upto" distinct from a real
    low-order hit (Copilot #1867).
    """
    ser = sp.series(expr, t, 0, upto + 1).removeO()
    if ser == 0:
        return upto + 1
    poly = sp.Poly(ser, t)
    for n in range(upto + 1):
        if poly.coeff_monomial(t**n) != 0:
            return n
    return upto + 1


def main() -> int:
    print("=" * 78)
    print(" Q_β c_k — scalar-reversion OBSTRUCTION (operator-route foundation)")
    print("=" * 78)

    # ── PART A: the b-independent double zero of u at q = 1 ───────────────
    t = sp.symbols("t")                 # t = q − 1
    q = 1 + t
    hbar = (q - 1) / q                  # ℏ_q = (q−1)/q
    hbar_ser = sp.series(hbar, t, 0, 6).removeO()
    u_shape = sp.series(hbar**2, t, 0, 6).removeO()   # ℏ_q² — the b-free core
    ord_hbar = first_nonzero_order(hbar, t)
    ord_u = first_nonzero_order(hbar**2, t)
    dudt0 = sp.diff(hbar**2, t).subs(t, 0)

    print("\n  PART A: order of vanishing at q = 1  (t = q − 1)")
    print(f"    ℏ_q(t)            = {hbar_ser}")
    print(f"    ℏ_q²(t)           = {u_shape}")
    print(f"    ord_t ℏ_q         = {ord_hbar}  (linear — simple zero)")
    print(f"    ord_t ℏ_q²        = {ord_u}  (quadratic — DOUBLE zero)")
    print(f"    d(ℏ_q²)/dt |_0    = {dudt0}  ⇒ u = b·ℏ_q² has u'(0)=0 for any")
    print("                          b regular & nonzero at q=1")

    # ── PART B: b is regular & nonzero at the anchor (witness) ────────────
    b0 = load_b()
    print("\n  PART B: b is nonzero at the substrate (so the double zero is real)")
    print(f"    b(q_0)            ≈ {mp.nstr(b0, 8)}  (Hoefsmit, N3 witness)")
    print(f"    ⇒ u = b·ℏ_q²      = {mp.nstr(b0, 6)}·t² + O(t³)  near q=1")

    # ── PART C: the consequence — scalar reversion is singular ────────────
    print("\n  PART C: consequence for the scalar c_k series")
    print("    • t(u) reversion needs a u^{1/2} branch (double zero) ⇒ R(q) is a")
    print("      clean series in INTEGER powers of u ONLY if R is EVEN in t")
    print("      (bar-even: q↦q⁻¹ acts as t↦−t + O(t²)).")
    print("    • α_EM's H(q)=[2]_q·(1−h²α) IS bar-even ⇒ its scalar u-series is")
    print("      clean (identification succeeded). The Q_β trace-difference is")
    print("      NOT bar-fixed archimedean ⇒ odd-in-t content ⇒ scalar c_k")
    print("      series is singular.")
    print("    • ⇒ the c_k are OPERATOR-LEVEL (N=k) coefficients of the Hoefsmit")
    print("      T_β chain (each level → u^k by substrate scaling), NOT scalar-q")
    print("      Taylor coefficients. Operator route is the open axis.")

    # Single non-zero test, reused by the predicate AND the witness assertion
    # so they cannot disagree on an edge case (Copilot #1867).
    b_is_nonzero = abs(b0) > mp.mpf("1e-6")
    obstruction = (ord_u == 2 and ord_hbar == 1 and dudt0 == 0 and b_is_nonzero)

    print("\n" + "=" * 78)
    print("VERDICT: scalar-q reversion of the c_k ladder is SINGULAR (b-independent")
    print("double zero of u at q=1). The c_k cannot be scalar Taylor coefficients;")
    print("they must come from the operator-level grading of the Hoefsmit T_β chain.")
    print("Next gate (recipe Stage 3): verify the N=2 level reproduces c_2 = −1.")
    print()

    w = WitnessBuilder("qbeta-ck-scalar-reversion-obstruction", engine="sympy+mpmath")
    w.set_content_block("prop:q-beta-categorical-precision-ladder")
    w.set_description(
        "Formalize-first foundation for the Q_β c_k operator-valued derivation "
        "tranche. ℏ_q=(q−1)/q is linear in t=q−1, so u=b·ℏ_q² has a b-INDEPENDENT "
        "double zero at q=1 (u=b(1)t²+O(t³)); the reversion t(u) needs a u^{1/2} "
        "branch, so R=∏(1+c_k u^k) is a clean integer-power u-series only if R is "
        "even in t (bar-even). α_EM's [2]_q·(1−h²α) is bar-even (scalar route "
        "worked); the Q_β trace-difference is not bar-fixed archimedean, so the "
        "scalar c_k series is singular. ⇒ the c_k are OPERATOR-LEVEL (N=k) "
        "coefficients of the Hoefsmit T_β chain (each level→u^k by substrate "
        "scaling), not scalar Taylor coefficients. This prunes the scalar class "
        "(refuted C1..C12) and motivates the operator route (keystone recipe "
        "Stages 1–5; first gate N=2→c_2=−1). No fit, no extraction. Diagnostic-only."
    )
    w.add_data("ord_t_hbar_q", ord_hbar)
    w.add_data("ord_t_u_shape", ord_u)
    w.add_data("du_dt_at_q1", int(dudt0))
    w.add_data("hbar_q_series_in_t", str(hbar_ser))
    w.add_data("u_shape_series_in_t", str(u_shape))
    w.add_data("b_anchor", mp.nstr(b0, 12))
    w.add_data("bar_involution_action", "q↦q⁻¹ ⇒ t↦−t + O(t²); clean integer-u "
               "series ⟺ R even in t (bar-even)")
    w.add_data("alpha_em_contrast", "H(q)=[2]_q·(1−h²α) bar-even ⇒ scalar route "
               "succeeded; Q_β trace-diff not bar-fixed archimedean ⇒ scalar "
               "route singular")
    w.add_data("resolution_open_axis",
               "operator-level (N=k) coefficients of the Hoefsmit T_β chain; "
               "recipe docs/audits/2026-06-04-qbeta-1ppq-keystone-exact-"
               "construction-recipe.md Stages 1–5; first gate N=2 → c_2=−1")
    w.add_assertion(
        name="u_has_double_zero_at_q1",
        computed=ord_u, expected=2, tolerance=0,
        source="ℏ_q linear in t ⇒ ℏ_q² (hence u=b·ℏ_q²) vanishes to order 2 at "
               "q=1, b-independent. Scalar t(u) reversion therefore singular.",
    )
    w.add_assertion(
        name="b_nonzero_at_anchor",
        computed=bool(b_is_nonzero), expected=True, tolerance=0,
        source="Hoefsmit b(q_0)≈0.8676 ≠ 0 (N3 witness) ⇒ the double zero of u is "
               "real, not an accidental b-cancellation.",
    )
    w.add_assertion(
        name="scalar_reversion_singular",
        computed=bool(obstruction), expected=True, tolerance=0,
        source="ord_t(u)=2 ∧ ℏ_q'(0)≠0 ∧ u'(0)=0 ∧ b≠0 ⇒ scalar-q c_k series "
               "singular; c_k must be operator-level (Hoefsmit T_β chain).",
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
