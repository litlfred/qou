import { remark } from "../../schema/builders";

export default remark({
  label: "rem:affine-chart-origin-of-i-and-q",
  title:
    "Affine-chart origin of the categorical coordinates $i$ and $q$",
  tags: [
    "categorical-coordinate",
    "affine-chart",
    "chart-transition",
    "projective-line",
    "imaginary-unit",
    "substrate-parameter",
    "braiding",
  ],
  uses: [
    "prop:spectral-chart-correspondence",
    "def:quantum-gauge-group",
    "rem:i-as-braiding-orientation",
    "rem:braiding-unit-circle-convention",
  ],
  interprets: "def:projective-line-object",
});
