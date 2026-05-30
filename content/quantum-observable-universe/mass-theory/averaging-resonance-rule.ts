import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:averaging-resonance-rule",
  title:
    "Averaging-resonant rung selection: $k = \\lfloor n_{\\mathrm{total}}/2 \\rfloor$ via half-fill cyclic structure of $\\sigma_{\\mathrm{avg}}$",
  lean: {
    ref: "qou:QOU.BraidKnot.AveragingResonanceRule",
    validation: "not_checked",
  },
  uses: [
    "def:bar-involution",
    "prop:pn-averaging-uniqueness",
  ],
  cites: [
    "wenzl1988",
    "jones1987",
  ],
  tags: [
    "averaging-resonance",
    "half-fill-cyclicity",
    "rung-selection",
    "bar-invariant",
    "level-selection-rule",
    "open-problem",
    "conditional-on-class",
  ],
});
