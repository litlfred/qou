import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-09",
      body:
        "**The stated derivation does not go through.** The text derives " +
        "trace invariance under word reversal \"by the Markov trace " +
        "cyclicity axiom $\\mathrm{tr}_M(ab) = \\mathrm{tr}_M(ba)$\". " +
        "Cyclicity gives invariance under *rotation* of a word " +
        "($\\mathrm{tr}(vw) = \\mathrm{tr}(wv)$, formalised as " +
        "`QOU.markovTrace_append_comm`); reversal is a different " +
        "operation, and for non-commuting matrices " +
        "$\\mathrm{tr}(ABC) \\neq \\mathrm{tr}(CBA)$ in general. The claim " +
        "is plausible by a different route — the anti-automorphism of " +
        "$H_n(q)$ fixing each generator, under which characters are " +
        "invariant — but that route is not in the corpus. Reversal " +
        "invariance is therefore carried as the conjectural class field " +
        "`trace_reversal_invariant`, not proved. The block's structural " +
        "claims about $T$ (involution, crossing-count and generator-sign " +
        "preservation, acting only on crossing order) *are* proved " +
        "unconditionally in the Lean sibling.",
    },
  ],
  label: "conj:t-from-trace-cyclicity",
  title:
    "Time-reversal $T$ as Markov-trace word reversal (trace cyclicity dual)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.TFromTraceCyclicity",
    validation: "validated",
  },
  uses: [
    "prop:cpt-d6-d7-d8-closure",
    "def:bar-involution",
    "conj:cpt-orbit-closure-density",
    "thm:jones-markov-trace",
  ],
  cites: [
    "jones1987",
    "kassel1995",
    "wenzl1988",
  ],
  tags: [
    "tier:S",
    "time-reversal",
    "duality-d8",
    "markov-trace-cyclicity",
    "word-reversal",
    "cpt-decomposition",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
