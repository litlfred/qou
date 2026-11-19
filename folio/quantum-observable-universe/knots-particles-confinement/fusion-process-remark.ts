import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fusion-process-remark",
  title: "Fusion processes in the strong sector",
  interprets: "def:fusion-process",
  tags: ["fusion", "strong-sector"],
  uses: [
    "def:fusion-process",
    "def:interaction-sector-taxonomy",
  ],
});
