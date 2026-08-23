import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data. The $n = 2$ case is formalised faithfully — both partitions factor through the genuine cyclotomic denominator $D_2 = \\Phi_4\\Phi_8 = (t^2+1)(t^4+1) \\neq 0$; the $n = 3, 4$ denominators are canonical verified for all 18 partitions in the witness and tracked for formalisation." },
  ],
  label: "prop:y-lambda-cyclotomic-factorization",
  title:
    "Cyclotomic factorisation of $y_\\lambda$ at $H_n(R, q)$ for small $n$ via Wenzl-bridge",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.y_lambda_cyclotomic_factorization",
    validation: "not_checked",
  },
  uses: ["prop:y-lambda-closed-form-wenzl-bridge"],
  cites: ["wenzl1988", "macdonald1995"],
  tags: [
    "y-lambda",
    "cyclotomic-polynomial",
    "schur-element",
    "closed-form",
    "wenzl-bridge",
    "q-rational",
    "principal-specialization",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probes/y_lambda_cyclotomic_factorization_probe.py",
    witness: "computations/probes/y-lambda-cyclotomic-factorization-probe.witness.json",
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (denominator_factors_as_cyclotomic_product). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
  },
});
