import { definition } from "../../schema/builders";

export default definition({
  label: "def:motivic-galois-character",
  title:
    "Motivic Galois character $\\chi^{\\mathrm{mot}}_A$ of the Frobenius--Hopf aether",
  tags: [
    "motivic-galois",
    "frobenius",
    "yekutieli",
    "cyclotomic-place",
    "axiom",
  ],
  uses: ["def:adelic-substrate", "def:motivic-substrate"],
  cites: ["yekutieli2010", "tate1967"],
  lean: {
    ref: "qou:QOU.LiftingDescent.MotivicGaloisCharacter",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "note",
      body:
        "Lean: the formal-chain `class MotivicGaloisCharacter` takes a " +
        "`MotivicSubstrate K0 Mhat Target` instance as a hypothesis and " +
        "exposes $\\chi^{\\mathrm{mot}}_A$ with its compatibility with each " +
        "local realization $\\rho_p$; the `sorry` in any concrete instance " +
        "is the substrate axiom.",
    },
  ],
});
