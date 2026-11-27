import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quantum-volume-remark",
  title: "Quantum volume of a homogeneous gas",
  interprets: "def:quantum-volume",
  tags: ["definition-commentary"],
  uses: [
    "def:quantum-volume",
  ],
});
