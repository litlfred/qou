#!/usr/bin/env python3
"""The Milnor deficit sign (−1)^{A−1} (#4389) and my weight bar-sign (−1)^{n-1} (#4399) agree in VALUE
but not in MECHANISM — the weight-parity ⇒ deficit-sign derivation route is REFUTED. Exact (sympy),
no fit. Anti-laundering safeguard: the (−1)^{A−1} match is a convergence, not a derivation.

CONTEXT: #4399 Tie B flagged the coincidence (−1)^{3A−1}=(−1)^{A−1} between the Ocneanu-weight
bar-parity and the Milnor-parity cluster-deficit sign as a "candidate derivation, not proved". This
probe settles it: the route is refuted, with a concrete structural reason.

THE STRUCTURAL OBSTRUCTION (exact):
  A. The proved Borromean deficit closed form is 1 − τ_Borr = h⁴(3+h²)/(h²+4):
       - leading order h⁴ = h^{2(A−1)} (A=3) — the Milnor / (A−1)-fold-commutator depth;
       - the weight prefactor h^{n-1} = h⁸ (n=9) is ABSENT — because τ_A is a NORMALIZED (link/unlink)
         ratio, the (q−q⁻¹)^{n-1} Ocneanu weight prefactor CANCELS;
       - the deficit is bar-even (a function of h²) — its sign is a leading-COEFFICIENT effect, not a
         bar-parity flip.
  B. Orders (all A): deficit order 2(A−1) is even and STRICTLY BELOW the weight order 3A−1
     (3A−1 − 2(A−1) = A+1 > 0). So the weight prefactor is subleading AND cancelled ⇒ it cannot set
     the deficit's leading sign.
  C. Parity coincidence: (−1)^{3A−1} = (−1)^{A−1} (numerically equal) — but from DISTINCT-order
     objects (B). Same value, different mechanism.

VERDICT (scope-(a), refutation): the weight bar-parity CANNOT be the mechanism of the Milnor deficit
sign (the weight cancels in the normalized trace). The (−1)^{A−1} match is a CONVERGENCE via distinct
mechanisms (Ocneanu-weight prefactor parity vs (A−1)-fold-commutator / Milnor depth), NOT a
derivation. This sharpens #4399 Tie B and forbids passing the coincidence off as a derivation of the
sign law #4389 leaves open (A=4 measured). Other derivations of the sign law remain open.

Lean: QOU/MassTheory/MilnorWeightParityConvergence.lean (deficit_order_even, weight_order_gt_deficit,
weight_parity_eq_cluster_sign, convergence_not_derivation) — sorry-free.

EXPLORATORY — audit + witness only; no fit, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    h = sp.symbols("h", positive=True)
    deficit = h ** 4 * (3 + h ** 2) / (h ** 2 + 4)          # 1 − τ_Borr, proved closed form (A=3)
    series = sp.expand(sp.series(deficit, h, 0, 8).removeO())
    # lowest-degree (leading) power in h
    terms = sp.Add.make_args(series)
    lead_pow = min(int(sp.degree(sp.Poly(t, h))) for t in terms)
    bar_even = sp.simplify(deficit.subs(h, -h) - deficit) == 0
    weight_prefactor_absent = (lead_pow == 4)               # h⁴ present, h⁸ (=n-1 for A=3) absent

    rows = []
    for A in (2, 3, 4):
        n = 3 * A
        rows.append({
            "A": A, "n": n,
            "deficit_order_2A_minus_2": 2 * (A - 1),
            "weight_order_n_minus_1": n - 1,
            "weight_order_exceeds_deficit": (n - 1) > 2 * (A - 1),
            "weight_bar_sign": (-1) ** (n - 1),
            "milnor_deficit_sign": (-1) ** (A - 1),
            "signs_equal": ((-1) ** (n - 1)) == ((-1) ** (A - 1)),
        })
    all_signs_equal = all(r["signs_equal"] for r in rows)
    all_weight_subleading = all(r["weight_order_exceeds_deficit"] for r in rows)

    result = {
        "A_borromean_closed_form": {
            "deficit": "h⁴(3+h²)/(h²+4)  (1 − τ_Borr, proved, A=3)",
            "leading_power": lead_pow,
            "leading_is_2A_minus_2": lead_pow == 4,
            "weight_prefactor_h8_absent": bool(weight_prefactor_absent),
            "bar_even": bool(bar_even),
            "meaning": "leading h⁴=h^{2(A−1)} (Milnor depth); the h⁸=h^{n-1} Ocneanu weight prefactor "
                       "is ABSENT — τ_A is a normalized ratio, the weight CANCELS. Deficit bar-even ⇒ "
                       "sign is a coefficient effect, not a bar-parity flip.",
        },
        "B_C_order_and_parity": {
            "rows": rows,
            "all_weight_orders_exceed_deficit": bool(all_weight_subleading),
            "all_signs_equal": bool(all_signs_equal),
        },
        "verdict": {
            "classification": "scope-(a) REFUTATION of the weight-parity ⇒ deficit-sign route.",
            "reason": "the (q−q⁻¹)^{n-1} weight prefactor cancels in the normalized trace τ_A and is "
                      "higher-order than the deficit — it cannot set the deficit's leading sign.",
            "convergence_not_derivation": "the (−1)^{A−1} match is a convergence via distinct "
                                          "mechanisms (weight-prefactor parity vs Milnor commutator "
                                          "depth), NOT a derivation. Sharpens #4399 Tie B.",
            "sign_law_status": "the Milnor-parity sign law (#4389) remains OPEN (A=4 measured); this "
                               "refutes ONE candidate derivation route, not the derivability itself.",
            "lean": "MilnorWeightParityConvergence.lean (sorry-free)",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "milnor-weight-parity-convergence",
        "description": ("The Milnor deficit sign (−1)^{A−1} (#4389) and the Ocneanu-weight bar-sign "
                        "(−1)^{n-1} (#4399) agree in VALUE but not MECHANISM. The proved Borromean "
                        "deficit h⁴(3+h²)/(h²+4) has leading order h⁴=h^{2(A−1)} with the weight "
                        "prefactor h^{n-1}=h⁸ ABSENT (τ_A is a normalized ratio ⇒ the weight cancels), "
                        "and is bar-even (sign is a coefficient effect). The weight order 3A−1 strictly "
                        "exceeds the deficit order 2(A−1), so the (cancelled, subleading) weight parity "
                        "CANNOT set the deficit sign. Hence the weight-parity ⇒ deficit-sign derivation "
                        "route is REFUTED (scope-a); the (−1)^{A−1} match is a convergence via distinct "
                        "mechanisms, not a derivation — sharpening #4399 Tie B and forbidding it being "
                        "passed off as a derivation of the sign law #4389 leaves open. Lean-proved "
                        "order/parity facts (MilnorWeightParityConvergence.lean). scope-(a), audit-"
                        "only, nothing wired; no fit."),
        "audit_only": True,
        "tier": "scope-(a) refutation of a derivation route (exact closed-form structure + Lean-proved "
                "order/parity facts); no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ / Milnor-parity sign law — mechanism of the deficit sign",
            "lean": "QOU/MassTheory/MilnorWeightParityConvergence.lean",
            "builds_on": "#4399 Tie B ((−1)^{A−1} convergence), #4389 (Milnor-parity sign law)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "milnor-weight-parity-convergence", payload,
        script_path=__file__, engine="sympy", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("deficit_leading_is_h4_weight_h8_absent", computed=str(bool(weight_prefactor_absent)), expected="True")
    wb.add_assertion("deficit_bar_even", computed=str(bool(bar_even)), expected="True")
    wb.add_assertion("all_weight_orders_exceed_deficit", computed=str(bool(all_weight_subleading)), expected="True")
    wb.add_assertion("all_signs_equal_convergence", computed=str(bool(all_signs_equal)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Milnor deficit sign vs weight bar-parity: convergence, NOT derivation ===")
    print(f"A. Borromean deficit h⁴(3+h²)/(h²+4): leading power = {lead_pow} (=h⁴=h^2(A-1)); "
          f"weight h⁸ absent: {weight_prefactor_absent}; bar-even: {bar_even}")
    print("B/C. order table (A | deficit 2(A-1) | weight n-1 | signs equal):")
    for r in rows:
        print(f"      A={r['A']} n={r['n']}: deficit {r['deficit_order_2A_minus_2']}  weight {r['weight_order_n_minus_1']}  "
              f"weight>deficit={r['weight_order_exceeds_deficit']}  sign {r['weight_bar_sign']:+d}=={r['milnor_deficit_sign']:+d}")
    print(f"VERDICT (scope-a): weight prefactor CANCELS in the normalized τ_A + is higher-order ⇒ cannot "
          f"set the deficit sign. The (−1)^(A-1) match is CONVERGENCE via distinct mechanisms, NOT a "
          f"derivation. Sign law #4389 stays open. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
