import { definition } from "../../schema/builders";

export default definition({
  label: "def:motivic-substrate",
  title:
    "The motivic aether $(K_0(\\mathrm{Var}_k), \\mathbb{L}, \\{\\rho_v\\})$",
  tags: [
    "motivic",
    "substrate",
    "grothendieck-ring",
    "lefschetz",
    "realization-tower",
    "axiom",
  ],
  uses: ["def:frobenius-hopf-substrate", "def:adelic-substrate"],
  cites: ["kontsevich1995", "denef-loeser2001", "tate1967"],
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.MotivicSubstrate",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "note",
      body:
        "Lean: the substrate is axiomatised as a `class MotivicSubstrate` " +
        "(AGENTS.md §3b) whose fields encode $K_0(\\mathrm{Var}_k)$, " +
        "$\\mathbb{L}$, the localization $\\widehat{\\mathcal{M}}$, and the " +
        "realization functors; the `sorry` in any concrete instance is the " +
        "substrate axiom (not a missing proof), and downstream results take " +
        "a `[MotivicSubstrate]` instance as an explicit hypothesis.",
    },
  ],
});
