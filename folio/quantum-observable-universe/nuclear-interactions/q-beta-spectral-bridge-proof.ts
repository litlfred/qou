import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-beta-spectral-bridge",
  title: "Proof of q beta spectral bridge",
  uses: ["prop:q-beta-spectral-bridge"],
  authorNotes: [
    {
      kind: "status",
      body: "Form A retired as canonical base under owner ruling 2026-09-08 in favour of Convention-D Markov trace z_D = q^3/(q^2+1); the -0.052 next-order figure quoted prior to 2026-10-10 was the Convention-C value.",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalisation note: the companion Lean module records the algebraic bridge identities (`polynomial_bridge_identity`, `leading_order_ratio_identity`, `bridge_first_order_remainder`) with no `sorry`; an older note about deferring `Real.log` steps via `sorry` (`-- Ref: [leitner2026]`) was superseded. Numerical witness moved from prose: `computations/q_beta_spectral_bridge_witness.py` (`computations/q-beta-spectral-bridge.witness.json`, 50 dps).",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/q_beta_spectral_bridge_witness.py",
    witness: [
      "computations/q-beta-spectral-bridge.witness.json",
      "computations/probes/gpmt-sign-block-qbeta-and-np-splitting.witness.json",
    ],
    status: "verified",
  },
});
