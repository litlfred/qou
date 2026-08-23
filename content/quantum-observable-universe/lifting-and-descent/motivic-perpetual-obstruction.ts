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
    // Take main's repoint, not this branch's. Earlier in this PR I set
    // `leanok` on `motivic_perpetual_obstruction` after `#print axioms` came
    // back clean — which was true and beside the point. main subsequently
    // showed that theorem carries a `[MotivicGaloisCharacter …]` binder it
    // NEVER USES: its `trace` is a free function and its conclusion is about
    // `trace`, so what it proves holds of any eventually-large integer
    // function and mentions no motivic structure at all. Sorry-free was never
    // the question. `_frobenius` supplies the missing link — the trace is the
    // image of the Frobenius family under a realization, and the conclusion is
    // about `hχ.frobenius_at p` itself.
    ref: "qou:QOU.LiftingDescent.motivic_perpetual_obstruction_frobenius",
    validation: "not_checked",
  },
});
