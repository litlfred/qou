import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:yekutieli-transcendence-shadow",
  title:
    "Algebraic independence as the transcendence shadow of non-vanishing obstructions",
  tags: [
    "yekutieli",
    "obstruction",
    "cosimplicial",
    "transcendence",
    "brane-tower",
    "algebraic-independence",
  ],
  uses: ["prop:cosimplicial-crossed-groupoid"],
  cites: ["yekutieli2010"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"The classes $\\kappa_n$ never vanish. The brane tower therefore never collapses to finite height\"",
    },
  ],
});
