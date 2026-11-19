import { definition } from "../../schema/builders";

export default definition({
  label: "def:typed-garside-element",
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation (moved from the definition prose 2026-11-19): What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here." },
  ],
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
});
