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
    // ── §1 dissolved: algebraic-substrate-reeb (substrate parameter,
    // Reeb derivation, Frobenius-Hopf substrate, Brings coordinate ring,
    // rigid dualizing complex) moved to
    // `quantum-observable-universes/sec:algebraic-substrate-reeb`.

    // ── §2 dissolved: cohomological-defect moved to descartes-universe
    // as sec:cohomological-defect (sitting adjacent to fundamental-particles
    // where the unit particle as defect narratively belongs).

    // ── §3 + §4 dissolved: spectral-trace-tannaka + weil-bound-stability
    // moved to `q-geometric-langlands/` as
    // `sec:q-gl-spectral-trace-tannaka` and `sec:q-gl-weil-bound-stability`.

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
