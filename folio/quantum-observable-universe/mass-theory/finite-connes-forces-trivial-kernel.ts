import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:finite-connes-forces-trivial-kernel",
  title:
    "Finite Connes distance forces a trivial kernel --- hence the quotient by the radical",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.finite_distance_forces_trivial_kernel",
    validation: "not_checked",
  },
  uses: ["prop:gram-degeneracy-blocks-connes"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Two qualifications travel with the repair. Deleting the radical is observationally\nfree --- no trace value moves, because the deleted block already contributed zero ---\nand that is established by\n[the branching identity](#prop:branching-identity-isospin-weights) rather than\nassumed here. Separately, the distance one recovers is not a Reeb step count at finite\n$q$; the mixing is quantified in\n[the finite-$q$ qualification](#rem:connes-distance-not-reeb-step-count)." },
  ],
  tags: ["connes-distance", "radical-quotient", "temperley-lieb"],
});
