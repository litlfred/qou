import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:weinberg-angle-categorical",
  title:
    "Weinberg angle $\\theta_W$ as Hecke-eigenvalue ratio on the EW Hoefsmit projectors",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.WeinbergAngleCategorical",
    validation: "not_checked",
  },
  tags: [
    "tier:E",
    "weinberg-angle",
    "electroweak-mixing",
    "hoefsmit-projector",
    "hecke-eigenvalue",
    "frobenius-trace",
    "categorical-physics",
    "open-problem",
    "tier-a",
  ],
  uses: ["def:coulomb-charge", "rem:flavor-charge-assignments"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-22",
      body: "Gating role for Coulomb added 2026-11-22 (issue #9102, PR #9103; audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §28–§29). Split: `QOU/QBeta/NeutralExchangeSplit.lean` (`neutralExchange_split`). Coulomb on nucleons iff the Z part is removed, for every s²; e² = 0 iff g′² = 0: `QOU/QBeta/CoulombNeedsZRemoval.lean` (`coulombShape_iff_Z_removed`, `photon_coupling_eq_zero_iff`). Both sorry-free. Related beans: `qou-zd6l` (vev automorphism, no instance), `qou-h72x` (sin²θ_W numbers inconclusive), `qou-z3x8` (electroweak scale v, no derivation), `qou-fbrp` (T₃ into Y and the normalisation).",
    },
    {
      kind: "status",
      body: "**Open.** The statement is currently a structural proposal;\nthe simple-multiplicity reading numerically fails. To promote\nto a `proposition`, the authoring sequence is:\n\n1. Discharge [`conj:categorical-linking-operation`](#conj:categorical-linking-operation)\n   first — needed to formalise the $W^3$–$B$ interaction.\n2. Discharge [`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)\n   structural assignment (which slot is $W^3$ vs $B$).\n3. Compute $\\cos\\theta_W, \\sin\\theta_W$ from the corrected\n   Hoefsmit-projector traces (using non-uniform multiplicities\n   + linking operation).\n4. Verify against CODATA $\\sin^2\\theta_W$ at the appropriate\n   precision (CODATA-$\\theta_W$ has relative uncertainty\n   $\\sim 10^{-3}$, much weaker than CODATA-$G_F$).",
    },
  ],
});
