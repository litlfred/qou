import { proof } from "../../schema/builders";

export default proof({
  label: "prf:unit-modulus-eigenvalue",
  title: "Proof of unit modulus eigenvalue",
  uses: ["prop:unit-modulus-eigenvalue"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): displayed formula. Both facts are proved in the Lean sibling\n. $\\square$" },
  ],
});
