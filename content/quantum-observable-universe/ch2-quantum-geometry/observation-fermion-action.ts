import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:observation-fermion-action",
  title: "The observer acts directly on fermions via the colour fibre",
  tags: [
    "observation",
    "fermion",
    "boson",
    "colour-fibre",
    "adjoint",
    "eigenspace",
    "R-matrix",
    "uncertainty",
  ],
  uses: [
    "def:observation",
    "prop:observation-energy",
    "rem:two-observer-parallelogram",
    "def:fermion-boson-decomposition",
    "prop:fibre-functor-atlas",
  ],
});
