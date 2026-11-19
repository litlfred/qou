import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jucys-murphy-central-elements-qou",
  title: "Proof of jucys murphy central elements qou",
  uses: ["prop:jucys-murphy-central-elements-qou"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/alpha/alpha-5-jucys-murphy-central.witness.json.",
    },
  ],
});
