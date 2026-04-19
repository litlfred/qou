import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-mass-markov",
  title: "Categorical mass as Markov trace",
  uses: [
    "def:mass-identity",
    "def:frobenius-pairing",
    "prop:frobenius-gram-matrix",
  ],
  tags: [
    "mass",
    "categorical-trace",
    "markov-trace",
    "frobenius",
    "nakayama",
    "hecke-algebra",
  ],
  lean: {
    decl: "QOU.BraidsAndKnots.categorical_mass_markov",
    file: "QOU/BraidsAndKnots.lean",
    validation: "not_checked",
  },
});
