import { table } from "../../schema/builders";
export default table({
  label: "tbl:substrate-consistency-window-table2-data",
  title: "Dimensionless couplings, kinematic ratios, and kaon CP-violation scale evaluated in the aether window",
  uses: ["prop:substrate-consistency-window"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      body: "The Chern-Simons Gram factor kappa remains an unproved sorry in the Lean formalization.",
    },
  ],
});
