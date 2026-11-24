import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fivetwo-level-seven-ladder",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoLevelSevenLadder.sum_of_numerators",
    validation: "not_checked",
  },
  title:
    "The level-seven ladder: three five-term instances give the three $\\mathbb{Q}(\\zeta_7)^{+}$ numerators, with the $7$ supplied by the quadratic residues mod $7$",
  tags: [
    "five-two",
    "level-seven",
    "cyclotomic",
    "five-term-relation",
    "quadratic-residues",
    "dilogarithm",
  ],
  uses: ["prop:fivetwo-saddle-sum-rule"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "**Proved sorry-free** over a generic `CommRing` — Lean " +
        "`QOU.QBeta.FiveTwoLevelSevenLadder.sum_of_numerators`, with " +
        "`numerators_of_five_term` supplying the three numerators " +
        "individually and `numerators_original_form` restating them. `L` is " +
        "an **abstract** function and the reflection identities are explicit " +
        "hypotheses, matching `FiveTwoSaddleSumRule.lean`'s treatment — so " +
        "nothing depends on a dilogarithm implementation or on the Bloch " +
        "group.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "**Conditional on its hypotheses, which are not proved here.** The " +
        "block derives the numerators *given* three five-term instances and " +
        "four reflection relations. It does **not** prove the five-term " +
        "relation, the inversion/Landen extensions, or Route 8's transport of " +
        "the sum rule to $\\mathbb{Q}(\\zeta_7)^{+}$. Those are inputs. The " +
        "Lean file's own scope note says the same.",
    },
    {
      kind: "note",
      date: "2026-08-19",
      body:
        "The cleared form ($7T = \\ldots$ rather than $T = \\ldots/7$) is " +
        "deliberate and `char_seven_forces` says why: in characteristic $7$ " +
        "the hypotheses *force* $3L_1 = 0$, hence $L_1 = 0$, and every target " +
        "degenerates to $0 = 0$. So the divided form is not merely " +
        "unavailable for want of $7^{-1}$ — it would be vacuous exactly where " +
        "it could not be stated. Worth keeping as an authoring pattern: clear " +
        "the denominator and let the content sit where the denominator is " +
        "invertible.",
    },
  ],
});
