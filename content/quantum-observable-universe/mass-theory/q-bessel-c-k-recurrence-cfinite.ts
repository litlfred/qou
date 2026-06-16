import { proof } from "../../schema/builders";

export default proof({
  label: "proof:q-bessel-c-k-recurrence-cfinite",
  of: "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  lean: {
    ref: "qou:QOU.QBeta.qbessel_coeff_closed_form",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/qbeta/qbeta_qbessel_contiguity_cfinite.py",
    witness: "computations/qbeta/qbeta-qbessel-contiguity-cfinite.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      body: "Wires up the Lean proof of the first-order c_k recursion to the compute that checks its q-holonomic structure against the #1839 canonical values."
    }
  ]
});
