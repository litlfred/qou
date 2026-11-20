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
    "lem:staircase-corner-hook",
    "conj:weinberg-angle-categorical",
  ],
  cites: ["hoefsmit1974", "mathas1999"],
  computation: {
    engine: "numpy",
    script: "computations/staircase_ew_residual_conjecture.py",
    witness: [
      "computations/staircase-ew-residual-conjecture.witness.json",
      "computations/close-321-weinberg-gap.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "tier:E",
    "staircase-partition",
    "ew-residual",
    "weinberg-angle",
    "hoefsmit-seminormal",
    "hecke-eigenvalue",
    "open-conjecture",
    "tier-a",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the conjecture is a hypothesis-only `class` whose spectral content uses `HoefsmitRepresentation.HasEigenvalueRatio`; downstream theorems take it as an instance hypothesis.",
    },
  ],
});
