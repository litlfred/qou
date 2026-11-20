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
      body: "Demoted from `thm:topological-mass` (owner, 2026-11-20, on PR #8526; bean qou-27ys). The blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, B08) found that kind, Lean and proof made three different claims. The kind was `theorem`. The `lean.ref` (`QOU.Torsion.mass_decomposition_categorical`) concluded the equality by projecting a field of an assumed context class. Both proof blocks established only the upper bound. That bound is now [prop:topological-mass-upper-bound](#prop:topological-mass-upper-bound). The equality is open: orthogonality of the splitting gives additivity of squared norms, not of norms.",
    },
    {
      kind: "note",
      date: "2026-11-20",
      body: "Equivalent form (owner-approved D1/D2, 2026-11-20; bean qou-27ys). The conjecture is equality in the triangle inequality. `QOU.Torsion.mass_decomposition_eq_iff` (PR #8581, sorry-free) proves it holds if and only if the descended trace value and every transient trace value lie pairwise on a common ray, in any strictly convex real normed space. For real values this means they share a sign; for complex values, that they share a phase. `QOU.Torsion.norm_add_lt_of_inner_eq_zero` proves that two non-zero orthogonal pieces give a strict inequality. So orthogonality of the splitting cannot be the route to equality, and the earlier sentence saying it was has been replaced. The only producer that evaluates the pieces separately (`computations/mass_endomorphism.py::mass_from_tower`) gives all-positive signed pieces for the electron, proton and neutron at the proton pin (`computations/probes/topological_mass_ray_alignment_probe.py`). That is scope (a) and weak: the producer defines mass as a sum of norms.",
    },
  ],
});
