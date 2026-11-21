import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:macroscopic-stability-equivalence",
  title:
    "Macroscopic stability is equivalent to the Riemann hypothesis",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): It is nonetheless carried here as a hypothesis rather than as an established input, because it is not available in the formal library.\n\n## Formalisation\n\nThe Lean sibling carries the statement as a conjecture class over a single datum, with **no instance**. The one theorem in the file is conditional on that class and derives the remaining equivalence $(1) \\Leftrightarrow (3)$ by transitivity; it is a derivation from the hypotheses, not a restatement of one.\n\n## Two inconsistent axioms removed\n\nUntil 2026-08-22 the Lean sibling asserted the two equivalences as axioms, each quantified over its two arguments **independently**:\n\nThis is machine-checked: a standalone file restating the second axiom derives $\\bot$ from it in four lines, with the axiom audit confirming that the derivation rests on nothing else.\n\nThe containment was not by design: the file had never compiled at all, and content-block Lean siblings sit outside the paper package's build globs, so nothing had ever checked it.\n\nThe removed axioms were headed as external results of von Koch and of Weil." },
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
