import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:staircase-ew-residual",
  title:
    "Staircase EW-residual: $q^{1/(2k-1)}$ as pairwise eigenvalue ratio of $\\beta_{\\mathrm{EW}}$ on $V_{\\rho_k}$",
  lean: {
    ref: "qou:QOU.StaircaseCornerHook.StaircaseEWResidual",
    validation: "not_checked",
  },
  uses: [
    "def:staircase-partition",
    "lem:staircase-corner-hook",
    "prop:hoefsmit-ew-cell-content",
    "prop:weinberg-angle-categorical",
  ],
  cites: ["hoefsmit1974", "mathas1999"],
  computation: {
    engine: "numpy",
    script: "folio-assistant/computations/staircase_ew_residual_conjecture.py",
    witness: [
      "folio-assistant/computations/staircase-ew-residual-conjecture.witness.json",
      "folio-assistant/computations/close-321-weinberg-gap.witness.json",
    ],
    status: "verified",
  },
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
