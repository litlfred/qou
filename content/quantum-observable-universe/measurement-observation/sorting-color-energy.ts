import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sorting-color-energy",
  proofs: ["prf:sorting-color-energy"],
  lean: { ref: "qou:QOU.BraidKnot.sorting_color_energy", validation: "not_checked" },
  title:
    "Sorting deposits energy $q + q^{-1}$ per crossing in the colour fibre",
  tags: [
    "sorting",
    "colour-fibre",
    "energy",
    "R-matrix",
    "adjoint",
    "symmetric",
    "antisymmetric",
    "observation",
  ],
  uses: ["rem:observation-braid"],
});
