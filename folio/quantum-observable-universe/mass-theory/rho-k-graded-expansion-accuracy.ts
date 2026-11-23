import { remark } from "../../schema/builders";

/**
 * Comparison of the truncated graded rho_K expansion with measured atomic
 * masses. Moved out of prop:rho-k-graded-expansion on 2026-11-15 under the
 * owner's ruling that data and fits do not belong in statements.
 */
export default remark({
  label: "rem:rho-k-graded-expansion-accuracy",
  title: "Accuracy of the truncated graded $\\rho_K$ expansion against measured masses",
  interprets: "prop:rho-k-graded-expansion",
  uses: ["prop:rho-k-graded-expansion", "thm:wedderburn-mass-formula", "prop:atomic-mass-gb-nf"],
  computation: {
    engine: "mpmath",
    script: "computations/rho_k_graded_atomic_mass.py",
    witness: ["computations/rho-k-graded-atomic-mass.witness.json"],
    status: "verified",
    requires: ["numpy", "sympy", "mpmath"],
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from the Statement, Significance and Production wiring sections of `prop:rho-k-graded-expansion` (owner ruling 2026-11-15: data and fits go in remarks, not statements).",
    },
  ],
  tags: ["rho-k", "accuracy", "codata-comparison", "production-wiring"],
});
