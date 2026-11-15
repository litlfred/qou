import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qbeta-per-block-chi-closed-forms",
  title: "Proof of qbeta per block chi closed forms",
  uses: ["prop:qbeta-per-block-chi-closed-forms"],
  authorNotes: [
    {
      kind: "status",
      body: "All theorems are sorry-free and locally verified. The three originally deferred sorries (derivative at $q=1$, Markov-parameter symmetric form, and $z$-recursion uniqueness) were discharged during local Lean verification.",
    },
  ],
});
