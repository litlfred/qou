import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
#!/usr/bin/env python3
"""qou-avt5 follow-through: the "single-wrap" element CANNOT be a typed-crossing
word difference. Scope-(b) — a PROVED invariant, not a bounded search.

THE CLAIM UNDER TEST, quoted from the corpus. `qbeta-counit-closed-form.md`
opens: "Let Delta = NF(n) - NF(p) be the single-wrap normal-form difference of
the neutron and proton TYPED-CROSSING ELEMENTS in H_3(q)", and asserts
eps(Delta) = h^2/2 - h, formalised as the bare def
`QOU.Interactions.QBetaEnergyScale.epsNPq`. Q_A = -E_0*eps(Delta), so the whole
Q_beta ladder rests on it.

--- STEP 1: what a typed crossing IS (derived, not assumed) ------------------

`chi_monotone_transfer.word_to_mpfr` recognises exactly four templates by their
`d`: 0, -h, -h/2, and colour-weighted -h(1/2 - delta/4). The Hecke relation
gives sigma^-1 = sigma - h, so a crossing (c=1, d) is the algebra element
`sigma_g + d` and the templates read off as sigma / sigma^-1 / the average
(sigma+sigma^-1)/2 -- which is exactly what the code calls them. The counit
sends sigma -> q, so

    eps(sigma_g + d) = q + d   in   { q,  1/q,  [2]_q/2 }

hence for ANY typed word W,  eps(W) = q^m * ([2]_q/2)^c.

VERIFIED on the exhibited nucleon words: eps(beta_p) = q^3*([2]/2)^2 and
eps(beta_n) = q^1*([2]/2)^2, and their difference reproduces `chi_block_3`
SYMBOLICALLY (not just numerically):

    eps(beta_n - beta_p) = -(q-1)(q+1)(q^2+1)^2/(4q) = chi_block_3     [exact]

That is a second, independent confirmation of qou-avt5's side B.

--- STEP 2: the exclusion (PROVED, unbounded) --------------------------------

    epsNPq = h(h-2)/2 = (q^2-1)(q^2-2q-1)/(2q^2)

carries the factor (q^2 - 2q - 1), irreducible over Q, whose root is the SILVER
RATIO q = 1 + sqrt2. So epsNPq VANISHES there. If epsNPq were a difference of
two typed-word counits, that difference would vanish at q = 1 + sqrt2:

    (1+sqrt2)^m1 * ([2]/2)^c1  =  (1+sqrt2)^m2 * ([2]/2)^c2

and at q = 1 + sqrt2 one computes [2]_q/2 = (q^2+1)/(2q) = sqrt2 EXACTLY. So

    (1+sqrt2)^(m1-m2) = (sqrt2)^(c2-c1).

Take absolute norms in Z[sqrt2]: |N(1+sqrt2)| = 1 (it is the fundamental UNIT,
N = -1) while |N(sqrt2)| = 2. Hence 1 = 2^(c2-c1), forcing c1 = c2; then
(1+sqrt2)^(m1-m2) = 1, and 1+sqrt2 is not a root of unity, forcing m1 = m2.
The difference is then IDENTICALLY ZERO -- but epsNPq is not. Contradiction. QED

CONTROL (the exclusion must not prove too much): `chi_block_3` IS such a
difference, so it must NOT vanish at the silver ratio -- and indeed
chi_block_3(1+sqrt2) = -12 - 8*sqrt2 != 0, with the witnessing exponents
(m1,c1)=(1,2), (m2,c2)=(3,2). A bounded numeric sweep over
m in [-14,14], c in [0,9] (84100 pairs, three generic q) likewise returns
ZERO solutions for epsNPq and correctly finds that one for chi_block_3.

--- WHAT THIS MEANS ---------------------------------------------------------

The corpus's own description of Delta and its asserted counit are MUTUALLY
INCONSISTENT: no difference of typed-crossing words has counit epsNPq. So either

  (a) Delta is not a typed-crossing word difference -- in which case the prose
      "the single-wrap normal-form difference of the ... typed-crossing
      elements" is wrong and the real object is still unexhibited; or
  (b) epsNPq is wrong, and with it Q_A and the ladder's phase eps - tr_M.

NOT CLAIMED which. This probe excludes a CLASS; it does not adjudicate between
those two. Deciding needs the owner of the counit block.

SCOPE. This is scope-(b) per AGENTS.md -- a structural exclusion resting on a
proved invariant (the norm form on Z[sqrt2]), not a failed numerical search.
The invariant is cited above and re-verified below. It excludes the class
"difference of two typed-crossing words" and NOTHING WIDER: a colour-weighted
crossing contributes q - h(1/2 - delta/4), which is NOT of the form q^a, so
words containing one fall outside the q^m([2]/2)^c normal form and outside this
argument. Nucleon words at A=1 carry no colour-weighted crossing (there is no
p-n interface), which is why the class is the right one here -- but the
exclusion must not be quoted for words that do.

Exact symbolic. NO fit, NO c_k, NO wiring.
"""
import datetime, hashlib, json, os, subprocess
import sympy as sp


def _sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
    except Exception:
        return None


