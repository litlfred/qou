import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qou-continuum-kernel-is-frobenius-gram",
  title:
    "QOU's natural quadratic continuum kernel is the Frobenius Gram matrix $G_{\\lambda\\mu} = \\mathrm{tr}_M(b_\\lambda \\cdot b_\\mu)$",
  uses: [
    "prop:operator-selection-lp",
    "prop:frobenius-gram-matrix",
    "prop:cfs-as-traceful-projection-of-qou",
  ],
  cites: ["wenzl1988"],
  tags: [
    "frobenius-gram",
    "continuum-kernel",
    "lp-duality",
    "quadratic-action",
    "established",
  ],
  proofs: ["prf:qou-continuum-kernel-is-frobenius-gram"],
});
