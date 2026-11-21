import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tannaka-krein-isomorphism",
  title: "Tannaka--Krein duality for the substrate",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.IsTannakaKreinDual",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-reeb-derivation",
    "def:local-cohomology-group",
  ],
  tags: [
    "tannaka-krein",
    "duality",
    "representation",
    "quantum-group",
    "reconstruction",
  ],
  cites: ["reshetikhin1991"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean carrier `IsTannakaKreinDual` states the condition over arbitrary parameter categories and is satisfiable." },
  ],
});
