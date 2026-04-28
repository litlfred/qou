import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:descartes-braid-structure",
  lean: { ref: "qou:QOU.Descartes.descartes_braid_structure",
    validation: "not_checked",
  },
  title: "Braid-group structure of a Descartes universe",
  tags: ["descartes-universe", "braid-group", "dic3"],
  uses: [
    "prop:braid-action-tensor",
    "def:coral-sector-coords",
    "rem:r-matrix-braiding",
    "ex:trefoil-operator-algebra",
    "prop:brings-is-qou",
    "ex:p-adic-realisation",
  ],
  proofs: ["prf:descartes-braid-structure"],
});
