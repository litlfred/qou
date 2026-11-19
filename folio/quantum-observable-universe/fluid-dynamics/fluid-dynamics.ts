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
        "madelung-acoustic-metric",
        "madelung-divisor-topology",
        "hamilton-jacobi-phase",
        "q-navier-stokes",
        "q-navier-stokes-archimedean",
        "q-ns-properties",
        "q-metric-contact-deformation",
        "geodesic-vortices",
        "two-vortex-channel-algebra",
        "two-vortex-scattering-channels",
        "braid-fluid",
        "braid-fluid-table-data",
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
        // Detangler R3 (2026-05-23): 6-row classical-vs-q-deformed
        // correspondence table extracted from vortex-intensity-modes.md.
        "vortex-intensity-modes-table-data",
        "discrete-vortex-spectrum",
        "discrete-vortex-spectrum-novelty",
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
        "kelvin-dispersion-derivation-steps",
        "kelvin-dispersion-derivation-interpretation",
        "kelvin-classical-limit",
        "acoustic-horizon-conditions",
        "acoustic-horizon-thermodynamics",
        "acoustic-horizon-conditions-interpretation",
        "acoustic-gravitational-emergence",
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
        "p1-spectral-sobolev-proof",
        "quantum-peter-weyl",
        "quantum-peter-weyl-proof",
        "quantum-peter-weyl-interpretation",
        "p1-nonlinear-uniqueness",
        "p1-nonlinear-uniqueness-novelty",
        "q-ns-proof-details",
      ],
    }),

    // ── §3. The NS obstruction ───────────────────────────────────────
    // ── §3. The NS obstruction (2026-05-19 split): 19-block section
    //   split into 2 sub-sections following the statement → tower
    //   pedagogy. The existing ns-obstruction-intro stays at the top
    //   of the statement sub-section as the umbrella narrative.
    //   Densities 11/8, both within the 3-18 band; chapter's 41%
    //   cross-section ratio finding drops mechanically.

    // §3a — NS obstruction: statement and observability
    section({
      title: "NS obstruction: statement and observability",
      label: "sec:ns-obstruction-statement",
      blocks: [
        "ns-obstruction-intro",
        "observability-in-fluid-context",
        "observability-independent-motivation",
        "observability-independent-motivation-table-data",
        "substrate-line-bundle",
        "substrate-line-bundle-base-not-fibre",
        "substrate-gm-torsion",
        "observability-q-independent",
        "observability-q-independent-proof",
        "core-levi-form",
        "core-levi-interpretation",
        "ns-regular-qou",
        "ns-obstruction",
        "ns-obstruction-remark",
        "ns-obstruction-spectral-gap",
        "ns-classical-formulation",
      ],
    }),

    // §3b — NS obstruction tower, specialisations, and observable MTC
    section({
      title: "NS obstruction tower, specialisations, and observable MTC",
      label: "sec:ns-obstruction-tower-mtc",
      blocks: [
        "intro-ns-obstruction-tower-mtc",
        "ns-obstruction-tower",
        "ns-obstruction-tower-summary",
        "ns-obstruction-computation",
        "ns-obstruction-computation-asymptotic",
        "ns-obstruction-computation-interpretation",
        "ns-kummer-specialisation",
        "ns-kummer-specialisation-consequence",
        "ns-singularity-descartes",
        "ns-singularity-descartes-proof",
        "ns-singularity-descartes-interpretation",
        "torus-ns-regular",
        "torus-ns-regular-table-data",
        "reeb-beltrami-regular-flow",
        "reeb-beltrami-regular-flow-proof",
        "reeb-beltrami-regular-flow-scope",
        "root-of-unity-truncation",
        "root-of-unity-truncation-interpretation",
        // ── Observable MTC / anyons (Track B) ──────────────────────
        "observable-mtc",
        "observable-mtc-remark",
        "observable-mtc-braiding",
        "bn-mtc-action",
        "bn-mtc-action-proof",
      ],
    }),

    // ── §4. Approaches and open problems ──────���──────────────────────
    section({
      title: "Approaches and open problems",
      label: "sec:ns-approaches",
      blocks: [
        "ns-approaches-intro",
        "qns-unit-layers",
        "qns-shell-tail-collapse",
        "qns-shell-tail-collapse-interpretation",
        "regularity-breakdown",
        "regularity-breakdown-table-data",
        "p2-critical-exponent",
        "ns-surreal-bound",
        "p4-universality",
        "p4-universality-argument",
        "p4-universality-interpretation",
        "p5-counterexample",
        "q-aubin-lions",
        "q-bkm-criterion",
        "q-bkm-criterion-interpretation",
        "vorticity-lower-bound",
        "vorticity-lower-bound-argument",
        "levi-degeneracy-conjecture",
        "crow-approach-amplification",
        "townsend-biot-savart-strain",
        "hyperbolic-overlap-saturation",
        "leray-profile",
        "leray-profile-construction",
        "q-ns-research-programme",
        "outro-fluid-dynamics",
      ],
    }),
  ],
});
