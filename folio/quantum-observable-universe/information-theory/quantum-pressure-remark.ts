import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quantum-pressure-remark",
  title: "Bulk and boundary pressure",
  interprets: "def:quantum-pressure",
  tags: ["definition-commentary"],
  uses: [
    "def:quantum-pressure",
  ],
});
