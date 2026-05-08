import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:alpha-em-gluon-octet-form",
  title:
    "Conjectured closed form $1/\\alpha_{EM} = 45 \\cdot [3]_q \\cdot (1 + \\delta_{CS} + 8q \\cdot \\delta_{CS}^2)$ (PSLQ-empirical, derivation incomplete)",
  uses: [
    "thm:em-spectral-completeness",
    "cor:gauge-coupling-uniqueness",
    "prop:exterior-square-borromean",
    "prop:gram-determinant-plancherel-ratio",
    "prop:force-carrier-bring-uniqueness",
  ],
  cites: ["jones1987", "kassel1995"],
  tags: [
    "alpha-em",
    "fine-structure",
    "conjecture",
    "pslq-empirical",
    "derivation-open",
  ],
});
