import { proof } from "../../schema/builders";

export default proof({
  label: "prf:cyclotomic-orbit-sum-all-depths",
  title: "Proof of cyclotomic orbit sum all depths",
  uses: ["prop:cyclotomic-orbit-sum-all-depths"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/jonquiere-cyclotomic-general.witness.json.",
    },
  ],
});
