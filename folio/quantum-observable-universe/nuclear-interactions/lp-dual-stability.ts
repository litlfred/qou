import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lp-dual-stability",
  lean: { ref: "qou:QOU.ParticleInteractions.lp_dual_stability", validation: "not_checked" },
  title:
    "LP dual stability: the confined optimum is LP-stable and strongly dual",
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
      kind: "status",
      date: "2026-11-21",
      body:
        "**Narrowed to the two claims Lean derives** (owner instruction \"1 2\", thread \"N2 Lean foundations\"). Until this date the block stated four claims and its Lean returned four fields of a context record, the self-assuming projection of AGENTS.md §3b-cond item 5. `QOU.ParticleInteractions.lp_dual_stability` now writes the operator-selection LP in standard form and derives LP-stability ($Gx^* \\ge 0$) from feasibility and strong duality from the in-repo `lp_strong_duality_uncond`, sorry-free. The shadow-price bound $|y^*_i| \\le \\kappa(G)\\|t\\|$ and the instability of $\\sigma_0\\sigma_1^{-1}$ are not consequences of LP duality; they moved to `rem:lp-dual-stability-confinement-reading`, which records that neither is currently checked. The title, which named the shadow-price bound, changed accordingly.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** The Lean states the LP over `ℝ`: feasibility uses the order `x ≥ 0`, and strong duality comes from the in-repo LP duality theorem over `ℝ`. The block therefore sits on the archimedean side of the §7c wall. (Until 2026-11-21 this note named the fields `t_norm` and `κ_G` of the old context record; that record and the shadow-price bound it carried are gone.)",
    },
  ],
});
