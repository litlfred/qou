#!/usr/bin/env python3
"""qbeta_fmap_power_class_prune.py — Arm-1 of the power-class pincer (§4.4).

Executes the probe committed in the formalize-first gate
docs/scope/2026-07-06-qbeta-fmap-power-class-pincer-scope.md (§4.4): the
symbolic, anchor-free verification of the Arm-1 (integer-u grading)
obstructions against the pure-power f-map class f = A·(Δtr_M)^m, m = 1..6
(refuted-class map row C19, landed partial 2026-07-13 with Arm-2 Lean only).

Inputs (all exact, corpus-pinned):
  * Δtr_M = the atom-word Markov-trace difference rational
    (−u¹⁰−2u⁹−u⁸−2u⁶+4u⁵+2u⁴+u²−2u+1)/(4u⁴(u²+1)), u = √q, from the
    habiro-mode-to-ladder-bridge witness — the provenance of the pinned a_n.
  * The pinned ℏ_q-Taylor a₁..a₉ = −5/4, −13/8, −33/16, −77/32, −177/64,
    −25/8, −891/256, −3923/1024, −4277/1024 (C13 data, same witness),
    re-derived here exactly.
  * Recorded observation (not an input): the per-block paper closed forms
    weighted by the EXPLICIT CanonicalMarkovWeightsH3 instance give a
    DIFFERENT inhabitant (that instance is "one valid inhabitant of the
    class, NOT THE canonical Wenzl–Markov instance").

Arm-1 invariants verified (scope §4.2(1); ε := ℏ_q, u_L = b·ℏ_q² = O(ε²);
the ladder carries only integer u_L powers and NO u¹ rung — c₁ = 0 is the
PR #1602 Lean-proved cancellation):

  m odd (1,3,5): leading [ε^m]((Δtr_M)^m) = a₁^m ≠ 0 ⇒ the image starts at a
      HALF-INTEGER u_L power — forbidden. UNCONDITIONAL.
  m = 2: leading [ε²] = a₁² = 25/16 ≠ 0 ⇒ the image starts at u_L¹ — the
      forbidden c₁ rung. UNCONDITIONAL.
  m = 4, 6: leading order admissible (u_L², u_L³), but the FIRST ODD-ε
      coefficient [ε^{m+1}]((Δtr_M)^m) = m·a₁^{m−1}·a₂ ≠ 0 (exact) ⇒ the
      half-integer obstruction fires at sub-leading order. UNCONDITIONAL —
      this is the piece C19 recorded as conditional-only (ζ₄ arm) pending
      this probe.

RESULT (if all checks pass): the ENTIRE pure-power class f = A·(Δtr_M)^m,
m = 1..6, is refuted UNCONDITIONALLY on Arm-1 alone, with zero anchor
sweeps; Arm-2 (ζ₄ character parity, Lean `pow_even_faithful_four_mul_zero`)
stands as an independent conditional confirmation for even m. The surviving
f-space is non-monomial (the C19 "merges into the keystone W_λ axis"
characterization). Scope-(b) with the invariant cited: integer-u_L grading +
the Lean-proved c₁ = 0 rung. No c_k value produced; nothing wired; no fit.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent          # computations/probes
ROOT = HERE.parent                               # computations/
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))

q, u, h, eps = sp.symbols("q u h epsilon", positive=True)

A_PINNED = ["-5/4", "-13/8", "-33/16", "-77/32", "-177/64",
            "-25/8", "-891/256", "-3923/1024", "-4277/1024"]
N_ORD = 10   # ε-series order (need ε^7 for m=6; margin to ε^9)


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" Arm-1 power-class prune: f = A·(Δtr_M)^m, m = 1..6 (scope §4.4, exact)")
    print("=" * 78)

    # ── 1. the exact Δtr_M — the bridge (atom-word) object, the a_n provenance ──
    # The C13 a_n are the ℏ_q-Taylor of the FULL atom-word Markov-trace
    # difference tr_M(neutron) − tr_M(proton) (habiro-coefficients-atomic →
    # habiro-mode-to-ladder-bridge). NOTE (recorded, not assumed): the
    # per-block paper closed forms weighted by the EXPLICIT
    # CanonicalMarkovWeightsH3 instance (y = (z, 1/2−z, z), z = √q/(1+q) =
    # markov_parameter) produce a DIFFERENT inhabitant (ratio ≈ 1.52,
    # non-constant) — the explicit instance is "one valid inhabitant of the
    # class, NOT THE canonical Wenzl–Markov instance" (qbeta_utils docstring).
    # The pincer runs on the atom-word object, whose a_n are the pinned data.
    br = json.loads((ROOT / "habiro" / "habiro-mode-to-ladder-bridge.witness.json").read_text())
    num = sp.sympify(br["data"]["delta_trM"]["numerator"], locals={"u": u})
    den = sp.sympify(br["data"]["delta_trM"]["denominator"], locals={"u": u})
    dtr = (num / den).subs(u, sp.sqrt(q))

    # recorded observation: the explicit-instance per-block weighting differs
    pb = json.loads((ROOT / "qbeta" / "qbeta-per-block-paper-closed-forms.witness.json").read_text())
    forms = {k: sp.sympify(v, locals={"q": q}) for k, v in pb["data"]["paper_closed_forms"].items()}
    z = sp.sqrt(q) / (1 + q)
    dtr_explicit = sp.simplify(z * forms["(3)"] + (sp.Rational(1, 2) - z) * forms["(2,1)"] + z * forms["(1,1,1)"])
    explicit_differs = sp.simplify(dtr_explicit - dtr) != 0
    print(f"\n[1] Δtr_M = bridge atom-word rational (a_n provenance); explicit-instance"
          f" per-block weighting is a different inhabitant: {explicit_differs}")

    # ── 2. exact ℏ_q-Taylor + cross-check a₁..a₉ ──
    #     ℏ_q = (q−1)/q  ⇔  q = 1/(1−ε)
    dtr_eps = dtr.subs(q, 1 / (1 - eps))
    ser = sp.series(dtr_eps, eps, 0, N_ORD).removeO()
    a = [sp.simplify(ser.coeff(eps, n)) for n in range(N_ORD)]
    ok_a = all(sp.Rational(A_PINNED[n - 1]) == a[n] for n in range(1, 10)) and a[0] == 0
    print(f"[2] ℏ_q-Taylor a₁..a₉ match the pinned C13 values exactly: {ok_a}")
    for n in range(1, 5):
        print(f"      a_{n} = {a[n]}")
    assert ok_a, "pinned a_n cross-check failed"

    # ── 3. the Arm-1 obstructions, m = 1..6, exact ──
    print("\n[3] Arm-1 obstructions (ε := ℏ_q; u_L = O(ε²); no u¹ rung — c₁=0, PR #1602):")
    results = {}
    dm = sp.Integer(1)
    for m in range(1, 7):
        dm = sp.expand(dm * ser)                      # (Σ aₙ εⁿ)^m, truncated
        dm = sum(dm.coeff(eps, n) * eps ** n for n in range(N_ORD))  # re-truncate
        if m % 2 == 1:                                 # odd m: leading ε^m
            lead = sp.simplify(dm.coeff(eps, m))
            verdict = "REFUTED (leading half-integer u_L^{%s/2}; [ε^%d]=%s ≠ 0)" % (m, m, lead)
            key_coeff, expect = lead, sp.simplify(a[1] ** m)
            ok = (lead != 0) and sp.simplify(lead - expect) == 0
        elif m == 2:                                   # forbidden u¹ rung
            lead = sp.simplify(dm.coeff(eps, 2))
            verdict = "REFUTED (forbidden c₁ rung; [ε²]=%s = a₁² ≠ 0)" % lead
            key_coeff, expect = lead, sp.simplify(a[1] ** 2)
            ok = (lead != 0) and sp.simplify(lead - expect) == 0
        else:                                          # m = 4, 6: first odd-ε subleading
            sub = sp.simplify(dm.coeff(eps, m + 1))
            expect = sp.simplify(m * a[1] ** (m - 1) * a[2])
            verdict = ("REFUTED unconditional (sub-leading odd-ε fires: [ε^%d]=%s = m·a₁^%d·a₂ ≠ 0)"
                       % (m + 1, sub, m - 1))
            key_coeff = sub
            ok = (sub != 0) and sp.simplify(sub - expect) == 0
        results[f"m={m}"] = {"verdict": verdict, "obstruction_coeff": str(key_coeff),
                             "closed_form_check": str(expect), "exact_match": bool(ok)}
        print(f"    m={m}: {verdict}   [closed-form check: {ok}]")
        assert ok, f"obstruction coefficient mismatch at m={m}"

    print("\n  PINCER COMPLETE: pure-power class m=1..6 refuted UNCONDITIONALLY on Arm-1;")
    print("  Arm-2 (ζ₄, Lean) stands as independent conditional confirmation for even m.")
    print("  Surviving f-space: non-monomial (keystone W_λ axis). No c_k; no fit; no wiring.")

    witness = {
        "computation": "qbeta-fmap-power-class-prune",
        "description": (
            "Arm-1 (integer-u grading) symbolic verification of the power-class "
            "pincer (scope doc 2026-07-06, refuted-class row C19): Δtr_M = the "
            "atom-word bridge rational (the a_n provenance); pinned a_1..a_9 "
            "re-derived exactly; the explicit-instance per-block weighting is "
            "recorded as a DIFFERENT inhabitant (not used). Obstructions all fire with exact closed forms: odd m -> "
            "leading a_1^m != 0 (half-integer u_L); m=2 -> a_1^2 = 25/16 (forbidden "
            "c_1 rung, PR #1602); m=4,6 -> first odd-eps sub-leading coefficient "
            "m*a_1^(m-1)*a_2 != 0 (half-integer obstruction at sub-leading order). "
            "FULL pure-power class f = A*(Delta tr_M)^m, m=1..6, refuted "
            "UNCONDITIONALLY on Arm-1 alone (zero anchor sweeps); the zeta_4 Arm-2 "
            "Lean prune remains an independent conditional confirmation for even m. "
            "Scope-(b) with invariant cited (integer-u_L grading + Lean-proved "
            "c_1=0). Surviving f-space: non-monomial (keystone W_lambda axis). "
            "auditOnly; no c_k value; no fit; no wiring."
        ),
        "audit_only": True,
        "content_block": "prop:q-beta-categorical-precision-ladder",
        "inputs": {
            "per_block_closed_forms_recorded_differs": "computations/qbeta/qbeta-per-block-paper-closed-forms.witness.json",
            "bridge_rational": "computations/habiro/habiro-mode-to-ladder-bridge.witness.json",
            "explicit_weights": "y = (z, 1/2 - z, z), z = sqrt(q)/(1+q) (CanonicalMarkovWeightsH3.explicitInstance)",
        },
        "hbar_taylor_a1_a9": [str(a[n]) for n in range(1, 10)],
        "obstructions": results,
        "assertions": [
            {"label": "explicit-instance per-block weighting recorded as a DIFFERENT inhabitant", "passed": bool(explicit_differs)},
            {"label": "pinned a_1..a_9 reproduced exactly", "passed": bool(ok_a)},
            {"label": "all six Arm-1 obstructions fire with exact closed forms",
             "passed": all(r["exact_match"] for r in results.values())},
        ],
    }
    witness["allPassed"] = all(x["passed"] for x in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-fmap-power-class-prune.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
