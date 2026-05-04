import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-calibration-inputs",
  title:
    "Exactly three calibration inputs ($m_e$, $m_\\mu/m_e$, $Q_\\beta(n)$), aligned to the three Wedderburn channels of $H_3(R, q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.three_calibration_inputs",
    validation: "not_checked",
  },
  uses: [
    "rem:calibration-inputs",
    "prop:three-parameters-wedderburn",
    "prop:categorical-mass-markov",
  ],
  cites: ["codata2022"],
  tags: [
    "calibration",
    "three-parameters",
    "mass-scale",
    "energy-scale",
    "substrate-parameter",
    "wedderburn",
    "cohomology",
    "no-fitting",
    "predictive-content",
  ],
});
