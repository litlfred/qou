import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-endomorphism",
  title: "Mass endomorphism conjecture",
  uses: [
    "def:mass-identity",
    "def:hecke-mass-element",
    "prop:hecke-mass-trace",
    "prop:categorical-mass-markov",
    "thm:topological-mass",
    "prop:knot-operator-selection",
    "prop:frobenius-gram-matrix",
    "conj:topological-decomposition-mass",
  ],
  tags: [
    "mass",
    "endomorphism",
    "quantum-dilogarithm",
    "volume-conjecture",
    "higgs",
    "brane-tower",
    "open-problem",
  ],
});
