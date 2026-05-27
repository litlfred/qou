import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:t-from-trace-cyclicity",
  title:
    "Time-reversal $T$ as Markov-trace word reversal (trace cyclicity dual)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.TFromTraceCyclicity",
    validation: "not_checked",
  },
  uses: [
    "def:bar-involution",
    "prop:cpt-orbit-closure-density",
    "def:hecke-normal-form",
    "thm:jones-markov-trace",
    "prop:atom-knot-mass-derivation",
  ],
  cites: [
    "jones1987",
    "kassel1995",
    "wenzl1988",
  ],
  tags: [
    "time-reversal",
    "duality-d8",
    "markov-trace-cyclicity",
    "word-reversal",
    "cpt-decomposition",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
  ],
});
