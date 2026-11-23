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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean status.** We axiomatise the conjecture as a hypothesis-only `class`. We state the spectral content explicitly using `HoefsmitRepresentation.HasEigenvalueRatio`. Downstream Lean theorems take this class as an instance hypothesis and remain rigorous-conditional results." },
  ],
});
