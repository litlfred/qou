import { proof } from "../../schema/builders";

export default proof({
  label: "prf:wigner-np-pairing",
  title: "Proof of wigner np pairing",
  uses: ["prop:wigner-np-pairing"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: jet-knot-invariants.witness.json.",
    },
  ],
});
