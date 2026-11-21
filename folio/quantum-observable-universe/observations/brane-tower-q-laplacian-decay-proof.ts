import { proof } from "../../schema/builders";

export default proof({
  label: "prf:brane-tower-q-laplacian-decay",
  title: "Proof of the brane-tower convergence bound",
  uses: ["prop:brane-tower-q-laplacian-decay", "prop:delta-max-uniform-bound"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): A bounded sequence of powers has $\\lambda_1 \\leq 1$ (Lean `QOU.QBeta.lam_le_one_of_pow_bounded`)." },
  ],
});
