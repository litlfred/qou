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
  ],
});
