import { definition } from "../../schema/builders";

/**
 * §3b-cond hypothesis class encoding the hook-shape formula for
 * the $u$-pole maximizer of $\mathrm{tr}_M$ on canonical atomic
 * braids.
 *
 * Conditional-class carrier for `prop:dominant-pole-partition-hook`
 * per CLAUDE.md §3b-cond.  The proposition asserts that for every
 * $(Z, N)$ with $Z + N \geq 1$, the partition
 * $\lambda_\star(Z, N) = (Z + 2N + 1, 1^{2Z + N - 1})$ uniquely
 * maximizes $|\mathrm{ord}_{u=0}(y_\lambda \cdot \chi^\lambda_q
 * (\beta(Z, N)))|$ over $\lambda \vdash 3A$.  The formula is
 * empirically verified for $\{p, D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$
 * in `per-irrep-pole-atom-crystal.witness.json` but is not
 * substrate-derived (Kashiwara-crystal limit + SYT eigenline tally
 * + uniqueness argument is multi-page work not currently in the
 * repository).
 *
 * The class lets downstream Z/N-dependent derivations (e.g.\ the
 * $\Delta_{\mathrm{coupling}}(Z, N)$ form discussed in the
 * substrate-derivation audit doc) sit on a categorical foundation:
 * assume the hook formula, derive the downstream form, then
 * discharge the assumption when the hook proposition is
 * unconditionally established.
 */
export default definition({
  label: "def:has-hook-maximizer",
  title:
    "Hook-maximizer hypothesis class $\\mathrm{HasHookMaximizer}\\,Z\\,N$ (§3b-cond)",
  uses: [
    "prop:per-nucleon-shift-additive-linearity",
    "rem:crystal-bases-path-a",
  ],
  cites: ["kashiwara1991"],
  lean: {
    ref: "qou:QOU.BraidKnot.HasHookMaximizer",
    validation: "stub",
  },
  tags: [
    "crystal-bases",
    "kashiwara",
    "hook-shape",
    "u-pole",
    "dominant-partition",
    "conditional-class",
    "section-3b-cond",
    "infrastructure",
  ],
});
