import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:three-calibration-discipline",
  label: "rem:three-calibration-discipline-discussion",
  title: "Cohomological alignment and overdetermination",
  tags: ["calibration", "cohomology-alignment", "audit", "discipline"],
  authorNotes: [
    {
      kind: "note",
      body: "Cohomological dimension equality formalized as QOU.Mass.calibrations_eq_cohomology.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/alpha_em_form_ladder_probe.py",
    witness: "computations/alpha-em-form-ladder.witness.json",
    status: "verified",
  },
});
