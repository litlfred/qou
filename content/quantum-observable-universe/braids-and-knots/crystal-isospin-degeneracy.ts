import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crystal-isospin-degeneracy",
  title:
    "Crystal-limit isospin degeneracy: $S_{\\mathrm{crystal}}$ is invariant under $\\sigma_i \\leftrightarrow \\sigma_i^{-1}$",
  lean: {
    ref: "qou:QOU.BraidKnot.crystal_isospin_degeneracy",
    validation: "not_checked",
  },
  uses: [
    "conj:shell-correction-term-seven",
    "conj:crystal-graph-realization",
    "prop:content-scaling-correspondence",
    "prop:spin-involution-lp-dual-invariance",
    "rem:lp-dual-isospin-invariance",
  ],
  tags: [
    "crystal-limit",
    "term-7",
    "isospin",
    "tritium",
    "helium-3",
    "shadow-price",
    "q-curvature",
    "shell-correction",
  ],
  cites: ["kashiwara1991", "lecouvey2007"],
});
