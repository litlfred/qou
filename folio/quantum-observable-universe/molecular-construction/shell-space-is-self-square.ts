import { conjecture } from "../../schema/builders";

/**
 * The residual conjecture of the electron-shell capacity program: the shell
 * state space IS the self-square V ⊗ V of the angular object, rather than
 * merely having a dimension that agrees with it.
 *
 * Isolated by the owner ruling of 2026-06-20
 * (docs/audits/2026-06-20-shell-2n2-from-self-square-no-second-su2.md §Residual
 * conjecture): "the shell state space *is* the self-square [n]_q² of the
 * angular element (the V⊗V coproduct). Everything else is exact."
 *
 * Lean sibling carries the conjecture as a content-bearing class per
 * AGENTS.md §3b, plus the exact q-Clebsch-Gordan identity it needs and the
 * sub-shell decomposition derived from it.
 */
export default conjecture({
  label: "conj:shell-space-is-self-square",
  title:
    "The shell state space is the self-square of the angular object",
  lean: {
    ref: "qou:QOU.Molecular.ShellSpaceIsSelfSquare",
    validation: "not_checked",
  },
  uses: [
    "prop:shell-capacity-self-square",
    "conj:orbital-space-normal-bundle",
  ],
  tags: [
    "shell-capacity",
    "self-square",
    "q-clebsch-gordan",
    "coproduct",
    "no-second-su2",
    "open-problem",
  ],
});
