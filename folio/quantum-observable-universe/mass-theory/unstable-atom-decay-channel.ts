import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Statement restated 2026-11-21 to what the Lean proves (owner ruling on the PR #8819 follow-up).** The earlier statement asserted that the decay channel λ*(K, q) exists and is the unique violated constraint. The `lean.ref` theorem `decay_channel` proves less. (1) Existence of λ* is not formalised. (2) Uniqueness is taken from the hypothesis `hsel` (off the boundary variety every minimiser equals `lamStar`), which is the LP-duality input of `prop:mass-coefficient-shadow-price` assumed, not derived. (3) The second conjunct is the intermediate value theorem for an arbitrary continuous `E : ℝ → ℝ`; `IsMinimiser`, `OnBoundary` and `E` are free parameters, not built from the atom. The Lean file's own module docstring lists these gaps. The narrative proof also asserts that the LP relaxation equals the convex hull of the integer solutions, which is false in general, and its scope note concedes that x = 0 is feasible. Found by the blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B02; bean qou-ni0g).",
    },
  ],
  label: "prop:unstable-atom-decay-channel",
  title: "Uniqueness of the decay channel off the boundary variety",
  lean: { ref: "qou:QOU.BraidKnot.UnstableAtom.decay_channel",
    validation: "not_checked",
  },
  uses: ["def:unstable-atom", "prop:mass-coefficient-shadow-price"],
  tags: ["decay", "instability", "ilp", "phase-boundary"],
});
