import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:closure-unseen-subword",
  title:
    "No closure distinguishes two elements exactly when they differ by a commutator; " +
    "closure is a Bell pairing",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.ClosureUnseen.unseen_iff",
  },
  uses: ["def:hochschild-homology", "thm:jones-markov-trace"],
  cites: ["loday-1998", "kassel1995"],
  tags: [
    "braid-closure",
    "trace",
    "hochschild-homology",
    "commutator",
    "coevaluation",
    "entanglement",
    "categorical-derivation",
  ],
});
