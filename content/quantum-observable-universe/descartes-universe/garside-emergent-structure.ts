import { remark } from "../../schema/builders";

export default remark({
  label: "rem:garside-emergent-structure",
  title:
    "Nucleons, shells, and confinement are emergent from $H_{3A}(q)$",
  tags: [
    "emergent",
    "garside-element",
    "confinement",
    "nuclear-shell",
    "magic-numbers",
    "quark",
    "nucleon",
  ],
  interprets: "def:two-stage-garside",
  uses: [
    "def:two-stage-garside",
    "prop:confinement-lp",
    "prop:braiding-induced-ordering",
  ],
});
