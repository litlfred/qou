import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:brings-is-qou",
  label: "rem:brings-is-qou-verification",
  title: "Verification of the QOU data for Bring's surface",
  uses: [
    "prop:brings-is-qou",
    "def:brings-surface",
    "thm:qu-to-qou",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"The obstruction classes $\\kappa_n \\neq 0$ persist at every level by [motivic perpetual obstruction](#thm:motivic-perpetual-obstruction) applied with $\\chi(A) = -6$.\"",
    },
  ],
});
