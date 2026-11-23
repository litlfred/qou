import { remark } from "../../schema/builders";

export default remark({
  label: "rem:frobenius-gram-matrix-context",
  title: "NF Markov-trace computation, operator identification via the dual, and the annihilation identity",
  interprets: "prop:frobenius-gram-matrix",
  tags: ["frobenius", "gram-matrix", "markov-trace", "operator-selection"],
  uses: ["prop:frobenius-gram-matrix"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Proved in [`MarkovGramDegenerate.lean`](../lean/QOU/QBeta/MarkovGramDegenerate.lean): `block_mem_radical` (a zero-weight block lies in the radical) `$\\to$` `gram_det_eq_zero_of_radical_combination` ($\\det G = 0$), with `pairing_descends` and `mem_radical_of_pairing_zero` giving the descent." },
  ],
});
