import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:symmetric-point-channel-collapse",
  label: "rem:symmetric-point-resolution-loss",
  title: "The symmetric point loses resolution, not spectrum",
  tags: ["symmetric-point", "degeneration", "plancherel", "stratification"],
  uses: [
    "prop:symmetric-point-channel-collapse",
    "prop:physical-units-gap-linear",
    "conj:yang-mills-mass-gap",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Numerical verification at fifty digits is recorded in `q1-mass-gap-probe.witness.json`." },
  ],
});
