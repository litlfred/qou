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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The full witness data is recorded in `tau-leptonic-decay.witness.json`." },
  ],
});
