import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-trace-operator-construction",
  interprets: "rem:markov-trace-inductive-limit",
  title:
    "Markov-trace operator construction",
  uses: [
    "rem:markov-trace-inductive-limit",
    "rem:hecke-algebra-type-scaffold",
  ],
  cites: [
    "jones1985",
    "wenzl1988",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "markov-trace-operator",
    "von-neumann-factor",
    "inductive-limit",
    "audit-forward-reference",
  ],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "status",
      date: "2026-06-03",
      body: "**Primary content moved to [`docs/audits/2026-06-03-wip-scaffolding-markov-trace-operator-construction.md`](../../../docs/audits/2026-06-03-wip-scaffolding-markov-trace-operator-construction.md).** Per AGENTS.md canonical-no-negative-result-in-paper discipline + the refined WIP-scaffolding checker (PR #1766): the `[scaffolding, open-rd-item-4]` tag pair signals in-flight R&D content; primary material now lives in the audit doc. The Lean class scaffolding stays in place — downstream Lean files import the classes as hypotheses.",
      see: "https://github.com/litlfred/qou/pull/1767",
    },
    {
      kind: "note",
      date: "2026-06-03",
      body: "Item 4 of the post-PR-#665 open R&D inventory. The class fields (`HnHilbertRep n q`, `HnInductiveEmbedding n q`, `MarkovTraceVNFactor q`) follow the explicit-residual pattern; the GNS state and bicommutant closure of the inductive-limit algebra remain the substantive open R&D, with per-$n$ discharge status recorded in the audit doc. This block is retained as an interpretive forward-reference; it makes no logical claim.",
    },
  ],
});
