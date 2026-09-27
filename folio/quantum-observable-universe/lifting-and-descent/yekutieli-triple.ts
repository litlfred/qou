import { definition } from "../../schema/builders";

export default definition({
  label: "def:yekutieli-triple",
  // Was `qou:QOU.YekutieliTripleMapping` — no such declaration exists anywhere
  // in the Lean tree (0 matches). It did NOT fail loudly: `parseLeanRef` reads
  // the module as `QOU`, so it resolved to `lean/QOU.lean` — the 954-line root
  // import aggregator. Every checker consuming this block's `.lean` was
  // therefore auditing a bare list of `import` lines, and passing.
  //
  // Repointed at the module that actually declares the structure, over the
  // §7c-canonical ground ring `R_q = ℤ[q, q⁻¹]` (`LaurentPolynomial ℤ`).
  // The module segment must be the FILE (`…CosimplicialCrossedGroupoid`), not
  // the Lean namespace: the shorter `qou:QOU.LiftingDescent.YekutieliTriple`
  // has no matching file, so the resolver's basename fallback lands on
  // `QOU/Torsion/YekutieliTriple.lean` — the ℝ-typed duplicate, i.e. the wrong
  // side of the §7c wall. Verified with the canonical resolver.
  lean: {
    ref: "qou:QOU.LiftingDescent.CosimplicialCrossedGroupoid.YekutieliTriple",
    validation: "not_checked",
  },
  title: "Lifting triple mapping",
  tags: ["yekutieli", "triple", "gerbe", "transition-function"],
  uses: ["lem:descent"],
});
