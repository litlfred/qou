import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:dt-spectrum-bar-eigenspace",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoDTSpectrumSplit",
    validation: "validated",
  },
  title:
    "The DT-spectrum split is the bar-eigenspace decomposition of the $q\\to0$ Stokes constants",
  uses: [],
  cites: ["garoufalidis-gu-marino2021"],
  tags: [
    "g3-aomega",
    "route-c",
    "bar-parity",
    "dt-invariant",
    "chirality",
    "stokes-constant",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): module `QOU.QBeta.FiveTwoDTSpectrumSplit`: `Splus0`/`Sminus0`, `dt_spectrum_two_element`, `barSwap`, `barSwap_involutive`, `barEvenPair_fixed`, `barOddPair_negated`, `barGrading_faithful`, `dtPair52_chiral`, `dtPair52_grading`, `symmetric_scalar_blind_to_chirality`.",
    },
  ],
});
