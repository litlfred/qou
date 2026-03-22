import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:jet-prolongation-C",
  title: "Archimedean realisation of jet prolongation",
  tags: ["archimedean", "jet-bundle"],
  uses: ["prop:jet-prolongation", "def:c-quantum-observable-universe"],
  proofs: ["prf:jet-prolongation-C"],
});
