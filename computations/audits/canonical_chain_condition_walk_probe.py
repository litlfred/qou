#!/usr/bin/env python3
"""Walking the canonical derivation chain: where do CONDITIONS emerge?

WHAT THIS IS
------------
`docs/canonical-derivation-cheat-sheet.md` states the chain as eleven steps from
the substrate q_0 to MeV observables.  Each step is written as though its output
follows from its input.  This probe walks the chain asking a different question:
**at each step, what condition enters that the previous step does not force?**

It is a PARTIAL walk.  Steps 5, 6 and 10 are measured here; steps 1, 3, 4, 7, 8,
9 and 11 are NOT and are listed as not-yet-walked in the companion audit doc.
Step 2's condition is already documented in the cheat sheet itself (§2a, the
curvature 2-form is stipulated rather than computed) and is cited, not re-derived.

Companion: `docs/audits/2026-09-14-canonical-chain-condition-walk.md`
Bean: `qou-u96j`

THE THREE MEASURED FINDINGS
---------------------------

**C5 (step 5, Wedderburn + partitions) -- the sum is over TWO-ROW partitions.**
The step is stated as `H_n(q) = (+)_{lam |- n} M_{d_lam}` with
`tr_M = sum_lam y_lam chi^lam` -- over ALL partitions of n.  Measured against the
committed `y-lambda-at-q0.witness.json`, every y_lam with three or more rows is
EXACTLY 0, at every n from 2 to 12 (at n=12: 7 nonzero, 70 zero).  The production
family is `y_lambda_su_n(n, q, 2)` and that trailing `2` is a row cap.

    🛑 SECTION 6 CORRECTS THE FRAMING OF THIS ONE, AND THE CORRECTION MATTERS.
    This paragraph first called the row cap "a condition the step statement does
    not carry", which reads as though it were a truncation bolted on at step 5.
    It is not.  The cap is DERIVED, in the corpus, from the step-1 choice of the
    fibre `V`, and it is what FORCES the Markov parameter.  What step 5's
    statement omits is the HYPOTHESIS, not the truncation.  See section 6.

**C5b -- `alpha` is not an ad-hoc ratio; it is a Wenzl weight, and it is DERIVED.**
`y_(3)` at n = 3 equals `(q^4+1)/(q^2+1)^2` exactly.  That is the same `alpha`
that the 2026-09-08 Q_beta ruling names as the augmentation-to-z_D factor and that
`QOU/Hecke/MarkovCrossingReversal.lean` found relating the two admissible cells of
the flavour split.  Section 6 shows it is not merely *observed* to equal `y_(3)`:
it follows from `markovWeights_eq_jones_of_threeRow_eq_zero` as
`y_(3) = 1 - 2/[2]_q^2`.

**C3 (step 3) -- the whole fork reduces to ONE condition, and it sits at step 1.**
`rem:markov-axioms-primitive` states correctly that axioms 1-2 admit a
ONE-PARAMETER FAMILY, so the cheat sheet's "unique trace tr_M" at step 3 is the
compressed form.  But the parameter is then FORCED, by a sorry-free chain:

    V = fundamental of SU_q(2)        <- the hypothesis, and the only one
      => l(lambda) <= 2               lem:feynman-eigenbasis-decomposition
      => y_(1^3) = 0
      => [+ faithfulness]             markovWeights_eq_jones_of_threeRow_eq_zero
      => y_(2,1) = 1/[2]_q^2, y_(3) = alpha, z = q^3/(q^2+1) = z_D

and the competing root z = q is `markovWeights_degenerate_root`: y = (1,0,0), so
`y_(2,1) = 0` and the trace is NOT FAITHFUL on TL_3.  That is a DERIVATION-FIRST
discriminator on the fork `qou-99qc` / `qou-qqm4` have been carrying, using no
residual at all -- and it points AWAY from the cell that reproduced the
flavour-split baseline exactly in #7334.  Recorded; the owner call is not taken.

A measurement note worth keeping: `grep -c sorry` on
`MarkovTraceTLUniqueness.lean` returns 1, and that hit is the word inside a
COMMENT ("sorry-free, lean-direct exit 0").  The file has no `sorry` tactic.
Counting the word is not counting the tactic.

**C5c -- the normalisation is DIMENSION-WEIGHTED, and a naive reading gets it
wrong.**  `sum_lam d_lam * y_lam = 1` exactly at every n (this is `tr_M(1) = 1`,
since `chi^lam(1) = d_lam`).  The unweighted `sum_lam y_lam` is 1 only at n = 2,
where every d_lam is 1, and then falls: 0.7527, 0.5666, 0.3804 at n = 3, 4, 5.
Recorded because the author's first reading of the witness was the unweighted one
and it produced a false "the y are not a measure" claim.

**C10 (step 10, confinement SDP) -- `n_target` carries three inequivalent
production meanings, and the cheat sheet states an objective the code does not
have.**  Section 4 below.

WHAT THIS PROBE DOES NOT CLAIM
------------------------------
Nothing here says any of these conditions is WRONG.  A condition that is correct
and simply unstated is still worth surfacing, because the chain is the document
agents reason from.  Scope (a) throughout: measured observations about what the
corpus contains, with no invariant excluding any of the readings.

Run: python3 computations/audits/canonical_chain_condition_walk_probe.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

import sympy as sp
from mpmath import mp

mp.dps = 60

ROOT = pathlib.Path(__file__).resolve().parents[2]
_q = sp.symbols("q", positive=True)
ALPHA = (_q**4 + 1) / (_q**2 + 1) ** 2

def dim_irrep(lam) -> int:
    """d_lambda for S_n by the hook-length formula.  Computed, not tabulated --
    the witness reaches n = 12 and a hand table would be both long and a place
    for a typo to hide."""
    lam = [p for p in lam if p]
    n = sum(lam)
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    num = 1
    for k in range(1, n + 1):
        num *= k
    den = 1
    for i, row in enumerate(lam):
        for j in range(row):
            den *= (row - j) + (conj[j] - i) - 1
    return num // den


def main() -> int:
    ok = True

    wit = json.loads((ROOT / "computations" / "y-lambda-at-q0.witness.json").read_text())
    by_n = wit["data"]["by_n"]
    q0 = mp.mpf(wit["q0Value"])
    print(f"source: y-lambda-at-q0.witness.json   q0Anchor = {wit['q0Anchor']}   "
          f"q0 = {mp.nstr(q0, 20)}")

    print()
    print("1. STEP 5 -- THE PARTITION SUM IS OVER TWO-ROW PARTITIONS ONLY")
    print("   cheat sheet: 'H_n(q) = (+)_{lam |- n} M_{d_lam}; tr_M = sum y_lam chi^lam'")
    allgood = True
    for n_str in sorted(by_n, key=int):
        rows = by_n[n_str]
        nz = [tuple(r["partition"]) for r in rows if mp.mpf(r["y_at_q0_50dps"]) != 0]
        zr = [tuple(r["partition"]) for r in rows if mp.mpf(r["y_at_q0_50dps"]) == 0]
        good = all(len(p) <= 2 for p in nz) and all(len(p) >= 3 for p in zr)
        allgood &= good
        print(f"   n={n_str:>2s}: {len(nz):>2d} nonzero (max rows {max(len(p) for p in nz)}), "
              f"{len(zr):>3d} zero (min rows {min((len(p) for p in zr), default=0)})   "
              f"{'OK' if good else 'PATTERN BROKEN'}")
    ok &= allgood
    print(f"   -> at EVERY n from 2 to {max(by_n, key=int)}: every partition with >= 3 rows")
    print("      is EXACTLY zero and every nonzero one has <= 2 rows.  The production")
    print("      family is y_lambda_su_n(n, q, 2); the trailing 2 is a ROW CAP.")

    print()
    print("2. STEP 5b -- alpha IS THE TRIVIAL BLOCK'S WENZL WEIGHT, EXACTLY")
    y3w = mp.mpf([r for r in by_n["3"] if r["partition"] == [3]][0]["y_at_q0_50dps"])
    a0 = mp.mpf(str(sp.N(ALPHA.subs(_q, sp.Float(str(q0), 50)), 46)))
    agree = abs(y3w - a0) < mp.mpf("1e-45")
    ok &= agree
    print(f"   y_(3) at n=3            = {mp.nstr(y3w, 30)}")
    print(f"   alpha = (q^4+1)/(q^2+1)^2 = {mp.nstr(a0, 30)}")
    print(f"   agree to 45 dps: {agree}   |diff| = {mp.nstr(abs(y3w-a0), 6)}")
    print("   -> the alpha of the 2026-09-08 Q_beta ruling and of the flavour-split")
    print("      fork is not an ad-hoc ratio; it is this Wenzl weight.")

    print()
    print("3. STEP 5c -- THE NORMALISATION IS DIMENSION-WEIGHTED")
    for n_str in sorted(by_n, key=int):
        rows = by_n[n_str]
        s = sum(mp.mpf(r["y_at_q0_50dps"]) for r in rows)
        sd = sum(mp.mpf(r["y_at_q0_50dps"]) * dim_irrep(r["partition"]) for r in rows)
        unit = abs(sd - 1) < mp.mpf("1e-40")
        ok &= unit
        print(f"   n={n_str:>2s}: sum(y) = {mp.nstr(s, 18):>22s}    "
              f"sum(d*y) = {mp.nstr(sd, 18):>10s}  == 1 ? {unit}")
    print("   -> sum(d_lam y_lam) = 1 is tr_M(1) = 1, since chi^lam(1) = d_lam.")
    print("      The UNWEIGHTED sum is 1 only at n=2 (all d=1).  The author's first")
    print("      reading of this witness was the unweighted one and produced a false")
    print("      'the y are not a measure' claim; recorded so it is not repeated.")

    print()
    print("4. STEP 10 -- n_target HAS THREE INEQUIVALENT PRODUCTION MEANINGS")
    callers = {
        "computations/aK_via_lp_dual_hecke_basis.py":
            (r"n_target\s*=\s*tr_M_atom", "|tr_M(W_atom)| -- a Markov trace (REAL)"),
        "computations/pn_alpha_lp_dual.py":
            (r"target_net\s*=\s*float\(pn_vec\.sum\(\)\)",
             "sum of the p/n element vector (REAL, alpha-dependent)"),
        "computations/option_b_proton_mass_full_chain.py":
            (r"n_target=float\(n_gg\)", "count of gamma-gamma insertions (INTEGER)"),
    }
    found = 0
    for rel, (pat, gloss) in callers.items():
        txt = (ROOT / rel).read_text()
        m = re.search(pat, txt)
        hit = m is not None
        ok &= hit
        found += hit
        line = txt[:m.start()].count("\n") + 1 if m else "-"
        print(f"   {rel}:{line}")
        print(f"      {gloss}   {'FOUND' if hit else 'NOT FOUND'}")
    print(f"   -> {found}/3 confirmed at source.  The spec block")
    print("      content/.../appendix-mass-binding-algorithms/mba-step10-confinement-sdp.md")
    print("      declares 'Target net constraint n_target in Z_{>=0}' -- an INTEGER.")
    print("      Two of the three production callers pass a real.")

    print()
    print("5. STEP 10b -- THE CHEAT SHEET STATES AN OBJECTIVE THE CODE DOES NOT HAVE")
    cs = (ROOT / "docs" / "canonical-derivation-cheat-sheet.md").read_text()
    has_btgt = "B_\\mathrm{tgt}" in cs or "B_tgt" in cs
    spec = (ROOT / "folio" / "quantum-observable-universe"
            / "appendix-mass-binding-algorithms" / "mba-step10-confinement-sdp.md").read_text()
    spec_has_btgt = "B_tgt" in spec or "B_\\mathrm{tgt}" in spec
    spec_has_sum = "Σ_i t_i x_i" in spec or "t_i x_i" in spec
    ok &= has_btgt and (not spec_has_btgt) and spec_has_sum
    print(f"   cheat sheet mentions a B_tgt in step 10          : {has_btgt}")
    print(f"   the authoritative algorithm block mentions B_tgt : {spec_has_btgt}")
    print(f"   the algorithm block's objective is  min sum t_i x_i : {spec_has_sum}")
    print("   -> the cheat sheet renders step 10 as 'min ||tr_M(T_w) E_0 - B_tgt||',")
    print("      i.e. minimising distance to a MEASURED BINDING.  The algorithm block")
    print("      and pyhecke.lp_dual_solver.solve_operator_selection_lp(t, G, n_target)")
    print("      have no such term.  The defect points the SAFE way -- the doc looks")
    print("      MORE fitted than the code -- but it is in the PRIMARY coordination")
    print("      document, and an agent reading it would conclude the chain fits AME.")

    print()
    print("6. STEP 3 -- AND THE WHOLE FORK REDUCES TO **ONE** CONDITION, AT STEP 1")
    print("   [This section CORRECTS section 1's framing -- see the docstring.]")
    qs = sp.symbols("qs", positive=True)
    t2 = qs + 1 / qs
    y21 = 1 / t2**2
    y3 = 1 - 2 * y21
    zz = qs**2 / t2
    a_sym = (qs**4 + 1) / (qs**2 + 1) ** 2
    zD_sym = qs**3 / (qs**2 + 1)
    e1 = sp.simplify(y3 - a_sym)
    e2 = sp.simplify(zz - zD_sym)
    ok &= (e1 == 0) and (e2 == 0)
    print("   rem:markov-axioms-primitive: axioms 1-2 admit a ONE-PARAMETER FAMILY;")
    print("   axiom 3's member is then FORCED, and the forcing is sorry-free Lean:")
    print()
    print("     V = fundamental of SU_q(2)         <- HYPOTHESIS, and the only one")
    print("       => l(lambda) <= 2 row cap          lem:feynman-eigenbasis-decomposition")
    print("       => y_(1^3) = 0")
    print("       => [+ faithfulness y_(2,1) != 0]   markovWeights_eq_jones_of_threeRow_eq_zero")
    print("       => y_(2,1) = 1/[2]_q^2, y_(3) = (q^4+1)/(q^2+1)^2, z = q^3/(q^2+1)")
    print()
    print(f"   y_(3) - alpha = {e1}      z - z_D = {e2}      "
          f"{'BOTH EXACT' if e1 == 0 and e2 == 0 else 'MISMATCH'}")
    dy3 = mp.mpf(str(sp.N(y3.subs(qs, sp.Float(str(q0), 50)), 46)))
    dy21 = mp.mpf(str(sp.N(y21.subs(qs, sp.Float(str(q0), 50)), 46)))
    w21 = mp.mpf([r for r in by_n["3"] if r["partition"] == [2, 1]][0]["y_at_q0_50dps"])
    match = abs(dy3 - y3w) < mp.mpf("1e-45") and abs(dy21 - w21) < mp.mpf("1e-45")
    ok &= match
    print(f"   derived vs committed witness at q0: y_(3) and y_(2,1) both agree: {match}")
    print()
    print("   SO: the two-row cap is NOT a truncation bolted onto step 5 -- it is")
    print("   DERIVED from the step-1 choice of V, and it is what FORCES z_D.  And")
    print("   alpha is not merely 'observed to equal y_(3)': it IS y_(3), derived.")
    print()
    print("   The augmentation z = q is markovWeights_degenerate_root: y = (1,0,0),")
    print("   so y_(2,1) = 0 and the trace is NOT FAITHFUL on TL_3.")
    print(f"   check  z*[2]_q - q^2  at z=q  =  {sp.factor(sp.simplify(qs*t2 - qs**2))}"
          "   (= 1, so != q^2)")
    print("   -> that is a DERIVATION-FIRST discriminator on the fork qou-99qc /")
    print("      qou-qqm4 have been carrying, and it uses no residual at all.  The")
    print("      cell that reproduced the flavour-split baseline exactly (#7334) is")
    print("      the corpus's own proved-degenerate root.  Recorded; the owner call")
    print("      on which cell to adopt is NOT taken here.")

    print()
    print("7. STEP 1/4 -- WHERE V COMES FROM, AND THE CYCLE AT THE ROOT")
    quotes = [
        ("folio/quantum-observable-universe/braids-and-knots/why-b3.md",
         "The Descartes condition $\\chi(A) = -6$ forces the gauge group to be a "
         "quantum form of $\\mathrm{SU}(2)$",
         "chi = -6  =>  SU(2)  =>  dim V = 2"),
        ("folio/quantum-observable-universe/brings-surface/chi-minus-six-chain.md",
         "**Step 1: Start with the QOU triple.** We have $(\\mathbf{C}, A, \\tau)$ "
         "with gauge group $G = \\mathrm{SU}(2)$",
         "the chi = -6 chain STARTS FROM SU(2)"),
        ("folio/quantum-observable-universe/brings-surface/chi-minus-six-chain.md",
         "so the chain locates the value rather than deriving it from the axioms alone",
         "the chain DECLARES its step-5 circularity, in its own words"),
        ("folio/quantum-observable-universe/brings-surface/cohomological-embedding.md",
         "This uniquely forces $g = 4$ and $\\chi = -6$",
         "a SECOND route: the embeddability pattern T_{2,3}, T_{2,9} in / T_{2,11} out"),
    ]
    for rel, needle, gloss in quotes:
        present = needle in (ROOT / rel).read_text()
        ok &= present
        print(f"   [{'FOUND' if present else 'MISSING'}] {rel.split('/')[-1]}")
        print(f"            {gloss}")
    print()
    print("   Step 1's own proposition (prop:braid-action-tensor) says 'For each")
    print("   object V in C' -- ARBITRARY.  So V is not fixed at step 1; it is fixed")
    print("   by step 4 (Bring, chi = -6), which the chain draws DOWNSTREAM of it.")
    print("   The dependency is a CYCLE, and only half of it is declared:")
    print()
    print("     why-b3:             chi = -6  FORCES  SU(2)  =>  dim V = 2")
    print("     chi-minus-six step1: STARTS FROM  G = SU(2)  and uses it at step 2")
    print("     chi-minus-six step5: reads 6 off Bring, which step 7 then identifies")
    print("                          <- THIS one the block declares; the step-1 one it does not")
    print()
    print("   NOT a claim that the mathematics is wrong.  Each block is fine as a")
    print("   CONSISTENCY statement.  The measured fact is that, read as derivations,")
    print("   they form a cycle, and that the everything-hangs-on-it condition")
    print("   (dim V = 2) is assumed at step 1 of the chain presented as deriving it.")
    print("   cohomological-embedding's route may be independent -- it does not")
    print("   visibly assume SU(2) -- but it takes a knot-embedding PATTERN as input,")
    print("   which relocates the condition rather than removing it.")
    print()
    print("   ALSO: two blocks disagree on the RANK.  why-b3 says SU(2) has 'rank 1'")
    print("   (correct); descartes-knot-eigenbasis-derivation says chi = -6 'sets the")
    print("   genus g = 4 and gauge group SU_q(2) to rank 2'.  SU(2) has rank 1; 2 is")
    print("   dim V.  One of the two is stating a wrong rank as a derived consequence.")

    # ---------------------------------------------------------------------
    print()
    print("8. STEP 9 -- the exit to R is SCOPED, and one of its three names does")
    print("   not resolve.")
    print()

    step9 = [
        ("folio/quantum-observable-universe/mass-theory/"
         "archimedean-realization-functor.md",
         "The word \"functor\" in the name and label is **legacy**",
         "the block WITHDRAWS 'functor': R_top is a realization/evaluation,\n"
         "            a ring hom out of K_0(Var), not a functor.  Candid, not a defect."),
        ("folio/quantum-observable-universe/mass-theory/"
         "archimedean-realization-functor-interpretation.md",
         "\\quad\\text{on } \\widehat{\\mathcal{M}}_{\\mathrm{QOU}}",
         "the identification R_top = tau_arch is SCOPED to a subset M_QOU"),
        ("folio/quantum-observable-universe/mass-theory/vol-through-tau.md",
         "On the algebraic quantum volume, $\\tau_{\\mathrm{arch}}$ coincides with",
         "a SIBLING states the same agreement scoped to the algebraic quantum\n"
         "            volume -- and `def:algebraic-quantum-volume` EXISTS"),
        ("folio/quantum-observable-universe/mass-theory/vol-as-motivic-period.md",
         "These pictures agree on the algebraic quantum volume domain",
         "and a third states it for all three pictures, same scope"),
    ]
    for rel, needle, gloss in step9:
        present = needle in (ROOT / rel).read_text()
        ok &= present
        print(f"   [{'FOUND' if present else 'MISSING'}] {rel.split('/')[-1]}")
        print(f"            {gloss}")

    # M_QOU: how many times does it occur in the whole corpus?
    hits = 0
    for p in (ROOT / "folio").rglob("*.md"):
        try:
            if "\\widehat{\\mathcal{M}}_{\\mathrm{QOU}}" in p.read_text(encoding="utf-8"):
                hits += 1
        except Exception:                                   # pragma: no cover
            continue
    ok &= hits == 1
    print()
    print(f"   M_QOU occurrences across content/**.md : {hits}")
    print()
    print("   So the agreement is stated THREE times under TWO names for the same")
    print("   domain.  Two of them say 'the algebraic quantum volume', which")
    print("   resolves to `def:algebraic-quantum-volume`.  The third says M_QOU,")
    print("   which occurs exactly ONCE in the corpus -- in the sentence that uses")
    print("   it -- and is defined nowhere.")
    print()
    print("   THE SUBSTANCE IS FINE AND THE CORPUS IS CAREFUL HERE.  The condition")
    print("   entering at step 9 is real, declared, and correctly scoped: the")
    print("   'exclusive exit to R' is established ON the algebraic quantum volume,")
    print("   not in general.  The defect is one undefined SYMBOL in one remark,")
    print("   where its two siblings use a defined one.  A one-symbol fix.")
    print()
    print("   NOT claimed: that chi_top is ill-defined.  The remark allows it to be")
    print("   'an integer (Euler characteristic) OR a refined Hodge-theoretic")
    print("   invariant like hyperbolic volume' -- two invariants with different")
    print("   codomains under one name -- and chi_top has NO notation-register")
    print("   entry.  That is an overload worth noting, but the blocks that USE it")
    print("   scope it to the volume domain, so it is not measured as a defect here.")

    print()
    print("VERDICT:", "PASS -- steps 5 and 10 each carry a condition the chain's own "
          "step statement does not state; alpha is identified as a Wenzl weight; "
          "step 9's exit to R is correctly scoped under one undefined symbol"
          if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
