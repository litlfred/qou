import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:qbeta-c-k-closed-forms",
  label: "rem:qbeta-c-k-closed-forms-derivation",
  title: "Open derivation paths, precision leverage, and SDP evidence for the $c_k$",
  tags: ["qbeta", "precision-ladder", "ck-coefficients", "sdp", "derivation-chain"],
  uses: ["conj:qbeta-c-k-closed-forms"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The empirical $c_k$ from `binding_q_target_sweep` are **fits**" },
  ],
});
