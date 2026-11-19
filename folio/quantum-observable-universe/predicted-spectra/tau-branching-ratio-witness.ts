import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:tau-leptonic-universality",
  label: "rem:tau-branching-ratio-witness",
  title:
    "Numerical witness: $\\mathrm{BR}(\\tau \\to e) / \\mathrm{BR}(\\tau \\to \\mu) \\approx 1.028$",
  tags: [
    "tau-decay",
    "branching-ratio",
    "witness",
    "computation",
    "lepton-universality",
    "PDG",
  ],
  uses: ["prop:tau-leptonic-universality"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Witness moved from prose: `tau-leptonic-decay.witness.json`.",
    },
  ],
});
