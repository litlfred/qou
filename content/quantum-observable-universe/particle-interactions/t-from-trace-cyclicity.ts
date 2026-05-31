import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:t-from-trace-cyclicity",
  title:
    "Time-reversal $T$ as Markov-trace word reversal (trace cyclicity dual)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.TFromTraceCyclicity",
    validation: "not_checked",
  },
  uses: [
    "conj:cpt-d6-d7-d8-closure",
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
