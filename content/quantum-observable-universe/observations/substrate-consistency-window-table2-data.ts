import { table } from "../../schema/builders";
export default table({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Corrected (row 2).** The row read “EM/strong ratio | " +
        "$\\tanh(\\ln q)$”. Two problems, both downstream of the " +
        "`def:coulomb-charge` decomposition correction: (1) $\\tanh(\\ln q)$ is " +
        "the ratio of the two *per-crossing* weights, whereas the channel " +
        "*totals* carry the multiplicity factor $(p + m)/(p - m)$, so the bare " +
        "constant as a channel ratio holds only at $m = 0$; (2) naming the " +
        "channels “EM” and “strong” asserts the " +
        "identification withdrawn upstream (the bar-odd coefficient is a " +
        "sign-blind crossing count; $Q$ scales the bar-even channel). Relabelled " +
        "to the per-crossing bar-odd/bar-even weight ratio, which is what the " +
        "formula and the $0.104$ value actually are. The numerical value is " +
        "unchanged.",
      see: "docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md",
    },
  ],
  label: "tbl:substrate-consistency-window-table2-data",
  title: "Table 2 from prop:substrate-consistency-window",
  uses: ["prop:substrate-consistency-window"],
  tags: ["extracted-table"],
});
