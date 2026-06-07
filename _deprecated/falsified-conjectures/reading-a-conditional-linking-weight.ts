import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:reading-a-conditional-linking-weight",
  title:
    "Reading-A linking-weight: $\\mathrm{linkingWeight}(q) = \\tfrac{5}{2} + (-G) h^2$ (conditional)",
  lean: {
    ref: "qou:QOU.BraidKnot.ReadingAValidAtH2",
    validation: "not_checked",
  },
  uses: [
    "thm:lambda-scale-substrate-form",
  ],
  cites: [
    "adams1985hyperbolic",
    "yekutieli2015",
  ],
  tags: [
    "linking-weight",
    "reading-a",
    "borromean",
    "conjecture",
    "h2-coefficient",
    "open-problem",
    "ppm-coincidence-basin",
    "falsified-candidate",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-06-07",
      body:
        "**Falsified candidate, retained for audit only — NOT a live open " +
        "conjecture and NOT production.** The h² coefficient −G (Catalan) " +
        "directly contradicts the PROVED Family-A theorem " +
        "(`thm:lambda-scale-substrate-form`, linkingWeight = 5/2 + (3/4)·h²), " +
        "and the Wedderburn-sum incarnation of Reading-A was falsified across " +
        "five structural routes. It is carried as a conditional class with an " +
        "explicit Lean `sorry` purely to record the striking ppm-level " +
        "numerical coincidence at the substrate anchor; Family-A remains the " +
        "proved, production linking-weight. The conditional status is also " +
        "stated in the block body's '## Status (read this carefully)' section " +
        "— this note lifts it to the manifest. (Conjecture-triage 2026-06-07.)",
      see: "docs/audits/2026-06-07-conjecture-triage.md",
    },
  ],
});
