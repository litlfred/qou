import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cp-violation-spectral-form",
  title:
    "$\\delta_{\\mathrm{CP}}$ as imaginary part of the alternating-block character",
  lean: {
    ref: "qou:QOU.Observations.cp_violation_spectral_form",
    validation: "not_checked",
  },
  uses: [
    "prop:pauli-factor-wedderburn",
    "sec:cp-violation-evidence",
  ],
  tags: [
    "cp-violation",
    "delta-cp",
    "imaginary-character",
    "alternating-block",
    "complex-substrate",
    "ckm-phase",
  ],
});
