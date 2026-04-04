import { chapter, section } from "../../schema/builders";

/**
 * Chapter 10: Fluid Dynamics of the Brane.
 *
 * The brane of a quantum observable universe carries a natural fluid
 * dynamics whose viscosity, vortex spectrum, and turbulence structure
 * are determined by the substrate parameter q.  Three sections:
 * (1) the brane fluid and its q-deformed hydrodynamics,
 * (2) global regularity of the q-NS system for q > 1,
 * (3) the NS obstruction — a categorical invariant that determines
 *     whether the classical (q = 1) Navier–Stokes equation admits
 *     finite-time blowup.
 */
export default chapter({
  number: 7,
  title: "Fluid Dynamics of the Brane",
  label: "chap:fluid-dynamics",
  sections: [
    // ── §1. The brane fluid ──────���───────────────────────────────────
    section({
      title: "The brane fluid",
      label: "sec:brane-fluid",
      blocks: [
        "brane-fluid",
        "madelung-fluid",
        "hamilton-jacobi-phase",
        "q-navier-stokes",
        "geodesic-vortices",
        "braid-fluid",
        "planck-reynolds",
        "vortex-intensity-modes",
        "discrete-vortex-spectrum",
        "discrete-vortex-physical",
        "helicity-conservation",
        "helicity-physical",
        "q-turbulence-spectrum",
        "q-turbulence-prediction",
        "vortex-reconnection",
        "berry-vortex-moduli",
        "kelvin-dispersion-derivation",
        "kelvin-classical-limit",
        "acoustic-horizon-conditions",
      ],
    }),

    // ── §2. Global regularity for q > 1 ────────���────────────────────
    section({
      title: "Global regularity for $q > 1$",
      label: "sec:q-ns-regularity",
      blocks: [
        "q-ns-wellposedness",
        "q-ns-proof-strategy",
        "p1-spectral-sobolev",
        "quantum-peter-weyl",
        "p1-nonlinear-uniqueness",
        "q-ns-proof-details",
      ],
    }),

    // ── §3. The NS obstruction ───────────────────────────────────────
    section({
      title: "The NS obstruction",
      label: "sec:ns-obstruction",
      blocks: [
        "observability-in-fluid-context",
        "observability-independent-motivation",
        "substrate-line-bundle",
        "substrate-gm-torsion",
        "observability-q-independent",
        "core-levi-form",
        "core-levi-interpretation",
        "ns-regular-qou",
        "ns-classical-formulation",
        "ns-obstruction-tower",
        "ns-obstruction-computation",
        "ns-kummer-specialisation",
        "ns-singularity-descartes",
        "torus-ns-regular",
        "root-of-unity-truncation",
      ],
    }),

    // ── §4. Approaches and open problems ──────���──────────────────────
    section({
      title: "Approaches and open problems",
      label: "sec:ns-approaches",
      blocks: [
        "regularity-breakdown",
        "p2-critical-exponent",
        "p3-blowup-yekutieli",
        "p4-universality",
        "p5-counterexample",
        "q-aubin-lions",
        "q-bkm-criterion",
        "vorticity-lower-bound",
        "levi-degeneracy-conjecture",
        "q-ns-research-programme",
      ],
    }),
  ],
});
