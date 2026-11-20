import { proposition } from "../../schema/builders";

/**
 * The A₂ root system emerges from the Hecke relations of H₃(q).
 *
 * This is the foundational result of the eightfold-way chapter:
 * the braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ encodes the A₂ Cartan matrix,
 * and the six roots at 120° angles emerge from the Weyl group S₃ acting
 * on the weight space.
 *
 * DERIVATION SOURCE: Purely from QOU's categorical axioms. The A₂
 * structure is a theorem of B₃ representation theory, not an imported
 * physics result.
 */
export default proposition({
  label: "prop:a2-from-three-strands",
  title: "The $A_2$ root system from the Hecke algebra $H_3(q)$",
  uses: [
    "def:braid-group",
    "rem:hecke-algebra-from-braiding",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): > ([Proposition](#prop:schur-weyl-eightfold), where the framework\n> supplies $\\dim V = 2$)" },
  ],
  // The A₂ Cartan data this block states (fixed integer matrix, off-diagonal
  // −1, Serre exponent, root-angle ratio) is machine-checked in
  // WeylInvarianceQDeformation. There is no separate A2FromThreeStrands
  // module — the earlier ref to one did not resolve.
  //
  // The ref now names a DECLARATION, not the module: `cartanMatrix_A2` is the
  // definition packaging the A₂ Cartan datum. Pointing at a theorem would
  // overstate — no declaration in the corpus states this block's headline
  // ("H₃(q) has Coxeter type A₂ and its weight lattice supplies (I₃, Y)"),
  // which the .md itself records as holding by construction. The theorems
  // built on the datum (`cartan_A2_offdiag`, `serre_exponent_A2`,
  // `root_angle_ratio_A2`) live in the same module.
  lean: { ref: "qou:QOU.Eightfold.WeylInvarianceQDeformation.cartanMatrix_A2" },
});
