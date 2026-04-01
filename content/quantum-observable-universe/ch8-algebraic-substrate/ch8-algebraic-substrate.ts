import { chapter, section } from "../../schema/builders";

/**
 * Chapter 8: The Algebraic Substrate.
 *
 * Five-step development: (1) Frobenius-Hopf substrate and Reeb derivation,
 * (2) unit particle as a cohomological defect, (3) spectral trace and
 * Tannaka-Krein duality, (4) geometric stability via the Weil bound,
 * (5) classical limit and the macroscopic continuum.
 */
export default chapter({
  number: 8,
  title: "The Algebraic Substrate",
  label: "chap:algebraic-substrate",
  sections: [
    // ── §1. The Algebraic Substrate and the Reeb Derivation ─────────
    section({
      title: "The algebraic substrate and the Reeb derivation",
      label: "sec:algebraic-substrate-reeb",
      blocks: [
        "substrate-preamble",
        "frobenius-hopf-substrate",
        "substrate-parameter-planck",
        "categorical-reeb-derivation",
        "brings-coordinate-ring",
        "rigid-dualizing-complex",
        "substrate-self-duality",
      ],
    }),

    // ── §2. The Unit Particle as a Cohomological Defect ─────────────
    section({
      title: "The unit particle as a cohomological defect",
      label: "sec:cohomological-defect",
      blocks: [
        "cohomological-defect-intro",
        "levi-form-defect",
        "maximal-ideal-defect",
        "local-cohomology-group",
        "unit-particle-state",
        "topological-charge-quantization",
        "defect-legendrian-knot",
      ],
    }),

    // ── §3. The Spectral Trace and Tannaka-Krein Duality ────────────
    section({
      title: "The spectral trace and Tannaka--Krein duality",
      label: "sec:spectral-trace-tannaka",
      blocks: [
        "spectral-trace-intro",
        "q-von-mangoldt-function",
        "q-chebyshev-function",
        "tannaka-krein-isomorphism",
        "explicit-formula",
      ],
    }),

    // ── §4. Geometric Stability via the Weil Bound ──────────────────
    section({
      title: "Geometric stability via the Weil bound",
      label: "sec:weil-bound-stability",
      blocks: [
        "weil-bound-intro",
        "local-q-zeta-function",
        "hasse-weil-bound",
        "spectral-half-line",
        "unitary-stability",
      ],
    }),

    // ── §5. The Classical Limit and the Macroscopic Continuum ───────
    section({
      title: "The classical limit and the macroscopic continuum",
      label: "sec:classical-limit",
      blocks: [
        "classical-limit-intro",
        "classical-limit-functor",
        "quantum-gap-collapse",
        "classical-riemann-zeta",
        "classical-riemann-hypothesis",
        "macroscopic-stability-equivalence",
      ],
    }),
  ],
});
