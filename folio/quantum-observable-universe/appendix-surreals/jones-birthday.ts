import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c) — but, unlike its file-mates, **this conjecture " +
        "does not itself use $\\mathbb{R}$**, and the distinction is worth " +
        "recording rather than papering over. `JonesBirthday K` is stated " +
        "as `[SurrealField K]` with the single field " +
        "`knot_inhabited : Nonempty Knot`; no real number appears in it. Nor " +
        "does the refinement it names need one: the grading is by " +
        "`SurrealField.birthday : K → Ordinal`, so the intended invariant " +
        "$\\tilde J$ is indexed by ordinals, which is combinatorial rather " +
        "than archimedean. The two ingredients that would be needed to state " +
        "the strict-refinement claim in full — `JonesPolynomial : Knot → ℕ → K` " +
        "and a refinement predicate — are likewise real-free.\n\n" +
        "The archimedean placement is therefore *inherited* twice over, and " +
        "both routes are real. First, the class binder: `SurrealField` is " +
        "declared as `Field K, LinearOrder K, IsStrictOrderedRing K` plus a " +
        "distinguished embedding `ofReal : ℝ →+* K`, so every statement in " +
        "the appendix sits over an $\\mathbb{R}$-algebra even when it never " +
        "writes an $\\mathbb{R}$. Second, the file: " +
        "`QOU/AppendixSurreals/Conjectures.lean` is shared with conjectures " +
        "that genuinely are archimedean — `KashaevSurreal` " +
        "(`Real.pi`, `standardPart : K → ℝ`, `HyperbolicVolume : Knot → ℝ`), " +
        "`surrealLog`/`surrealExp` defined through `Real.log`/`Real.exp`, " +
        "`classicalLimit` on `ℝ → ℝ`, and the Hahn-series substrate's " +
        "$\\exists\\,\\alpha : \\mathbb{N} \\to \\mathbb{R}$. Splitting the " +
        "ordinal-graded conjectures out into their own file would be the " +
        "§7c-clean placement; it is a move across the whole appendix, not " +
        "something this block should do alone, so it is recorded here " +
        "instead. Per AGENTS.md §7ab the surreal layer is Language-tier " +
        "bookkeeping either way.",
      see: "folio/quantum-observable-universe/lean/QOU/AppendixSurreals/Conjectures.lean",
    },
  ],
  label: "conj:jones-birthday",
  title:
    "Birthday refinement of the Jones polynomial",
  lean: { ref: "qou:QOU.AppendixSurreals.JonesBirthday", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "jones-polynomial",
    "birthday",
    "knot-invariant",
    "refinement",
    "open-problem",
  ],
  uses: ["prop:hoefsmit-is-surreal-construction"],
  cites: ["gonshor1986"],
});
