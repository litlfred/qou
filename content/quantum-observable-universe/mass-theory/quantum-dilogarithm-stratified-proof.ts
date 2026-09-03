import { proof } from "../../schema/builders";

export default proof({
  label: "prf:quantum-dilogarithm-stratified",
  of: "prop:quantum-dilogarithm-stratified",
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-26",
      body:
        "Step 1's orthogonality condition was corrected from `k + ℓ ≠ N` (anti-diagonal) to `k ≠ ℓ` (diagonal) — bean `qou-xsv8`. The correction *repairs* Step 4, which needs the diagonal form and did not follow from the anti-diagonal one. The in-prose note states the mathematics; this records the provenance.",
    },
  ],
  uses: [
    "prop:quantum-dilogarithm-stratified",
    "cor:quantum-dilogarithm",
    "prop:categorical-mass-markov",
  ],
  tags: [
    "quantum-dilogarithm",
    "brane-tower",
    "centre-stratification",
  ],
});
