import { remark } from "../../schema/builders";

export default remark({
  label: "rem:operational-entropy-remark",
  title: "Operational entropy in q-bits",
  interprets: "def:operational-entropy",
  tags: ["definition-commentary"],
  uses: [
    "def:operational-entropy",
  ],
});
