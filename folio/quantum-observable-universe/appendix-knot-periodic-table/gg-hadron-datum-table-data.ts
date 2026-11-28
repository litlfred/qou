import { table } from "../../schema/builders";

export default table({
  label: "tbl:gg-hadron-datum-table-data",
  title:
    "Table K.2: Proper $\\gamma\\gamma$ photonic, single-hadron ($A = 1$), light-nuclei ($A = 2\\ldots 4$), and exploratory multi-strand datum tables (80-digit proton-anchored evaluation)",
  uses: ["rem:gg-hadron-datum-table"],
  cites: ["codata2022", "ame2020"],
  computation: {
    engine: "mpmath",
    script: "computations/gg_hadron_datum_table.py",
    witness: "computations/gg-hadron-datum-table.witness.json",
    status: "verified",
  },
  tags: [
    "archimedean-bridge",
    "hecke",
    "gamma-gamma",
    "hadrons",
    "nuclides",
    "extracted-table",
  ],
});
