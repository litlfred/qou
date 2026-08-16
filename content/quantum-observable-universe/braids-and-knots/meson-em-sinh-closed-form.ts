import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-em-sinh-closed-form",
  title:
    "Meson EM sinh-channel closed-form $1 + \\hbar_q - \\hbar_q^2/2 = (3q^2 - 1)/(2q^2)$",
  lean: {
    ref: "qou:QOU.BraidKnot.meson_EM_closed_form",
  },
  uses: [],
  computation: {
    engine: "mpmath",
    script: "computations/meson_em_sinh_closed_form.py",
    // The witness is named after the block and its producer's `computation`
    // field is this block's own slug -- provenance, not a decimal coincidence.
    // The block's alpha_em^-1 ~ 137.0359351 is this witness's
    // 137.03593508992864 rounded, and it is the framework's DERIVED value
    // ("No measured constant is imported"), so it is exactly the kind of
    // number that must be traceable to a producer rather than to CODATA.
    witness: [
      "computations/meson-em-sinh-closed-form.witness.json",
    ],
    status: "verified",
    requires: ["mpmath"],
  },
  cites: [
    "kassel1995",
  ],
  tags: [
    "meson",
    "em-coupling",
    "sinh-channel",
    "planck-quantum",
    "closed-form",
    "categorical-derivation",
  ],
});
