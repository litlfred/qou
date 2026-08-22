import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confinement-topological",
  title: "Proof of confinement topological",
  uses: ["prop:confinement-topological"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-22",
      body:
        "**Part (i)'s spectrum is right in shape and wrong in its numbers, " +
        "and the descent mechanism it states does not hold.** Checked " +
        "against the canonical `pyhecke.gram` at $q_0$ — see bean " +
        "`qou/6hm4`.\n\n" +
        "The prose spectrum $\\{\\lambda_+, \\lambda_+, \\lambda_+, " +
        "\\lambda_{\\max}, \\lambda_0, \\lambda_-\\}$ matches exactly, and " +
        "$\\lambda_- < 0$ is **true**. But the canonical values are " +
        "$\\{-0.7527, 0, 0.7527, 0.7527, 0.7527, 4.2303\\}$: " +
        "$\\lambda_- = -0.7527$, not the stated $\\approx -0.855$, and " +
        "$\\lambda_- = -\\lambda_+$ exactly. The $-0.855$ figure belongs to a " +
        "different Gram (it appears in `molecular-frobenius-lp` and " +
        "`qbeta-symbolic-sdp-strict-complementarity`).\n\n" +
        "**$\\lambda_0 = 0$ exactly** ($1.85\\times10^{-16}$), and the proof " +
        "names it without saying so. That zero is the trace-form radical — " +
        "the $q$-antisymmetriser — which `qou/k4f8` proves is identically " +
        "singular in $\\mathbb{Q}(q)$ and which forces $y_0^* = 0$. The " +
        "proof's own eigendecomposition contains the degeneracy, unlabelled.\n\n" +
        "**The stated mechanism fails on both clauses.** The proof says " +
        "*\"the eigenvector $v_-$ satisfies $t \\cdot v_- < 0$ while " +
        "$Gv_- \\ge 0$ in certain components\"*. At $q_0$, " +
        "$v_- = (0,0,0,\\tfrac{1}{\\sqrt2},-\\tfrac{1}{\\sqrt2},0)$ — the " +
        "$L_+ - L_-$ direction — and $t \\cdot v_- = 0$, not negative " +
        "(because $t\\cdot v = (Gv)_0 = \\lambda (v)_0$ and $(v_-)_0 = 0$), " +
        "while $Gv_- = (0,0,0,-0.532,+0.532,0)$ has a negative component. " +
        "Moving along $v_-$ changes the objective not at all and violates " +
        "Frobenius positivity immediately.\n\n" +
        "**No direction can do what the sentence asks.** Because the basis " +
        "contains $\\mathbf{1}$, $t$ is row 0 of $G$, so $t \\cdot x = " +
        "(Gx)_0$ for *every* $x$ — hence $t \\cdot x \\ge 0$ for every " +
        "feasible $x$. The objective is bounded below by one of its own " +
        "constraints, so it cannot be decreased below $0$ within the " +
        "feasible set. A negative eigenvalue of $G$ is real, but it is not " +
        "what the LP exploits.\n\n" +
        "Part (iii)'s $4^6$ enumeration cites " +
        "`confinement-lp.witness.json`, which lives in `_deprecated/` — " +
        "already flagged as a `da-reproducibility` warn on " +
        "`prop:confinement-topological`. Two further defects in that file, " +
        "not previously recorded: its `gram_matrix` is **not symmetric** " +
        "($\\max|G-G^\\mathsf{T}| = 0.4269$; a trace form is symmetric for " +
        "any trace, stale values included, since $\\mathrm{tr}(ab) = " +
        "\\mathrm{tr}(ba)$), and swapping rows 3 and 4 makes it exactly " +
        "symmetric — so its committed `gram_eigenvalues` are the spectrum " +
        "of an asymmetric matrix, not of a Gram.",
    },
  ],
});
