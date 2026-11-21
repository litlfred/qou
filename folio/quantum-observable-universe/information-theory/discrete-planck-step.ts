import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:planck-time",
  label: "rem:discrete-planck-step",
  title: "Discrete time at the Big Bang: one Planck step of Reeb flow",
  tags: [
    "planck-time",
    "discrete-time",
    "big-bang",
    "reeb-flow",
    "information-theory",
    "dynamical-flow",
    "primordial-vortex",
    "finite-field",
    "p-adic",
    "algebraic-dynamics",
  ],
  uses: [
    "rem:julia-set-reeb",
    "def:bundle-initial-conditions",
    "prop:substrate-radial-coordinate",
    "rem:witt-lift-qou",
  ],
  cites: ["thooft2016"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-25",
      body:
        "**Atomicity claim now has a Lean carrier (primary conjecture, open).** " +
        "This remark's 'there is no sub-step resolution' / 'one full Reeb circuit = one unit of time' " +
        "claim is formalized as the content-bearing §3b-tax primary conjecture class " +
        "`QOU.AlgebraicSubstrate.SubstrateClock.PlanckStepAtomicity` " +
        "(`lean/QOU/AlgebraicSubstrate/PlanckStepAtomicity.lean`, no instance — the ℕ-indexing of " +
        "`InformationTheoreticTime.stepCount` is a modeling chart, not a derivation). " +
        "Atomicity conditionally discharges substrate clock uniqueness (SCU) via " +
        "`substrateClockUniqueness_of_planckStepAtomicity`. Per §3a a remark cannot carry the claim; " +
        "promoting it to a dedicated conjecture block with this Lean as sibling is a recorded follow-up.",
      see: "docs/audits/2026-07-25-planck-step-atomicity-formalization.md",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([bundle initial conditions](#def:bundle-initial-conditions))" },
  ],
});
