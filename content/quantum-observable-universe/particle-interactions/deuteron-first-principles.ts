import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:schur-weyl-mass-decomposition",
  label: "rem:deuteron-first-principles",
  title:
    "Deuteron ($^2$H) binding from first principles: full $H_6(q)$ Schur--Weyl sum",
  tags: [
    "deuteron",
    "binding-energy",
    "first-principles",
    "schur-weyl",
    "hecke-character",
    "witness",
    "numerical",
  ],
  uses: [
    "rem:q-character-closes-parity-gap",
    "thm:knot-mass-formula-unified",
  ],
});
