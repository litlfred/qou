import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-turing-completeness-classical",
  title:
    "Classical Turing-completeness of steady Euler / Reeb flows (Cardona–Miranda–Peralta-Salas–Presas)",
  lean: {
    ref: "qou:QOU.Information.ReebTuringClassical",
    validation: "not_checked",
  },
  uses: [],
  cites: ["cardona2021", "cardona2023"],
  tags: [
    "reeb-flow",
    "euler-flow",
    "turing-completeness",
    "contact-geometry",
    "undecidability",
    "information-theory",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-25",
      body:
        "Split out of rem:reeb-turing-completeness so the proved q=1 result is a proposition, distinct from the conjectural q-deformed lift (conj:quantum-computational-universality). Lean carrier is an external-theorem sorry (-- Ref: cardona2021); not re-formalised.",
    },
  ],
});
