import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ns-obstruction-tower",
  lean: { ref: "qou:QOU.FluidDynamics.ns_obstruction_tower", validation: "not_checked" },
  title:
    "The NS obstruction class in the Yekutieli tower",
  uses: [
    "def:ns-regular-qou",
    "prop:core-levi-form",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"Consequently, $\\kappa_n \\neq 0$ unconditionally for all $n$.\"",
    },
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Proof step (d) withdrawn after owner ruling Q1 " +
        "($\\varTheta = f\\,\\xi^\\flat$, 2026-10-13).** It read: \"Relying on " +
        "core-Levi equivalence, the local cohomology holds a nonzero value if and " +
        "only if the Levi form maintains strict non-degeneracy at $p$: " +
        "$H^1_{\\mathfrak{m}_p}(A) \\neq 0 \\Leftrightarrow \\lambda_\\parallel(p) > 0$ " +
        "and $\\lambda_\\perp(p) > 0 \\Leftrightarrow \\kappa(p) = a_\\perp/a_\\parallel " +
        "\\in (0, \\infty)$. If the core flattens completely, one Levi eigenvalue " +
        "collapses. The local cohomology subsequently degenerates from " +
        "$V_{1/2}^{\\oplus 2}$ down to a quotient, forcing the obstruction class " +
        "$\\kappa_n|_\\Sigma$ to deform safely toward zero.\" In dimension 3 the " +
        "Levi datum is the scalar $\\xi\\cdot\\mathrm{curl}\\,\\xi$ " +
        "(`prop:core-levi-form`), so the eigenvalue pair does not exist; no " +
        "replacement is offered. (e) now cites (a)–(c). **The proposition's " +
        "statement is unaffected**: it never mentioned Levi data, and its Lean " +
        "(`ns_obstruction_tower`, `NsObstructionTowerContext`) carries both " +
        "directions of the iff as explicit hypotheses and has no Levi field. The " +
        "proof was already scoped as non-discriminating ((b)/(e): " +
        "$H^2(\\Sigma, \\cdot) = 0$ on the one-dimensional locus) before this " +
        "change. Not edited, and carrying the same withdrawn step as Lean: " +
        "`QOU/FluidDynamics/yekutieli_levi_unification.lean` " +
        "(`NSObstructionLeviData`, field for step (d)) and " +
        "`qou_ns_in_qou.lean` (`QOUFluidUniverseLevi`, branch A). Bean `qou-fm7s`." +
        " Update 2026-11-15 (owner option 1, PR #7747): all of these are now re-scoped; see bean qou-fm7s.",
    },
  ],
  tags: [
    "obstruction",
    "yekutieli",
    "cohomology",
    "navier-stokes",
    "boundary-observability",
    "euler-class",
  ],
});
