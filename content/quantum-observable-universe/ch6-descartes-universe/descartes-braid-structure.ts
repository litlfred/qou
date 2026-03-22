import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:descartes-braid-structure",
  title: "Braid-group structure of a Descartes universe",
  tags: ["descartes-universe", "braid-group", "dic3"],
  uses: [
    "def:descartes-condition",
    "prop:braid-action-tensor",
    "def:su2-generators",
    "rem:chirality-trefoil",
    "def:chiral-sector-coords",
    "rem:r-matrix-braiding",
    "ex:trefoil-operator-algebra",
    "prop:brings-is-qou",
    "ex:p-adic-realisation",
  ],
  proofs: ["prf:descartes-braid-structure"],
});
