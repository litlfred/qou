import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The analytic input ... is now formalised, but not yet *connected*: the Lean statements above still assume the saddle as hypotheses and prove the algebra downstream, which is where the rigidity lives. Both inputs are machine-checked separately. `kashaev_log_sum_asymptotic` gives the expansion with an explicit remainder ...; `hasSum_gaussian_theta` gives Laplace's method for the sum as an *exact* Jacobi-theta identity ... What is still assumed is the step from those two theorems to the hypotheses `hc` and `hτ`" },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). This one is archimedean at the level of the " +
        "*definition*, not merely of the proof: `twoPointExponent` is the " +
        "logarithmic slope " +
        "$(\\log c_1 - \\log c_2)/(\\log t_1 - \\log t_2)$, so `Real.log` is " +
        "the object, not a tactic. Remove the logarithm and there is no " +
        "exponent to be invariant. Downstream, " +
        "`k_const_iff_exponent_neg_half` uses `Real.sqrt` and the strict " +
        "positivity $0 < t_i$, $0 < c_i$; the saddle group " +
        "(`saddle_forces_cot`, `c_sq_sqrt_three_of_saddle`, " +
        "`k_sq_eq_half_of_saddle`) quantifies over " +
        "$\\theta \\in (\\pi/2, \\pi)$ with `Real.sin`. Every one of those is " +
        "on the §7c archimedean row of the table.\n\n" +
        "This is not the fibre-vs-observable confusion warned about in " +
        "AGENTS.md (\"Im(q) at fibre vs observable level\"): the statements " +
        "here are deliberately at the *observable* level. They are about a " +
        "measured real power law $c_\\sigma = k\\,|\\tau|^{p}$ and about which " +
        "half of it survives a change of normalisation convention — the " +
        "exponent does, the prefactor does not. There is no formal-$q$ fibre " +
        "object being evaluated, so there is nothing to restate over " +
        "$\\mathbb{Z}[q,q^{-1}]$; the file's own scope note is accurate that " +
        "it carries no geometric content, only the algebra of a power law and " +
        "its logarithm.",
      see: "folio/quantum-observable-universe/lean/QOU/OneLoopPrefactorInvariance.lean",
    },
  ],
  label: "prop:one-loop-prefactor-provenance",
  title:
    "The 1-loop prefactor law splits: the exponent $-1/2$ is normalisation-invariant and measured, and the constant $k = 2^{-1/2}$ is forced by the saddle condition rather than calibrated on $4_1$",
  lean: {
    ref: "qou:QOU.OneLoopPrefactorInvariance.k_const_iff_exponent_neg_half",
    validation: "validated",
  },
  uses: [
    // conj:b1-hyperbolic-rows-theorem removed (qou-tm3c): the .md is about the DGLZ / van der Veen saddle point and never cites the depth correspondence.
  ],
  cites: [
    "dimofte-gukov-lenells-zagier-2009",
    "gukov-murakami-2008",
    "vanderveen2008",
    "dimofte-garoufalidis-2013",
    "garoufalidis-yoon-2024",
  ],
  tags: [
    "one-loop",
    "prefactor",
    "adjoint-torsion",
    "volume-conjecture",
    "whitehead-link",
    "borromean-rings",
    "normalisation-convention",
    "c-sigma",
    "van-der-veen",
    "dglz",
    "kashaev-invariant",
    "figure-eight",
    "saddle-point",
  ],
});
