import { proposition } from "../../schema/builders";

/**
 * Hook-shape formula for the u-pole maximizer λ_⋆(Z, N) of tr_M
 * on the canonical atomic braid β(Z, N) at H_{3A}(q).
 *
 * Conditional on the §3b-cond class `HasHookMaximizer` per CLAUDE.md
 * §3b-cond: the formula is verified for the 5 atoms {p, D, T, ³He,
 * ⁴He} in `per-irrep-pole-atom-crystal.witness.json` and reads off
 * directly from the crystal-bases SYT-eigenline tally, but the
 * universal claim (all Z, N ≥ 0 with Z + N ≥ 1) is not formally
 * derived from substrate primitives — it is encoded as the class
 * hypothesis `HasHookMaximizer Z N`.
 *
 * Promotes the empirical finding documented in
 * `rem:crystal-bases-path-a` to a structural proposition that any
 * downstream Z/N-dependent derivation can take as a categorical
 * input (instead of an empirical-only observation).
 *
 * The hook shape encodes the substrate Z↔N asymmetry directly:
 * width w(Z, N) = Z + 2N + 1, depth d(Z, N) = 2Z + N, so
 * w − d = N − Z + 1.  This is the partition-lattice manifestation
 * of the per-nucleon shift formula 18Z + 21N + 1 — protons are
 * column-favouring (depth-2 per nucleon), neutrons row-favouring
 * (width-2 per nucleon), and the +1 anchor cell is the
 * inter-nucleon interface contribution.
 */
export default proposition({
  label: "prop:dominant-pole-partition-hook",
  title:
    "Hook formula for the $u$-pole maximizer $\\lambda_\\star(Z, N) = (Z + 2N + 1, \\, 1^{2Z + N - 1})$ on canonical atomic braids (conditional on §3b-cond $\\mathrm{HasHookMaximizer}$)",
  uses: [
    "def:has-hook-maximizer",
    "prop:per-nucleon-shift-additive-linearity",
    "rem:crystal-bases-path-a",
  ],
  cites: ["kashiwara1991", "brundankleshchev2009"],
  lean: {
    ref: "qou:QOU.BraidKnot.DominantPolePartitionHook",
    validation: "stub",
  },
  tags: [
    "crystal-bases",
    "kashiwara",
    "u-pole",
    "dominant-partition",
    "hook-shape",
    "conditional-class",
    "section-3b-cond",
    "shift-derivation",
  ],
  computation: {
    engine: "sympy",
    script:
      "folio-assistant/computations/per_irrep_pole_atom_crystal.py",
    witness:
      "folio-assistant/computations/per-irrep-pole-atom-crystal.witness.json",
    status: "verified",
  },
});
