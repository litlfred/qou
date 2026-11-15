import { lemma } from "../../schema/builders";

/**
 * The corner-removal induction step for Piece A.
 *
 * Removing a removable corner (r,s) from a Young diagram of size n changes
 * the hook lengths in a tightly controlled way: only the corner's own row and
 * column move, and each of those cells loses exactly one from its hook. So
 * the change in Σ h² is a sum of `2h − 1` terms plus the corner's own `1²`,
 * and this lemma evaluates that change in closed form.
 *
 * The right-hand side `(s − r)² + 2n − 1` is exactly what an induction on
 * |λ| has to discharge: `(s − r)` is the content of the corner, so it matches
 * the change in Σ content², and `2n − 1 = n² − (n − 1)²` matches the change
 * in the `+ n²` term.
 *
 * This is an ALTERNATIVE route to `lem:piece-a-hook-content-identity`.  The
 * route Lean takes is arm-leg / β-set, not this one.
 */
export default lemma({
  label: "lem:piece-a-corner-removal-obligation",
  title:
    "Corner-removal obligation: the hook-square change on removing a corner is $(s-r)^2 + 2n - 1$",
  uses: ["lem:piece-a-hook-content-identity"],
  cites: ["macdonald1995", "stanley1999"],
  tags: [
    "piece-a",
    "hook-length",
    "corner-cell",
    "young-diagram",
    "induction",
    "combinatorial-lemma",
  ],
  computation: {
    engine: "python",
    script: "computations/probes/piece_a_corner_removal_probe.py",
    witness: "computations/probes/piece-a-corner-removal.witness.json",
    status: "verified",
    requires: [],
  },
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "**No Lean backing, deliberately unclaimed.** The draft this block " +
        "was promoted from named seven Lean declarations — `colLen_corner`, " +
        "`hook_r_j`, `hook_i_s`, `sum_hook_r`, `sum_hook_s`, " +
        "`sz_decomposition`, `corner_removal_obligation` — and **none of the " +
        "seven exists anywhere in the repository**. Rather than carry a " +
        "dangling `lean.ref`, the block states the mathematics and cites the " +
        "exhaustive probe instead: all five steps and the assembled " +
        "obligation are checked on every corner of every partition of " +
        "$n \\le 16$ (2,455 corners).",
    },
  ],
});
