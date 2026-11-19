import { proof } from "../../schema/builders";

export default proof({
  label: "prf:derived-mass-formula-light-isotopes",
  title: "Proof of derived mass formula light isotopes",
  uses: ["prop:derived-mass-formula-light-isotopes"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: derived-only-formula.witness.json.",
    },
    {
      kind: "note",
      body: "The canonical evaluation is recorded in derived-only-formula.witness.json, now under fsh-guts/deprecated/computations/.",
    },
  ],
});
