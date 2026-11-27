import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:aether-parameter",
  label: "rem:c-aether-via-levi",
  renamedFrom: ["rem:c-substrate-via-levi"],
  title: "Archimedean aether via the Levi form",
  tags: ["substrate", "levi-form", "archimedean"],
  uses: [
    "ex:instanton",
    "ex:self-dual-curvature",
  ],
});
