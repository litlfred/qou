import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:staircase-ew-residual",
  title:
    "Staircase EW-residual: $q^{1/(2k-1)}$ as pairwise eigenvalue ratio of $\\beta_{\\mathrm{EW}}$ on $V_{\\rho_k}$",
  lean: {
    ref: "qou:QOU.StaircaseCornerHook.StaircaseEWResidual",
    validation: "not_checked",
  },
  uses: [
    "def:staircase-partition",
    "lem:staircase-corner-hook",
    "conj:hoefsmit-ew-cell-content",
    "conj:weinberg-angle-categorical",
  ],
  cites: ["hoefsmit1974", "mathas1999"],
  tags: [
    "staircase-partition",
    "ew-residual",
    "weinberg-angle",
    "hoefsmit-seminormal",
    "hecke-eigenvalue",
    "open-conjecture",
    "tier-a",
  ],
});
