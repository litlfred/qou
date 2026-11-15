import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:macroscopic-stability-equivalence",
  title:
    "Macroscopic stability is equivalent to the Riemann hypothesis",
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-22",
      body:
        "Demoted **theorem → conjecture** (bean `qou-rhax`). The Lean sibling " +
        "carried two axioms that proved `False` — each stated an `Iff` between " +
        "propositions with independently-quantified arguments, which forces " +
        "`RiemannHypothesis` to be constant in ζ, and it is not. Both are " +
        "removed and replaced by a single content-bearing conjecture class over " +
        "one datum, with no instance. `validation` moved `not_checked` → " +
        "`lean_direct_exit_0`: the file had never compiled (22 errors) and now " +
        "does, sorry-free, with `#print axioms` clean on all three declarations.",
    },
  ],
  lean: { ref: "qou:QOU.AlgebraicSubstrate.macroscopic_stability_equivalence" },
  uses: [
    "thm:quantum-gap-collapse",
  ],
  tags: [
    "stability",
    "equivalence",
    "riemann-hypothesis",
    "macroscopic",
    "continuum",
  ],
  cites: ["vonkoch1901"],
});
