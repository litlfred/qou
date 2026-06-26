import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "status", date: "2026-06-26", body: "The Lean formalization currently provides partial coverage: the sub-lemmas for Coulomb reversal, pair crossing energy, and bare mass invariance are `sorry`-free, resting on basic arithmetic and ring properties. The remaining gap—the full proposition declaration and the explicit algebraic demonstration of sign reversal under $q \\leftrightarrow q^{-1}$—is highly plausible to close. The formal proof already establishes that the mirror operation swaps the topological crossing counts; upgrading this to the algebraic trace substitution is a localized, routine goal that does not threaten the structural validity of the antiparticle mechanism." },
  ],
  label: "prop:antiparticle-crossing-reversal",
  lean: { ref: "qou:QOU.Torsion.antiparticle_crossing_reversal" },
  title: "Antiparticles from crossing reversal",
  uses: ["def:knot-particle-generation"],
  tags: [
    "trefoil", "chirality", "electron", "positron",
    "antiparticle", "crossing-energy",
  ],
});
