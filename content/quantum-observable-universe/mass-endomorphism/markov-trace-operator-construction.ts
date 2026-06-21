import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-trace-operator-construction",
  interprets: "rem:markov-trace-inductive-limit",
  title:
    "Markov-trace operator construction (forward-reference to WIP-scaffolding audit)",
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
    {
      kind: "status",
      date: "2026-06-03",
      body: "**Primary content moved to [`docs/audits/2026-06-03-wip-scaffolding-markov-trace-operator-construction.md`](../../../docs/audits/2026-06-03-wip-scaffolding-markov-trace-operator-construction.md).** Per AGENTS.md canonical-no-negative-result-in-paper discipline + the refined WIP-scaffolding checker (PR #1766): the `[scaffolding, open-rd-item-4]` tag pair signals in-flight R&D content; primary material now lives in the audit doc. The Lean class scaffolding stays in place — downstream Lean files import the classes as hypotheses.",
      see: "https://github.com/litlfred/qou/pull/1767",
    },
  ],
});
