import { table } from "../../schema/builders";

export default table({
  label: "tbl:tower-binding-energy-table-data",
  title:
    "Predicted vs observed binding energies (Z = 1 to 20) from the 3-channel brane tower",
  caption:
    "Tower-binding-energy formula predictions $B_{\\mathrm{pred}}$ vs " +
    "observed $B_{\\mathrm{obs}}$ for representative isotopes from " +
    "hydrogen through calcium, at $q_0 \\approx 1.110$. Zero fitted " +
    "parameters; mean mass error 0.071\\% across $Z = 1$ to $Z = 20$.",
  uses: ["prop:tower-binding-energy"],
  tags: [
    "binding-energy",
    "brane-tower",
    "predictions-table",
    "zero-fitting",
  ],
});
