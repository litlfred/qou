import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "**Conditional on the Wigner axiom since 2026-09-15.** The block formerly wrote the universal obstruction class as `chi(A) in HH^2 ~ k` and called it \"a single integer\". Under the 2026-09-15 analysis (`docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md` §2.4) the one-dimensionality of `HH^2` is not a consequence of the QOU axioms — at `q = 1` Whitehead's lemma gives `HH^2(U(g), M) = 0` — so it is now the named hypothesis `conj:wigner-axiom`, the class is written `w(A)`, and the integer is `chi_eu(M_0)`, the Euler characteristic of the base curve.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:skein-resolution-obstruction",
  title:
    "Skein resolution obstruction $\\kappa_c^{\\mathrm{comp}}(L, q)$",
  tags: [
    "obstruction",
    "yekutieli",
    "skein-resolution",
    "computational-horizon",
    "P-vs-NP",
    "q-dependent",
    "cohomology",
  ],
  lean: { ref: "qou:QOU.SkeinResolutionObstruction",
    validation: "not_checked",
  },
  // Detangler forward-ref demote (bean foxn): def:computational-horizon
  // (information-theory, a later chapter) is a thematic link, not a logical
  // dependency — the .md defines κ_c^comp self-containedly via χ(A) + Kummer
  // reduction and never references it. Dropped the spurious forward edge.
  uses: [
    "conj:wigner-axiom",
    "thm:qou-obstruction-reduction",
    "rem:kummer-filtration-obstruction",
    "prop:ns-obstruction-tower",
  ],
});
