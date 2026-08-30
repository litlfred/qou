import { conjecture } from "../../schema/builders";

/**
 * Conjectural bridge from the S₅-isotypic decomposition of L²(M, Ω) to the
 * Askey scheme of orthogonal polynomials.
 *
 * The global states are indexed by partitions of 5. The claim is about what
 * they look like LOCALLY: projected into coordinate patches near the cone's
 * singularities, they should approximate the classical orthogonal families —
 * Bessel in the radial regime, Hermite where the local geometry is quadratic.
 *
 * Conjectural. No local model has been computed, and nothing downstream
 * depends on it.
 */
export default conjecture({
  label: "conj:tetraplectic-askey-localisation",
  title:
    "Local Askey-scheme approximation of the $S_5$-isotypic states on the Bring cone",
  uses: ["def:bring-cone-tetraplectic-structure"],
  cites: ["askey1989qhermite", "foth2002"],
  tags: [
    "tetraplectic",
    "askey-scheme",
    "orthogonal-polynomials",
    "bring-cone",
    "open-problem",
    "conjectural-framing",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**Framing, not a result, and nothing in the corpus consumes it.** " +
        "Promoted from the exposition `bring_tetraplectic.md` §2, which " +
        "already labelled it a conjecture. Making it checkable would mean " +
        "writing the local model at one singularity of $C(\\mathcal{B})$ and " +
        "computing the leading behaviour of one isotypic component there — " +
        "not done.",
    },
  ],
});
