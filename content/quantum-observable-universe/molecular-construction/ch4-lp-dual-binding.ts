import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ch4-lp-dual-binding",
  lean: { ref: "qou:QOU.Molecular.ch4_lp_dual_binding", validation: "not_checked" },
  title: "$S_4$-symmetric strand ordering minimises $\\Phi_1$ for $CH_4$",
  uses: [
    "conj:q-integer-mass-formula",
    "def:ch4-molecular-braid",
    "prop:h2-lp-dual-binding",
  ],
  tags: ["CH4", "LP-dual", "tetrahedral", "S4-symmetry"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/Molecular/ch4_lp_dual_binding.lean` " +
        "carries the per-bond and total binding energies `E_bind_per_bond`, `E_bind_CH`, `E_bind_total` as physical quantities. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
