import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-volume",
  label: "rem:quantum-volume-interpretation",
  title: "Volume as knot capacity of $S^3$ fibres",
  tags: [
    "volume",
    "s3-fibre",
    "knot-capacity",
    "configuration-space",
    "classical-limit",
  ],
  uses: [
    "def:quantum-volume",
    "ex:hydrogen-knot-structure",
  ],
});
