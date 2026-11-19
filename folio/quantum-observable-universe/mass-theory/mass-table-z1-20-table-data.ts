import { table } from "../../schema/builders";
export default table({
  label: "tbl:mass-table-z1-20-table-data",
  title: "Wedderburn three-invariant atomic mass predictions $\\mathfrak{m}_{\\mathrm{pred}}$ against AME values for $Z = 1$ to $20$",
  uses: ["rem:mass-table-z1-20"],
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/wedderburn_mass_table_convention_d.py",
    witness: [
      "computations/wedderburn-mass-table-convention-d.witness.json",
    ],
  },
  tags: ["extracted-table"],
});
