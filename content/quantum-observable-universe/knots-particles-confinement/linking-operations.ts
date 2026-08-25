import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: enumeration of the two geometric linking operations. Split out of `def:knot-particle-generation` (which retains the torus-knot generator family) so each block defines a single definiendum." },
  ],
  label: "def:linking-operations",
  defines: ["linking-operations"],
  title: "The two geometric linking operations",
  tags: [
    "knot",
    "linking",
    "hopf-link",
    "color-tube",
    "exceptional-divisor",
  ],
  lean: { ref: "qou:QOU.Torsion.LinkingOperation",
    validation: "not_checked",
  },
  uses: ["def:knot-particle-generation"],
});
