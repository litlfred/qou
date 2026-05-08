import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:upstream-mathlib-additions",
  title:
    "Upstream Mathlib additions: complex dilogarithm via tsum + BW formula + Cl_2 oddness",
  uses: [
    "rem:three-substantive-mathlib-fillers",
    "rem:clausen-function-mathlib-filler",
    "rem:bloch-wigner-mathlib-filler",
  ],
  cites: ["zagier1986", "bloch2000"],
  tags: [
    "mathlib-filler",
    "complex-dilogarithm",
    "bloch-wigner-dilogarithm",
    "clausen-oddness",
    "lean-construction",
    "upstream-contribution",
  ],
  lean: {
    ref: "qou:QOU.Descartes.UpstreamAdditions.complexLiTwo",
    validation: "not_checked",
  },
});
