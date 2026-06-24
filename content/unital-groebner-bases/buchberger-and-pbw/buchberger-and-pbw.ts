import { chapter, section } from "../../schema/builders";

/**
 * Chapter 2: Buchberger's Theorem and PBW.
 *
 * A version of Buchberger's criterion over commutative ground rings,
 * with the Poincaré–Birkhoff–Witt theorem as a corollary.
 */
export default chapter({
  title: "Buchberger's Theorem and the PBW Corollary",
  label: "chap:ugb-buchberger",
  sections: [
    section({
      title: "S-polynomial cancellation",
      label: "sec:ugb-s-poly-cancel",
      blocks: [
        "s-polynomial-decomposition",
        "s-polynomial-decomposition-proof",
      ],
    }),
    section({
      title: "Buchberger's theorem over $R$",
      label: "sec:ugb-buchberger",
      blocks: [
        "buchberger-theorem",
        "buchberger-theorem-proof",
      ],
    }),
    section({
      title: "Jet-stratified reduction",
      label: "sec:ugb-jet-stratified",
      blocks: [
        "jet-stratified-reduction",
      ],
    }),
    section({
      title: "The PBW theorem over a commutative ring",
      label: "sec:ugb-pbw",
      blocks: [
        "pbw-corollary",
        "pbw-corollary-proof",
      ],
    }),
  ],
});
