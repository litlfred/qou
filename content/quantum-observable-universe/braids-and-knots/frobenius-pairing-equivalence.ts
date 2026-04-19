import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-pairing-equivalence",
  lean: {
    decl: "QOU.BraidsAndKnots.Stubs.frobenius_pairing_equivalence",
    file: "QOU/BraidsAndKnots/Stubs.lean",
    validation: "not_checked",
  },
  title:
    "Rigid-monoidal Frobenius pairing equals the Markov-trace inner product under fibre-functor descent",
  uses: [
    "prop:frobenius-pairing-exists",
    "prop:categorical-mass-markov",
    "thm:jones-markov-trace",
    "def:categorical-action",
  ],
  tags: [
    "frobenius-pairing",
    "markov-trace",
    "fibre-functor",
    "descent",
    "rigid-monoidal",
  ],
});
