import { table } from "../../schema/builders";
export default table({
  label: "tbl:qvalue-observation-table-data",
  title: "Predicted vs observed $\\beta^-$ $Q$-values, $q$-weighted method (convention C)",
  uses: ["rem:qvalue-observation"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-20",
      body:
        "Every row is a convention-C output of the q-weighted method in " +
        "`computations/_deprecated/qvalue-representation-theory.py`, as the referring block " +
        "`rem:qvalue-observation` already states. The `F_shell` column carries that file's " +
        "hard-coded constants (0.590 is `F_deg2 = 0.5904`), which are not computed there. The " +
        "q-weighted stage has no convention-D producer. The convention-D bare and combined " +
        "figures are in `computations/spectral-decomposition-qvalue-d.witness.json`. " +
        "The title was relabelled to say so (bean qou-wlnx).",
    },
  ],
});
