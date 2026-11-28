import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-tail-cyclotomic-iff-n-le-5",
  title:
    "The Habiro tail $D(n)$ is a cyclotomic product exactly for $n \\leq 5$",
  uses: [],
  cites: ["billeyswanson2023"],
  computation: {
    engine: "python",
    script: "computations/cyclotomic_boundary_q1_proof_checks.py",
    witness: "computations/cyclotomic-boundary-q1-expansion.witness.json",
    status: "verified",
  },
  tags: ["habiro-tail", "cyclotomic", "computer-assisted"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body: "Computer-assisted. Lean covers n <= 20 (`QOU.Mass.CyclotomicBoundaryCertified`), the 2-adic lemma (`QOU.Mass.InvolutionTwoAdic`) and both hook identities for every partition (`QOU.Mass.HookContentBeta`); the Jucys-Murphy class sums and closed forms for all n are checked as symbolic identities by `computations/cyclotomic_boundary_q1_proof_checks.py`. The class sums are not in Lean: Mathlib has Young diagrams but no standard-tableau counts, characters of S_n or Jucys-Murphy elements, so they need either that theory or a combinatorial up-down (differential poset) recursion for sums of f^λ times content power sums. An independent review found no gap. The full chain is not in Lean, so the block carries no `lean.ref`.",
    },
  ],
});
