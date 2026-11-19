import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-beta-spectral-bridge",
  title: "Proof of q beta spectral bridge",
  uses: ["prop:q-beta-spectral-bridge"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalisation note: the companion Lean module records the algebraic bridge identities (`polynomial_bridge_identity`, `leading_order_ratio_identity`, `bridge_first_order_remainder`) with no `sorry`; an older note about deferring `Real.log` steps via `sorry` (`-- Ref: [leitner2026]`) was superseded. Numerical witness moved from prose: `computations/q_beta_spectral_bridge_witness.py` (`computations/q-beta-spectral-bridge.witness.json`, 50 dps).",
    },
  ],
});
