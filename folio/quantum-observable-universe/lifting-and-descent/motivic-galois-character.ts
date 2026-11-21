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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([adelic substrate](#def:adelic-substrate))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Working directly with $\\chi^{\\mathrm{mot}}_A$ replaces per-level Čech-cocycle non-vanishing arguments with a single non-vanishing theorem about the character ([motivic perpetual obstruction](#thm:motivic-perpetual-obstruction), proved via Route A: prime-ideal collapse, $C = a_0(-1) + 2 \\cdot a_1(-1)$)." },
  ],
});
