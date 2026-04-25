import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-dual-space-derivation",
  title:
    "Chirality $a_K = \\prod_{pn} (1 + \\mathrm{sign}\\cdot h)$ from symmetric-channel trace duality",
  lean: {
    ref: "qou:QOU.BraidKnot.chirality_dual_space_derivation",
    validation: "not_checked",
  },
  uses: [
    "prop:chirality-from-frobenius-self-pairing",
    "prop:chirality-writhe-ribbon-derivation",
    "prop:figure-eight-bw-coefficients",
    "prop:three-parameters-wedderburn",
    "thm:frobenius-codim-universal",
    "thm:jones-markov-trace",
  ],
  tags: [
    "chirality",
    "dual-space",
    "wedderburn",
    "symmetric-channel",
    "per-crossing",
    "term-5",
    "derivation",
  ],
});
