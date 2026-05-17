#!/usr/bin/env python3
"""Probe: extract c_3 from Taylor expansion of tr_M(σ_1²) at q=1+ε.

Ports PR #661's c_2 = b² derivation methodology to c_3. PR #661 derived
c_2 by expanding F_2 = 1 - b²·ℏ_q^4 at q=1+ε and reading off the
ε^4 coefficient; this probe attempts the analogous extraction at
ε^6 for c_3, working from the actual Markov trace of σ_1² rather
than PR #664's hardcoded textbook Jones value.

Q_β factor at N=3 (per PR #655, PR #664):
    F_3 = 1 + c_3 · ℏ_q^6
PR #664 claims c_3 = -2 via "Jones-Hopf at q=1" reasoning.

Method:
  ℏ_q = (q-1)/q = ε/(1+ε), so ℏ_q^6 ~ ε^6 (leading order).
  Compute tr_M(σ_1²) symbolically; substitute q → 1+ε; Taylor
  expand to ε^6; read off the coefficient.

Result (NEGATIVE):
  - tr_M_symbolic(σ_1²) at ε^6 = +7/8
  - tr_M_canonical(σ_1²) at ε^6 = -63/256
  - Neither equals -2.

PR #664's c_3 = -2 claim is not recoverable from a direct Taylor
expansion of σ_1² in H_2 under either of the two tr_M implementations
on main. Either:

  (a) c_3 in the Q_β ladder requires a DIFFERENT categorical object
      (not σ_1² in H_2 — perhaps a V_(2,2,2)-projected object in H_6
      as PR #664's proof sketch hand-waves), OR
  (b) c_3 requires a WRITHE-CORRECTED tr_M, with the correction
      factor itself an order-ε^6 expansion, OR
  (c) the Hopf-Jones-textbook value -(q + q⁻¹) at q=1 is the c_3
      value by *convention* (the precision-ladder is defined to pick
      up this normalization), not by Taylor extraction.

In any of cases (a)/(b)/(c), PR #664's probe still hardcodes the
answer (-2 written twice, "verified" to be equal) and the genuine
derivation is open.

Output: c3-taylor-extraction.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hoefsmit_symbolic import tr_M_symbolic, Q  # noqa: E402
from markov_weights_symbolic import tr_M_canonical  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    eps = sp.Symbol("ε", real=True)
    q_eps = 1 + eps
    crossings = [(0, "sigma"), (0, "sigma")]

    print("=" * 90)
    print("  Probe — c_3 from Taylor extraction of tr_M(σ_1²) at q=1+ε")
    print("=" * 90)
    print()
    print("  Method: ε = q - 1 → Taylor expansion to ε^6; coefficient")
    print("          ε^6 is the c_3 candidate under the order-h^6")
    print("          identification (since ℏ_q ~ ε near q=1).")
    print()

    # (i) tr_M_symbolic (Hoefsmit, w_λ·χ^λ/f^λ)
    trM_sym = tr_M_symbolic(crossings, 2)
    trM_sym_eps = sp.series(trM_sym.subs(Q, q_eps), eps, 0, 7).removeO()
    coeffs_sym = {k: sp.cancel(trM_sym_eps.coeff(eps, k)) for k in range(7)}
    print("  (i) tr_M_symbolic(σ_1²):")
    for k, c in coeffs_sym.items():
        print(f"      ε^{k}: {c}")
    print()

    # (ii) tr_M_canonical (Wenzl, y_λ·χ^λ)
    trM_can, _ = tr_M_canonical(crossings, 2)
    trM_can_simple = sp.cancel(trM_can.subs(Q, q_eps))
    trM_can_eps = sp.series(trM_can_simple, eps, 0, 7).removeO()
    coeffs_can = {
        k: sp.nsimplify(sp.cancel(trM_can_eps.coeff(eps, k)), rational=True, tolerance=1e-10)
        for k in range(7)
    }
    print("  (ii) tr_M_canonical(σ_1²):")
    for k, c in coeffs_can.items():
        print(f"      ε^{k}: {c}")
    print()

    # ── Compare to PR #664's c_3 = -2 ──
    c3_claimed = sp.Integer(-2)
    c3_from_sym = coeffs_sym[6]
    c3_from_can = coeffs_can[6]
    sym_matches = sp.cancel(c3_from_sym - c3_claimed).equals(0)
    can_matches = sp.cancel(c3_from_can - c3_claimed).equals(0)

    print(f"  PR #664 claim: c_3 = -2")
    print(f"  ε^6 from tr_M_symbolic:  {c3_from_sym}   matches -2? {sym_matches}")
    print(f"  ε^6 from tr_M_canonical: {c3_from_can}   matches -2? {can_matches}")
    print()

    if not sym_matches and not can_matches:
        print("  RESULT: neither tr_M implementation's ε^6 coefficient")
        print("  for σ_1² equals -2.  PR #664's c_3 = -2 claim is not")
        print("  recoverable from a Taylor extraction of σ_1² in H_2.")
    print()

    builder = (
        WitnessBuilder("c3-taylor-extraction", engine="sympy")
        .set_description(
            "Genuine c_3 extraction attempt via Taylor expansion of "
            "tr_M(σ_1²) at q=1+ε to ε^6. Ports PR #661's c_2 = b² "
            "methodology. NEGATIVE RESULT: neither of the two tr_M "
            "implementations on main yields ε^6 = -2 for σ_1²; "
            "PR #664's c_3 = -2 claim is not recoverable from this "
            "direct route. The probe documents that the c_3 categorical "
            "derivation requires either (a) a different categorical "
            "object (V_(2,2,2)-projected in H_6), (b) a writhe-corrected "
            "tr_M, or (c) a convention choice the PR didn't make."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-pr-664-c3-c4-critical-review.md"
        )
        .add_data("taylor_coefficients_tr_M_symbolic",
                  {f"eps_{k}": str(v) for k, v in coeffs_sym.items()})
        .add_data("taylor_coefficients_tr_M_canonical",
                  {f"eps_{k}": str(v) for k, v in coeffs_can.items()})
        .add_data("c3_claimed_pr664", -2)
        .add_data("c3_from_tr_M_symbolic_eps_6", str(c3_from_sym))
        .add_data("c3_from_tr_M_canonical_eps_6", str(c3_from_can))
        .add_data("either_matches_negative_2", bool(sym_matches or can_matches))
        .add_assertion(
            name="taylor_extraction_does_not_yield_pr664_value",
            computed=bool(sym_matches or can_matches),
            expected=False,
            source=(
                "Direct Taylor extraction of σ_1² at q=1+ε to ε^6 in "
                "either tr_M implementation gives values (7/8 or -63/256) "
                "that do not match PR #664's c_3 = -2 claim."
            ),
        )
        .add_caveat(
            "This probe DOES NOT disprove c_3 = -2.  It shows the simplest "
            "interpretation of PR #664's claim (\"c_3 is the ε^6 coefficient "
            "of σ_1²'s Markov trace\") is FALSE.  The genuine derivation "
            "could still recover c_3 = -2 via the V_(2,2,2) channel in H_6 "
            "(per PR #664's hand-waved proof sketch Step 2) or via a "
            "writhe-correction step — both of which remain to be done."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
