import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:trm-hopf-sigma1-sq-closed-form",
  lean: {
    ref: "qou:QOU.Braiding.TrMHopfSigma1SqClosedForm",
    validation: "not_checked",
  },
  title: "Closed form for the canonical Markov trace of σ_1² (Hopf+ braid)",
  tags: ["hecke-algebra", "markov-trace", "closed-form", "hopf-braid", "binomial-series"],
  uses: ["thm:jones-markov-trace"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/Braiding/TrMHopfSigma1SqClosedForm.lean` uses " +
        "`Real.sqrt`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "**Convention D correction, and the §7c note above is now stale.** " +
        "The boxed closed form was derived from the excised convention C, " +
        "$z = 1/(q^{1/2}+q^{-1/2})$, which is why it carried half-integral " +
        "powers: $(q-q^{-1})\\cdot z$ collapses to $q^{1/2}-q^{-1/2}$ only " +
        "because $q - q^{-1} = (q^{1/2}-q^{-1/2})(q^{1/2}+q^{-1/2})$. Under " +
        "the production convention D, $z = q^3/(q^2+1)$, the answer is " +
        "**rational** in $q$: $\\mathrm{tr}_M(\\sigma_1^2) = (q^4+1)/(q^2+1) " +
        "= q[2]_{q^2}/[2]_q$, giving $1.12808874411435378559$ at $q_0$ " +
        "against the withdrawn C value $1.10438805825918163783$. The " +
        "$\\varepsilon$-expansion is correspondingly no longer binomial — it " +
        "is a period-8 damped oscillation with radius of convergence " +
        "$\\sqrt2$ — so Table 1's $\\binom{-1/2}{k-1}$ column and Table 2's " +
        "bare-Markov column have both been recomputed. **Two follow-ups, " +
        "neither done here.** (i) The Lean module " +
        "`lean/QOU/Braiding/TrMHopfSigma1SqClosedForm.lean` still states the " +
        "C form over `Real.sqrt`; under D no square root occurs, so the §7c " +
        "archimedean justification in the note above no longer holds and the " +
        "statement should move to a generic `CommRing` (or `Field`) base. " +
        "(ii) `computations/probe_F_n_categorical_derivation.py` verified the " +
        "C binomial coefficients and has not been re-run; the D coefficients " +
        "in Table 1 are exact rationals derived symbolically, not witnessed.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/gram_h3_symbolic_regression.py",
    witness: "computations/gram-h3-symbolic-regression.witness.json",
    status: "verified",
  },
});
