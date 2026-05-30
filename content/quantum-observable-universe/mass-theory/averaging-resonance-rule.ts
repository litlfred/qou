import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:averaging-resonance-rule",
  title:
    "Averaging-resonant rung selection: $k_{\\mathrm{res}}(n_{\\mathrm{total}}) = \\lfloor n_{\\mathrm{total}}/2 \\rfloor + \\mathbb{1}_{\\mathrm{wrap}}$",
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
    "closure-tier-a",
    "phase-1-discharge",
  ],
});
