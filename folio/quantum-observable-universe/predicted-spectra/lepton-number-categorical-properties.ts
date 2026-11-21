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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is `QOU/StandardModel/WritheLevelParity.lean`'s\n`leptonNumber_collapses_at_minimal_level`, and it is the same obstruction\n`LeptonNumberCarrierChirality.lean` proved for the unframed knot type," },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): `QOU/StandardModel/ChiralFermionBraidWords.lean` proves the writhes from the\nwords and shows the candidate" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): It is also what the corpus already does --\n`AntiparticleCrossingReversalContext` takes the mirror" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is forced:\n`QOU/StandardModel/LeptonNumberCarrierChirality.lean` proves $L$ cannot factor\nthrough" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): but the corpus's Vassiliev filtration\n(`QOU/KnotTheory/Vassiliev/`) grades" },
    {
      kind: "refined-framing",
      body: "An earlier version of this section asserted that the Skein module admits a natural ℤ-grading by the smoothing count.",
    },
  ],
});
