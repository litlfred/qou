import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:qou-existence-probability",
  label: "rem:logical-existence-categorical",
  title: "Logical existence as categorical quantity",
  uses: [
    "def:qou-existence-probability",
    "def:q-motivic-zeta",
    "conj:q-motivic-transfer",
  ],
  cites: ["denef2001"],
  tags: ["motivic-integration", "model-theory", "interpretation"],
});
