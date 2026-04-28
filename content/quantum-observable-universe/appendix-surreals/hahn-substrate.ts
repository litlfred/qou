import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hahn-substrate",
  title:
    "Substrate parameter as a Hahn series in $\\varepsilon$ over $\\mathbf{No}$",
  tags: [
    "surreal-numbers",
    "substrate-parameter",
    "hahn-series",
    "graded-ring",
    "infinitesimal",
    "open-problem",
    "speculative",
  ],
  uses: [
    "def:substrate-parameter",
    "def:standard-part-functor",
  ],
  cites: [
    "ehrlich2012",
    "alling1987",
    "berarducci-mantova2018",
  ],
});
