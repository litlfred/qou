import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mass-tower-coefficient-stratification",
  title: "Proof of mass tower coefficient stratification",
  uses: ["prop:mass-tower-coefficient-stratification"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: wedderburn-strata-witness.json.",
    },
  ],
});
