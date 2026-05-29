import { remark } from "../../schema/builders";

export default remark({
  label: "rem:complex-chirality-rotation",
  title: "Chirality as continuous phase rotation in the pre-observable sector",
  lean: {
    ref: "qou:QOU.ComplexChiralityRotation.ComplexChiralityRotation",
    validation: "not_checked",
  },
  uses: [
    "rem:complex-substrate-interpretation",
    "rem:chirality-trefoil-electron-positron",
  ],
  tags: ["complex-q", "chirality", "CPT", "phase", "conjecture"],
});
