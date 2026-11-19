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
    {
      kind: "note",
      body: "Computational witness: computations/q1-mass-gap-probe.witness.json.",
    },
  ],
});
