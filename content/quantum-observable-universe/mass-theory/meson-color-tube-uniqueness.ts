import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-color-tube-uniqueness",
  title: "Meson m_K/m_π ratio uniqueness via the α_shift universal chain",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988"],
  // Note: uses are kept light — the structural dependency on
  // prop:alpha-shift-torus-knot is documented in the narrative,
  // following the planned-block convention.
  uses: [],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "uniqueness", "meson"],
  lean: { ref: "qou:QOU.BraidKnot.meson_ratio_via_alpha_shift" },
});
