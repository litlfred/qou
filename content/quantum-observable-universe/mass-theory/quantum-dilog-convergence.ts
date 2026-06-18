import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-dilog-convergence",
  title:
    "Convergence of the quantum dilogarithm $\\Phi_q$ on $\\lvert z\\rvert < q$",
  // The proof lives in the library file PhiQConvergence.lean (sorry-free);
  // ref the library decl directly — no sibling stub (CLAUDE.md no-shadowing).
  lean: {
    ref: "qou:QOU.MassEndomorphism.PhiQConvergence.quantumDilog_multipliable",
    validation: "not_checked",
  },
  uses: ["cor:quantum-dilogarithm"],
  cites: ["habiro2004cyclotomic"],
  tags: [
    "brane-tower",
    "quantum-dilogarithm",
    "convergence",
    "algebraic-cauchy-limit-half",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-06-18",
      body:
        "**Promoted from infrastructure to proposition (2026-06-18).** The " +
        "Multipliable statement `QOU.MassEndomorphism.PhiQConvergence." +
        "quantumDilog_multipliable` is proved sorry-free (via " +
        "`summable_q_inv_geometric` + `quantumDilog_factors_nonzero` + " +
        "`Real.multipliable_one_add_of_summable`); this block elevates it to a " +
        "first-class theorem. It is the convergence half of " +
        "`conj:brane-tower-z-habiro` that survives the n⋆ refutation. Does NOT " +
        "wire to the production mass table (see prop:mass-endomorphism-tower, " +
        "which uses the bounded −Li₂^q form at the physical z = |V̂_i| < 1).",
      see: "docs/audits/2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md",
    },
  ],
});
