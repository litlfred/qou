import { remark } from "../../schema/builders";

export default remark({
  label: "rem:jet-tower-convergence-context",
  title: "Boundedness hypothesis, engineering consequence, and confinement-SDP relation for jet-tower convergence",
  interprets: "prop:jet-tower-convergence",
  tags: ["jet-tower", "convergence", "confinement-sdp", "brane-tower"],
  uses: ["prop:jet-tower-convergence"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: computations/jet-tower-delta-max.witness.json, sdp-lift-audit.witness.json.",
    },
  ],
});
