import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jonquiere-cyclotomic-tate-rationality",
  title: "Proof of jonquiere cyclotomic tate rationality",
  uses: ["prop:jonquiere-cyclotomic-tate-rationality"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/jonquiere-cyclotomic-general.witness.json.",
    },
  ],
});
