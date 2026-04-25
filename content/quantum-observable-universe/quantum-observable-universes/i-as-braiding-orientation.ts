import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braiding-induced-ordering",
  label: "rem:i-as-braiding-orientation",
  title: "The imaginary unit $i$ as braiding-orientation datum",
  tags: [
    "braiding",
    "orientation",
    "imaginary-unit",
    "wick-rotation",
    "cr-structure",
    "arrow-of-time",
    "cpt-symmetry",
  ],
  uses: [
    "sec:linearisation-convention",
    "rem:laplace-fourier-wick-rotation",
    "prop:braiding-induced-ordering",
  ],
});
