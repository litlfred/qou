import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sorting-color-energy",
  lean: {
    decl: "QOU.BraidsAndKnots.sorting_color_energy",
    file: "QOU/BraidsAndKnots.lean",
    validation: "not_checked",
  },
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
