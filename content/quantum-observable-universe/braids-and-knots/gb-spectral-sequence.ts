import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gb-spectral-sequence",
  title:
    "GB-filtration spectral sequence and $E_\\infty$ convergence of the 6-term mass",
  lean: {
    ref: "qou:QOU.BraidKnot.gb_spectral_sequence",
    validation: "not_checked",
  },
  uses: [
    "def:confinement-level",
    "def:hecke-normal-form",
    "prop:gb-residue-spectral-sum",
    "prop:graded-trace-residue-split",
    "prop:schur-weyl-mass-decomposition",
    "thm:frobenius-codim-universal",
    "thm:knot-mass-formula-unified",
  ],
  tags: [
    "spectral-sequence",
    "cohomology",
    "hochschild",
    "gb-filtration",
    "e-infinity",
    "convergence",
  ],
});
