import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:topological-mass-formula",
  title: "Topological mass formula (Archimedean)",
  tags: ["mass", "archimedean", "knot-volume", "quantum-planck"],
  uses: [
    "conj:topological-mass",
    "def:quantum-planck-constant",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "Demoted from `prop:topological-mass-formula` (owner ruling 1(a), 2026-11-20, PR #8526 comment 7041693067; bean qou-tm3c). The derivation starts from the equality in [conj:topological-mass](#conj:topological-mass), which is open since #8555. Step 2 also takes the dilogarithm sum identity as a hypothesis (field `exceptional_sum_eq` of the Lean structure `QOU.Torsion.ArchimedeanMassFormula`). The Lean sibling proves only Step 3: given both evaluations, the sum is $\\mathrm{Vol}(K)/\\hbar_q^2$.",
    },
  ],
  lean: { ref: "qou:QOU.Torsion.ArchimedeanMassFormula",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean formalisation isolates this identity as a hypothesis on\nthe archimedean structure rather than a derived theorem;" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): $q$-deformation; this is `Hypothesis 2 (Dilogarithm evaluation)`\non the Lean structure\n[`qou:QOU.ArchimedeanMassFormula`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/lean/QOU/ArchimedeanMassFormula.lean),\nfield `exceptional_sum_eq`):" },
  ],
});
