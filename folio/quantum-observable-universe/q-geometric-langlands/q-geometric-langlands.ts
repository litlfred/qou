import { chapter, section } from "../../schema/builders";

/**
 * Chapter: q-Geometric Langlands Correspondence.
 *
 * Develops the q-deformed Geometric Langlands correspondence within
 * the QOU framework.  The substrate parameter q ∈ G_m^{nt} defines a
 * G_m-family of deformations; the obstruction classes κ_n
 * and their Kummer filtration control q-flatness; the Iwahori--Hecke algebra
 * H_n(q) from Ch 4 provides q-Hecke operators; and the fibre functor
 * τ from Ch 1 mediates the automorphic–spectral equivalence via
 * Tannaka–Krein reconstruction.
 *
 * The main conjecture asserts an equivalence between q-D-modules on
 * Bun_{G_q} and QCoh on LocSys_{Ǧ_q}, well-defined on the non-torsion
 * locus of G_m.
 */
export default chapter({
  title: "$q$-Geometric Langlands Correspondence",
  label: "chap:q-geometric-langlands",
  sections: [
    // ── Introduction ─────────────────────────────────────────────────
    section({
      title: "Introduction",
      label: "sec:q-gl-intro",
      blocks: [
        "q-gl-intro",
      ],
    }),

    // ── q-Local systems and q-connections ────────────────────────────
    section({
      title: "$\\mathbb{G}_m$-torsors and $q$-local systems",
      label: "sec:q-local-systems",
      blocks: [
        "q-local-systems-intro",
        "q-local-system",
        "q-local-system-remark",
        "q-flat-connection",
        "q-flat-connection-remark",
      ],
    }),

    // ── q-Hecke correspondences ──────────────────────────────────────
    section({
      title: "$q$-Hecke correspondences",
      label: "sec:q-hecke-correspondences",
      blocks: [
        "q-hecke-correspondences-intro",
        "q-hecke-operator",
        "q-hecke-eigensheaf",
        "q-hecke-eigenvalue",
        "q-hecke-eigenvalue-proof",
      ],
    }),

    // ── The q-Geometric Langlands conjecture ─────────────────────────
    section({
      title: "The $q$-Geometric Langlands conjecture",
      label: "sec:q-gl-conjecture",
      blocks: [
        "q-gl-conjecture-intro",
        "q-langlands-dual",
        "q-oper",
        "q-gl-conjecture",
        "q-gl-obstruction-calc",
        "q-gl-obstruction-calc-proof",
        "q-gl-kummer-filtration",
        "q-gl-fiber-functor",
        "q-gl-fiber-functor-proof",
      ],
    }),

    // ── q-Opers and the spectral side ────────────────────────────────
    section({
      title: "$q$-Opers and the spectral side",
      label: "sec:q-opers",
      blocks: [
        "q-opers-intro",
        "q-oper-hecke",
        "q-oper-hecke-proof",
      ],
    }),

    // ── Classical limit and physical interpretation ──────────────────
    section({
      title: "Classical limit and physical interpretation",
      label: "sec:q-gl-classical-limit",
      blocks: [
        "q-gl-classical-limit-intro",
        "q-gl-classical-limit",
        "q-gl-classical-limit-proof",
        "q-gl-obstruction-classical-compatibility",
        "q-gl-physical-interpretation",
        "q-gl-automorphic-observability",
      ],
    }),

    // ── Spectral trace and Tannaka–Krein duality ─────────────────────
    // Absorbed from former `algebraic-substrate / sec:spectral-trace-tannaka`
    // (now dissolved). This content is foundational number-theoretic
    // material for the explicit formula and the q-Langlands automorphic
    // side; it sits naturally here rather than as an isolated chapter.
    section({
      title: "Spectral trace and Tannaka--Krein duality",
      label: "sec:q-gl-spectral-trace-tannaka",
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

    // ── Geometric stability via the Weil bound ───────────────────────
    // Absorbed from former `algebraic-substrate / sec:weil-bound-stability`
    // (now dissolved). The Hasse--Weil bound and the geometric-RH
    // statement are q-Langlands-side stability results.
    section({
      title: "Geometric stability via the Weil bound",
      label: "sec:q-gl-weil-bound-stability",
      blocks: [
        "weil-bound-intro",
        "local-q-zeta-function",
        "hasse-weil-bound",
        "hasse-weil-bound-proof",
        "spectral-half-line",
        // P3 reorder (2026-05-19): unitary-stability moved before
        // geometric-rh-exposition. unitary-stability uses
        // cor:spectral-half-line and conj:explicit-formula (both
        // already earlier); geometric-rh-exposition uses
        // unitary-stability for narrative interpretation. The
        // detangler-watcher flagged geometric-rh-exposition →
        // unitary-stability as an intra-section H1 forward ref;
        // swap makes it a backward ref, no new cascade.
        "unitary-stability",
        "geometric-rh-exposition",
      ],
    }),
    section({
      title: "$L$-values, mirror symmetry, and the quantum Langlands dual",
      label: "sec:q-geometric-langlands-orphan-reconnect",
      blocks: [
        "intro-orphan-reconnect",
        "cyclotomic-l-value-decomposition",
        "cyclotomic-l-value-decomposition-details",
        "mirror-3d-3d-correspondence",
        "modular-s-transform-q-q-tilde",
        "mutant-jones-bloch-group-intro",
        "quantum-langlands-dual",
        "outro-q-geometric-langlands",
      ],
    }),
  ],
});
