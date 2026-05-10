import { remark } from "../../schema/builders";

export default remark({
  label: "rem:crystal-bases-path-a",
  title:
    "Crystal-bases Path A: GS-reduction-free pole-order verification of $\\mathrm{shift}_{\\mathrm{NF}}(\\beta_K) = 18Z + 21N + 1$",
  interprets: "prop:per-nucleon-shift-additive-linearity",
  uses: [
    "prop:per-nucleon-shift-additive-linearity",
    "prop:crystal-isospin-degeneracy",
    "conj:crystal-graph-realization",
  ],
  tags: [
    "crystal-bases",
    "kashiwara",
    "path-a",
    "pole-order",
    "u-pole",
    "gs-reduction",
    "compute-optimization",
    "shift-derivation",
    "h-followup",
  ],
  cites: ["kashiwara1991", "lecouvey2007", "brundankleshchev2009"],
});
