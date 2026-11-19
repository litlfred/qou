import { remark } from "../../schema/builders";

export default remark({
  label: "rem:interaction-sector-taxonomy-remark",
  title: "Processes, parity and the electromagnetic cell of the taxonomy",
  interprets: "def:interaction-sector-taxonomy",
  tags: ["interaction-sector", "bar-parity"],
  uses: [
    "def:interaction-sector-taxonomy",
    "def:fusion-process",
    "conj:binding-qbeta-complex-volume",
  ],
});
