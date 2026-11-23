import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-satisfies-blitvic-hypothesis",
  title:
    "The Hecke generators under the Markov trace do not satisfy Blitvić's pair-partition hypothesis",
  lean: { ref: "qou:QOU.Observations.markovTrace_centred_cube_ne_zero", validation: "not_checked" },
  uses: [
    "rem:non-commutative-probability-dictionary",
    "thm:jones-markov-trace",
  ],
  cites: ["blitvic2012", "wenzl1988"],
  tags: [
    "q-clt",
    "blitvic",
    "pair-partition",
    "hecke-quadratic-relation",
    "established",
    "negative-result",
  ],
  proofs: ["prf:hecke-satisfies-blitvic-hypothesis"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-18",
      body:
        "**Rewritten as a negative result.** The earlier statement claimed that odd centred moments vanish. That claim is false: the third centred moment is $-357/250$ at $q = 2$ under convention D. Lean: `markovTrace_centred_cube_ne_zero`, sorry-free, for every Markov trace family on the Hecke tower. The earlier Lean derived odd vanishing from a Markov axiom stated for all $x$, which no Markov trace satisfies.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** *(Superseded 2026-08-09 — this note argues from " +
        "the excised **convention C**; see the correction immediately below. " +
        "The argument is kept intact as the record of what was claimed, with " +
        "the convention labelled inline where it is used.)* The carrier `A` of " +
        "`HeckeSatisfiesBlitvicHypothesisContext` is already a generic " +
        "`Type u` with its own `ringA` — only the *trace codomain* is `ℝ` " +
        "(`tr_M : A → ℝ`, `z_real : ℝ`, `pairWeight : ℕ → List ℕ → ℕ → ℝ`, " +
        "`centredMoment : List ℕ → ℝ`). That codomain is `ℝ` because of what " +
        "`z_real` is: the class docstring defines the Markov parameter as " +
        "`z = 1 / (q^{1/2} + q^{-1/2})` — the excised **convention C** — i.e. " +
        "it requires a **square root of " +
        "`q`**, which a generic commutative ring need not admit (§7c puts " +
        "radicals on the `ℝ` side). The odd-length vanishing itself would " +
        "generalise to any `AddCommMonoid` codomain, so this is a " +
        "specialisation of the *scalar field*, not of the algebra — and it is " +
        "the square root, not the ordering, that forces it.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "**The note above is obsolete, and its conclusion no longer follows.** " +
        "It justifies the `ℝ` codomain by *one* fact and one only: that " +
        "$z = 1/(q^{1/2} + q^{-1/2})$ needs a square root of $q$. That is the " +
        "**excised convention C**. Production is **convention D**, " +
        "$z = q^{3}/(q^{2}+1)$ — a rational function of $q$, no radical, never " +
        "leaving $\\mathbb{Q}(q)$. " +
        "[`markov-trace-frobenius-selection-proof`](#prf:markov-trace-frobenius-selection) " +
        "already retired the matching $\\mathbb{Q}(q^{1/2})$ hypothesis for the " +
        "same reason (\"an artefact of convention C … convention D's " +
        "$z = q^{3}/(q^{2}+1)$ does not\"); this block was missed when that " +
        "correction was propagated. " +
        "By the old note's own reasoning — \"the odd-length vanishing itself " +
        "would generalise to any `AddCommMonoid` codomain … it is the square " +
        "root, not the ordering, that forces it\" — removing the square root " +
        "removes the stated obstruction, so under convention D the `ℝ` " +
        "specialisation has no argument behind it. " +
        "**This is deliberately NOT asserted as a licence to generalise the Lean " +
        "class.** Losing the *stated* reason for `ℝ` is not the same as proving " +
        "no reason exists; `pairWeight` and `centredMoment` have not been " +
        "audited for a hidden order or completeness dependence. The claim here " +
        "is only that the justification on record is a convention-C artefact. " +
        "Whether `HeckeSatisfiesBlitvicHypothesisContext` can actually be " +
        "restated over a generic `CommRing` is an open Lean question — bean " +
        "`qou-emyt`.",
    },
  ],
});
