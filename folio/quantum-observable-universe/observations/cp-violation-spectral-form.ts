import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cp-violation-spectral-form",
  title:
    "$\\delta_{\\mathrm{CP}}$ as imaginary part of the alternating-block character",
  lean: {
    ref: "qou:QOU.Observations.CPViolationSpectralForm",
    validation: "not_checked",
  },
  uses: [
    "prop:pauli-factor-wedderburn",
    "sec:cp-violation-evidence",
    "conj:complex-chirality-rotation",
  ],
  tags: [
    "cp-violation",
    "delta-cp",
    "imaginary-character",
    "alternating-block",
    "complex-substrate",
    "ckm-phase",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
