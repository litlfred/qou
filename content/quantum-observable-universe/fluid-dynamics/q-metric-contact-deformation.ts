import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-navier-stokes",
  label: "rem:q-metric-contact-deformation",
  title:
    "$q$-deformation as a contact metric change (Miranda picture)",
  // rem:reeb-contact-universal-computer stays a dependency: it lives in
  // `quantum-observable-universes` (chapter 2) while this block is in
  // `fluid-dynamics` (chapter 18), so it points BACKWARD across sixteen
  // chapters. The reader passed it long ago -- an ordinary prerequisite, not
  // a preview.
  uses: ["rem:reeb-contact-universal-computer"],
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
    // Reclassified from a dependency: same-chapter, pos 9 -> 95, and the
    // prose names it as the programme this chapter builds toward rather than
    // as something the reader needs first. This retires one of
    // fluid-dynamics' twelve pre-existing forward edges by classifying it
    // correctly. NOTE: never write a closing square bracket inside a comment
    // in this array — the manifest parsers match it non-greedily and stop at
    // the first one, silently dropping every entry after this point.
    "rem:q-ns-research-programme",
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
