import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:isovector-chiral-residue",
  title: "Binding isovector coefficient as the $W_\\lambda$ chiral residue (conditional)",
  uses: [
    "prop:mirror-baseline-cancellation",
    "prop:chirality-residue-mass-term",
    "rem:archimedean-chirality",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.binding_isovector_mirror_from_chiral",
  },
  tags: [
    "mba",
    "sidecar",
    "delta-lambda",
    "isovector",
    "chirality",
    "bring-surface",
    "keystone-residual-i",
    "conditional",
  ],
});
