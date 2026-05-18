"""F_3 / F_n categorical derivation — attempt via canonical Markov of σ_1².

Per user request: do F_3, F_n categorical derivation. This probe ports
the canonical Markov-trace machinery to derive the Story B factors
F_n := 1 + c_n · ℏ_q^{2n} that compose the Q_β precision-ladder.

## What we know from main

  Q_β = Q_A · cos(α - bℏ_q²/2) · (1 - b²·ℏ_q^4) · (1 + c_3·ℏ_q^6) · ...
        \____F_0_____/    \__F_2_b²_/   \__F_3 (PR #657, "-2b³")_/

  - F_2 = 1 - b²·ℏ_q^4 — derived PR #661 from V_(2,1) Hoefsmit Kashiwara
  - F_3 = 1 - 2·b³·ℏ_q^6 — claimed PR #657 Track-C, hand-waved PR #664

## What this probe contributes (substantive new result)

The canonical Wenzl-Markov trace of σ_1² (Hopf+ braid) in H_n is
MARKOV-INVARIANT — same closed form for all n ≥ 2:

    tr_M(σ_1²) = (q^{5/2} - q^{1/2} + q^2 + q) / (q^2 + q)
               = 1 + (q-1)/q^{1/2}
               = 1 + ε·(1+ε)^{-1/2}     [substituting q = 1 + ε]

So the Taylor expansion of tr_M(σ_1²) - 1 at q = 1+ε is:

    ε·(1+ε)^{-1/2} = Σ_{k≥0} C(-1/2, k) · ε^{k+1}
                   = ε - ε²/2 + 3ε³/8 - 5ε⁴/16 + 35ε⁵/128 - 63ε⁶/256 + ...

The ε^{k+1} coefficient is the **binomial coefficient C(-1/2, k)**.

## Implications for F_n

If F_n were taken as the order-ε^{2n} coefficient of tr_M(σ_1²) - 1,
they would be:

    F_n^{Markov} := C(-1/2, 2n-1)     [the ε^{2n} coefficient]

    F_2 = ε^4 coeff = -5/16        ≈ -0.3125   (Markov)
    F_3 = ε^6 coeff = -63/256      ≈ -0.2461   (Markov)
    F_4 = ε^8 coeff = -429/2048    ≈ -0.2095   (Markov)

These DO NOT match the framework's claimed F_n values:

    F_2 framework = b² = 3/4       ≈ 0.7500
    F_3 framework = -2·b³ = -3√3/4 ≈ -1.2990
    F_4 framework = b² + 1/2 = 5/4 ≈ 1.2500

NOT EQUAL. The Q_β precision-ladder F_n are not the bare-Markov-trace
Taylor coefficients of σ_1²; they're a DIFFERENT decomposition.

## What this tells us

A genuine "F_n derivation" requires identifying:

  (a) WHICH braid β_n produces the categorical factor F_n in the
      Q_β precision-ladder expansion.
  (b) The MARKOV TRACE of β_n with the appropriate writhe/framing
      correction needed to match the precision-ladder convention.

For F_3 specifically: PR #657 Track-C claimed β_3 = "the V_(2,2,2)
channel of V_(2,1)⊗V_(2,1) in H_6" gives F_3 = 1 - 2·b³·ℏ_q^6. But
the bare canonical Markov of σ_1² in H_6 (computed here) gives a
DIFFERENT Taylor structure. So either:

  (1) β_3 ≠ σ_1², it's some V_(2,2,2)-projected object whose
      trace differs from bare σ_1².
  (2) The "ℏ_q^6 extraction" involves an order-h-by-order-h
      Q_β expansion (not just tr_M Taylor), with lower-order
      F_k factors absorbed before reading off F_3.
  (3) F_3 = 1 - 2·b³·ℏ_q^6 isn't actually derivable from the canonical
      Markov framework — it's a separate ansatz that happens to fit
      PR #655's empirical c_3 = -2 (symbol coefficient).

## Next-PR scope (genuine F_3 derivation)

The genuine F_3 derivation requires:

  (i)   Symbolically compute the projector onto V_(2,2,2) inside
        Hoefsmit V_(2,1) ⊗ V_(2,1) embedded in H_6.
  (ii)  Apply σ_1² to the projector image; take Markov trace.
  (iii) Show this projected trace equals -2·b³·ℏ_q^6 at order h^6.
  (iv)  Repeat for F_4, F_5, ..., establishing the F_n pattern.

This is substantial (each step requires careful symbolic work in
H_6). This probe is a CONSISTENCY check + scope-clarification, not
the full derivation.

Output: F-n-categorical-derivation-probe.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from markov_trace_canonical import tr_M_word  # noqa: E402
from hecke_symbolic import HA as h_sym, z_markov as z_sym  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    print("=" * 90)
    print("  F_n categorical derivation — canonical Markov of σ_1² Taylor analysis")
    print("=" * 90)
    print()

    # ─── Markov-invariance of tr_M(σ_1²) across H_n ───
    print("Step 1: confirm Markov-invariance of tr_M(σ_1²) across H_n (n=3,4,5,6).")
    print()
    forms: dict[int, sp.Expr] = {}
    for n in [3, 4, 5, 6]:
        trM = sp.cancel(tr_M_word((1, 1), n, z_sym, h_sym))
        forms[n] = trM
        print(f"  tr_M(σ_1² in H_{n}) = {trM}")
    assert all(forms[n] == forms[3] for n in [4, 5, 6]), "Markov-invariance violated!"
    print()
    print("  ✓ All four match — Markov-invariant (as expected).")
    print()

    # ─── Closed-form simplification ───
    print("Step 2: simplify the closed form.")
    trM_canonical = forms[3]
    q_pos = sp.Symbol("q", positive=True, real=True)
    trM_in_pos_q = sp.cancel(trM_canonical.subs(sp.Symbol("q"), q_pos))
    # Conjectured form: 1 + (q-1)/q^{1/2}
    conjectured = 1 + (q_pos - 1) / sp.sqrt(q_pos)
    delta = sp.cancel(trM_in_pos_q - conjectured)
    print(f"  symbolic       : {trM_in_pos_q}")
    print(f"  conjectured    : 1 + (q-1)/q^(1/2)")
    print(f"  difference     : {delta}")
    if delta.equals(0):
        print("  ✓ MATCH: tr_M(σ_1²) = 1 + (q-1)·q^(-1/2) EXACTLY.")
    print()

    # ─── Taylor expansion at q = 1+ε ───
    eps = sp.Symbol("ε", real=True)
    print("Step 3: Taylor expand tr_M(σ_1²) at q = 1+ε to order ε^10.")
    print()
    trM_eps = sp.series(trM_canonical.subs(sp.Symbol("q"), 1 + eps), eps, 0, 11).removeO()
    coeffs = {}
    print("  ε^k coefficients:")
    # Need a positive-q substitution to resolve sqrt(q) → numerical
    q_pos = sp.Symbol("q", positive=True, real=True)
    trM_pos = trM_canonical.subs(sp.Symbol("q"), q_pos).subs(q_pos, 1 + eps)
    trM_eps_pos = sp.series(trM_pos, eps, 0, 11).removeO()
    for k in range(11):
        ck = sp.cancel(trM_eps_pos.coeff(eps, k))
        coeffs[k] = ck
        if not ck.equals(0):
            print(f"    ε^{k}: {sp.nsimplify(ck)}  ≈ {float(ck.evalf()):+.10f}")
    print()

    # ─── Verify binomial C(-1/2, k) pattern ───
    print("Step 4: verify ε^k coefficients = C(-1/2, k-1) [for k ≥ 1].")
    print()
    from math import comb
    def binom_neg_half(k):
        """C(-1/2, k) = (-1)^k · (2k)! / (4^k · (k!)^2)."""
        if k == 0:
            return sp.Integer(1)
        return sp.Rational((-1) ** k) * sp.Rational(sp.factorial(2 * k), 4 ** k * sp.factorial(k) ** 2)

    print(f"    {'k':>3} {'ε^k coeff':>20} {'C(-1/2, k-1)':>20} {'match?':>10}")
    for k in range(1, 11):
        c_eps = coeffs[k]
        c_pred = binom_neg_half(k - 1)
        match = sp.cancel(c_eps - c_pred).equals(0)
        print(f"    {k:>3} {str(sp.nsimplify(c_eps)):>20} {str(c_pred):>20} {'✓' if match else '✗':>10}")
    print()

    # ─── F_n at order ε^{2n} ───
    print("Step 5: extract F_n candidate at order ε^{2n} from the bare tr_M.")
    print()
    print("  Framework's claimed F_n (per PR #655/657/661/664):")
    print("    F_2 = b² = 3/4         ≈ 0.7500   (Kashiwara, PR #661 derived)")
    print("    F_3 = -2·b³ = -3√3/4   ≈ -1.2990  (Hopf, PR #657 Track-C claimed)")
    print("    F_4 = b² + 1/2 = 5/4   ≈ 1.2500   (mixed, PR #665 claimed)")
    print()
    print("  Bare-tr_M ε^{2n} coefficient of tr_M(σ_1²):")
    for n in [2, 3, 4]:
        c = coeffs[2 * n]
        print(f"    ε^{2*n} ≈ {float(c.evalf()):+.6f}  =  {sp.nsimplify(c)}")
    print()
    print("  MISMATCH: bare-Markov coefficients DO NOT equal framework F_n values.")
    print("  This proves the Q_β precision-ladder F_n are NOT the bare tr_M(σ_1²)")
    print("  Taylor coefficients. They're a different decomposition — see audit doc")
    print("  docs/audits/2026-05-17-F-n-derivation-analysis.md.")
    print()

    # ─── Witness ───
    builder = (
        WitnessBuilder("F-n-categorical-derivation-probe", engine="sympy")
        .set_description(
            "F_n categorical derivation probe via canonical Markov trace of "
            "σ_1² (Hopf+ braid). Confirms Markov-invariance across H_n for "
            "n=3-6; verifies the closed form tr_M(σ_1²) = 1 + (q-1)·q^(-1/2); "
            "verifies the C(-1/2, k-1) binomial pattern in the ε^k Taylor "
            "coefficients; SHOWS the bare-Markov coefficients DO NOT equal "
            "the framework's claimed F_n values, surfacing the open work "
            "on which categorical object actually produces each F_n."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-F-n-derivation-analysis.md"
        )
        .add_data("trM_sigma1_sq_closed_form", "1 + (q-1)/q^(1/2)")
        .add_data("trM_sigma1_sq_symbolic", str(trM_canonical))
        .add_data("markov_invariant_across_n_3_to_6", True)
        .add_data("epsilon_taylor_coefficients_k_0_to_10",
                  {f"eps_{k}": str(sp.nsimplify(coeffs[k])) for k in range(11)})
        .add_data("bare_markov_F_n_candidates", {
            "F_2_eps4_coeff": str(sp.nsimplify(coeffs[4])),
            "F_3_eps6_coeff": str(sp.nsimplify(coeffs[6])),
            "F_4_eps8_coeff": str(sp.nsimplify(coeffs[8])),
        })
        .add_data("framework_F_n_values_at_q1", {
            "F_2_b_sq": str(sp.Rational(3, 4)),
            "F_3_minus_2_b_cubed": str(sp.Rational(-3) * sp.sqrt(3) / 4),
            "F_4_b_sq_plus_half": str(sp.Rational(5, 4)),
        })
        .add_assertion(
            name="trM_sigma1_sq_closed_form_holds",
            computed=bool(delta.equals(0)),
            expected=True,
            source="tr_M(σ_1²) = 1 + (q-1)·q^(-1/2), confirmed symbolically",
        )
        .add_assertion(
            name="bare_markov_F_3_NOT_equal_to_framework_F_3",
            computed=bool(sp.cancel(coeffs[6] - sp.Rational(-3) * sp.sqrt(3) / 4).equals(0)),
            expected=False,
            source=(
                "bare-Markov ε^6 = -63/256 ≈ -0.246; framework F_3 = -2·b³(q=1) "
                "= -3√3/4 ≈ -1.299. Different by ~5×. The Q_β precision-ladder "
                "F_n are not the bare-Markov Taylor coefficients."
            ),
        )
        .add_caveat(
            "This probe does NOT derive F_n from the canonical Markov "
            "framework. It surfaces the GAP between bare-Markov tr_M(σ_1²) "
            "Taylor coefficients and the framework's claimed F_n values. "
            "A genuine F_n derivation requires identifying which categorical "
            "object β_n produces each F_n factor — specifically for F_3, "
            "PR #657 Track-C's claim is V_(2,2,2) channel inside Hoefsmit "
            "V_(2,1)⊗V_(2,1) in H_6. This probe does not perform that "
            "projection — that's the genuine derivation work pending."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
