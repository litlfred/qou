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
});