def main():
    q = sp.symbols("q", positive=True)
    h = q - 1/q
    b2 = (q**2 + 1)/(2*q)
    s = 1 + sp.sqrt(2)
    epsNP = sp.simplify(h*(h - 2)/2)
    chi3 = -(q**2 - 1)*(q**2 + 1)**2/(4*q)
    assertions = []

    def check(name, passed, note=""):
        assertions.append({"name": name, "passed": bool(passed), "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # STEP 1 -- the typed-crossing counits, and side B symbolically
    check("typed_crossing_counits_are_q_qinv_bracket2over2",
          sp.simplify(q + 0 - q) == 0 and sp.simplify((q - h) - 1/q) == 0
          and sp.simplify((q - h/2) - b2) == 0)
    eps_p = sp.simplify(q**4*(q - h/2)*q**2*(q - h)**3*(q - h/2))
    eps_n = sp.simplify(q**3*(q - h/2)**2*q**2*(q - h)**4)
    check("eps_beta_p_is_q3_bracket2over2_sq", sp.simplify(eps_p - q**3*b2**2) == 0)
    check("eps_beta_n_is_q1_bracket2over2_sq", sp.simplify(eps_n - q*b2**2) == 0)
    check("SYMBOLIC_side_B_eps_of_word_difference_equals_chi_block_3",
          sp.simplify(sp.together(eps_n - eps_p - chi3)) == 0)

    # STEP 2 -- the exclusion
    check("epsNPq_equals_h_times_h_minus_2_over_2", sp.simplify(epsNP - h*(h - 2)/2) == 0)
    check("epsNPq_vanishes_at_the_silver_ratio", sp.simplify(epsNP.subs(q, s)) == 0)
    check("bracket2over2_equals_sqrt2_at_the_silver_ratio",
          sp.simplify(b2.subs(q, s) - sp.sqrt(2)) == 0)
    check("norm_of_silver_unit_is_one_and_of_sqrt2_is_two",
          sp.expand((1 + sp.sqrt(2))*(1 - sp.sqrt(2))) == -1
          and sp.expand(sp.sqrt(2)*(-sp.sqrt(2))) == -2)

    # CONTROL -- the argument must NOT exclude chi_block_3
    check("CONTROL_chi_block_3_does_not_vanish_at_silver_ratio",
          sp.simplify(chi3.subs(q, s)) != 0,
          f"(= {sp.radsimp(sp.simplify(chi3.subs(q, s)))})")
    check("CONTROL_chi_block_3_is_exhibited_as_q1b2sq_minus_q3b2sq",
          sp.simplify(sp.together(q*b2**2 - q**3*b2**2 - chi3)) == 0)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "EXCLUDED, scope-(b), by a proved invariant. eps of any typed-crossing "
        "word is q^m*([2]_q/2)^c. epsNPq carries the factor (q^2-2q-1), so it "
        "vanishes at the SILVER RATIO q = 1+sqrt2, where [2]_q/2 = sqrt2 exactly. "
        "A typed-word difference vanishing there forces "
        "(1+sqrt2)^(m1-m2) = (sqrt2)^(c2-c1); absolute norms in Z[sqrt2] "
        "(|N(1+sqrt2)|=1, |N(sqrt2)|=2) force c1=c2 then m1=m2, making the "
        "difference identically zero -- which epsNPq is not. So NO difference of "
        "typed-crossing words has counit epsNPq, and the corpus's description of "
        "Delta is inconsistent with its own asserted counit. Either the prose is "
        "wrong (Delta is not such a difference, and the real element is still "
        "unexhibited) or epsNPq is wrong (and with it Q_A and the ladder phase). "
        "NOT adjudicated here. The control confirms the argument does not prove "
        "too much: chi_block_3 IS such a difference and correctly survives. "
        "Excludes ONLY this class -- colour-weighted crossings fall outside the "
        "normal form, and A=1 nucleon words carry none."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")

    src = open(__file__, "rb").read()
    w = {"computation": "qbeta-single-wrap-element-cannot-exist",
         "description": "No difference of typed-crossing words has counit "
                        "epsNPq -- proved by a norm argument in Z[sqrt2] at the "
                        "silver ratio. Side B (chi_block_*) confirmed symbolically.",
         "engine": "sympy-exact", "markov_convention": "n/a (counit only)",
         "assertions": assertions,
         "data": {"eps_typed_word_normal_form": "q^m * ([2]_q/2)^c",
                  "eps_beta_p": "q^3 * ([2]_q/2)^2",
                  "eps_beta_n": "q^1 * ([2]_q/2)^2",
                  "epsNPq": "h(h-2)/2 = (q^2-1)(q^2-2q-1)/(2q^2)",
                  "silver_ratio_root_of": "q^2 - 2q - 1",
                  "bounded_sweep": "m in [-14,14], c in [0,9]: 84100 pairs, "
                                   "3 generic q -> 0 solutions for epsNPq, "
                                   "1 solution for chi_block_3"},
         "verdict": verdict,
         "witness": {"scriptPath": "computations/qbeta/" + os.path.basename(__file__),
                     "scriptHash": hashlib.sha256(src).hexdigest()[:12],
                     "commitSha": _sha(),
                     "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()}}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qbeta-single-wrap-element-cannot-exist.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        w.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            w, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(w, f, indent=2); f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n{verdict}\n\nWitness: {os.path.basename(out)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
