import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-beta-spectral-bridge",
  title: "Proof of q beta spectral bridge",
  uses: ["prop:q-beta-spectral-bridge"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): No `sorry` exists in the companion Lean for the `Real.log` steps; the Lean section's sentence about deferring them is out of date." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): We verified this proposition numerically at 50 decimal places via [`q_beta_spectral_bridge_witness.py`](https://github.com/litlfred/qou/blob/main/computations/q_beta_spectral_bridge_witness.py) ([`q-beta-spectral-bridge.witness.json`](https://github.com/litlfred/qou/blob/main/computations/q-beta-spectral-bridge.witness.json))." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean formalization\n\nThe companion Lean repository records the bridge identities (`polynomial_bridge_identity`, `leading_order_ratio_identity`, `bridge_first_order_remainder`). We defer the `Real.log` steps via `sorry` (`-- Ref: [leitner2026]`)." },
  ],
});
