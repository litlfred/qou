import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:jet-horizon",
  label: "rem:stretched-horizon",
  title: "The stretched horizon as the degree-$1$ quotient sheaf $\\Gamma(\\mathcal{H}, A_1/A_0)$",
  tags: [
    "jet-horizon",
    "black-hole-complementarity",
    "stretched-horizon",
    "hawking-radiation",
    "membrane-paradigm",
  ],
  uses: [
    "def:jet-horizon",
    "rem:hawking-radiation",
  ],
  cites: ["susskind1993", "susskindthorlacius1994"],
});
