import { remark } from "../../schema/builders";

export default remark({
  label: "rem:jet-tower-convergence-context",
  title: "Boundedness hypothesis, engineering consequence, and confinement-SDP relation for jet-tower convergence",
  interprets: "prop:jet-tower-convergence",
  tags: ["jet-tower", "convergence", "confinement-sdp", "brane-tower"],
  uses: ["prop:jet-tower-convergence"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (cf. `sdp-lift-audit.witness.json`: every real Hecke word has $x^T G x \\ge 0$)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the `uniform_bound_pass` flag in [`jet-tower-delta-max.witness.json`](../../../computations/jet-tower-delta-max.witness.json) is **true** for D, T, ${}^{3}$He" },
  ],
});
