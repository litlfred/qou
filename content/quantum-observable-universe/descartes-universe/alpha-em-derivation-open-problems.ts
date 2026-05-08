import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-derivation-open-problems",
  title:
    "Open problems: deriving the $1.55 \\times 10^{-3}$ correction to the bare $1/\\alpha_{EM} = q[9]_q[10]_q$",
  interprets: "prop:em-coupling-projection",
  uses: [
    "prop:em-coupling-projection",
    "conj:em-coupling-chern-simons",
    "conj:alpha-em-gluon-octet-form",
    "conj:em-coupling-bring-zero-mode",
    "conj:archimedean-functor-uniqueness",
    "rem:figure-8-archimedean-illustration",
    "prop:gram-determinant-plancherel-ratio",
    "rem:gram-kappa-spectral-interpretation",
  ],
  tags: [
    "alpha-em",
    "fine-structure",
    "open-problem",
    "derivation-roadmap",
  ],
});
