import { remark } from "../../schema/builders";

export default remark({
  label: "rem:parity-regime-dispatch",
  title: "Parity regime dispatch for Q-values",
  interprets: "thm:parity-regime-selection",
  tags: ["parity", "regime-selection", "q-value", "empirical-comparison"],
  uses: [
    "thm:parity-regime-selection",
    "prop:branching-qvalue-factorization",
    "prop:confinement-lp",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-16",
      body:
        "Split out of `thm:parity-regime-selection` on owner ruling 2026-11-16. " +
        "The three regime formulas were previously carried as Lean class fields " +
        "and projected back out, so the theorem assumed its own conclusion. They " +
        "are a per-case dispatch, chosen rather than derived, and carry no Lean claim.",
    },
  ],
});
