import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gluon-octet-ruled-out",
  title:
    "Refutation: $45 \\cdot [3]_q \\cdot (1 + \\delta_{CS} + 8q\\,\\delta_{CS}^2)$ cannot be a closed-form $\\tau_{\\mathrm{arch}}$-image of $1/\\alpha_{EM}$",
  uses: [
    "prop:archimedean-functor-uniqueness",
    "prop:em-coupling-bring-zero-mode",
    "conj:alpha-em-gluon-octet-form",
    "rem:alpha-em-derivation-open-problems",
  ],
  cites: ["suslin1991", "bloch2000"],
  tags: [
    "alpha-em",
    "fine-structure-constant",
    "refutation",
    "ruled-out",
    "pslq",
    "structural-audit",
    "multiplicative-family",
  ],
  lean: {
    ref: "qou:QOU.Descartes.gluon_octet_ruled_out",
    validation: "not_checked",
  },
});
