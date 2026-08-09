import { remark } from "../../schema/builders";

export default remark({
  label: "rem:isospin-selection-class-inhabited",
  title:
    "$\\mathrm{InterfaceExchangeAntisymmetry}$ is inhabited by $\\langle\\mathrm{select},\\,\\mathrm{rfl}\\rangle$ --- the class carries physics, not a constraint",
  interprets: "def:nucleon-pair-isospin-channel",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.ColorFlavorIsospinSelection.trivially_inhabited",
    validation: "not_checked",
  },
  uses: ["def:nucleon-pair-isospin-channel"],
  tags: ["conditional-class", "vacuity", "isospin", "colour-system"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "Retraction carrier. The class docstring in " +
        "lean/QOU/BraidsAndKnots/ColorFlavorIsospinSelection.lean previously ended 'so it is " +
        "not vacuously satisfiable', which is false; trivially_inhabited is the machine-verified " +
        "correction. The four downstream theorems (charge_symmetric_pp_nn, " +
        "like_nucleon_forced_to_altT1, only_singlet_channel_free, " +
        "pn_symmetric_groups_with_like_nucleons) remain CONDITIONAL — their prose must not be " +
        "read as unconditional — but they are conditional on a physical identification rather " +
        "than on an open mathematical hypothesis.",
    },
  ],
});
