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
    "prop:schur-weyl-mass-decomposition",
    "rem:q-character-closes-parity-gap",
    "rem:mn-classical-parity-blind",
    "prop:categorical-mass-markov",
    "thm:jones-markov-trace",
    "prop:figure-eight-bw-coefficients",
    "thm:frobenius-codim-universal",
    "thm:knot-mass-formula-unified",
  ],
});
