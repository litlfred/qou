import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-self-duality",
  lean: { ref: "qou:QOU.categorical_self_duality",
    validation: "not_checked",
  },
  title: "Categorical self-duality",
  tags: ["self-duality", "yang-mills"],
  uses: ["def:categorical-instanton"],
  proofs: ["prf:categorical-self-duality"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-self-duality-0.svg", blockIndex: 0, hash: "c997dc218a1d" },
  ],
  authorNotes: [
    { kind: "status", date: "2026-10-11", body: "The Lean backing `QOU.categorical_self_duality` does **not** carry the Bogomolny argument: it is a structural accessor for the `self_dual` field of `CategoricalInstanton`, so it records that an object of that structure satisfies the condition the structure imposes, not that a critical point of $S[\\nabla]$ is such an object. The implication above is established in narrative here and is not formalised. (Relocated from the block prose by the paper-voice commentary audit.)" },
  ],
});
