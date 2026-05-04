import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-endomorphism",
  title: "Mass endomorphism conjecture",
  lean: {
    ref: "qou:QOU.MassEndomorphism.MassEndomorphism",
    validation: "not_checked",
  },
  uses: [
    "prop:hecke-mass-trace",
    "prop:categorical-mass-markov",
    "def:habiro-ring",
    "def:z-habiro-ring",
    "def:qz-bicompletion",
    "conj:brane-tower-z-habiro",
    "def:motivic-substrate",
    "def:archimedean-realization-functor",
    "thm:topological-mass",
  ],
  tags: [
    "mass",
    "endomorphism",
    "quantum-dilogarithm",
    "volume-conjecture",
    "higgs",
    "brane-tower",
    "habiro-ring",
    "open-problem",
  ],
});
