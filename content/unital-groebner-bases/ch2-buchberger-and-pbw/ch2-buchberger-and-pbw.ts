import { chapter, section } from "../../schema/builders";

/**
 * Chapter 2: Buchberger's Theorem and PBW.
 *
 * A version of Buchberger's criterion over commutative ground rings,
 * with the Poincaré–Birkhoff–Witt theorem as a corollary.
 */
export default chapter({
  number: 2,
  title: "Buchberger's Theorem and the PBW Corollary",
  label: "chap:ugb-buchberger",
  sections: [
    section({
      title: "S-polynomial cancellation",
      label: "sec:ugb-s-poly-cancel",
      blocks: [
        "s-polynomial-decomposition",
      ],
    }),
    section({
      title: "Buchberger's theorem over $R$",
      label: "sec:ugb-buchberger",
      blocks: [
        "buchberger-theorem",
      ],
    }),
    section({
      title: "The PBW theorem over a commutative ring",
      label: "sec:ugb-pbw",
      blocks: [
        "pbw-corollary",
      ],
    }),
  ],
});
