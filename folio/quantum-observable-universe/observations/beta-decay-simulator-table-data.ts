import { table } from "../../schema/builders";

export default table({
  label: "tbl:beta-decay-simulator-table-data",
  title: "Verification nuclei: $Q$-values and observed half-lives",
  caption:
    "Six reference nuclei used by the beta-decay half-life simulator: " +
    "${}^{3}\\mathrm{H}$, ${}^{14}\\mathrm{C}$, ${}^{60}\\mathrm{Co}$, " +
    "${}^{90}\\mathrm{Sr}$, ${}^{137}\\mathrm{Cs}$, ${}^{210}\\mathrm{Bi}$. " +
    "Experimental $Q$-values and observed half-lives from ENSDF.",
  uses: ["sim:beta-decay-halflife"],
  tags: ["beta-decay", "half-life", "verification-nuclei", "ensdf"],
});
