import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-relation",
  title: "Frobenius relation",
  uses: ["def:quantum-universe"],
  examples: ["ex:frobenius-su2"],
  hasProof: true,
  tags: ["category-theory", "frobenius"],
});
