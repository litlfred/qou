import { remark } from "../../schema/builders";

export default remark({
  label: "rem:crossing-energy-sign",
  title: "Sign convention and reading of the crossing energy",
  interprets: "def:crossing-energy",
  tags: ["crossing-energy", "skein"],
  uses: [
    "def:crossing-energy",
  ],
});
