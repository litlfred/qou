import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:binding-qbeta-complex-volume",
  label: "rem:complex-volume-character-variety-path",
  title:
    "Bound $\\leftrightarrow$ free as a character-variety path: the deformation reading of $\\mathfrak{V}$",
  lean: {
    ref: "qou:QOU.MassEndomorphism.AWDeformationPath",
    validation: "not_checked",
  },
  uses: [
    "conj:binding-qbeta-complex-volume",
  ],
  cites: [
    "murakami-h2011",
    "hikami2001",
    "neumann-zagier1985",
    "garoufalidis-zagier-2024",
  ],
  tags: [
    "complex-volume",
    "character-variety",
    "deformation-path",
    "chern-simons",
    "askey-scheme",
    "fibre-level",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is formalized in the conjecture class `AWDeformationPath`. The class specifies\n\nis a derived theorem (`AWDeformationPath.channel_ladders` via `recurrence_invol_descent`), rather than an assumption." },
  ],
});
