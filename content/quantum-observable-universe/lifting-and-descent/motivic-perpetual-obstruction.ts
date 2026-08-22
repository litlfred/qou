import { theorem } from "../../schema/builders";

// Block-kind history:
//   2026-05-02  `lemma` -> `conjecture` (cones-doc audit; the sibling
//               .lean carried a `sorry`, so `lem:` was drift).
//   2026-08-22  `conjecture` -> `theorem`, label `conj:` -> `thm:`.
//               Route A (prime-ideal collapse) closed it: the library
//               decl QOU.LiftingDescent.motivic_perpetual_obstruction is
//               sorry-free, `#print axioms` = {propext, Classical.choice,
//               Quot.sound}. The stale sibling .lean -- which still held
//               the pre-Route-A `sorry` under an older MotivicGaloisCharacter
//               signature, and SHADOWED the proved library decl per
//               AGENTS.md 0a -- was deleted in the same change.
// The theorem is CONDITIONAL in the AGENTS.md "conditional-proved !=
// premise-established" sense: it takes the trace-growth bound `h_bound`
// as an explicit hypothesis. The empty-exception-set form is discharged
// only for the concrete QOU instances (proton C=4, deuteron C=-32) in
// MotivicPerpetualObstructionFromTrace.lean.
export default theorem({
  label: "thm:motivic-perpetual-obstruction",
  title:
    "Motivic perpetual obstruction: $\\chi^{\\mathrm{mot}}_A$ is non-trivial at almost every finite place when $\\chi(A) \\neq 0$",
  tags: [
    "tier:S",
    "motivic-galois",
    "perpetuity",
    "yekutieli",
    "kummer-tower",
    "frobenius",
  ],
  uses: [
    "def:motivic-galois-character",
    "rem:kummer-tower",
  ],
  cites: ["yekutieli2010"],
  lean: {
    ref: "qou:QOU.LiftingDescent.motivic_perpetual_obstruction",
    validation: "leanok",
  },
});
