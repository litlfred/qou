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
    {
      kind: "caveat",
      date: "2026-11-21",
      body:
        "The table predates the owner rulings of 2026-11-18 to 2026-11-21 " +
        "(`docs/coordination/owner-rulings.md`): the corrected photon, the electron " +
        "word sigma0 sigma1 sigma0, and the two-term Lagrangian trace for every " +
        "beta-decay route. It is a historical comparison, not the scored Q_beta cell " +
        "(that is the T3 weight-split value, 0.3254 MeV). The sign theorem it " +
        "interprets is pure algebra and is unaffected.",
    },
  ],
});
