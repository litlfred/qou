import { remark } from "../../schema/builders";

export default remark({
  label: "rem:clausen-function-mathlib-filler-open-gaps",
  title: "Mathlib gaps still open after the $\\mathrm{Cl}_2$ filler",
  interprets: "rem:figure-8-archimedean-illustration",
  uses: ["prop:em-coupling-bring-zero-mode"],
  tags: ["mathlib-filler", "bloch-wigner", "lean-infrastructure", "open-gaps"],
});
