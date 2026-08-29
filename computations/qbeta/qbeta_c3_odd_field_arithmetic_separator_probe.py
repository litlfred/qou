#!/usr/bin/env python3
"""
Arithmetic separator (scope-(a) refinement of the CLOSED parity↔chirality
dictionary): the bar-ODD c₃ carrier's quadratic field is ℚ(√−19) (from
disc(C_Hopf)=−76=−4·19), which is DISTINCT from the bar-EVEN / 4₁ / Φ_b field
ℚ(√−3). The two channels are separated by their ramified ODD PRIME — 19 (odd,
Hopf) vs 3 (even, amphichiral 4₁). Sympy-exact. No c_k value, nothing wired, no
tier change (registry §8 flip-flop guard).

Context (all corpus, already closed):
  * parity↔chirality dictionary CLOSED (2026-07-07-parity-chirality-dictionary-closed):
    even ↔ amphichiral 4₁ (CS=0, 𝔙 real, trace field ℚ(√−3), resurgence e_k∈ℚ(√3));
    odd ↔ chiral Hopf ↔ C_Hopf(y)=y³−6y²+10y−6, disc=−76<0, complex roots.
  * KC19/KC20 + bridge: the odd carrier is anchor-INVARIANT (fixes the classical
    shadow C_Hopf(2)=−2=J_Hopf(1); does NOT carry the c₃ substrate swing, which
    lives in w(q)'s fibre structure).

WHAT IS NEW HERE (grep-confirmed not explicit in the corpus): the dictionary
records the disc SIGNS (even +17 real / odd −76 complex) but never states that the
odd carrier's quadratic FIELD ℚ(√−19) is arithmetically distinct from the 4₁/Φ_b
field ℚ(√−3), nor draws the ramified-odd-prime separator (19 vs 3).

Two exact facts + one strict scope guard:

  1. ODD CARRIER FIELD = ℚ(√−19). disc(C_Hopf) = −76 = −2²·19, so the cubic's
     quadratic resolvent subfield is ℚ(√−76) = ℚ(√−19); ramified odd prime 19.

  2. SEPARATOR FROM 4₁/Φ_b = ℚ(√−3). The even channel / figure-eight state
     integral lives in ℚ(√−3) (4₁ Eisenstein trace field; prime 3). ℚ(√−19) ≠
     ℚ(√−3) (19/3 not a rational square) ⇒ NEITHER field contains the other. So
     the 4₁/Φ_b arithmetic (prime 3) does NOT contain the odd carrier's
     field-of-definition (prime 19).

  3. SCOPE GUARD (STRICT — this is scope-(a), NOT a scope-(b) "Φ_b excluded"):
     the separator constrains the ALGEBRAIC / anchor-INVARIANT field-of-definition
     of the odd carrier only. It does NOT (i) exclude the Φ_b state-integral, which
     is a transcendental object that may carry arithmetic beyond its trace field,
     nor (ii) address the anchor-DEPENDENT c₃ swing, which lives in w(q)'s fibre
     structure (KC19) — a separate open problem. What it DOES say: any closure of
     the odd channel's algebraic content must SUPPLY the disc-19 Hopf field; a
     mechanism confined to ℚ(√−3) (e.g. the bare 4₁ perturbative expansion) cannot
     generate it. This sharpens the search target, it does not close or refute.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def main():
    Y = sp.symbols('Y')
    C_Hopf = Y**3 - 6*Y**2 + 10*Y - 6      # odd / chiral Hopf sector (KC20 §5)
    C_unknot = 2*Y**2 - 7*Y + 4            # even / unknot sector (for reference)

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    disc_hopf = sp.discriminant(C_Hopf, Y)          # -76
    # squarefree part of the discriminant = the quadratic subfield generator
    sf = sp.factorint(-disc_hopf)                   # 76 = 2^2 * 19
    squarefree = 1
    for p, e in sf.items():
        if e % 2 == 1:
            squarefree *= p
    # odd_field_gen = sqrt(-19)
    odd_ramified_prime = squarefree                 # 19

    # 1. odd carrier field = Q(sqrt(-19))
    check("odd_carrier_field_is_Qsqrt_minus19",
          disc_hopf == -76 and odd_ramified_prime == 19,
          f"disc(C_Hopf)={disc_hopf} = -2²·19 ⇒ quadratic subfield ℚ(√−19); "
          "ramified odd prime 19 (the odd/Hopf chiral channel)")

    # 2. distinct from the 4_1 / Phi_b field Q(sqrt(-3)), prime 3
    even_prime = 3
    distinct = (sp.sqrt(-odd_ramified_prime) != sp.sqrt(-even_prime)) and \
               (not sp.sqrt(sp.Rational(odd_ramified_prime, even_prime)).is_rational)
    check("separated_from_4_1_phib_field_Qsqrt_minus3",
          distinct and odd_ramified_prime != even_prime,
          f"odd ℚ(√−{odd_ramified_prime}) vs even/4₁/Φ_b ℚ(√−{even_prime}): "
          f"{odd_ramified_prime}/{even_prime} not a rational square ⇒ neither field contains "
          "the other; the 4₁/Φ_b arithmetic (prime 3) does NOT contain the odd carrier's field")

    # 3. scope guard: the separator is anchor-INVARIANT / algebraic; the swing is separate
    #    (encode the guard as a checked fact: C_Hopf is anchor-invariant at the shadow,
    #     so the field distinction is an algebraic statement, not a swing statement)
    c_hopf_shadow = C_Hopf.subs(Y, 2)               # -2 (classical, anchor-invariant)
    scope_ok = (c_hopf_shadow == -2)
    check("scope_guard_algebraic_not_swing",
          scope_ok,
          "SCOPE-(a): the field distinction is ALGEBRAIC (anchor-invariant; C_Hopf(2)=−2 fixed). "
          "It does NOT exclude the transcendental Φ_b, nor address the anchor-dependent c₃ swing "
          "(w(q) fibre, KC19) — it only says the odd algebraic field-of-definition is ℚ(√−19), "
          "not ℚ(√−3); a closure must SUPPLY the disc-19 field")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "ARITHMETIC SEPARATOR (scope-(a), new refinement of the closed parity↔chirality "
        "dictionary; no c_k value, nothing wired): the bar-ODD c₃ carrier's quadratic field is "
        "ℚ(√−19) (disc(C_Hopf)=−76=−2²·19), DISTINCT from the bar-EVEN / 4₁ / Φ_b field ℚ(√−3). "
        "The channels are separated by their ramified odd prime — 19 (odd, chiral Hopf) vs 3 "
        "(even, amphichiral 4₁) — and neither field contains the other (19/3 not a rational "
        "square). CONSEQUENCE (scope-(a)): the odd channel's anchor-invariant algebraic "
        "field-of-definition is NOT contained in the 4₁/Φ_b arithmetic; a closure supplying only "
        "ℚ(√−3) (e.g. the bare 4₁ perturbative expansion) cannot generate the disc-19 Hopf field "
        "— it must supply that field. STRICT SCOPE GUARD: this does NOT exclude the transcendental "
        "Φ_b state-integral (which may carry richer arithmetic) and does NOT address the "
        "anchor-dependent c₃ swing (w(q) fibre, KC19, separate). It sharpens the search target, "
        "does not close or refute. NO tier change; NOTHING WIRED."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "qbeta-c3-odd-field-arithmetic-separator",
        "description": "The bar-odd c₃ carrier field ℚ(√−19) (disc C_Hopf=−76) is distinct from "
                       "the even/4₁/Φ_b field ℚ(√−3); channels separated by ramified odd prime "
                       "19 vs 3. Scope-(a): a closure must supply the disc-19 field; does NOT "
                       "exclude Φ_b or address the c₃ swing. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-11-qbeta-c3-kc19-kc20-consistency.md",
        "tier": "symbolic-exact (sympy; field arithmetic refinement of the closed dictionary)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "disc_C_Hopf": int(disc_hopf), "odd_ramified_prime": int(odd_ramified_prime),
            "odd_field": "Q(sqrt(-19))", "even_4_1_phib_field": "Q(sqrt(-3))",
            "even_ramified_prime": 3, "disc_C_unknot": int(sp.discriminant(C_unknot, Y)),
            "verdict": verdict,
        },
        "context": {
            "refines": "docs/audits/2026-07-07-parity-chirality-dictionary-closed.md (adds the "
                       "explicit ℚ(√−19)≠ℚ(√−3) field separator, not previously stated)",
            "scope_a_only": "constrains the algebraic/anchor-invariant field-of-definition; does "
                            "NOT exclude Φ_b, does NOT address the anchor-dependent c₃ swing (KC19)",
            "gate": "registry §8 flip-flop guard — no c_k value, no wiring, no tier change",
        },
    }
    out = os.path.join(_here, "qbeta-c3-odd-field-arithmetic-separator.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
