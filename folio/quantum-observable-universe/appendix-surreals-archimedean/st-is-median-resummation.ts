import { remark } from "../../schema/builders";

export default remark({
  label: "rem:st-is-median-resummation",
  title:
    "The standard-part map acts as Écalle median resummation on transseries values",
  interprets: "def:ecalle-borel-resummation",
  tags: [
    "surreal-numbers",
    "standard-part",
    "median-resummation",
    "resurgence",
    "transseries",
    "archimedean",
  ],
  uses: [
    "def:standard-part-functor",
    "def:ecalle-borel-resummation",
    "conj:kashaev-surreal",
  ],
  cites: ["crew2023", "ecalle1981", "berarducci-mantova2018", "mcspirit-rolen2025"],
});
