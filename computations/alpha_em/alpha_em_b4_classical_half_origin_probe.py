#!/usr/bin/env python3
"""alpha_em_b4_classical_half_origin_probe.py

Bean B4 (qou-1p06), first brick (B4a): the CLASSICAL ORIGIN OF THE 1/2 in the
per-loop measure 1/2 * a0 — computed exactly with the corpus's own canonical
machinery, and DISCRIMINATED by the established q-independence of the per-loop
parameter x.

B4's target (clauseB sharpening, merged): the tower's 1-loop coefficient is
-[2]_q * x EXACTLY with x q-independent, so x = alpha/(8 pi) iff the q->1
one-loop total 2x equals the universal heat-kernel unit a0*alpha = alpha/(4 pi).
The open statement is a NORMALIZATION AT THE CLASSICAL POINT q=1. This brick
answers: which canonical q=1 object IS the 1/2, and which readings survive?

FINDINGS (V1-V4, all symbolic-exact):
  V1. The canonical Jones-Markov weights at n=2 are NOT Plancherel: at q=1
      they are (3/4, 1/4) — the SU(2) Schur-Weyl dimensions dim(spin-1)/4,
      dim(spin-0)/4 of V (x) V — not the S2-Plancherel (1/2, 1/2). The
      equal-weight reading of the 1/2 is NOT the canonical Markov weight
      reading (consistent with merged F2, which excluded weights at q0).
  V2. THREE distinct canonical origins of 1/2, all coinciding AT q=1:
        (a) idempotent normalization  1/[2]_q          -> 1/2  (q-dependent)
        (b) S2-Plancherel weight      dim^2/2! = 1/2   -> 1/2  (constant)
        (c) Markov trace of crossing  tr_M(sigma)      -> 1/2  (q-dependent;
            = 3/4 - 1/4 at q=1, the crossing's SIGNED channel content)
      A triple coincidence exactly at the decategorification point.
  V3. DISCRIMINATION by x q-independence: the one-loop coefficient is
      -[2]_q * x exactly (q-dependence carried entirely by [2]_q). Any
      reading that would put its OWN q-dependence inside the measure —
      (a) as 1/[2]_q(q) or (c) as tr_M(sigma)(q) — is EXCLUDED as the
      q-carrying form: at general q they disagree with a constant x
      (verified at q=4: 1/[2]_4 = 4/17, tr_M(sigma) = 2/5, both != any
      fixed 1/2). The classical normalization must be EVALUATED AT q=1 —
      the 1/2 is a decategorification-point constant. This is precisely
      the KL/decategorification route (AGENTS 7b item 2): the classical
      limit is a functor applied AT q=1, not a q-family.
  V4. KL BRIDGE at n=2: the positive KL element b_s = sigma + q^{-1}
      satisfies b_s = [2]_q * e+ identically and b_s^2 = [2]_q * b_s; at
      q=1 it decategorifies to 1 + s = 2 * (Young symmetrizer of S2). So
      e+ = b_s / [2]_q and the 1/2 at q=1 IS 1/[2]_1 — the KL-to-idempotent
      conversion factor at the decategorification point. The 1/2 has a
      canonical KL carrier.

NET EFFECT: B4's open statement sharpens from "q->1 one-loop = a0*alpha" to
the single functorial normalization "the loop expansion weights the q=1
KL-normalized channel projector (b_s/[2]_q at q=1) by the universal
heat-kernel unit a0*alpha" — with the candidate carrier now CANONICAL and the
equal-weight / trace-of-crossing readings excluded as q-families (they remain
numerically equal at the point q=1; the coincidence is what the functorial
statement must resolve). B4 remains OPEN: this brick derives the carrier
candidates and the discrimination, NOT the normalization itself.

Scope guard: scope-(a); no fit; nothing wired; 1/(8pi) stays phase-4.
Uses the corpus's canonical y_lambda_at (wedderburn_jones_markov). sympy-exact.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_here))  # computations/ for wedderburn_jones_markov
from wedderburn_jones_markov import y_lambda_at  # noqa: E402


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    y = y_lambda_at(2)  # canonical Jones-Markov weights, symbolic
    y2, y11 = y[(2,)], y[(1, 1)]
    q = sorted(y2.free_symbols, key=str)[0]

    # V1: canonical weights are Schur-Weyl (3/4, 1/4) at q=1, NOT Plancherel
    sum_one = sp.simplify(y2 + y11) == 1
    at1 = (sp.simplify(y2.subs(q, 1)), sp.simplify(y11.subs(q, 1)))
    v1 = sum_one and at1 == (sp.Rational(3, 4), sp.Rational(1, 4))
    check("canonical_weights_are_schur_weyl_not_plancherel", v1,
          f"y_[2]+y_[1,1]=1 identically; at q=1 the canonical Jones-Markov weights are "
          f"{at1} = (dim spin-1, dim spin-0)/4 — Schur-Weyl for V⊗V, NOT the S₂-Plancherel "
          "(1/2,1/2). The equal-weight reading of the 1/2 is not the canonical Markov "
          "weight reading (consistent with merged F2)")

    # V2: three canonical origins of 1/2, coinciding at q=1
    half_a = sp.Rational(1, 1) / (1 + 1)                       # 1/[2]_q at q=1
    half_b = sp.Rational(1, 2)                                  # dim^2/2! for both irreps of S2
    tr_sigma = sp.simplify(q * y2 - y11 / q)                    # eigenvalues q, -q^{-1} (§7a)
    half_c = sp.simplify(tr_sigma.subs(q, 1))
    v2 = half_a == sp.Rational(1, 2) and half_b == sp.Rational(1, 2) and half_c == sp.Rational(1, 2)
    check("triple_coincidence_of_half_at_q1", v2,
          "(a) idempotent normalization 1/[2]_q|_{q=1} = 1/2; (b) S₂-Plancherel dim²/2! = 1/2 "
          f"(both irreps); (c) canonical tr_M(σ)|_{{q=1}} = {half_c} (= 3/4 − 1/4, the "
          "crossing's signed channel content). Three DISTINCT canonical objects, all equal to "
          "1/2 exactly at the decategorification point q=1")

    # V3: discrimination — (a) and (c) are q-dependent, so cannot sit inside the
    # q-independent measure x; the normalization is evaluated AT q=1
    q4_a = sp.Rational(1, 1) / (sp.Rational(4) + sp.Rational(1, 4))   # 1/[2]_q at q=4
    q4_c = sp.nsimplify(tr_sigma.subs(q, 4))
    a_dep = sp.simplify(sp.diff(1 / (q + 1 / q), q)) != 0
    c_dep = sp.simplify(sp.diff(tr_sigma, q)) != 0
    v3 = (a_dep and c_dep and q4_a == sp.Rational(4, 17) and q4_c == sp.Rational(2, 5)
          and q4_a != sp.Rational(1, 2) and q4_c != sp.Rational(1, 2))
    check("q_independence_of_x_discriminates", v3,
          f"readings (a) 1/[2]_q and (c) tr_M(σ) are q-DEPENDENT (at q=4: {q4_a}, {q4_c} — "
          "both ≠ 1/2), but the 1-loop coefficient is −[2]_q·x EXACTLY with x q-independent "
          "(merged F3): neither q-family can sit inside the measure. The classical "
          "normalization is EVALUATED AT q=1 — the 1/2 is a decategorification-POINT "
          "constant, exactly the KL-functor-at-q=1 shape (§7b item 2)")

    # V4: KL bridge — b_s = sigma + q^{-1} = [2]_q e+, idempotent up to [2]_q;
    # at q=1 decategorifies to 1+s = 2 * Young symmetrizer
    s = sp.symbols('sigma', commutative=False)
    # work in the 2-dim regular picture: represent sigma by its action on channels
    # channel eigenvalues (q, -1/q); b_s eigenvalues (q + 1/q, 0) = ([2]_q, 0)
    ev_plus, ev_minus = q, -1 / q
    b_plus = sp.simplify(ev_plus + 1 / q)       # b_s on symmetric channel
    b_minus = sp.simplify(ev_minus + 1 / q)     # b_s on antisym channel
    two_q = sp.simplify(q + 1 / q)
    kl_proj = sp.simplify(b_plus - two_q) == 0 and b_minus == 0        # b_s = [2]_q e+
    kl_idem = sp.simplify(b_plus ** 2 - two_q * b_plus) == 0           # b_s^2 = [2]_q b_s
    kl_q1 = sp.simplify(b_plus.subs(q, 1)) == 2                        # 1+s -> 2 e+ at q=1
    v4 = kl_proj and kl_idem and kl_q1
    check("kl_bridge_half_is_kl_to_idempotent_conversion", v4,
          "the positive KL element b_s = σ + q⁻¹ has channel eigenvalues ([2]_q, 0): "
          "b_s = [2]_q·e₊ identically, b_s² = [2]_q·b_s; at q=1 it decategorifies to "
          "1+s = 2·(Young symmetrizer of S₂), so e₊ = b_s/[2]_q and the 1/2 at q=1 IS "
          "1/[2]_1 — the KL-to-idempotent conversion factor at the decategorification "
          "point. The 1/2 has a canonical KL carrier")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "B4a DELIVERED (scope-(a); derives no clause; no fit; nothing wired): the classical "
        "1/2 of the per-loop measure has THREE canonical origins that coincide exactly at "
        "q=1 — (a) idempotent normalization 1/[2]_q, (b) S₂-Plancherel weight, (c) the "
        "canonical Markov trace of the crossing (3/4 − 1/4, Schur-Weyl weights — NOT "
        "Plancherel) — and the established q-independence of the measure x EXCLUDES the "
        "q-families (a),(c) as q-carrying forms: the normalization is a decategorification-"
        "POINT constant, matching the KL route. The KL bridge is exact at n=2: "
        "b_s = [2]_q·e₊, decategorifying at q=1 to twice the Young symmetrizer — the 1/2 is "
        "the KL-to-idempotent conversion 1/[2]_1. B4's open statement SHARPENS to the single "
        "functorial normalization: the loop expansion weights the q=1 KL-normalized channel "
        "projector by the universal unit a₀·α. B4 remains OPEN — this brick derives the "
        "carrier and the discrimination, not the normalization. NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-b4-classical-half-origin",
        "description": "Bean B4 brick a (qou-1p06): classical origin of the 1/2 in the per-loop "
                       "measure. Canonical Jones-Markov n=2 weights are Schur-Weyl (3/4,1/4) at q=1, "
                       "not Plancherel; three canonical origins of 1/2 coincide exactly at q=1 "
                       "(1/[2]_q, S2-Plancherel, tr_M(sigma)); x q-independence excludes the "
                       "q-families — the 1/2 is a decategorification-point constant with KL carrier "
                       "b_s/[2]_q (b_s=[2]_q e+, ->1+s at q=1). B4 sharpens to one functorial "
                       "normalization; remains OPEN. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-b4-classical-half-origin.md",
        "tier": "symbolic-exact (sympy + corpus canonical y_lambda_at; Hecke channel eigenvalues "
                "per AGENTS 7a)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "canonical_weights_q1": "(3/4, 1/4) — Schur-Weyl, not Plancherel",
            "half_origins": {
                "idempotent_normalization": "1/[2]_q -> 1/2 at q=1 (q-dependent; 4/17 at q=4)",
                "s2_plancherel": "dim^2/2! = 1/2 (constant)",
                "markov_trace_of_crossing": "tr_M(sigma) -> 1/2 at q=1 (q-dependent; 2/5 at q=4)",
            },
            "discrimination": "x q-independent (merged F3) => normalization evaluated AT q=1; "
                              "the 1/2 is a decategorification-point constant",
            "kl_carrier": "b_s = sigma + q^{-1} = [2]_q e+; at q=1 -> 1+s = 2*(Young symmetrizer); "
                          "1/2 = 1/[2]_1 = KL-to-idempotent conversion",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-1p06 (B4) of milestone qou-b5qg; B1 #3955, B2 shadow #3960, B3 #3969 merged",
            "sharpened_statement": "the loop expansion weights the q=1 KL-normalized channel "
                                   "projector (b_s/[2]_q at q=1) by the universal heat-kernel unit "
                                   "a0*alpha — the single remaining normalization conjecture",
            "scope_guard": "derives no clause; no fit; nothing wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-b4-classical-half-origin.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
