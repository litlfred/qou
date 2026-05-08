import { remark } from "../../schema/builders";

export default remark({
  label: "rem:clausen-function-mathlib-filler",
  title:
    "Clausen function $\\mathrm{Cl}_2$ as repo-internal Mathlib filler",
  interprets: "rem:figure-8-archimedean-illustration",
  uses: [
    "rem:figure-8-archimedean-illustration",
    "prop:em-coupling-bring-zero-mode",
  ],
  cites: ["thurston1978", "zagier1986"],
  tags: [
    "mathlib-filler",
    "clausen-function",
    "bloch-wigner",
    "hyperbolic-volume",
    "figure-8-knot",
    "borromean-rings",
    "catalan-constant",
    "lean-infrastructure",
  ],
});
