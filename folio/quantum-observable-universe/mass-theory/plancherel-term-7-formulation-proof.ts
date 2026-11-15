import { proof } from "../../schema/builders";

export default proof({
  label: "prf:plancherel-term-7-formulation",
  title: "Proof of plancherel term 7 formulation",
  uses: ["prop:plancherel-term-7-formulation"],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "Earlier drafts and the legacy formalism called w_λ(q) = dim_q²/[n]_q! the q-Plancherel weight and claimed Σ_λ w_λ(q) = 1.",
    },
  ],
});
