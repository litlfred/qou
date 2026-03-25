import { paper, chapterRef } from "../schema/builders";

/**
 * Unital Gröbner Bases over Arbitrary Commutative Ground Rings
 *
 * arXiv:math/0409565v2 [math.RA]
 */
export default paper({
  title: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings",
  authors: ["Frederick Leitner", "Robert Pawloski"],
  date: "2004-10-14",
  abstract:
    "Let $R$ be a commutative ring with unity and let $A$ be a not necessarily " +
    "commutative $R$-algebra which is free as an $R$-module. If $I$ is an ideal " +
    "in $A$, one can ask when $A/I$ is also free as an $R$-module. We show that " +
    "if $A$ has an admissible system and $I$ has a unital Gröbner basis then " +
    "$A/I$ is free as an $R$-module. We prove a version of Buchberger's theorem " +
    "over $R$ and, as a corollary, we obtain a Gröbner basis proof of the " +
    "Poincaré–Birkhoff–Witt Theorem over a commutative ground ring.",
  macros: {
    LM: { tex: "\\operatorname{LM}", unicode: "LM" },
    LC: { tex: "\\operatorname{LC}", unicode: "LC" },
    LT: { tex: "\\operatorname{LT}", unicode: "LT" },
  },
  chapters: [
    chapterRef({ dir: "ch0-introduction" }),
    chapterRef({ dir: "ch1-unital-groebner-bases" }),
    chapterRef({ dir: "ch2-buchberger-and-pbw" }),
  ],
});
