import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:binding-deuteron-force-carrier",
  title:
    "Deuteron force-carrier identification: $T(2, 3)$ candidate with $\\alpha_{\\mathrm{shift}} = 3$",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988"],
  uses: [
    "prop:binding-alpha-shift-extension",
    "prop:alpha-shift-torus-knot",
  ],
  defines: [],
  tags: [
    "binding",
    "alpha-shift",
    "deuteron",
    "force-carrier-knot",
    "phase-3-candidate",
    "conditional-on-class",
  ],
  lean: { ref: "qou:QOU.BraidKnot.deuteronForceCarrierKnot" },
});
