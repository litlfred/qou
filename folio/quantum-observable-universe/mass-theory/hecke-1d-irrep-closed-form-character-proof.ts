import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hecke-1d-irrep-closed-form-character",
  title: "Proof of hecke 1d irrep closed form character",
  uses: ["prop:hecke-1d-irrep-closed-form-character"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/q-beta-1d-irrep-universal-closed-form.witness.json.",
    },
  ],
});
