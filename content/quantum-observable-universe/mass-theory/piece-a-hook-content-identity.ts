import { lemma } from "../../schema/builders";

/**
 * Piece A of Identity I — the per-partition hook–content identity.
 *
 * Identity I is `2·M(n) = n(3n−1)`, and its content decomposition
 * splits into two pieces:
 *
 *   Piece A  (the `2n²` half):  Σ_□ h(□)² = Σ_□ c(□)² + n²,  per partition
 *   Piece B  (the `n(n−1)` half): E_Planch[Σ_□ c(□)²] = C(n,2)
 *
 * This block is Piece A.  Its point is what it does NOT use: no
 * hook-length formula, no dimension, no SYT count, no RSK.  It is a
 * single-Young-diagram combinatorial fact, so it is not blocked on the
 * representation-theoretic infrastructure that Piece B needs.
 *
 * Two routes toward it are carried in this section: the Jucys–Murphy /
 * Specht trace route (`lem:piece-a-specht-character-trace`), which supplies
 * the content-sum side representation-theoretically, and the corner-removal
 * induction (`lem:piece-a-corner-removal-obligation`).
 */
export default lemma({
  label: "lem:piece-a-hook-content-identity",
  title:
    "Piece A — the hook–content identity $\\sum_{\\square} h(\\square)^2 = \\sum_{\\square} c(\\square)^2 + n^2$",
  lean: {
    ref: "qou:QOU.BraidKnot.PieceA.pieceA",
    validation: "not_checked",
  },
  uses: [],
  cites: ["macdonald1995", "stanley1999"],
  tags: [
    "piece-a",
    "hook-length",
    "cell-content",
    "young-diagram",
    "identity-i",
    "hlf-free",
    "plancherel",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "**What Lean actually proves, and by which route.** The general-`n` " +
        "statement is sorry-free twice over: `QOU.BraidKnot.PieceA.pieceA` " +
        "over Mathlib's `YoungDiagram` (bean `qou-o5xj`), and " +
        "`QOU.BraidKnot.IdentityI.sumSqHooks_eq_sumSqContents_add_sq` over " +
        "weakly-decreasing `List ℕ`. Both take the **arm–leg / β-set** route " +
        "— expand `h = arm + leg + 1`, reduce to a pair count. Neither takes " +
        "the corner-removal induction of " +
        "`lem:piece-a-corner-removal-obligation`, which remains an " +
        "unformalised alternative.",
    },
  ],
});
