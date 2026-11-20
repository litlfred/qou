import { proposition } from "../../schema/builders";

/**
 * The Delta quartet: the fully symmetric three-quark channel at N = 2 flavours,
 * with its third-isospin labelling.
 *
 * Owner decision 5b (2026-10-10, bean qou-nmib): add a NEW block citing the
 * sorry-free N = 2 results of QOU/EightfoldWay/SymmetricChannelDimension.lean.
 * prop:borromean-decuplet is deliberately left unchanged -- its claim and its
 * lean.ref (the N = 3 obstruction-side `eightfold_channels_at_three`) stand.
 *
 * WHY THIS BLOCK IS NOT GATED ON N = 3. The decuplet needs three flavours
 * (Omega-minus is sss), which the framework does not supply (bean qou-j3w6;
 * RowCapObstruction.lean proves the obstruction). The quartet lives entirely
 * at N = 2, the flavour dimension the single-fibre tower does have, so nothing
 * here is conditional on the chapter's open problem.
 *
 * Lean (all sorry-free; #print axioms = propext, Classical.choice, Quot.sound):
 *   quadruplet_dim       dim of degree-3 forms in 2 variables = C(4,3) = 4
 *                        (a consequence of finrank_homogeneousSubmodule,
 *                        general N, n, base semiring -- not a hardcoded table)
 *   twoI3_quartetPoint   the ladder 2I3 = 3, 1, -1, -3 is ATTAINED
 *   twoI3_mem_ladder     every diagram point carries one of those -- CLOSED
 *   twoI3_odd            2I3 is odd at every point (half-integral weights)
 *   twoI3_injOn          distinct points carry distinct 2I3 -- FAITHFUL
 * The ref names `quadruplet_dim`, the dimension statement; the four I3
 * theorems sit in the same section of the same module and are cited in the .md.
 *
 * CONTRAST with prop:baryon-octet-decomposition: there the weight map is proved
 * NON-injective (Lambda / Sigma^0 share a weight); here it is proved INJECTIVE.
 *
 * SCOPE. Weights only. No isospin SU(2) action, no raising/lowering operators,
 * no spin-3/2, no masses. Model register: "Delta quartet" names a construction;
 * no experimental comparison is made in this block.
 *
 * PLACEMENT: directly after borromean-decuplet-derivation in
 * sec:baryon-multiplets, after prop:schur-weyl-eightfold, so its uses[] edge
 * runs backward. Section 5 -> 6 blocks, inside the detangler 3-18 band.
 */
export default proposition({
  label: "prop:delta-quartet-isospin-ladder",
  title: "The $\\Delta$ quartet as the symmetric channel at two flavours",
  uses: [
    "prop:schur-weyl-eightfold",
  ],
  lean: { ref: "qou:QOU.EightfoldWay.SymmetricChannelDimension.quadruplet_dim" },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean.**  `QOU.EightfoldWay.SymmetricChannelDimension`:\n`quadruplet_dim` (the dimension, as a consequence of the general\n`finrank_homogeneousSubmodule`), `twoI3_quartetPoint` (attained),\n`twoI3_mem_ladder` (closed), `twoI3_odd` (odd) and `twoI3_injOn` (faithful)." },
  ],
});
