import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braid-link-types",
  title:
    "Concrete braid and link types: 2-strand Markov closure ($\\widehat{\\sigma^2} = \\text{Hopf link}$) and the $\\sigma^2 \\to \\text{Hopf} \\to -2$ chain",
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
    {
      kind: "status",
      body: "Lean stub: **no `sorry`s**. The 2-strand case is fully closed.\nThe n-strand generalisation is enumerated as concrete combinatorial\ntheorems to be added in follow-up files.",
    },
  ],
});
