import { remark } from "../../schema/builders";

export default remark({
  interprets: "lem:genus-from-hecke-completeness",
  label: "rem:torus-evaluation-block-rank",
  title: "The torus-knot evaluation matrix is block-diagonal, so its rank is bounded below five",
  tags: ["torus-knot", "hecke-algebra", "rank", "genus", "scope-b"],
  uses: ["lem:genus-from-hecke-completeness"],
  computation: {
    script: "computations/audits/genus_completeness_rank_probe.py",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body: "Separated out of `lem:genus-from-hecke-completeness`, whose statement previously read the count and the span as equivalent (\"Equivalently, the count ... first reaches or exceeds 5 at genus g = 4\"). They are not equivalent — six vectors in a five-dimensional space need not span it — and here the span provably fails. The count half is true and stays in the lemma; the span half is false and is recorded here with its scope.",
    },
  ],
});
