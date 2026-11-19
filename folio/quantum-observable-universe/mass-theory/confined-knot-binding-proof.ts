import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confined-knot-binding",
  title: "Proof of confined knot binding",
  uses: ["prop:confined-knot-binding"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: confined-knot-binding.witness.json.",
    },
  ],
});
