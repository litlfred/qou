import { table } from "../../schema/builders";
export default table({
  label: "tbl:substrate-consistency-window-table1-data",
  title: "Independent determinations of the aether parameter $q$ from lepton, electromagnetic, and weak observables",
  uses: ["prop:substrate-consistency-window"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      body: "40-dps inversion and uncertainty-to-shift ratio 1.82e5 (five orders of magnitude, correcting an earlier six-orders statement) reproduced in substrate_consistency_window_q_from_alpha_em_probe.py.",
    },
  ],
});
