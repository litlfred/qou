import { definition } from "../../schema/builders";

export default definition({
  label: "def:nucleon-pair-isospin-channel",
  title:
    "Colour-system selection by isospin: $\\mathrm{select}(p) = \\mathrm{altT_1}$ iff $T(p) = 1$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.ColorFlavorIsospinSelection.select",
    validation: "not_checked",
  },
  uses: ["prop:isospin-singlet-binds-more"],
  tags: ["isospin", "colour-system", "nucleon-pair", "conditional-class"],
});
