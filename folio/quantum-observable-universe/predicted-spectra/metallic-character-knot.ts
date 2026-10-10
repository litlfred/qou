import { proposition } from "../../schema/builders";

export default proposition({
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
