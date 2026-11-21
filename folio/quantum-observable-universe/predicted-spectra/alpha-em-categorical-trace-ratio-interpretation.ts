import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-categorical-trace-ratio-interpretation",
  title:
    "Interpretation: $\\alpha_{EM}$ as $h^2$ over force-carrier categorical traces, and its role in the Hartree-energy conjecture",
  interprets: "prop:alpha-em-categorical-trace-ratio",
  uses: [
    "conj:force-carrier-intertwining-correspondence",
    "conj:e-hartree-categorical-derivation",
  ],
  tags: [
    "alpha-em",
    "delta-q-decoration",
    "categorical-trace",
    "hartree-energy",
    "force-carrier",
  ],
});
