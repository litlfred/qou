import { remark } from "../../schema/builders";

/**
 * Computational spacetime and the observer.
 *
 * Interpretive remark: observer time as computational (Planck-operation)
 * time, points as morphisms from the terminal object, the time step as
 * an endofunctor, and the proposed four-way dictionary (category theory /
 * knot theory / CFT / information theory) for the discrete Planck step.
 * The sibling .lean (pre-existing on main) formalizes the
 * computational-distance structure on Bring's-surface observers
 * (computationalDistance, symmetry, involution invariance); the wider
 * categorical setup (PointMorphism, flowPoint, ParticleSection,
 * functorialFlowPoint) lives in lean/QOU/CategoricalDynamics.lean. The
 * "Rosetta stone" uniqueness of the time functor is a heuristic
 * identification, flagged as such in the prose (and left as a
 * commented-out awaited statement in CategoricalDynamics.lean).
 */
export default remark({
  label: "rem:computational-spacetime-observer",
  interprets: "def:information-theoretic-time",
  title: "Computational spacetime and the observer",
  lean: { ref: "qou:QOU.computationalDistance" },
  uses: [
    "def:information-theoretic-time",
    "def:brings-surface",
    "thm:jones-markov-trace",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: `**Base ring (§7c) — \`ℝ\` is load-bearing by meaning.** \`BringsObserver\` carries \`comp_time\` and \`spatial_coord\`, and \`computationalDistance\` is a distance between two observers. Coordinates of a spacetime point and a distance between them are real quantities; a generic commutative ring has no notion of either.`,
    },
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
