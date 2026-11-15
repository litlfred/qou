import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:crossing-energy",
  label: "rem:unit-circle-photonic-sector",
  title: "Phase on the circle, mass off it",
  tags: ["symmetric-point", "unit-circle", "photon", "crossing-energy"],
  uses: [
    "def:crossing-energy",
    "def:categorical-dirac-operator",
  ],
});
