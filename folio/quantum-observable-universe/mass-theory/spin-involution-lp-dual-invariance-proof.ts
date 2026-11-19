import { proof } from "../../schema/builders";

export default proof({
  label: "prf:spin-involution-lp-dual-invariance",
  title: "Proof of spin involution lp dual invariance",
  uses: ["prop:spin-involution-lp-dual-invariance"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: computations/alpha/alpha-5-lp-dual-crystal.witness.json, canonical evaluation-phiq-pair-knot-markov-trace.witness.json.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/alpha/alpha_5_lp_dual_crystal.py",
    witness: [
      "computations/alpha/alpha-5-lp-dual-crystal.witness.json",
      "computations/h2-molecular-binding.witness.json",
    ],
    status: "verified",
  },
});
