import { definition } from "../../schema/builders";

export default definition({
  label: "def:motivic-substrate",
  title:
    "The motivic substrate $(K_0(\\mathrm{Var}_k), \\mathbb{L}, \\{\\rho_v\\})$",
  tags: [
    "motivic",
    "substrate",
    "grothendieck-ring",
    "lefschetz",
    "realization-tower",
    "axiom",
  ],
  uses: ["def:arc-space"],
  cites: ["kontsevich1995", "denef-loeser2001", "tate1967"],
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.MotivicSubstrate",
    validation: "not_checked",
  },
});
