import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gamma-gamma-generates-particles",
  title: "$\\gamma\\gamma$ production generates the operator basis",
  tags: [
    "photon",
    "pair-production",
    "gamma-gamma",
    "hecke-algebra",
    "generation",
    "chirality",
    "knot-operator",
  ],
  uses: ["def:breit-wheeler-pair-production"],
  lean: {
    ref: "qou:QOU.Archimedean.GammaGammaGeneration.gamma_gamma_chirality_surjective",
    validation: "not_checked",
  },
});
