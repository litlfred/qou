import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-em-sinh-closed-form",
  title:
    "Meson EM sinh-channel closed-form $1 + \\hbar_q - \\hbar_q^2/2 = (3q^2 - 1)/(2q^2)$",
  lean: {
    ref: "qou:QOU.BraidKnot.meson_EM_closed_form",
  },
  uses: [],
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
