import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-alpha-shift-extension",
  title: "Binding A≥3 via per-rep Reeb phase at a force-carrier torus knot",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988"],
  uses: [],
  defines: [],
  tags: ["normalization", "no-fitting", "uniqueness", "binding", "alpha-shift"],
  lean: { ref: "qou:QOU.BraidKnot.binding_unique_via_alpha_shift" },
});
