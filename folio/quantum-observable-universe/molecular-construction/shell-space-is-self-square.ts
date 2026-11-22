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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): proved for every $n$ in the Lean sibling as `qCG_self_square`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling records this as `subshell_decomposition_of_self_square`, derived from the conjectural hypothesis rather than assumed alongside it, together with a concrete refuting witness `not_selfSquare_linear` showing that the class is not satisfied by an arbitrary dimension function." },
    {
      kind: "note",
      body: "Before `qCG_self_square`, only the $q = 1$ integer specialisation $\\sum_{\\ell<n}(2\\ell+1) = n^2$ was formalised; the $q$-deformed statement had been checked symbolically for $n = 1,\\ldots,8$ in `computations/shell_capacity_chebyshev_bridge.py`.",
    },
  ],
});
