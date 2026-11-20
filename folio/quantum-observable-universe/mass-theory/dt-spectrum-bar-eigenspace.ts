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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (conditional on the DT/BPS bridge `conj:stokes-dt-bps-bridge`)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\n`QOU.QBeta.FiveTwoDTSpectrumSplit` (core integers, no archimedean structure)\ncarries the certified matrices `Splus0`/`Sminus0`, the split\n`dt_spectrum_two_element`, and the M0 capstone: `barSwap` with\n`barSwap_involutive`; the eigenspace laws `barEvenPair_fixed`,\n`barOddPair_negated`; the faithful reconstruction `barGrading_faithful`; the\nchirality witness `dtPair52_chiral` and grading `dtPair52_grading` $=(7,1)$; and\n`symmetric_scalar_blind_to_chirality`." },
  ],
});
