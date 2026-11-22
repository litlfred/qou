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
 * This is an ALTERNATIVE route to `lem:piece-a-hook-content-identity`; that
 * block's Lean proof takes the arm-leg / β-set route. This identity itself is
 * proved in `QOU/BraidKnot/PieceACornerRemoval.lean`.
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
  lean: {
    ref: "qou:QOU.BraidKnot.PieceACornerRemoval.corner_removal",
  },
  computation: {
    engine: "python",
    script: "computations/probes/piece_a_corner_removal_probe.py",
    witness: "computations/probes/piece-a-corner-removal.witness.json",
    status: "verified",
    requires: [],
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Proved in Lean, sorry-free:** " +
        "`QOU.BraidKnot.PieceACornerRemoval.corner_removal`, over `ℤ`, for any " +
        "Young diagram and any removable corner. The proof splits the cells " +
        "by the corner's column (`card_cells_split`) and uses " +
        "`colLen_corner` (column `s` has `r + 1` cells). This replaces the " +
        "2026-08-24 caveat, which recorded that the seven declarations an " +
        "earlier draft named never existed. The exhaustive probe " +
        "($n \\le 16$, 2,455 corners) stays as an independent check.",
    },
  ],
});
