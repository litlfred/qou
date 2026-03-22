import { chapter, section } from "../../schema/builders";

/**
 * Chapter 6: The Descartes Universe.
 *
 * The Descartes condition χ(A) = −6, its implications for the genus-4
 * base curve, chirality, colour sectors, braid-group structure, and
 * the Descartes theorem identifying Bring's surface as a terminal object.
 */
export default chapter({
  number: 6,
  title: "The Descartes Universe",
  label: "chap:descartes",
  sections: [
    section({
      title: "The Descartes condition",
      label: "sec:descartes-condition",
      blocks: [
        "descartes-condition",
        "descartes-calabi-yau",
        "descent-one-dim",
        "genus-maximal-descent",
        "genus-maximal-descent-proof",
      ],
    }),

    section({
      title: "Leptons and chirality",
      label: "sec:descartes-leptons-chirality",
      blocks: [
        "descartes-leptons",
        "descartes-chirality",
        "light-cone-affine",
      ],
    }),

    section({
      title: "Trefoil subgroups and Bring's curve",
      label: "sec:trefoil-brings",
      blocks: [
        "chirality-trefoil",
        "brings-curve",
      ],
    }),

    section({
      title: "Colour-sector coordinates on the exceptional fibre",
      label: "sec:colour-sector-coords",
      blocks: [
        "exceptional-divisor",
        "chiral-sector-coords",
      ],
    }),

    section({
      title: "Categorical braid structure",
      label: "sec:descartes-braid",
      blocks: [
        "descartes-braid-structure",
        "descartes-braid-structure-proof",
        "skein-archimedean-shadow",
      ],
    }),

    section({
      title: "The Descartes theorem",
      label: "sec:descartes-theorem",
      blocks: [
        "descartes",
        "descartes-proof",
        "universality-general",
        "descartes-yekutieli",
        "observation-brings",
      ],
    }),
  ],
});
