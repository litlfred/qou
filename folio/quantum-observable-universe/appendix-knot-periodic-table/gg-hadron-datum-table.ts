import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gg-hadron-datum-table",
  title:
    "Proper $\\gamma\\gamma$ photonic, single-hadron, and light-nuclei ($A = 1\\ldots 4$) datum atlas",
  uses: [
    "def:hecke-normal-form",
    "def:photon",
    "prop:borromean-two-photon-factorisation",
    "rem:knot-particle-dictionary",
    "rem:particle-nf-table",
  ],
  interprets: "prop:borromean-two-photon-factorisation",
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
    "normal-form",
    "gamma-gamma",
    "hadrons",
    "binding-energy",
    "appendix",
  ],
});
