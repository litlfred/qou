import { remark } from "../../schema/builders";

export default remark({
  label: "rem:covalent-bond-types-remark",
  title: "Single, double and triple bonds",
  interprets: "def:covalent-bond-types",
  tags: ["definition-commentary"],
  uses: [
    "def:covalent-bond-types",
  ],
});
