import { table } from "../../schema/builders";

export default table({
  label: "tbl:hadron-level-knot-table-data",
  title: "Hadron-level knot decomposition: nucleons + 14 atoms",
  caption:
    "Per-atom Markov trace $\\mathrm{tr}_M$, net coefficient, binding " +
    "energy $B$ (MeV), and Frobenius-positivity check for the proton + " +
    "neutron + 13 representative atoms through ${}^{56}$Fe. All 19 atoms " +
    "pass the Frobenius positivity check $G \\cdot \\vec{c} \\geq 0$.",
  uses: ["rem:hadron-level-knot-table"],
  tags: ["hecke", "normal-form", "hadron", "knot-table", "appendix"],
});
