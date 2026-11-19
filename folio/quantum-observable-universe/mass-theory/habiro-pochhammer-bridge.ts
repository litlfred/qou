import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-pochhammer-bridge",
  title:
    "Habiro–Markov bridge via Pochhammer factorisation",
  lean: {
    ref: "qou:QOU.BraidKnot.HabiroPochhammerBridge",
  },
  uses: [
    "prop:habiro-precision-ladder-equivalence",
    "thm:jones-markov-trace",
    "def:habiro-ring",
  ],
  cites: [
    "habiro2000",
    "jones1987",
  ],
  tags: [
    "habiro-ring",
    "pochhammer",
    "normalization-bridge",
    "1ppQ",
  ],
  computation: {
    engine: "sympy",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/markov/markov-substrate-realization.witness.json",
    status: "verified",
  },
});
