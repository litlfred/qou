import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qou-continuum-kernel-is-frobenius-gram",
  title: "Proof: QOU's quadratic continuum kernel is the Frobenius Gram matrix",
  uses: [
    "prop:qou-continuum-kernel-is-frobenius-gram",
    "prop:operator-selection-lp",
    "prop:frobenius-gram-matrix",
  ],
});
