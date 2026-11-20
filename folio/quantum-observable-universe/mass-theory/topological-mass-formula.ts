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
});
