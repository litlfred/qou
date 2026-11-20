import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jackson-q-bessel-contiguity",
  of: "prop:jackson-q-bessel-contiguity-recurrence",
  lean: {
    ref: "qou:QOU.QBeta.qbessel_first_kind_coeff_closed_form",
    validation: "validated",
  },
  computation: {
    engine: "sympy",
    script: "computations/qbeta/qbessel_jackson_contiguity.py",
    witness: "computations/qbeta/qbessel-jackson-contiguity.witness.json",
    status: "verified",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The closed forms are proved in `QBesselContiguityRecurrence.lean`. Computations verify" },
    {
      kind: "status",
      body: "Wires the Lean proofs of the first- and second-kind Jackson q-Bessel (SU_q(1,1)) coefficient contiguity recurrences (qbessel_first_kind_coeff_closed_form, qbessel_second_kind_coeff_closed_form) to a computation: the closed-form ratios equal the actual Jackson coefficient ratios (symbolic, all k≤6, plus 60 dps), and the q-hypergeometric product solution reproduces the coefficients. Partners of the already-wired third-kind second-order q-difference equation. Fibre-level (formal q) skeleton; no binding/Q_β scale claimed; c_k stay cal-anchored."
    }
  ]
});
