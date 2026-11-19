import { proof } from "../../schema/builders";

export default proof({
  label: "prf:cyclotomic-depth3-dimension-synthesis",
  title: "Proof of cyclotomic depth3 dimension synthesis",
  uses: ["prop:cyclotomic-depth3-dimension-synthesis"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/cyclotomic-depth3-dimension-pslq.witness.json.",
    },
  ],
});
