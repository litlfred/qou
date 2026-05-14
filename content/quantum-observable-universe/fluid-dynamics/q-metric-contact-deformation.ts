import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-navier-stokes",
  label: "rem:q-metric-contact-deformation",
  title:
    "$q$-deformation as a contact metric change (Miranda picture)",
  uses: [
    "def:q-navier-stokes",
    "def:categorical-reeb-derivation",
    "prop:core-levi-form",
  ],
  cites: ["cardonamirandaperaltasalaspresas2021"],
  tags: [
    "q-deformation",
    "contact-geometry",
    "metric-change",
    "reeb",
    "miranda",
    "fluid-dynamics",
  ],
});
