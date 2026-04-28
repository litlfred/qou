import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:magic-numbers-from-q",
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
  ],
});
