import { chapter, section } from "../../schema/builders";

/**
 * Chapter 20 — Measurement and Observation.
 *
 * Quantum measurement is realised in the QOU framework as the
 * fibre-functor $\tau$ extracting a complex vector space from the
 * categorical state. Measurement, decoherence, and the projective
 * collapse postulate are all consequences of how $\tau$ interacts
 * with the rigid-braided substrate; the chapter develops these as
 * categorical statements rather than additional postulates.
 *
 * Part IV chapter (Dynamics, Information, and Emergence). Consolidates
 * ~200 blocks of measurement / decoherence / fibre-functor content
 * currently scattered across braids-and-knots, observations,
 * information-theory, and the surreal-number appendix.
 *
 * Phase 6 scaffold (2026-05-25): chapter directory + manifest exist but
 * blocks not yet migrated.
 */
export default chapter({
  title: "Measurement and Observation",
  label: "chap:measurement-observation",
  sections: [
    section({
      title: "Introduction",
      label: "sec:measurement-observation-intro",
      blocks: ["intro"],
    }),
    section({
      title: "Bundle Structure and Observation",
      label: "sec:bundle-observation",
      blocks: [
        "bundle-observation-intro",
        "quarks-borromean-picture",
        "bundle-initial-conditions",
        "observation-braid",
        "sorting-color-energy",
        "sorting-color-energy-proof",
        "sorting-color-energy-table-data",
        "bundle-isotopy-equivalence",
        "torsion-knot-flow",
        "bundle-category",
        "outro-measurement-observation",
      ],
    }),
  ],
});
