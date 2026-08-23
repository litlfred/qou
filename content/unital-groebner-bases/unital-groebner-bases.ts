import { paper, chapterRef } from "../schema/builders";

/**
 * Unital Gröbner Bases over Arbitrary Commutative Ground Rings
 *
 * Paper by Frederick Leitner and Robert Pawloski (arXiv:math/0409565v2).
 * Proves that quotients A/I are free R-modules when I has a unital
 * Gröbner basis, and obtains PBW over commutative rings as a corollary.
 */
export default paper({
  title: "Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings",
  authors: ["Frederick Leitner", "Robert Pawloski"],
  affiliations: ["University of Arizona"],
  date: "2004-10-14",
  abstract:
    "Let $R$ be a commutative ring with unity and let $A$ be a not necessarily " +
    "commutative $R$-algebra which is free as an $R$-module.  If $I$ is an ideal " +
    "in $A$, one can ask when $A/I$ is also free as an $R$-module.  We show that " +
    "if $A$ has an admissible system and $I$ has a unital Gröbner basis then $A/I$ " +
    "is free as an $R$-module.  We prove a version of Buchberger's theorem over $R$ " +
    "and, as a corollary, we obtain a Gröbner basis proof of the " +
    "Poincaré--Birkhoff--Witt Theorem over a commutative ground ring.",
  // The three leading-term operators. Both chapter generations use them:
  // the monolith writes `\mathrm{LT}` inline, the ch0/ch1/ch2 blocks write
  // `\LT`. Defining them here makes the short form resolve (it was an
  // undefined control sequence in 8 of the newly-wired blocks) without
  // rewriting any `.md`, and both spellings then typeset identically.
  macros: {
    LM: { tex: "\\mathrm{LM}", unicode: "LM" },
    LC: { tex: "\\mathrm{LC}", unicode: "LC" },
    LT: { tex: "\\mathrm{LT}", unicode: "LT" },
  },
  chapters: [
    chapterRef({ dir: "introduction" }),
    chapterRef({ dir: "unital-groebner-bases-chapter" }),
    chapterRef({ dir: "buchberger-and-pbw" }),
  ],
});
