import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bar-involution-grading-lean-proofs",
  interprets: "def:bar-involution",
  title: "The $\\mathbb{Z}/2\\mathbb{Z}$ bar-grading: Lean $\\leftrightarrow$ paper proof bridge",
  uses: [
    "def:bar-involution",
  ],
  tags: [
    "lean-infrastructure",
    "bar-invariance",
    "bar-grading",
    "categorical-action",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This remark is the $\\mathbb{Z}/2\\mathbb{Z}$ bar-grading Lean $\\leftrightarrow$\npaper bridge for the [bar-involution](#def:bar-involution): the bar-grading\nsubring/module structure and the Lean theorems with their\nnarrative proofs.\n\n## Proofs (Lean $\\leftrightarrow$ paper bridge)\n\nEvery Lean theorem in [`bar-involution.lean`](bar-involution.lean) has both a narrative proof here and a `sorry`-free formal proof.\n\nLean names cited in the proofs: `BarInvolution.bar_zero`, `bar_one`, `of_mul_antisym`, `IsBarSymmetric.mul`, `of_sym_mul`, `bar_natCast n` (in the `IsBarSymmetric` predicate), `Field R`, `bar_inv`, `bar_two`, `bar_natCast`, `bar_neg`, `pow_two_mul`, `of_sym`, `pow_two_mul_add_one`, `of_antisym`, `bar_half`, `barSkewProjection_of_antisym`.\n\nAll 33 theorems / definitions in [`bar-involution.lean`](bar-involution.lean) have narrative proofs here and `sorry`-free Lean proofs." },
  ],
});
