import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-mass-formula",
  title: "Topological mass formula (Archimedean)",
  tags: ["mass", "archimedean", "knot-volume", "quantum-planck"],
  uses: [
    "conj:topological-mass",
    "def:quantum-planck-constant",
  ],
  lean: { ref: "qou:QOU.Torsion.ArchimedeanMassFormula",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean formalisation isolates this identity as a hypothesis on\nthe archimedean structure rather than a derived theorem;" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): $q$-deformation; this is `Hypothesis 2 (Dilogarithm evaluation)`\non the Lean structure\n[`qou:QOU.ArchimedeanMassFormula`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/lean/QOU/ArchimedeanMassFormula.lean),\nfield `exceptional_sum_eq`):" },
  ],
});
