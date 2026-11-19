import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hecke-algebra-type-scaffold",
  interprets: "rem:braid-group-n-strand",
  title:
    "Iwahori-Hecke algebra $H_n(R, q)$: the Lean type and its defining relations",
  uses: ["rem:h3-hecke-idempotents"],
  cites: [
    "kassel1995",
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "lean-infrastructure",
    "hecke-algebra-type",
    "wedderburn",
    "audit-forward-reference",
  ],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "status",
      date: "2026-06-03",
      body: "**Primary content moved to [`docs/audits/2026-06-03-wip-scaffolding-hecke-algebra-type-scaffold.md`](../../../docs/audits/2026-06-03-wip-scaffolding-hecke-algebra-type-scaffold.md).** Per AGENTS.md canonical-no-negative-result-in-paper discipline + the refined WIP-scaffolding checker (PR #1766): the `[scaffolding, open-rd-item-2]` tag pair signals in-flight R&D content; primary material now lives in the audit doc. The Lean class scaffolding stays in place — downstream Lean theorems take `[HeckeRelations n q]` and `[HeckeWedderburn n q]` as hypotheses.",
      see: "https://github.com/litlfred/qou/pull/1767",
    },
    {
      kind: "note",
      date: "2026-06-03",
      body: "Item 2 of the post-PR-#665 open R&D inventory. The class fields follow the explicit-residual pattern, and the per-$n$ discharge status ($n = 2$ trivial, $n = 3$ partial via Hoefsmit, $n = 6, 12$ open) is recorded in the audit doc. This block is retained as an interpretive forward-reference; it makes no logical claim.",
    },
  ],
});
