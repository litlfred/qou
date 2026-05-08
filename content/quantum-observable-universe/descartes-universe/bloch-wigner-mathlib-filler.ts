import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bloch-wigner-mathlib-filler",
  title:
    "Bloch-Wigner dilogarithm $D$ on the unit circle — repo-internal Mathlib filler",
  interprets: "rem:clausen-function-mathlib-filler",
  uses: [
    "rem:clausen-function-mathlib-filler",
    "rem:figure-8-archimedean-illustration",
    "prop:em-coupling-bring-zero-mode",
  ],
  cites: ["thurston1978", "zagier1986"],
  tags: [
    "mathlib-filler",
    "bloch-wigner",
    "dilogarithm",
    "unit-circle",
    "figure-8-knot",
    "borromean-rings",
    "lean-infrastructure",
  ],
});
