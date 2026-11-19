import { proof } from "../../schema/builders";

export default proof({
  label: "prf:neutron-proton-mass-splitting",
  title: "Proof of neutron proton mass splitting",
  uses: ["prop:neutron-proton-mass-splitting"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-25",
      body: "The witness formerly cited, atom-mass-complete-wedderburn.witness.json, is absent from computations/: added 2026-04-10 in commit 1359fe23ac under folio-assistant/computations/, it left the tree in the miga migration. It is an atomic-mass witness with no quark Φ values, so it is the wrong artifact for this block. Re-derivation: computations/pn_splitting_proof_provenance_probe.py. All-pairs producer: computations/level1-qvalues.py; hadronic-scale comparison audited in docs/audits/2026-11-15-np-splitting-error-budget.md §18.",
    },
  ],
});
