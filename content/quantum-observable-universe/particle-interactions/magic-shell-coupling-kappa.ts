import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:magic-shell-coupling-kappa",
  title:
    "Magic-shell coupling slope $\\kappa = -E_0 \\cdot \\log(1/h) / ([2]_q [3]_q)$ — categorical closed form",
  lean: {
    ref: "qou:QOU.BraidKnot.MagicShellCouplingKappa",
    validation: "not_checked",
  },
  uses: [
    "prop:compound-beta-shell-calibration",
  ],
  cites: [],
  tags: [
    "magic-shell",
    "coupling-slope",
    "categorical-closed-form",
    "kappa",
    "h7a",
    "q-bracket",
    "no-empirical-fit",
  ],
  computation: {
    engine: "python",
    script:
      "computations/probe_kappa_categorical_h7a_closed.py",
    witness:
      "computations/kappa-categorical-h7a-closed.witness.json",
    status: "verified",
  },
});
