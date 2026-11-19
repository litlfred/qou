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
    {
      kind: "note",
      body: "Formalized in lean/QOU/QBeta/TemperleyLiebTower.lean (TemperleyLiebTower.traceRadical_two_sided).",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/spectral_decomposition_qvalue_d.py",
    witness: "computations/spectral-decomposition-qvalue-d.witness.json",
    status: "verified",
  },
});
