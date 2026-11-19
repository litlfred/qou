import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-radius-of-convergence-gate-evidence",
  title:
    "Evidence for the $\\mathfrak{Q}_\\beta$ radius-of-convergence conjecture from the $c_2, \\ldots, c_{10}$ window",
  interprets: "conj:q-beta-radius-of-convergence-gate",
  uses: [
    "conj:q-beta-radius-of-convergence-gate",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: qbeta-decay-sdp-extended-ck.witness.json.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/qbeta_decay_sdp_extended_ck.py",
    witness: [
      "computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json",
      "computations/qbeta/qbeta-radius-of-convergence-gate-probe.witness.json",
    ],
    status: "verified",
  },
});
