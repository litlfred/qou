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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean classes `HnHilbertRep n q`, `HnInductiveEmbedding n q`, and `MarkovTraceVNFactor q` encode the per-$n$ representation, the inductive embedding, and the GNS bicommutant factor hosting $\\mathrm{tr}_M$. Downstream files import these classes as hypotheses. The operator-algebra steps—the GNS state and the bicommutant closure—supply the per-$n$ instances." },
    {
      kind: "status",
      date: "2026-06-03",
      body: "**Primary content moved to [`docs/audits/2026-06-03-wip-scaffolding-markov-trace-operator-construction.md`](../../../docs/audits/2026-06-03-wip-scaffolding-markov-trace-operator-construction.md).** Per AGENTS.md canonical-no-negative-result-in-paper discipline + the refined WIP-scaffolding checker (PR #1766): the `[scaffolding, open-rd-item-4]` tag pair signals in-flight R&D content; primary material now lives in the audit doc. The Lean class scaffolding stays in place — downstream Lean files import the classes as hypotheses.",
      see: "https://github.com/litlfred/qou/pull/1767",
    },
    {
      kind: "note",
      date: "2026-06-03",
      body: "Item 4 of the post-PR-#665 open R&D inventory. The class fields follow the explicit-residual pattern; the GNS state and bicommutant closure of the inductive-limit algebra remain the substantive open R&D, with per-$n$ discharge status recorded in the audit doc. This block is retained as an interpretive forward-reference; it makes no logical claim.",
    },
  ],
});
