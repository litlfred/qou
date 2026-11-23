import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qbeta-z-recursion-to-ck-recursion-bridge",
  title: "Proof of qbeta z recursion to ck recursion bridge",
  uses: ["prop:qbeta-z-recursion-to-ck-recursion-bridge"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean proof is `field_simp` + `linarith` on the recursion equation.\n\n## Structural relationship to `CKRecursion`\n\nThe `QOU.QBeta.CKRecursion.CKRecursion ℝ` structure defined in\n\nwhere `kernel : Fin d → ℝ` is a fixed coefficient vector\n\n| **Kernel** | `Fin d → R` (constant) |\n\n| Yes (proven, `applyRecursion_linear`) |\n\nA literal `CKRecursion ℝ` instance cannot be\nconstructed from a `ZRecursionCoeffs` instance alone (the kernel\nshapes differ).\n\n- **A concrete `CKRecursion ℝ` instance.**" },
  ],
});
