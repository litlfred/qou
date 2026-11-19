import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quantum-temperature-remark",
  title: "Temperature, substrate density and entropy",
  interprets: "def:quantum-temperature",
  tags: ["definition-commentary"],
  uses: [
    "def:quantum-temperature",
  ],
});
