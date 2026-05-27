import { definition } from "../../schema/builders";

export default definition({
  label: "def:motivic-galois-character",
  title:
    "Motivic Galois character $\\chi^{\\mathrm{mot}}_A$ of the Frobenius--Hopf substrate",
  tags: [
    "motivic-galois",
    "frobenius",
    "yekutieli",
    "cyclotomic-place",
    "axiom",
  ],
  uses: ["def:adelic-substrate"],
  cites: ["yekutieli2010", "tate1967"],
  lean: {
    ref: "qou:QOU.LiftingDescent.MotivicGaloisCharacter",
    validation: "not_checked",
  },
});
