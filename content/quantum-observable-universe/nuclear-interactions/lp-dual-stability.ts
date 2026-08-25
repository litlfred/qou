import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lp-dual-stability",
  lean: { ref: "qou:QOU.ParticleInteractions.lp_dual_stability", validation: "not_checked" },
  title:
    "LP dual stability: confined hadrons have bounded shadow prices",
  tags: [
    "lp-duality",
    "stability",
    "confinement",
    "frobenius",
    "gram-matrix",
    "shadow-price",
    "hadron",
    "quark",
  ],
  uses: ["rem:confinement-nucleon-unit", "def:lp-stable", "def:lp-confined"],
  computation: {
    engine: "python",
    script: "computations/confinement-operator-selection.py",
    witness: "computations/confinement-operator-selection.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "Two fields of `lp_dual_stability.lean` are archimedean **spectral** " +
        "quantities rather than LP data: `t_norm : ℝ` is the Euclidean norm " +
        "`‖t‖` of the cost vector, and `κ_G : ℝ` is the condition number of " +
        "the Gram matrix (`≈ 7.0`), and the claim they appear in is the " +
        "shadow-price bound `|y*ᵢ| ≤ κ(G)·‖t‖`. A norm and a condition number " +
        "are `ℝ` by meaning — the same reading that made the `nrm : ℝ → ℝ` of " +
        "the topological-mass cluster LEGIT — so the block sits on the " +
        "archimedean side of the §7c wall by construction.",
    },
  ],
});
