import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-exponential-taylor",
  title: "Proof of q exponential taylor",
  uses: ["prop:q-exponential-taylor"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The $q$-heat kernel and its Gaussian core ([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)) are therefore well-defined at the physical value of $q$, avoiding any $|q| \\le 1$ restriction." },
  ],
});
