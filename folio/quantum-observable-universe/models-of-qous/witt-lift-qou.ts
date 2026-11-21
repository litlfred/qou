import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:skew-poisson-integration",
  label: "rem:witt-lift-qou",
  title: "Role in the QOU lifting theorem",
  uses: [
    "prop:skew-poisson-integration",
    "prop:jet-prolongation",
    "sec:enveloping-algebras-models",
    "ex:p-adic-realisation",
  ],
});
