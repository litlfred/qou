import { remark } from "../../schema/builders";

// Was prf:q-beta-spectral-bridge. The block it argued for is now the conjecture
// conj:q-beta-spectral-bridge (owner card, 2026-11-21: "Demote both"), so the
// argument is recorded as an interpretive sketch, not a proof (AGENTS.md §3b).
export default remark({
  label: "rem:q-beta-spectral-bridge-sketch",
  renamedFrom: ["prf:q-beta-spectral-bridge"],
  title: "Argument sketch for the Q_β spectral bridge",
  interprets: "conj:q-beta-spectral-bridge",
  uses: ["conj:q-beta-spectral-bridge", "prop:beta-decay-transfer-matrix"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): No `sorry` exists in the companion Lean for the `Real.log` steps; the Lean section's sentence about deferring them is out of date." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): We verified this proposition numerically at 50 decimal places via [`q_beta_spectral_bridge_witness.py`](https://github.com/litlfred/qou/blob/main/computations/q_beta_spectral_bridge_witness.py) ([`q-beta-spectral-bridge.witness.json`](https://github.com/litlfred/qou/blob/main/computations/q-beta-spectral-bridge.witness.json))." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean formalization\n\nThe companion Lean repository records the bridge identities (`polynomial_bridge_identity`, `leading_order_ratio_identity`, `bridge_first_order_remainder`). We defer the `Real.log` steps via `sorry` (`-- Ref: [leitner2026]`)." },
    {
      kind: "refined-framing",
      date: "2026-11-17",
      body: "Owner ruling (card D): state the one-site reading. With L_i = R_i = I the conversion telescopes T_nn -> T_mix -> T_pp, so V_pp/V_nn = 1 + zh exactly and the h^2 coefficient is -z^2/2 (sympy, z free). The two-independent-sites reading gives -z^2/4 and first-order term (z/4 - 1/2)h; at q0 the ratio is 0.9238 vs 0.9517 for the one-site reading. The corpus does not construct L_i, R_i for the free neutron, so the one-site reading is a stated model choice. Form A is the retired z = 1 cell.",
    },
  ],
});
