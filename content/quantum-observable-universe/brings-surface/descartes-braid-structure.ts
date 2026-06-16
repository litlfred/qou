import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:descartes-braid-structure",
  lean: { ref: "qou:QOU.Archimedean.descartes_braid_structure",
    validation: "not_checked",
  },
  title: "Braid-group structure of a Descartes universe",
  tags: ["archimedean-universe", "braid-group", "dic3"],
  uses: [
    "prop:braid-action-tensor",
    "def:coral-sector-coords",
    "rem:r-matrix-braiding",
    "ex:trefoil-operator-algebra",
    "prop:brings-is-qou",
    "ex:p-adic-realisation",
  ],
  proofs: ["prf:descartes-braid-structure"],
  computation: {
    engine: "python",
    script: "computations/probes/archimedean_knot_eigenbasis_probe.py",
    witness: "computations/probes/archimedean-knot-eigenbasis-probe.witness.json",
    status: "verified",
  },
});
