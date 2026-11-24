import { remark } from "../../schema/builders";

export default remark({
  label: "rem:habiro-ring-remark",
  title: "Elements and role of the Habiro ring",
  interprets: "def:habiro-ring",
  uses: [
    "def:habiro-ring",
    "def:algebraic-quantum-volume",
  ],
});
