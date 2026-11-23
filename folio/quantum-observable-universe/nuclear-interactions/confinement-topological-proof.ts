import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confinement-topological",
  title: "Proof of confinement topological",
  uses: ["prop:confinement-topological"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Witness:** `confinement-lp.witness.json`." },
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
        "**Part (iii) has been re-run live and does not hold** — " +
        "`computations/probes/confinement_b3_enumeration_recheck_probe.py`, " +
        "all 5460 words of length 1–6, witness committed. Its cited " +
        "`confinement-lp.witness.json` is in `_deprecated/` (an open " +
        "`da-reproducibility` warn on `prop:confinement-topological`), but " +
        "$|\\Delta\\mathrm{net}|$ is **trace-independent** — it reads only " +
        "`HA` and sums of NF coefficients — so the stale $\\mathrm{tr}_M$ " +
        "that caused the deprecation never affected this part. It was always " +
        "checkable.\n\n" +
        "- *\"All other words have $|\\Delta\\mathrm{net}| > 0.01$\"* is " +
        "**false**: 382 proton and 167 neutron words come in at or under " +
        "0.01. **187 and 139 of those sit inside the producer's own " +
        "enumerated lengths $\\{2,4,6\\}$**, so its own table contradicted " +
        "its prose.\n" +
        "- *\"The mirror … an order of magnitude worse\"* — the mirror is " +
        "not the runner-up. It ranks **12th of 5460** for the proton and " +
        "**111th** for the neutron; the best non-$\\mathcal{B}_3$ words " +
        "reach 0.00159 and 0.00202 against the mirror's 0.00354 / 0.00395.\n" +
        "- *\"and all shorter words\"* — the producer loops " +
        "`for length in [2, 4, 6]`. **Odd lengths were never enumerated**, " +
        "and they matter: the proton's second-best word overall is the " +
        "length-5 $\\sigma_0^{-1}\\sigma_1\\sigma_0^{-1}\\sigma_1\\sigma_1$.\n" +
        "- *\"$\\mathcal{B}_3$ achieves $|\\Delta\\mathrm{net}| = 0.000$\"* is " +
        "**circular**: the producer sets `target_net = " +
        "float(sum(b3_confined))`, so the target *is* $\\mathcal{B}_3$'s own " +
        "confined net. Any operator in that line scores 0.\n\n" +
        "Every figure survives both $q_0$ anchors (re-run under " +
        "`QOU_Q0_ANCHOR=ideal`; counts identical). **This refutes the " +
        "enumeration, not $\\mathcal{B}_3$** — a selection argument needs a " +
        "metric not defined from the answer.\n\n" +
        "The deprecated witness's `gram_matrix` is also **not symmetric** " +
        "($\\max|G-G^\\mathsf{T}| = 0.46$), and the cause is the same stale " +
        "trace, not a separate bug: rebuilding through the producer's own " +
        "`build_gram` with the power rule $[1,z,z,z^2,z^2,z^3]$ gives " +
        "$\\max|G-G^\\mathsf{T}| = 0.46$ and rank 6, while the canonical " +
        "`pyhecke.gram.TR_M` — differing in **one entry**, " +
        "$\\mathrm{tr}_M(e^-) = hz^2+z$ rather than $z^3$ — gives exactly " +
        "0.0 and rank 5. A Gram is symmetric for any genuine trace; the " +
        "power rule is not a trace. (`qou/6hm4` first read the asymmetry as " +
        "a row-ordering error because exchanging $L_+$ and $L_-$ happens to " +
        "symmetrise it — a coincidence in the numbers, corrected there.)",
    },
  ],
});
