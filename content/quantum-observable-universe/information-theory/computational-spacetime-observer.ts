import { remark } from "../../schema/builders";

/**
 * Computational spacetime and the observer.
 *
 * Interpretive remark: observer time as computational (Planck-operation)
 * time, points as morphisms from the terminal object, the time step as
 * an endofunctor, and the proposed four-way dictionary (category theory /
 * knot theory / CFT / information theory) for the discrete Planck step.
 * The categorical setup is formalized in
 * lean/QOU/CategoricalDynamics.lean (PointMorphism, flowPoint,
 * ParticleSection, functorialFlowPoint); the "Rosetta stone" uniqueness
 * of the time functor is a heuristic identification, flagged as such in
 * the prose (and left as a commented-out awaited statement in the Lean
 * file).
 */
export default remark({
  label: "rem:computational-spacetime-observer",
  interprets: "def:information-theoretic-time",
  title: "Computational spacetime and the observer",
  lean: { ref: "qou:QOU.CategoricalDynamics.flowPoint" },
  uses: [
    "def:information-theoretic-time",
    "def:brings-surface",
    "thm:jones-markov-trace",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-12",
      body:
        "Integrated from an orphan `.md` (no manifest) per the 2026-07-12 " +
        "exposition-drain ledger §5. The embedded Lean code fence was " +
        "removed from the prose (the definitions live in " +
        "`lean/QOU/CategoricalDynamics.lean`), intensifiers were toned " +
        "down, and the unproved identifications (time-functor uniqueness, " +
        "emergent Lorentz covariance, local-field promotion of $q$) are " +
        "now hedged explicitly as heuristic/speculative.",
    },
  ],
  tags: [
    "computational-time",
    "observer",
    "categorical-dynamics",
    "planck-step",
    "brings-surface",
    "interpretation",
  ],
});
