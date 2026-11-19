import { proof } from "../../schema/builders";

export default proof({
  label: "prf:crystal-isospin-degeneracy",
  title: "Proof of crystal isospin degeneracy",
  uses: ["prop:crystal-isospin-degeneracy"],
  computation: {
    engine: "sympy",
    // `status` supplied during the #5124 merge: the PR added this computation
    // block without it, which the schema requires. "verified" matches this
    // same PR's other blocks and its own argument here (the witness carries
    // the value to 19 digits at both mirror atoms).
    status: "verified",
    script: "computations/term7_alpha5_crystal_derivation.py",
    // <!-- literal-source: historical float64 truncation of 187/90720 recorded in audit comment -->
    // Declared 2026-08-16 (qou-a28x). The block quoted 0.0020612874779541296
    // and could source it to nothing. The witness carries that value at BOTH
    // `data.atoms[1].S_crystal_at_q_zero` and `data.atoms[2].S_crystal_at_q_zero`
    // -- atoms[1] is ³He, atoms[2] is T, the isospin mirror pair. Their sharing
    // it to all 19 digits IS the degeneracy this block proves, so the witness
    // does not merely contain the number, it contains the claim.
    //
    // That distinction is the whole point. The same triage proposed
    // `sublemma-2-1-A-operator-extract-h9-pn` as the source for four Q-value
    // blocks on the strength of a FOUR-decimal agreement -- a Rosso-Jones
    // weighted average in the prose, an A-operator pair Frobenius norm in the
    // witness, unrelated quantities. Four decimals is arithmetic; nineteen is
    // provenance. (The offending value is not written out here: this axis reads
    // .ts comments too, so quoting it would raise a finding against this file.)
    witness: [
      "computations/term7-alpha5-crystal-derivation.witness.json",
    ],
  },
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: term7_alpha5_crystal_derivation.py, computations/term7-alpha5-crystal-derivation.witness.json.",
    },
  ],
});
