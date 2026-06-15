"""qbeta_c3_multiblock_recursion_attack.py — multi-block Δτ_M probe
using the per-Wedderburn-block decomposition (NEAR-MATCH verdict,
NOT a c_3 derivation).

## Honest framing (read before editing)

The script name and its 1ppQ-ledger origin ("multi-block symbolic c_3
attack") record the original AIM. The VERDICT after running is:

  - Δτ_M(q) IS expressed in closed form as a rational function of q
    (numerator + denominator listed below).
  - c_3 itself is NOT derivable from this object alone — the f-map
    transform between Δτ_M's w = q-1 expansion and the ladder's
    u = b·ℏ_q² expansion is the missing keystone (open).
  - The cross-anchor swing measured here is the pre-stated NEAR-MATCH
    signature; per the 1ppQ-Q_β ledger, c_3 stays NEAR-MATCH and is
    NOT wired.

Renaming the file to `qbeta_delta_tau_M_multiblock_closed_form.py`
would more accurately describe the contents, but the original name
preserves the audit trail back to the ledger's "next-session
suggestion". See `docs/coordination/1ppq-qbeta.md` for the verdict.

## What this probes

Per the 1ppQ ledger, the f-map identification is the keystone for c_3
(and by extension c_4..c_7 via the established 3-term recursion). The
ledger's "next-session suggestion" was:

  "try the symbolic q-difference solve via sympy at multi-block level
   (Wedderburn (3) + (2,1) + (1,1,1)). Pre-stated failure mode: if the
   symbolic c_3 doesn't match empirical to compute precision at BOTH
   canonical q_0 AND the muon-pin cross-check anchor, it's another
   near-match — do not wire."

This probe is exactly that — entirely symbolic, NO fitting at q_0.

## Inputs (pre-archimedean, all from existing witnesses)

1. Per-block closed forms `χ_λ(Δ_T_β)(q)` (from
   `qbeta-per-block-paper-closed-forms.witness.json`):

      χ_(3)    = -(q²-1)(q²+1)²/(4q)
      χ_(2,1)  = (q²-1)(-q⁴-1)/(4q³)
      χ_(1,1,1) = -(q²-1)(q²+1)²/(4q⁵)

2. The z-recursion (from `qbeta-prearchimedean-z-recursion.witness.json`):

      4(n+1)·a_{n+1} + 6n·a_n + (2n-1)·a_{n-1} = 0,   z = √q/(1+q)
      a_0 = 1/2, a_1 = 0

   And the family for z^k:

      4(n+1)·b_{n+1} + 6n·b_n + (2(n-1)+k)·b_{n-1} = 0

3. NON-CANONICAL rational surrogate for the Wenzl y_λ(q) weights at
   n=3 (see `y_lambda_h3_symbolic` below). The CANONICAL Wenzl
   weights from `markov_weights_symbolic.solve_y_lambda(3)` involve
   $\sqrt q$ (via the Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$),
   so they are NOT rational in $q$. The rational surrogate used here
   reproduces the per-block COEFFICIENTS structure (dimensions
   $\{q^2, q, 1\}/((1+q)(1+q+q^2))$) but does NOT equal the canonical
   $y_\lambda(q)$ at numerical anchors — at the m_p-pin $q_0$ the
   canonical y_(3)≈0.4154 vs the surrogate y_(3)≈0.1747 (factor 2.379
   off). The surrogate is retained because the conclusion (NEAR-MATCH
   not closure) is robust to this choice and because the integer-
   numerator structure of Δτ_M is itself informative. A canonical-y_λ
   variant of this probe is open work — its result would still depend
   on the (open) f-map.

## Method (implemented)

Step 1 — Sum the per-block characters weighted by the rational y_λ
surrogate:

    Δτ_M(q) = Σ_{λ ∈ {(3),(2,1),(1,1,1)}} y_λ(q) · χ_λ(Δ_T_β)(q)

Result: a rational function of q with integer-coefficient numerator
(printed; also recorded in the witness).

Step 2 — Taylor-expand Δτ_M(q) around the classical point q = 1
in the variable w = q − 1, to 12 orders. Per-order coefficients are
printed and recorded.

Step 3 (NOT IMPLEMENTED — c_3 extraction requires the f-map) —
The c_3 of Q_β/Q_base = 1 + Σ_k c_k · u^k (u = b·ℏ_q²) is the
order-u³ coefficient of the log-expansion AFTER the f-map transform
between Δτ_M's w-expansion and the ladder's u-expansion. The exact
form of the f-map is the open keystone of the 1ppQ-Q_β closure
(per `docs/coordination/1ppq-qbeta.md`), so this script intentionally
STOPS at the Δτ_M closed form + w-expansion. c_3 is recorded in the
witness as `"NOT_DERIVED"`.

Step 3' (implemented in place of Step 3) — Cross-anchor numerical
evaluation of Δτ_M at q_proton and q_muon (both 50-dps canonical
anchors from `qou_substrate.constants`). The swing
|Δτ_M(q_proton) − Δτ_M(q_muon)| is the NEAR-MATCH diagnostic — it
quantifies how much the Δτ_M object moves between the two anchors,
NOT how much c_3 moves. The c_3 swing requires the f-map first.

## Witness invariant

Asserts Δτ_M(q) is rational in q (has no √q atoms). This is the
structural guarantee that distinguishes the Δτ_M surrogate object
from the canonical √q-bearing Markov trace.

## Honest expectation

Per `b502b9b83` audit: 6 mechanisms ruled out, and this approach
(symbolic q-difference at multi-block level) is NOT in that list —
but the order-audit `c_3-order-audit-accidental-coincidence.md`
notes that per-block Δtr_M is O(√u) while ladder c_3 is O(u³)
— a 5-order accidental coincidence pattern. If the symbolic
calculation reproduces the empirical c_3 EXACTLY at q_proton but
moves at q_muon, the order-audit interpretation is confirmed and
c_3 remains a NEAR-MATCH (no closure). If they match at BOTH
anchors EXACTLY, we have the f-map.

NO fitting, NO numerical tuning. Witness records the pre-archimedean
c_3 rational function + cross-anchor verdict.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _pb  # noqa: F401, E402

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def per_block_chi_diff(q: sp.Symbol) -> dict[tuple[int, ...], sp.Expr]:
    """Closed forms from qbeta-per-block-paper-closed-forms.witness.json."""
    return {
        (3,): -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q),
        (2, 1): (q ** 2 - 1) * (-q ** 4 - 1) / (4 * q ** 3),
        (1, 1, 1): -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q ** 5),
    }


def y_lambda_h3_symbolic(q: sp.Symbol) -> dict[tuple[int, ...], sp.Expr]:
    """NON-CANONICAL rational surrogate for the Wenzl y_λ(q) weights at n=3.

    WARNING — this is NOT the canonical y_λ. The canonical Wenzl weights
    from `markov_weights_symbolic.solve_y_lambda(3)` involve √q (via
    z = 1/(√q + 1/√q)); they are NOT rational in q.

    The rational surrogate below preserves the per-block dimension
    structure {q^2 : q : 1}/((1+q)(1+q+q²)) — sufficient to expose the
    NEAR-MATCH cross-anchor swing — but disagrees with the canonical
    weights numerically. At the m_p-pin q_0, the canonical formula gives
    y_(3) ≈ 0.4154 vs the surrogate y_(3) ≈ 0.1747 (off by ≈ 2.379).

    Use this only for the NEAR-MATCH diagnostic; do not feed downstream
    as if it were the canonical Markov weight.
    """
    return {
        (3,): q ** 2 / ((1 + q) * (1 + q + q ** 2)),
        (2, 1): q / ((1 + q) * (1 + q + q ** 2)),
        (1, 1, 1): 1 / ((1 + q) * (1 + q + q ** 2)),
    }


def main() -> None:
    q = sp.Symbol("q", positive=True)
    w = sp.Symbol("w")  # w = q - 1, expansion variable
    # NOTE: a ladder symbol u = b · ℏ_q² is intentionally NOT introduced
    # here — extracting c_3 from Δτ_M requires the f-map (open keystone,
    # see header). This script only computes the pre-archimedean object
    # Δτ_M and its w-expansion; c_3 itself is NOT derived.

    print("Multi-block pre-archimedean Δτ_M probe")
    print("(NEAR-MATCH diagnostic; c_3 NOT derived — f-map keystone open)")
    print("=" * 70)

    chi = per_block_chi_diff(q)
    yL = y_lambda_h3_symbolic(q)

    # ── Step 1: sum the per-block characters ──────────────────────
    print("\nStep 1: Δτ_M(q) = Σ y_λ · χ_λ(Δ_T_β)")
    delta_tau_M = sum(yL[L] * chi[L] for L in [(3,), (2, 1), (1, 1, 1)])
    delta_tau_M = sp.simplify(delta_tau_M)
    print(f"  Δτ_M(q) = {sp.simplify(delta_tau_M)}")

    # ── Step 2: expand around w = q − 1 ───────────────────────────
    print("\nStep 2: Taylor expand Δτ_M around q = 1 (w = q - 1)")
    dt_w = sp.series(delta_tau_M.subs(q, 1 + w), w, 0, 12).removeO()
    coeffs = [sp.Poly(dt_w, w).nth(k) for k in range(12)]
    print(f"  Order 0:  {coeffs[0]}")
    print(f"  Order 1:  {coeffs[1]}")
    print(f"  Order 2:  {coeffs[2]}")
    print(f"  Order 3:  {coeffs[3]}")
    print(f"  Order 4:  {coeffs[4]}")
    print(f"  Order 5:  {coeffs[5]}")
    print(f"  Order 6:  {coeffs[6]}")
    print(f"  Order 7:  {coeffs[7]}")

    # ── Step 3 (NOT IMPLEMENTED): c_3 extraction requires the f-map ──
    # The ladder Q_β = Q_base · (1 + Σ c_k · u^k) lives in the u = b·ℏ_q²
    # variable; c_3 is the coefficient of u³ in log(1 + Δτ_M / Q_base)
    # AFTER the variable change u = b·ℏ_q² and the substrate factor.
    # Per the order audit, the leading per-block term is O(√u) = O(w^½),
    # not O(u) = O(w) — so direct extraction of c_3 from the w-expansion
    # above is NOT possible without the f-map transform (the exact form
    # of which is the open keystone, per the 1ppQ-Q_β ledger). This
    # script intentionally STOPS at the Δτ_M closed form + w-expansion;
    # c_3 is recorded as "NOT_DERIVED" in the witness JSON below.

    # ── Step 3': cross-anchor numerical evaluation of Δτ_M ─────────
    print("\nStep 3': Cross-anchor evaluation of Δτ_M at q_proton vs q_muon")

    # q_0 anchors at 50-dps from the canonical qou_substrate module.
    # Required (not optional): the cross-anchor swing diagnostic only
    # has meaning if both anchors come from the canonical derivation.
    # A CODATA-derived approximation would silently change what the
    # swing measures (anchor vs. compute precision), so we fail fast
    # if the canonical module is unavailable.
    from q_parameter import Q_50_DIGIT_STR, q_muon_at  # canonical (re-exported)
    q_proton = sp.Rational(Q_50_DIGIT_STR)
    print(f"  q_proton = {sp.N(q_proton, 18)}")

    # Muon anchor: q_muon from m_μ/m_e closed form at 50 dps.
    # `q_muon_at` returns an mpmath mpf — convert via str to preserve
    # full precision when handing off to sp.Rational.
    q_muon = sp.Rational(str(q_muon_at(50)))
    print(f"  q_muon   = {sp.N(q_muon, 18)}")

    # Use 60-dps SymPy evaluation to match the witness `output_dps`
    # metadata. Anchors are 50-dps, so 60-dps gives ≥10 digits of
    # head-room on the diagnostic.
    dt_proton = sp.N(delta_tau_M.subs(q, q_proton), 60)
    dt_muon = sp.N(delta_tau_M.subs(q, q_muon), 60)
    print(f"\n  Δτ_M(q_proton) = {dt_proton}")
    print(f"  Δτ_M(q_muon)   = {dt_muon}")
    print(f"  swing = |Δτ_M(p) − Δτ_M(μ)| = {abs(dt_proton - dt_muon)}")

    # Real invariant for the assertion below: Δτ_M(q) has NO √q atoms.
    # Distinguishes the rational-surrogate Δτ_M object from the canonical
    # √q-bearing Markov trace; flags regressions if the surrogate is ever
    # accidentally swapped for the canonical y_λ.
    sqrt_q_atoms = [
        a for a in delta_tau_M.atoms(sp.Pow)
        if a.exp.is_Rational and not a.exp.is_Integer and a.base == q
    ]
    has_no_sqrt_q = 1.0 if not sqrt_q_atoms else 0.0

    # ── Witness ──────────────────────────────────────────────────
    wn = WitnessBuilder(
        "qbeta-c3-multiblock-recursion-attack",
        engine="sympy+mpmath",
    )
    wn.set_description(
        "Multi-block Δτ_M probe (NOT a c_3 derivation). Combines the exact "
        "pre-archimedean per-block closed forms χ_λ(Δ_T_β)(q) (from "
        "qbeta-per-block-paper-closed-forms.witness.json) with a "
        "NON-CANONICAL rational surrogate for the Wenzl y_λ(q) weights "
        "(canonical y_λ involves √q) to emit Δτ_M(q) as a rational "
        "function of q. Reports: (1) the closed form, (2) its Taylor "
        "expansion around q=1 in w=q−1 to 12 orders, (3) the cross-anchor "
        "swing of Δτ_M between q_proton and q_muon (the NEAR-MATCH "
        "diagnostic for the Δτ_M object — NOT for c_3, which requires "
        "the open f-map). c_3 is explicitly recorded as NOT_DERIVED. "
        "NO FITS."
    )
    wn.set_content_block("conj:qbeta-precision-ladder")
    wn.add_data("delta_tau_M_symbolic_q", str(delta_tau_M))
    wn.add_data("taylor_coeffs_w_expansion",
                {str(k): str(coeffs[k]) for k in range(12)})
    wn.add_data("delta_tau_M_q_proton", str(dt_proton))
    wn.add_data("delta_tau_M_q_muon", str(dt_muon))
    wn.add_data("cross_anchor_swing", str(abs(dt_proton - dt_muon)))
    wn.add_data("c_3_value", "NOT_DERIVED")
    wn.add_data(
        "c_3_status",
        "NEAR-MATCH (open). The Δτ_M closed form computed here does NOT "
        "yield c_3 directly. The f-map transform between Δτ_M's w = q-1 "
        "expansion and the Q_β ladder's u = b·ℏ_q² expansion is the "
        "missing keystone (open). Per the 1ppQ-Q_β ledger, c_3 = -2 "
        "remains a NEAR-MATCH (flip-flop history #1-5) — NOT wired as "
        "Taylor-exact. Also note: the y_λ used here is a NON-CANONICAL "
        "rational surrogate (canonical y_λ involves √q)."
    )
    wn.add_data(
        "structural_note",
        "Δτ_M(q) is a rational function of q (no √ — symbolic in q²). "
        "Per the per-block witness, the linear-in-h structure of (2,1) "
        "and the symmetric (3) ↔ (1,1,1) ↔ q ↔ 1/q pairing under "
        "antipode are exact at the rational-function level. The "
        "cross-anchor swing IS the order-of-magnitude diagnostic for "
        "whether c_3 derives from this object exactly or is a near-match."
    )
    # Real invariant: Δτ_M(q) is rational in q (no √q atoms).
    # `computed = has_no_sqrt_q` is 1.0 iff the SymPy atom scan above
    # found no half-integer powers of q in delta_tau_M. If a future
    # edit swaps the rational surrogate for the canonical √q-bearing
    # y_λ, this assertion will trip and surface the regression.
    wn.add_assertion(
        "delta_tau_M_rational_in_q",
        computed=has_no_sqrt_q,
        expected=1.0,
    )
    out = wn.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
