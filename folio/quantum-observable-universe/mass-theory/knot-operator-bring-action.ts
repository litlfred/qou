import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-operator-bring-action",
  title:
    "Knot-operator actions on the Bring surface and $\\mathrm{SO}(3)$ structure",
  interprets: "def:brings-surface",
  uses: [
    "rem:hecke-quandle",
    "prop:markov-trace-ratio-exact",
  ],
  cites: [
    "jones1987",
    "reshetikhin1991",
  ],
  tags: [
    "bring-surface",
    "knot-operator",
    "so3",
    "gram-matrix",
    "color-tube",
    "mass-tower",
  ],
});
