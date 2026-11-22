import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:surreal-limit-transfer",
  title:
    "Surreal limit transfer: limits as standard-part equalities via an $\\omega$-evaluation",
  lean: {
    ref: "qou:QOU.AppendixSurreals.SurrealLimitTransfer",
    validation: "not_checked",
  },
  tags: [
    "surreal-numbers",
    "standard-part",
    "nonstandard-analysis",
    "limits",
    "inequality-to-equality",
    "archimedean",
  ],
  uses: [
    "def:standard-part-functor",
    "rem:st-is-median-resummation",
  ],
  cites: ["robinson1966", "berarducci-mantova2018"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Original wording: \"derived, fully proved, from the class fields in the Lean sibling\"; \"The conjecture is carried as a content-bearing Lean `class` with **no instance** — the honest open state.\"; \"the axiomatised `SurrealField` interface alone\"." },
  ],
});
