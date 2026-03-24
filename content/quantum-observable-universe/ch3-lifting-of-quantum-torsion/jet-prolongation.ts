import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-prolongation",
  lean: { decl: "QOU.JetProlongation" },
  title: "Jet Prolongation",
  tags: ["jet-bundle", "frobenius-hopf", "prolongation"],
  examples: ["ex:jet-prolongation-su2"],
  uses: ["def:quantum-observable-universe"],
  proofs: ["prf:jet-prolongation"],
});
