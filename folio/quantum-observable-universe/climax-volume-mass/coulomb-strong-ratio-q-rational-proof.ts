import { proof } from "../../schema/builders";

export default proof({
  label: "prf:coulomb-strong-ratio-q-rational",
  title: "Proof of coulomb strong ratio q rational",
  uses: ["prop:coulomb-strong-ratio-q-rational"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Proof (Lean-formalised) | Two-step in `coulomb-strong-ratio-q-rational.lean`: | Closed by `field_simp; ring` — pure-algebraic, generic-ring style. | Uses `Real.exp_log` and the definitions of `Real.sinh`, `Real.cosh`, `Real.tanh` in Mathlib. | The composite (`prop:coulomb-strong-ratio-q-rational`) | Compliant with the `lusztig_q_0_imaginary_part_zero` invariant." },
  ],
});
