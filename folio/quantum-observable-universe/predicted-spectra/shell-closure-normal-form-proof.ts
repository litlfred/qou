import { proof } from "../../schema/builders";

export default proof({
  label: "prf:shell-closure-normal-form",
  title: "Proof of shell closure normal form",
  uses: ["prop:shell-closure-normal-form"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formal Lean proof of the optimal normal form reduction: `OptimalNF.lean`.",
    },
  ],
});
