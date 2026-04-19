import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:magic-numbers-from-q",
  lean: {
    decl: "QOU.Observations.magic_numbers_from_q",
    validation: "not_checked",
  },
  title:
    "Magic numbers emerge from per-partition nuclear character at $q_0$",
  tags: [
    "magic-numbers",
    "shell-closure",
    "hoefsmit",
    "wedderburn",
    "seminormal-form",
    "block-diagonal",
  ],
  uses: [
    "prop:shell-closure-nf-term-count",
    "prop:nuclear-knot-classification",
    "prop:bw-coefficient-shadow-price",
    "thm:wedderburn-mass-formula",
  ],
});
