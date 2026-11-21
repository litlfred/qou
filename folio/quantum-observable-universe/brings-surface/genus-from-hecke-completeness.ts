import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:genus-from-hecke-completeness",
  lean: { ref: "qou:QOU.Archimedean.genus_from_hecke_completeness",
    validation: "not_checked",
  },
  title: "Genus from Hecke completeness for torus knots",
  tags: ["torus-knot", "hecke-algebra", "completeness", "genus"],
  uses: ["prop:cohomological-embedding"],
  proofs: ["prf:genus-from-hecke-completeness"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-09-15",
      body: "**The span half of this lemma is withdrawn; the count half stands.** The statement previously read *\"the minimum genus at which the torus-knot evaluations span a 5-dimensional Iwahori--Hecke representation ... Equivalently, the count of embeddable torus knots first reaches or exceeds 5 at genus 4\"*, treating the two as the same claim. They are not: six vectors in a five-dimensional space need not span it. Here they provably do not, because a `T_{r,s}` is a closure on `r` strands and so evaluates only in the `H_r(q)` columns, making the character matrix block-diagonal with a bound of `2 + 2 = 4` at `g = 4` -- independent of `q`, so the appeal to *\"rank 5 for all q > 1, q not a root of unity\"* cannot be repaired by any choice of `q`. Exact symbolic rank over `Q(q)`: `computations/audits/genus_completeness_rank_probe.py`, ranks `1, 2, 3, 4, 4, 5, 5` at `g = 1..7`. Scope (b), invariant = rank subadditivity over a block decomposition. Recorded in `rem:torus-evaluation-block-rank`; bean `qou-r3wu`.",
    },
    {
      kind: "note",
      date: "2026-09-15",
      body: "The Lean sibling's `torusKnotEmbeddingCount` disagreed with this block's own table and was corrected in the same pass: it gave `4 => 5` where the table gives 6, and attributed `T_{3,5}` to `g = 3` where its Seifert genus `(3-1)(5-1)/2 = 4` puts it at `g = 4`. The understated value was exactly the one that made the theorem's `= 5` hold; with the true count the honest statement is `5 <= N(4)`, which is what the lemma claims.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The spanning statement is separated out as [the block-rank remark](#rem:torus-evaluation-block-rank), which records that the evaluation matrix has rank $4$ at $g = 4$, not $5$." },
  ],
});
