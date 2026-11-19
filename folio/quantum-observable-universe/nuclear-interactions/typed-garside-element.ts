import { definition } from "../../schema/builders";

export default definition({
  label: "def:typed-garside-element",
  title:
    "Typed Garside element of the nuclear braid",
  tags: [
    "garside-element",
    "hecke-algebra",
    "typed-crossing",
    "nuclear",
    "braid-word",
    "normal-form",
    "staircase",
  ],
  lean: { ref: "qou:QOU.Archimedean.TypedGarsideElement",
    validation: "not_checked",
  },
  uses: [
    "def:typed-crossing-operator",
    "prop:braiding-induced-ordering",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
