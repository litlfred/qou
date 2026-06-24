import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:degree-one-braid-trivial-volume",
  proofs: ["prf:degree-one-braid-trivial-volume"],
  title:
    "Degree-one Hecke elements have vanishing archimedean volume: $\\mathrm{Vol}\\bigl(\\overline{1 + \\sum_i \\phi_i \\sigma_i}\\bigr) = 0$",
  lean: {
    ref: "qou:QOU.Photon.geom_degree_one_zero",
    validation: "not_checked",
  },
  cites: ["jones1987", "kashaev1997"],
  tags: [
    "photon",
    "masslessness",
    "degree-one",
    "archimedean",
    "linearity",
    "unknot",
  ],
});
