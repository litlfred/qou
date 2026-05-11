import { chapter, section } from "../../schema/builders";

/**
 * Chapter 8: The Algebraic Substrate.
 *
 * Five-step development: (1) Frobenius--Hopf substrate and Reeb derivation,
 * (2) unit particle as a cohomological defect, (3) spectral trace and
 * Tannaka--Krein duality, (4) geometric stability via the Weil bound,
 * (5) classical limit and the macroscopic continuum.
 */
export default chapter({
  title: "The Algebraic Substrate",
  label: "chap:algebraic-substrate",
  sections: [
    // ── §1. The Algebraic Substrate and the Reeb Derivation ─────────
    section({
      title: "The algebraic substrate and the Reeb derivation",
      label: "sec:algebraic-substrate-reeb",
      blocks: [
        "algebraic-substrate-intro",
        "substrate-preamble",
        "frobenius-hopf-substrate",
        "substrate-parameter-planck",
        "categorical-reeb-derivation",
        "reeb-flow-bridge",
        "brings-coordinate-ring",
        "magic-numbers-bring",
        "rigid-dualizing-complex",
        "rigid-dualizing-brings",
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

    // ── §3. The Spectral Trace and Tannaka--Krein Duality ────────────
    section({
      title: "The spectral trace and Tannaka--Krein duality",
      label: "sec:spectral-trace-tannaka",
      blocks: [
        "spectral-trace-intro",
        "q-von-mangoldt-function",
        "q-chebyshev-function",
        "tannaka-krein-isomorphism",
        "tannaka-krein-su2",
        "explicit-formula",
        "yekutieli-quantum-li",
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
        "geometric-rh-exposition",
        "unitary-stability",
      ],
    }),

    // ── §5. The Classical Limit and the Macroscopic Continuum ───────
    section({
      title: "The classical limit and the macroscopic continuum",
      label: "sec:classical-limit",
      blocks: [
        "classical-limit-intro",
        "motivic-substrate",
        "adelic-substrate",
        "classical-limit-functor",
        "quantum-gap-collapse",
        "classical-limit-obstruction",
        "qou-obstruction-reduction",
        // Surreal error calculus: Reeb-ε primitive and the
        // squeeze inequality that unifies the millennium problems.
        "reeb-epsilon",
        "q-from-epsilon",
        "surreal-rate-calculus",
        "surreal-squeeze",
        // Graded-Mikusiński keystone: GS-depth = Goncharov period-depth.
        "gb-depth-period-correspondence",
        // Bi-filtration H_q^(n,K): depth axis × knot axis.
        "hq-bi-filtration",
        // Joint motivic-Galois × braid-group action on the bi-filtration.
        "joint-galois-braid-action",
        // Joint action verified on figure-8 cell (self-conjugate trivial case).
        "joint-galois-braid-figure-8-verified",
        // Joint action discharged in general (disjoint structure).
        "joint-galois-braid-discharged",
        // Graded Baer-* on H_q across the depth filtration.
        "graded-baer-star-Hq",
        // Two-filtration bridge: iterated-integral depth ↔ partition GB-depth.
        "two-filtration-bridge",
        // Two-filtration bridge map verified at small partitions (n ≤ 4).
        "two-filtration-bridge-small-cases",
        // Two-filtration bridge in full generality (bar-eigenspace).
        "two-filtration-bridge-general",
        // Geometric realisation question for Cl_3(2π/5) at Bring's ζ_5.
        "cl3-zeta5-geometric-realization",
        "classical-riemann-zeta",
        "classical-riemann-hypothesis",
        "macroscopic-stability-equivalence",
        "rh-surreal-bound",
        "adelic-tate-squeeze",
        "yang-mills-surreal-bound",
        "q-birch-swinnerton-dyer",
        "bsd-surreal-bound",
        "q-collatz-conjecture",
        "collatz-contact-boundary",
        "collatz-no-cycles",
        "collatz-three-forms",
        "collatz-hausdorff-comparison",
        "q-collatz-interpretation",
        "collatz-surreal-bound",
        "p-vs-np-conjecture",
        "p-vs-np-surreal-bound",
        // Unifies the four surreal-bound remarks as graded-Mikusiński
        // std-collapse instances at different depths.
        "surreal-bounds-graded-mikusinski",
        "millennium-unification",
      ],
    }),
  ],
});
