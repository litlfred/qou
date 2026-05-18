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
  title: "Fluid Dynamics of the Brane",
  label: "chap:fluid-dynamics",
  sections: [
    // ── §1a. q-deformed hydrodynamics ──────���───────────────────────────────────
    // (P4 split: 19-block sec:brane-fluid → 3 focused sections)
    section({
      title: "$q$-deformed hydrodynamics",
      label: "sec:q-hydrodynamics",
      blocks: [
        "fluid-dynamics-intro",
        "brane-fluid",
        "madelung-fluid",
        "hamilton-jacobi-phase",
        "q-navier-stokes",
        "q-metric-contact-deformation",
        "geodesic-vortices",
        "braid-fluid",
        "planck-reynolds",
      ],
    }),

    // ── §1b. Vortex spectrum and helicity ─────────────────────────────
    section({
      title: "Vortex spectrum and helicity",
      label: "sec:vortex-spectrum",
      blocks: [
        "vortex-spectrum-intro",
        "vortex-intensity-modes",
        "discrete-vortex-spectrum",
        "discrete-vortex-physical",
        "helicity-conservation",
        "helicity-physical",
        "vortex-reconnection",
      ],
    }),

    // ── §1c. Turbulence and acoustics ─────────────────────────────────
    section({
      title: "Turbulence and acoustics",
      label: "sec:turbulence-acoustics",
      blocks: [
        "turbulence-acoustics-intro",
        "q-turbulence-spectrum",
        "q-turbulence-prediction",
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
        "q-ns-regularity-intro",
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
        "ns-obstruction-intro",
        "observability-in-fluid-context",
        "observability-independent-motivation",
        "substrate-line-bundle",
        "substrate-gm-torsion",
        "observability-q-independent",
        "core-levi-form",
        "core-levi-interpretation",
        "ns-regular-qou",
        "ns-obstruction",
        "ns-classical-formulation",
        "ns-obstruction-tower",
        "ns-obstruction-computation",
        "ns-kummer-specialisation",
        "ns-singularity-descartes",
        "torus-ns-regular",
        "root-of-unity-truncation",
        // ── Observable MTC / anyons (Track B) ──────────────────────
        "observable-mtc",
        "bn-mtc-action",
      ],
    }),

    // ── §4. Approaches and open problems ──────���──────────────────────
    section({
      title: "Approaches and open problems",
      label: "sec:ns-approaches",
      blocks: [
        "ns-approaches-intro",
        "regularity-breakdown",
        "p2-critical-exponent",
        "p3-blowup-yekutieli",
        "ns-surreal-bound",
        "p4-universality",
        "p5-counterexample",
        "q-aubin-lions",
        "q-bkm-criterion",
        "vorticity-lower-bound",
        "levi-degeneracy-conjecture",
        "townsend-biot-savart-strain",
        "hyperbolic-overlap-saturation",
        "leray-profile",
        "q-ns-research-programme",
      ],
    }),
  ],
});
