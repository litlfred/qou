import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:qbeta-c-k-closed-forms",
  label: "rem:qbeta-c-k-closed-forms-derivation",
  title: "Open derivation paths, precision leverage, and SDP evidence for the $c_k$",
  tags: ["qbeta", "precision-ladder", "ck-coefficients", "sdp", "derivation-chain"],
  uses: ["conj:qbeta-c-k-closed-forms"],
  authorNotes: [
    {
      kind: "note",
      body: "Inadmissibility of $z = 1$ under convention D is formalized in `ConventionDAdmissibleRoots.lean`; the empirical $c_k$ sweep originates from `binding_q_target_sweep`.",
    },
  ],
});
