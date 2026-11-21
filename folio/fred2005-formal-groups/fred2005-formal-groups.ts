import { paper, chapterRef } from "../schema/builders";

/**
 * Non-Commutative Formal Groups in Positive Characteristic
 *
 * F. Leitner, arXiv:math/0602138 (2006), which the author identifies with
 * the 2005 University of Arizona thesis [fred2005]. Over a field of
 * characteristic p, strongly filtered, strongly multiplicative Poisson
 * structures on the splay of the distribution algebras of commutative
 * formal groups integrate to (geometric) non-commutative formal groups.
 */
export default paper({
  title: "Non-Commutative Formal Groups in Positive Characteristic",
  authors: ["Frederick Leitner"],
  affiliations: ["University of Arizona"],
  date: "2006",
  abstract:
    "Over a field $k$ of characteristic $p > 0$, the distribution algebra " +
    "$\\mathrm{Dist}(G)$ of a formal group $G$ has a Gröbner-basis presentation " +
    "in its divided-power generators. Poisson structures on the splay (free " +
    "product) of commutative algebras with internal symmetry give a PBW " +
    "theorem for the quotient $U = T/(fg - gf - \\pi(f,g))$, and strong " +
    "multiplicativity makes the comultiplication descend to $U$. For a " +
    "commutative geometric formal group $\\{H_i, H\\}$, a strongly filtered, " +
    "strongly multiplicative Poisson structure on the splay of the " +
    "$\\mathrm{Dist}(H_i)$ integrates to a geometric formal group " +
    "$\\{H_i, G\\}$ with $\\mathrm{Dist}(G) = U$.",
  macros: {},
  chapters: [
    chapterRef({ dir: "formal-groups-chapter" }),
  ],
});
