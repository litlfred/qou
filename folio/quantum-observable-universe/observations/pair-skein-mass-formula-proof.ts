import { proof } from "../../schema/builders";

export default proof({
  label: "prf:pair-skein-mass-formula",
  title: "Proof of the pair Skein mass formula",
  uses: ["lem:pair-skein-mass-formula"],
  authorNotes: [
    {
      kind: "note",
      body: "The convention-C denominator q^{1/2} + q^{-1/2} is named skeinNormaliserC in the sibling Lean module.",
    },
  ],
});
