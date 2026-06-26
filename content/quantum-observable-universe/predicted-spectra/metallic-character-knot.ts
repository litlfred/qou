import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "Replacing qualitative atomic structure models with a rigid residual-linking-number lambda(R) classification introduces a highly novel knot-theoretic metric for metallic versus noble traits, formalizing Reidemeister-transport conductivity as a core algebraic topological property." },
  ],
  label: "prop:metallic-character-knot",
  lean: { ref: "qou:QOU.Archimedean.metallic_character_knot", validation: "not_checked" },
  title:
    "Metallic character from incomplete sub-Hopf links",
  tags: [
    "metal",
    "metallic-bonding",
    "hopf-link",
    "sub-link",
    "trefoil",
    "delocalization",
    "conductivity",
    "incomplete-shell",
  ],
  uses: ["prop:noble-gas-characterization"],
});
