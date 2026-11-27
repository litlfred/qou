import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:parallel-fibre-noninteraction",
  title: "Parallel placement of one-dimensional channels forms a commutative monoid",
  lean: {
    ref: "qou:QOU.InformationTheory.OneDimChannel.ParallelNonInteraction.parallel_noninteraction",
    validation: "not_checked",
  },
  uses: ["def:one-dim-qou-channel"],
  tags: [
    "optical-fibre",
    "non-interaction",
    "markov-trace",
    "split-link",
    "commutative-monoid",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-22",
      body: "**Statement restated 2026-11-22 to what the Lean proves (owner ruling, round-trip pass 3).** `parallel` is defined in the Lean as the channel with trace `A.trace * B.trace`, so `parallel_noninteraction` holds by `rfl`; the factorisation is a definition, not a theorem. The former statement presented it as a consequence of split-link multiplicativity of the Markov trace, which the Lean does not model (a channel is a single ring element, with no strands or crossings). What is proved: the factorisation by definition, plus commutativity, associativity and the vacuum identity (`parallel_comm`, `parallel_assoc`, `vacuum_parallel`, `parallel_vacuum`). Found by the blind round-trip audit (docs/audits/2026-11-22-roundtrip-blind-audit-pass3.md, block P08).",
    },
  ],
});
