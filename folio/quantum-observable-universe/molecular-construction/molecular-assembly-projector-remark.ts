import { remark } from "../../schema/builders";

export default remark({
  label: "rem:molecular-assembly-projector-remark",
  title: "The assembly projector as a q-Young symmetriser",
  interprets: "def:molecular-assembly-projector",
  tags: ["definition-commentary"],
  uses: [
    "def:molecular-assembly-projector",
    "ex:benzene-symmetric-projector",
  ],
});
