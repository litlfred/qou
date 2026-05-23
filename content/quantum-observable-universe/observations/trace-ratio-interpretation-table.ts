import { table } from "../../schema/builders";

export default table({
  label: "tbl:trace-ratio-interpretation-data",
  title: "Trace ratio per affected generator: six verification nuclei",
  caption:
    "Computational results for the trace ratio " +
    "$\\hat{V}^{\\mathrm{par}} / \\hat{V}^{\\mathrm{dau}}$ across the " +
    "six verification nuclei (${}^3$H, ${}^{14}$C, ${}^{60}$Co, " +
    "${}^{90}$Sr, ${}^{137}$Cs, ${}^{210}$Bi), showing the squared " +
    "topological matrix element $|\\mathcal{M}_q|^2$ spans 10 orders " +
    "of magnitude.",
  uses: ["rem:trace-ratio-interpretation"],
  tags: ["markov-trace", "half-life", "verification-nuclei"],
});
