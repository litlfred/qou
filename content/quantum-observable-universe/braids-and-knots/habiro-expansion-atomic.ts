import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-expansion-atomic",
  title: "Habiro cyclotomic expansion of the atomic-braid Markov trace",
  uses: ["prop:full-pole-structure-mass-trace"],
  tags: [
    "habiro-ring",
    "cyclotomic-expansion",
    "markov-trace",
    "atomic-braid",
    "integrality",
  ],
  cites: ["habiro2002", "kassel1995", "jones1987"],
  lean: {
    ref: "qou:QOU.BraidKnot.habiro_expansion_atomic",
    validation: "not_checked",
  },
});
