import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sorting-color-energy",
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
  uses: [
    "def:observation",
    "def:crossing-energy",
    "rem:observation-braid",
    "def:r-matrix-braiding",
  ],
});
