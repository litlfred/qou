import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:e-infinity-page-identifications",
  label: "rem:gram-matrix-spectral-connection",
  title:
    "Gram matrix of Markov pairing $\\leftrightarrow$ Frobenius co-Casimir / $E_\\infty$ pairing",
  tags: [
    "gram-matrix",
    "frobenius",
    "co-casimir",
    "markov-pairing",
    "spectral-sequence",
  ],
  uses: [
    "prop:e-infinity-page-identifications",
    "prop:q-laplacian-spectral-tower",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): > ([`TemperleyLiebTower.traceRadical_two_sided`](../lean/QOU/QBeta/TemperleyLiebTower.lean)),\n\n> Proved in\n> [`MarkovGramDegenerate.lean`](../lean/QOU/QBeta/MarkovGramDegenerate.lean):\n> `block_mem_radical` `$\\to$` `gram_det_eq_zero_of_radical_combination` for the\n> vanishing, `pairing_descends` and `mem_radical_of_pairing_zero` for the\n> descent." },
  ],
});
