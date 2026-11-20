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
  ],
});
