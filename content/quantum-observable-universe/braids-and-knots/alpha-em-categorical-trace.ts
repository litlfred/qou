import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-categorical-trace",
  title: "Legacy closed form $1/\\alpha_{EM} = 45 \\cdot [3]_q \\cdot (1 + \\delta_{CS} + 8q \\cdot \\delta_{CS}^2)$ as a consequence of the spectral-completeness program",
  interprets: "thm:em-spectral-completeness",
  uses: [
    "thm:em-spectral-completeness",
    "cor:gauge-coupling-uniqueness",
    "prop:gram-determinant-plancherel-ratio",
    "prop:force-carrier-bring-uniqueness",
    "prop:exterior-square-borromean",
  ],
});
