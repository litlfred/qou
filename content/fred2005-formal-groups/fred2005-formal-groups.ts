import { paper, chapterRef } from "../schema/builders";

/**
 * Integration of Skewed-Poisson Structures on Non-commutative Formal Groups
 *
 * PhD thesis by Frederick Leitner, University of Arizona, 2005.
 * Proves that a skewed-Poisson structure on a commutative formal group
 * H / F_p integrates to a non-commutative formal group G / Z_p, with
 * strong multiplicativity preserved under Gröbner–Shirshov deformation.
 */
export default paper({
  title:
    "Integration of Skewed-Poisson Structures on Non-commutative Formal Groups",
  authors: ["Frederick Leitner"],
  affiliations: ["University of Arizona"],
  date: "2005",
  abstract:
    "A skewed-Poisson structure on a commutative formal group $H / \\mathbb{F}_p$ " +
    "is shown to integrate to a non-commutative formal group $G / \\mathbb{Z}_p$ " +
    "whose distribution algebra $\\mathrm{Dist}(G)$ admits a Gröbner–Shirshov " +
    "normal-form basis.  The comultiplication (strong multiplicativity) is " +
    "preserved under the deformation at every filtration degree.  The Witt " +
    "vector lift produces a formal group over $\\mathbb{Z}_p$ reducing to $H$ " +
    "modulo $p$, and the unit-root condition on the associated F-crystal is " +
    "shown to be equivalent to integrability of the skewed-Poisson structure.",
  macros: {},
  chapters: [
    chapterRef({ dir: "formal-groups-chapter" }),
  ],
});
