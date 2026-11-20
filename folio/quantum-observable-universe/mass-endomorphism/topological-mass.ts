import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:topological-mass",
  title: "Topological Decomposition of Mass",
  tags: ["mass", "topological-decomposition", "descent-involution"],
  uses: [
    "def:mass-identity",
    "def:brane-boundary",
    "prop:descent-eigenspaces",
    "prop:topological-mass-upper-bound",
    "lem:topological-mass-transient-localisation",
  ],
  computation: {
    engine: "sympy",
    script: "computations/mass-from-q-symbolic.py",
    witness: "computations/mass-from-q-symbolic.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "Demoted from `conj:topological-mass` (owner, 2026-11-20, on PR #8526; bean qou-27ys). The blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, B08) found that kind, Lean and proof made three different claims. The kind was `theorem`. The `lean.ref` (`QOU.Torsion.mass_decomposition_categorical`) concluded the equality by projecting a field of an assumed context class. Both proof blocks established only the upper bound. That bound is now [prop:topological-mass-upper-bound](#prop:topological-mass-upper-bound). The equality is open: orthogonality of the splitting gives additivity of squared norms, not of norms.",
    },
    {
      kind: "note",
      date: "2026-11-20",
      body: "**What a proof would need (owner request: \"can we prove the equality?\").** `topological-mass-upper-bound.lean` proves that the equality is equivalent to a common-ray (sign or phase) condition on the traces (`mass_eq_of_common_ray`, `sameRay_of_mass_eq`, `mass_eq_iff_sameRay`). A corpus-grep found that condition neither established nor refuted. `norm_additivity_of_nonneg_traces` in `topological-mass.lean` assumes it and is never discharged. Two results pull against it, and neither is a refutation: the unproved orthogonality claim of `lem:topological-mass-cat-eigenspace`, under which equality would force one term to vanish; and the negative baryon Markov trace (`mass-ordering-corrected`). There is also a dichotomy, `transient_trace_eq_zero_of_global_compat`: if trace-compatibility with descent holds on the whole algebra rather than on the descended subalgebra only, every transient trace is zero. The equality then holds trivially but with no transient contribution. The one positivity mechanism in the corpus, `trM_nonneg_of_reading3` (`MassTheory/CompositionFeasibilityProgram.lean`), has not been applied to the descended or transient parts. Tracked in bean qou-wuxx.",
    },
  ],
});
