import { proposition } from "../../schema/builders";

/**
 * Rewritten 2026-08-21 (bean qou-6y28). The original manifest imported
 * `Proposition` from "../../ontologist" — a module that has NEVER existed
 * in this repository (`git log --all` on that path returns zero commits).
 * It therefore never imported, the block never rendered, and no per-block
 * checker ever saw it, from 290ce47222 (2026-07-06) onward.
 *
 * Two fields from the original are deliberately NOT carried over:
 *
 *   - `status: "verified"`. AGENTS.md §4 is explicit that formalization
 *     status is DERIVED at build time and never stored in a `.ts`. A
 *     stored "verified" on a block nothing had ever checked is the exact
 *     claim that rule exists to prevent.
 *   - `statement` / `proofStrategy` as manifest strings. The narrative
 *     belongs in the `.md`, which already carries both verbatim.
 *
 * NOT wired into the chapter manifest, deliberately. Its central claim —
 * that the topological normalization FIXES c_4 = 2, enforcing C = -22 —
 * is a c_k claim, and per AGENTS.md every c_k result in the corpus is
 * convention-C-frame pending the D re-derivation (bean qou-cds1). Adding
 * it to the paper now would introduce an unscoped C-frame claim. The
 * wiring decision belongs after that re-derivation, or after review.
 */
export default proposition({
  label: "prop:qbeta-toroidal-harmonics-basis",
  title: "Toroidal harmonics global basis",
  lean: {
    ref: "qou:QOU.MassEndomorphism.QBetaToroidalHarmonicsBasis.parabolic_cylinder_order_gap_and_c4_iff",
    sorryFree: true,
    validation: "leanok",
  },
  tags: ["qbeta", "toroidal-harmonics", "habiro", "continuum-limit"],
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
});
