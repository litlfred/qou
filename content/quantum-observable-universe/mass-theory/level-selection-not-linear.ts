import { proposition } from "../../schema/builders";

/**
 * Conditional (§3b-cond) exclusion of linear / bond-count level-selection:
 * given the geometric tower lower bound (conj:tower-geometric-lower-bound) and
 * extensive binding for A ≥ 1, a geometric c·r^A eventually beats any linear
 * M·A, so no linear selection rule is consistent — the level is at most
 * logarithmic. Lean sorry-free (QOU.Mass.LevelSelection.no_linear_selection),
 * via Mathlib isLittleO_coe_const_pow_of_one_lt. The A ≥ 1 restriction (avoiding
 * the A=0 boundary artifact) is stated in the narrative.
 */
export default proposition({
  label: "prop:level-selection-not-linear",
  title: "Linear level-selection is excluded (exponential beats linear)",
  lean: {
    ref: "qou:QOU.Mass.LevelSelection.no_linear_selection",
    validation: "not_checked",
  },
  uses: ["conj:tower-geometric-lower-bound"],
  tags: ["binding", "level-selection", "logarithmic", "gap-a-3", "brane-tower"],
});
