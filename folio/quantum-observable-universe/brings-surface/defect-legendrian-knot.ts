import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:defect-legendrian-knot",
  title: "The unit defect as a Legendrian knot",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.defect_legendrian_knot",
    validation: "stub",
  },
  uses: [
    "def:unit-particle-state",
    "def:categorical-reeb-derivation",
  ],
  tags: ["legendrian", "knot", "contact-geometry", "torsion-leaf"],
});
