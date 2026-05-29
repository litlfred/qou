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
    "def:qz-bicompletion",
    "prop:brane-tower-z-habiro",
    "def:motivic-substrate",
    "def:archimedean-realization-functor",
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
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
  ],
});
