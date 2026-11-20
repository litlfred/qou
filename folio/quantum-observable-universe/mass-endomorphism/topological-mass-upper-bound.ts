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
      body: "Scope of the Lean. `QOU.Torsion.mass_upper_bound_localised` formalises only the norm step: given the trace value split as descended part plus a finite sum of transient parts, the norm is at most the sum of the norms. It holds over any seminormed additive commutative group and is sorry-free (lean-direct exit 0; axioms propext, Classical.choice, Quot.sound). The same file proves `transient_trace_eq_zero_of_global_compat` (sorry-free; axiom propext only). If the trace is compatible with descent on the whole algebra, every transient trace is zero. The equality of `conj:topological-mass` would then hold with no transient contribution, so a nonzero transient term needs compatibility on the descended subalgebra only, which is the form `lem:topological-mass-cat-descended` uses. The equality's common-ray characterisation is `mass_decomposition_eq_iff` (PR #8581). The split itself is not formalised here. It is supplied by [lem:topological-mass-cat-eigenspace](#lem:topological-mass-cat-eigenspace) and [lem:topological-mass-cat-transient](#lem:topological-mass-cat-transient).",
    },
  ],
});
