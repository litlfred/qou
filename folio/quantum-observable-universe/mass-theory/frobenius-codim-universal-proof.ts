import { proof } from "../../schema/builders";

export default proof({
  label: "prf:frobenius-codim-universal",
  title: "Proof of frobenius codim universal",
  uses: ["thm:frobenius-codim-universal"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational table: phase5-n8-dim-q-table.json.",
    },
  ],
});
