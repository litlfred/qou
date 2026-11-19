import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lepton-number-categorical-properties",
  interprets: "def:lepton-number-categorical",
  title:
    "Conservation, $\\mathbb{Z}$-grading, and the $\\chi = -6$ constraint on lepton number",
  tags: [
    "lepton-number",
    "skein-relation",
    "smoothing",
    "conservation-law",
    "categorical",
    "weak-force",
  ],
  uses: [
    "def:lepton-number-categorical",
    "def:beta-decay-skein",
    "prop:torus-knot-generators",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "An earlier version of this section asserted that the Skein module admits a natural ℤ-grading by the smoothing count.",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean formalisation references: Z-grading obstruction in `QOU.StandardModel.LeptonNumberGradingObstruction`; Vassiliev invariant filtration in `QOU/KnotTheory/Vassiliev/`; unframed knot-type chirality obstruction in `QOU/StandardModel/LeptonNumberCarrierChirality.lean` (`AntiparticleCrossingReversalContext`); chiral fermion braid words and `L = sign(writhe)` table check plus `leptonNumber_not_markov_invariant` in `QOU/StandardModel/ChiralFermionBraidWords.lean`; minimal-level collapse `leptonNumber_collapses_at_minimal_level` in `QOU/StandardModel/WritheLevelParity.lean`.",
    },
  ],
});
