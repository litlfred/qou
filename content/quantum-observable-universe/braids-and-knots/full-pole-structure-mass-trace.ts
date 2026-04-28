import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:full-pole-structure-mass-trace",
  title:
    "Full pole structure of the mass trace: all roots of unity, with interference",
  lean: {
    ref: "qou:QOU.BraidKnot.full_pole_structure",
    validation: "not_checked",
  },
  uses: ["prop:schur-weyl-mass-decomposition"],
  tags: [
    "residue",
    "root-of-unity",
    "habiro-ring",
    "cyclotomic",
    "interference",
    "mittag-leffler",
    "mass",
  ],
});
