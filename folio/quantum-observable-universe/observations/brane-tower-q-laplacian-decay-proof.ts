import { proof } from "../../schema/builders";

export default proof({
  label: "prf:brane-tower-q-laplacian-decay",
  title: "Proof of the brane-tower convergence bound",
  uses: ["prop:brane-tower-q-laplacian-decay", "prop:delta-max-uniform-bound"],
  authorNotes: [
    {
      kind: "status",
      body: "Bounded-power step lambda_1 <= 1 proved in Lean as `QOU.QBeta.lam_le_one_of_pow_bounded`.",
    },
  ],
});
