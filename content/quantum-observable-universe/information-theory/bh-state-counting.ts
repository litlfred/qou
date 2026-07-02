import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bh-state-counting",
  title: "Black-hole state counting: $\\dim_q$ of the exterior horizon-mode space is $\\exp S(M)$",
  lean: { ref: "qou:QOU.Information.BhStateCounting", validation: "stub" },
  tags: [
    "jet-horizon",
    "bekenstein-entropy",
    "black-hole-complementarity",
    "quantum-dimension",
    "markov-trace",
    "state-counting",
  ],
  uses: [
    "def:jet-horizon",
    "rem:hawking-radiation",
    "conj:lqg-entropy-qdim-partition-pole",
  ],
  cites: ["susskind1993", "bekenstein1973"],
});
