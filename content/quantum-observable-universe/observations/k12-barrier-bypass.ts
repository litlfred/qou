import { remark } from "../../schema/builders";

export default remark({
  label: "rem:k12-barrier-bypass",
  title:
    "Analytic bypass of the $k \\geq 12$ matrix-evaluation barrier",
  interprets: "prop:magic-numbers-from-q",
  uses: [
    "prop:magic-numbers-from-q",
    "conj:homological-shell-condensation",
    "conj:diagrammatic-double-magic-lr-fusion",
  ],
  tags: [
    "magic-numbers",
    "computational-limits",
    "hoefsmit",
    "homological",
    "k12-barrier",
  ],
});
