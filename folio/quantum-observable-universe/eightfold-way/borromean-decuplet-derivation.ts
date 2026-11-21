import { proposition } from "../../schema/builders";

/**
 * Borromean decuplet derivation.
 *
 * Connects the Schur-Weyl decuplet (symmetric partition (3) at N=3)
 * to the Borromean baryon structure from Chapter 9. The fully symmetric
 * channel of 3⊗3⊗3 gives the 10-dimensional decuplet, realized
 * topologically by three quark-unknots in the Borromean link.
 *
 * ANTI-FITTING: conditional on N=3 (the chapter's central open problem).
 * At N=2, the symmetric channel gives only a quadruplet.
 */
export default proposition({
  label: "prop:borromean-decuplet",
  title: "The baryon decuplet as symmetric Borromean channel",
  uses: [
    "prop:schur-weyl-eightfold",
    "def:borromean-baryon",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , whose weight\ndiagram and its degeneracy are treated in\n[the octet proposition](#prop:baryon-octet-decomposition)" },
  ],
  // Lean backs the DIMENSION claim the block states: the fully-symmetric
  // Schur-Weyl channel at N = 3 has dimension C(5,3) = 10 (the decuplet).
  // `eightfold_channels_at_three` proves sorry-free that weylDimSym 3 = 10
  // (= (3+2).choose 3), alongside the octet (8) and singlet (1) and the
  // 10 + 2·8 + 1 = 27 = 3³ channel arithmetic. It does NOT formalise the
  // topological realisation by the Borromean baryon (that is def:borromean-
  // baryon + the weight table) nor quantum Schur-Weyl duality itself
  // (chapter open problem, bean qou-8pl3); this backs the dimension shadow.
  lean: { ref: "qou:QOU.Eightfold.RowCapObstruction.eightfold_channels_at_three" },
});
