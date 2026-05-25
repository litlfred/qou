import { definition } from "../../schema/builders";

/**
 * Universal ILP algorithm for operator selection at every level.
 *
 * The same algorithm derives confinement (B₃), gluon (2σ₀),
 * electron attachment (σ₁⁻¹), and molecular bonding (inv trefoil).
 */
export default definition({
  label: "def:universal-ilp-algorithm",
  title: "Universal ILP algorithm for operator selection",
  lean: { ref: "qou:QOU.Interactions.universal_ilp",
    validation: "not_checked",
  },
  uses: [
    "conj:q-integer-mass-formula",
    "def:molecular-braid",
  ],
  tags: [
    "ILP",
    "operator-selection",
    "confinement",
    "gluon",
    "covalent-bond",
    "universal",
    "algorithm",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/universal-ilp.py",
    witness: "folio-assistant/computations/universal-ilp.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**Phase 1a — Option E (PR following #1252).** Gram-matrix stub " +
        "`gram_matrix _ ≡ 0` replaced with typeclass-driven version " +
        "`HasH3GramMatrix R q` consuming the empirical 6×6 Hoefsmit-" +
        "seminormal Gram from `gram-matrix-dual.witness.json`. Three " +
        "structural theorems discharged (`gram_matrix_symmetric`, " +
        "`gram_matrix_invertible`, `gram_matrix_nonzero`); " +
        "`frobenius_positive` is now a non-vacuous constraint " +
        "(prior stub was vacuously `0 · x = 0 ≥ 0`). Concrete " +
        "ℝ-valued instance at q_0 deferred to Phase 1b (rational " +
        "encoding of 36 decimal entries). See " +
        "`docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md` " +
        "for the full Phase 0/1/2/3/4 workplan.",
    },
  ],
});
