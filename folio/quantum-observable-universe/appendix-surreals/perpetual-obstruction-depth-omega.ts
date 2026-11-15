import { remark } from "../../schema/builders";

export default remark({
  label: "rem:perpetual-obstruction-depth-omega",
  title: "The perpetual obstruction as a single surreal grade",
  interprets: "thm:motivic-perpetual-obstruction",
  uses: [
    "thm:motivic-perpetual-obstruction",
    "def:surreal-blowup-calculus",
    "rem:conway-normal-form",
    "prop:cs-evaluation-faithfulness",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"asserts that the obstruction $\\kappa_n$ is non-trivial at\n*every* finite tower level $n$.\"",
    },
  ],
});
