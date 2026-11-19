import { proof } from "../../schema/builders";

export default proof({
  label: "prf:plancherel-term-7-formulation",
  title: "Proof of plancherel term 7 formulation",
  uses: ["prop:plancherel-term-7-formulation"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: coulomb-subtracted-binding.witness.json.",
    },
    {
      kind: "refined-framing",
      body: "Earlier drafts and the legacy formalism called w_λ(q) = dim_q²/[n]_q! the q-Plancherel weight and claimed Σ_λ w_λ(q) = 1.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/two_term_qed_isotope_and_nucleon_compute.py",
    witness: "computations/two-term-qed-isotope-and-nucleon-compute.witness.json",
    status: "verified",
  },
});
