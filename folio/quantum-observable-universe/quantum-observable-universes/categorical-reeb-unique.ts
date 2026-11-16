import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "The Lean link previously pointed at `CategoricalReeb.unique`, a wrapper around an axiom that was false: " +
        "the structure leaves `d` and `ι_ξ` free, so in `Type` any ξ on Bool satisfies every field with the same A, " +
        "forms and π_V. Axiom and wrapper removed; the link points at the refutation. The prose argument pins ξ " +
        "through the torus action, which the Lean structure does not record; open in Lean, bean qou-n2un.",
    },
  ],
  label: "prop:categorical-reeb-unique",
  title: "Uniqueness of the categorical Reeb derivation",
  lean: { ref: "qou:QOU.CategoricalReeb.not_unique_unconstrained",
    validation: "not_checked",
  },
  uses: ["thm:categorical-reeb-exists"],
  proofs: ["prf:categorical-reeb-unique"],
  tags: ["uniqueness", "reeb", "derivation"],
});
