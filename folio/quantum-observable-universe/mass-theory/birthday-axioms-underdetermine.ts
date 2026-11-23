import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:birthday-axioms-underdetermine",
  title:
    "The birthday axioms do not characterise Conway's birthday: a two-valued " +
    "function satisfies all six",
  tags: [
    "surreal",
    "hyperreal",
    "axiomatisation",
    "defect-report",
    "limit-transfer",
  ],
  lean: {
    ref: "qou:QOU.AppendixSurreals.HyperrealTransfer.flatBirthday_avg_le",
    validation: "leanok",
  },
  uses: ["prop:ideal-tetrahedron-relabelling-invariance"],
  cites: ["conway1976", "robinson1966"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The corpus's `SurrealField` class asks for more than an ordered field.\n\nThe practical consequence is recorded in the formalisation: the resulting `SurrealField` structure on $\\mathbb{R}^*$ is a plain definition and deliberately **never** a global instance. Registering it globally would silently apply every `SurrealField`-generic theorem to the hyperreals under a birthday that is not Conway's — turning a documented defect into a silent one." },
  ],
});
