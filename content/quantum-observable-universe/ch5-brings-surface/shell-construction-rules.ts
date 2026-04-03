import { remark } from "../../schema/builders";

export default remark({
  label: "rem:shell-construction-rules",
  title:
    "Construction rules for nuclear shells from the torus knot hierarchy",
  tags: [
    "shell-construction",
    "torus-knot",
    "magic-numbers",
    "groebner-normal-form",
    "borromean",
    "construction-rules",
  ],
  interprets: "cor:spectral-decomposition-qvalue",
  uses: [
    "cor:spectral-decomposition-qvalue",
    "prop:shell-closure-normal-form",
    "prop:skein-finiteness-bound",
    "prop:nuclear-groebner-reduction",
    "rem:fivefold-symmetry",
    "rem:force-knot-identification",
    "def:beta-decay-skein",
  ],
});
