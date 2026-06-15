import { proof } from "../../schema/builders";

export default proof({
  label: "proof:q-bessel-second-order-qdifference",
  of: "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  lean: {
    ref: "qou:QOU.QBeta.qbessel_second_order_recurrence",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "folio-assistant/computations/qbeta/qbessel_second_order_qdifference_equation.py",
    witness: "folio-assistant/computations/qbeta/qbessel-second-order-qdifference-equation.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      body: "Wires up the Lean proof of the second-order q-difference equation for the q-Bessel function to its computation and limits."
    }
  ]
});
