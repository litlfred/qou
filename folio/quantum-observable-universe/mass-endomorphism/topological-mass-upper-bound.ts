import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-mass-upper-bound",
  title: "Upper bound for the topological decomposition of mass",
  tags: ["mass", "topological-decomposition", "descent-involution", "upper-bound"],
  lean: {
    ref: "qou:QOU.Torsion.mass_upper_bound_localised",
    validation: "not_checked",
  },
  uses: [
    "def:mass-identity",
    "def:brane-boundary",
    "prop:descent-eigenspaces",
  ],
  proofs: ["prf:topological-mass-categorical", "prf:topological-mass"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body: "Scope of the Lean. `QOU.Torsion.mass_upper_bound_localised` formalises only the norm step: given the trace value split as descended part plus a finite sum of transient parts, the norm is at most the sum of the norms. It holds over any seminormed additive commutative group and is sorry-free (lean-direct exit 0; axioms propext, Classical.choice, Quot.sound). The split itself is not formalised here. It is supplied by [lem:topological-mass-cat-eigenspace](#lem:topological-mass-cat-eigenspace) and [lem:topological-mass-cat-transient](#lem:topological-mass-cat-transient).",
    },
  ],
});
