import { proof } from "../../schema/builders";

export default proof({
  label: "prf:physical-units-gap-linear",
  title: "Proof of physical units gap linear",
  uses: ["prop:physical-units-gap-linear"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/q1-mass-gap-probe.witness.json.",
    },
  ],
});
