import { proof } from "../../schema/builders";

export default proof({
  label: "prf:toffoli-lp-stability",
  title: "Proof of toffoli lp stability",
  uses: ["prop:toffoli-lp-stability"],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "This proof used to close with \"all amplitudes of the correct sign\", and located the sign reversal at q_Φ ≈ 0.466 with the claim that the gate fails CCNOT semantics on (q_Φ, 1). Both were withdrawn along with Φ.",
    },
    {
      kind: "status",
      date: "2026-08-30",
      body: "Sign-reduction second half (from P_{7,6}) and shadow-price finiteness step remain open (convention-D Markov-Gram form is singular on the full NF span). Legacy toffoli-lp-stability.witness.json reflects the pre-2026-08-30 convention-C producer with naive length trace rule.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/toffoli-lp-stability.witness.json",
      "computations/molecular-frobenius-lp.witness.json",
      "computations/probes/toffoli-qand-convention-d-derivation.witness.json",
    ],
    status: "verified",
  },
});
