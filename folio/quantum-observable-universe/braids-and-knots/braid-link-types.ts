import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braid-link-types",
  title:
    "Concrete Lean braid and link types: the 2-strand case discharges the Markov-closure axiom of `rem:markov-closure-map-axiomatic` ($\\widehat{\\sigma^2} = $ Hopf link), and composes to a fully Lean-proved chain $\\sigma^2 \\to $ Hopf $\\to -2$",
  interprets: "rem:markov-closure-map-axiomatic",
  uses: ["rem:markov-closure-map-axiomatic"],
  cites: ["jones1985"],
  tags: [
    "lean-infrastructure",
    "track-C-step-A",
    "braid-group",
    "link-type",
    "markov-closure",
    "hopf-link-explicit",
    "class-discharge",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The infrastructure provides explicit Lean types for generic braids and links." },
    {
      kind: "status",
      body: "Lean stub: **no `sorry`s**. The 2-strand case is fully closed.\nThe n-strand generalisation is enumerated as concrete combinatorial\ntheorems to be added in follow-up files.",
    },
  ],
});
