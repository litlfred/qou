import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-mass-formula-algebraic",
  title:
    "Topological mass formula (algebraic, $\\mathbb{Q}(q)$-side)",
  lean: {
    ref: "qou:QOU.Torsion.AlgebraicMassFormula",
    validation: "not_checked",
  },
  uses: ["lem:tower-pair-equality-fixed-level"],
  cites: [
    "kassel1995",
    "habiro2002",
    "kashaev1997",
    "murakami-murakami2001",
  ],
  tags: [
    "mass",
    "algebraic",
    "quantum-volume",
    "tau-wall",
    "narrative-replacement",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Status: provable** in $\\mathbb{Q}(q)$ from the upstream lemmas (mass\nformula, jet-tower-pair equality, algebraic-volume definition,\nMarkov-trace factorization). The corresponding Lean stub\n[qou:QOU.Torsion.AlgebraicMassFormula](topological-mass-formula-algebraic.lean)\nstates the identity as a `theorem` parametric on the substrate\npackage.\n\nThis block closes the **audit §4.B** wall risk for callers that\nneed the mass-volume identity on the algebraic side: those callers\nmust now route through\n[`prop:topological-mass-formula-algebraic`](#prop:topological-mass-formula-algebraic),\nnot [`conj:topological-mass-formula`](#conj:topological-mass-formula).\nThe two real-violation proofs identified by the **P0.1 sweep**\n([`docs/audits/-p0-1-wall-violation-sweep.md`](../../../docs/audits/-p0-1-wall-violation-sweep.md)) —\n[`local-substrate-q-proof.md`](../observations/local-substrate-q-proof.md)\nand\n[`skein-mass-relation-proof.md`](../observations/skein-mass-relation-proof.md) —\nare updated in this same workplan task to cite the algebraic\nversion with the $\\tau_{\\mathrm{arch}}$-specialisation as the\nfinal numerical step.",
    },
  ],
});
