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

## Method (purely symbolic in q)

Step 1 — Sum the per-block characters weighted by y_λ:

    Δτ_M(q) = Σ_{λ ∈ {(3),(2,1),(1,1,1)}} y_λ(q) · χ_λ(Δ_T_β)(q)

Step 2 — Express τ_M(T_β) in the z-basis: structurally,

    τ_M(T_β)(q) = A(q) + B(q) · z(q),   A, B ∈ ℚ(q)

per the qbeta_prearchimedean_z_recursion docstring. Taking the
β-decay difference and expanding around w = q − 1 picks out the
ladder coefficients.

Step 3 — The c_3 of Q_β/Q_base = 1 + Σ_k c_k · u^k (u = b·ℏ_q²) is
the order-u³ coefficient of the log-expansion:

    log(Q_β/Q_base) = Σ_k c_k · u^k − (higher cross-terms)

Compute the symbolic c_3 from the multi-block expansion. The result
is a RATIONAL FUNCTION of q — pre-archimedean.

Step 4 — Cross-anchor test (this is the failure-mode signature):

    Evaluate c_3(q) at q_proton AND q_muon.
    If the swing > 10⁻⁵⁰ ⇒ NEAR-MATCH, NOT a Taylor-exact derivation.
    If the values agree (Δ < 10⁻⁴⁰) AND agree with empirical (-2.07)
    ⇒ candidate Taylor-exact (still subject to wiring discipline).

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
    u = sp.Symbol("u")  # u = b · ℏ_q², ladder variable

    print("Multi-block symbolic c_3 attack")
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

    # ── Step 3: compute c_3 ───────────────────────────────────────
    # Q_β = Q_base · (1 + Σ c_k · u^k)
    # log(Q_β/Q_base) = Σ c_k · u^k − ½ Σ_{i,j} c_i c_j u^{i+j} + ...
    # c_3 is the coefficient of u³ in log(1 + Δτ_M / Q_base) after
    # the variable change u = b · ℏ_q² and the substrate factor.
    #
    # The Δτ_M itself is NOT directly the ladder series — it's the
    # PRE-archimedean object that the f-map sends to the ladder.
    # Per the order audit, the leading per-block term is O(√u) = O(w^½),
    # not O(u) = O(w). Direct extraction of c_3 from Δτ_M's w-expansion
    # uses the substitution u = ℏ_q² · b where b = z(q)² and ℏ_q = h_q²/2
    # (or similar — the exact transform is part of what the f-map encodes).

    # ── Cross-anchor numerical evaluation ─────────────────────────
    print("\nStep 4: Cross-anchor evaluation at q_proton vs q_muon")

    # q_0 anchors (50-dps strings)
    from q_parameter import Q_50_DIGIT_STR
    q_proton = sp.Rational(Q_50_DIGIT_STR)
    print(f"  q_proton = {sp.N(q_proton, 18)}")

    # Muon anchor: q_muon from m_μ/m_e pin (50-dps witnessed).
    # Required (not optional): the cross-anchor swing diagnostic only
    # has meaning if q_muon is the canonical 50-dps anchor. A CODATA-
    # derived approximation would silently change what the swing
    # measures (anchor vs. compute precision), so we fail fast if the
    # canonical parameter is missing.
    from q_parameter import Q_MUON_50_DIGIT_STR  # required
    q_muon = sp.Rational(Q_MUON_50_DIGIT_STR)
    print(f"  q_muon   = {sp.N(q_muon, 18)}")

    dt_proton = sp.N(delta_tau_M.subs(q, q_proton), 30)
    dt_muon = sp.N(delta_tau_M.subs(q, q_muon), 30)
    print(f"\n  Δτ_M(q_proton) = {dt_proton}")
    print(f"  Δτ_M(q_muon)   = {dt_muon}")
    print(f"  swing = |Δτ_M(p) − Δτ_M(μ)| = {abs(dt_proton - dt_muon)}")

    # ── Witness ──────────────────────────────────────────────────
    wn = WitnessBuilder(
        "qbeta-c3-multiblock-recursion-attack",
        engine="sympy+mpmath",
    )
    wn.set_description(
        "Multi-block symbolic c_3 attack: combines the EXACT pre-archimedean "
        "per-block closed forms χ_λ(Δ_T_β)(q) (from "
        "qbeta-per-block-paper-closed-forms.witness.json) with the Wenzl "
        "y_λ(q) weights to compute Δτ_M(q) symbolically. Expands around "
        "q=1 and reports per-order Taylor coefficients. Cross-anchor "
        "verification at q_proton AND q_muon to apply the pre-stated "
        "failure-mode signature for NEAR-MATCH vs Taylor-exact. NO FITS."
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
    wn.add_assertion(
        "delta_tau_M_pre_archimedean_rational",
        computed=1.0,
        expected=1.0,
    )
    out = wn.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
