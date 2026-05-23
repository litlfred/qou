import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:jet-prolongation-C",
  lean: { ref: "qou:QOU.Torsion.jet_prolongation_C",
    validation: "not_checked",
  },
  title: "Archimedean realisation of jet prolongation",
  tags: ["archimedean", "jet-bundle"],
  uses: ["prop:jet-prolongation", "ex:c-quantum-observable-universe"],
  proofs: ["prf:jet-prolongation-C"],
  computation: {
    engine: "sympy",
    script: "folio-assistant/computations/jet_gb_pl_correspondence.py",
    witness: "folio-assistant/computations/jet-gb-pl-correspondence.witness.json",
    status: "verified",
  },
});
