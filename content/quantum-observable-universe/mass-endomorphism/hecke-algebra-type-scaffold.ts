import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hecke-algebra-type-scaffold",
  interprets: "rem:braid-group-n-strand",
  title:
    "Iwahori-Hecke algebra $H_n(R, q)$ type scaffold (forward-reference to WIP-scaffolding audit)",
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
    {
      kind: "status",
      date: "2026-06-03",
      body: "**Primary content moved to [`docs/audits/2026-06-03-wip-scaffolding-hecke-algebra-type-scaffold.md`](../../../docs/audits/2026-06-03-wip-scaffolding-hecke-algebra-type-scaffold.md).** Per AGENTS.md canonical-no-negative-result-in-paper discipline + the refined WIP-scaffolding checker (PR #1766): the `[scaffolding, open-rd-item-2]` tag pair signals in-flight R&D content; primary material now lives in the audit doc. The Lean class scaffolding stays in place — downstream Lean theorems take `[HeckeRelations n q]` and `[HeckeWedderburn n q]` as hypotheses.",
      see: "https://github.com/litlfred/qou/pull/1767",
    },
  ],
});
