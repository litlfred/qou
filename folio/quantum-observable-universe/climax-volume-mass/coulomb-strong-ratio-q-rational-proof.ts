import { proof } from "../../schema/builders";

export default proof({
  label: "prf:coulomb-strong-ratio-q-rational",
  title: "Proof of coulomb strong ratio q rational",
  uses: ["prop:coulomb-strong-ratio-q-rational"],
  authorNotes: [
    {
      kind: "note",
      body: "Lean formalisation in coulomb-strong-ratio-q-rational.lean: qDiffOverSum_eq_qSqDiff_over_qSqSum (closed by field_simp; ring) and Real.tanh_log_eq_qDiffOverSum (via Real.exp_log, Real.sinh, Real.cosh, Real.tanh in Mathlib), compliant with lusztig_q_0_imaginary_part_zero.",
    },
  ],
});
