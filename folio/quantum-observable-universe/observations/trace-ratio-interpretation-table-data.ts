import { table } from "../../schema/builders";

export default table({
  label: "tbl:trace-ratio-interpretation-table-data",
  title: "Trace ratio per affected generator: six verification nuclei",
  caption:
    "Computational results for the trace ratio " +
    "$\\hat{V}^{\\mathrm{par}} / \\hat{V}^{\\mathrm{dau}}$ across the " +
    "six verification nuclei (${}^{3}\\mathrm{H}$, " +
    "${}^{14}\\mathrm{C}$, ${}^{60}\\mathrm{Co}$, ${}^{90}\\mathrm{Sr}$, " +
    "${}^{137}\\mathrm{Cs}$, ${}^{210}\\mathrm{Bi}$), showing the squared " +
    "topological matrix element $|\\mathcal{M}_q|^2$ spans 10 orders " +
    "of magnitude.",
  uses: ["rem:trace-ratio-interpretation"],
  tags: ["markov-trace", "half-life", "verification-nuclei"],
});
