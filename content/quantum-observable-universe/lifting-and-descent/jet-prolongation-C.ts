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
});
