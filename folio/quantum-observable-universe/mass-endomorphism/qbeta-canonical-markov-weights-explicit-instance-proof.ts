import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qbeta-canonical-markov-weights-explicit-instance",
  title: "Proof of qbeta canonical markov weights explicit instance",
  uses: ["prop:qbeta-canonical-markov-weights-explicit-instance"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-03",
      body: "The first bullet of \"It does not establish\" read *\"Identifying the canonical inhabitant remains open\"* until 2026-09-03, when `canonicalInstance` and its derivation from `HeckeMarkov3` landed. The Ocneanu-family and hook-content Lean results it relies on were prior art from PRs #5242 and #5575 and were credited late.",
    },
  ],
});
