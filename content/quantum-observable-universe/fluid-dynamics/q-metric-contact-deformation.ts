import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-navier-stokes",
  label: "rem:q-metric-contact-deformation",
  title:
    "$q$-deformation as a contact metric change (Miranda picture)",
  uses: [
    "rem:q-ns-research-programme",
    "rem:reeb-contact-universal-computer",
  ],
  // This block is the chapter overview (§0). It names results developed
  // across §3-§6 to lay out the picture; it does not depend on them, and a
  // reader is not expected to jump. Recorded as forward pointers rather than
  // dependencies -- see the `overview-source` rows of
  // docs/audits/uses-edge-rejections.json for why these are not `uses[]`.
  foreshadows: [
    "def:ns-obstruction",
    "prop:core-levi-form",
    "rem:hyperbolic-overlap-saturation",
    "rem:townsend-biot-savart-strain",
    "thm:q-ns-wellposedness",
  ],
  cites: ["cardona2021"],
  tags: [
    "q-deformation",
    "contact-geometry",
    "metric-change",
    "reeb",
    "miranda",
    "fluid-dynamics",
  ],
});
