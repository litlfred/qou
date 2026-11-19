import { proof } from "../../schema/builders";

export default proof({
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-30",
      body: "Withdrew identification of the core difference Delta_{02}(q) with Phi(q); under canonical convention D the derived flip amplitude is P_{7,6}(q) = -(q-1)(q+1)(q^6+q^4+2q^2+1)/(2q(q^2+1)^2).",
    },
  ],
  label: "prf:toffoli-transfer-matrix",
  title: "Proof of toffoli transfer matrix",
  uses: ["prop:toffoli-transfer-matrix"],
});
