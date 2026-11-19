import { chapter, section } from "../../schema/builders";

/**
 * Chapter 10: The Eightfold Way and Flavor Structure.
 *
 * Derives SU(3) flavor symmetry from QOU's three-strand braiding,
 * classifies the particles defined in Ch 9 (Knots, Particles, and
 * Confinement) into Eightfold Way multiplets, and connects
 * q-deformation to hyperbolic geometry and mass splitting.
 *
 * ANTI-FITTING DISCIPLINE: every claim in this chapter must trace
 * to QOU's categorical axioms. External papers (Gang–Yonekura,
 * Asselmeyer-Maluga, Klein-Kreisler et al.) provide evidence and
 * cross-checks, never axioms. Where external results align with
 * QOU derivations, state both the QOU derivation and the agreement.
 * Where they diverge, state the divergence honestly.
 *
 * Dependencies: Ch 6 (Braids and Knots), Ch 7 (Bring's Surface),
 * Ch 9 (Knots, Particles, and Confinement).
 *
 * New chapter created as part of the eightfold-way-chapter-2026-08-03
 * restructure.
 */
export default chapter({
  title: "The Eightfold Way and Flavor Structure",
  label: "chap:eightfold-way",
  sections: [
    // ── §1. The A₂ root system from three-strand braiding ────────
    // Derive the A₂ Lie algebra structure from H₃(q). The 6 roots
    // at 120° angles arise from the 3-strand Artin generators and
    // their Hecke relations.
    section({
      title: "The $A_2$ root system from three-strand braiding",
      label: "sec:a2-root-system",
      blocks: [
        "eightfold-intro",
        "a2-from-three-strands",
        // TODO: a2-root-system-proof, hexagonal-weight-lattice,
        // weyl-group-symmetry (Phase 2 continuation)
      ],
    }),

    // ── §2. Flavor representations and charge assignments ────────
    // The fundamental triplet 3 from unknot variants, the conjugate
    // 3̄, and the charge assignments (isospin, hypercharge).
    section({
      title: "Flavor representations and charge assignments",
      label: "sec:flavor-representations",
      blocks: [
        "flavor-charge-assignments",
        // Cross-chapter references (blocks live in SM appendix):
        // conj:sm-hypercharge-invariant — used via flavor-charge-assignments
        // rem:strand-twist-datum — referenced as candidate Y data
      ],
    }),

    // ── §3. The meson octet via tensor decomposition ─────────────
    // Derive 3 ⊗ 3̄ = 8 ⊕ 1 from the ⊗_K product. Construct
    // the 8 meson states on the hexagonal weight lattice.
    section({
      title: "The meson octet via tensor decomposition",
      label: "sec:meson-octet",
      blocks: [
        "meson-octet-decomposition",
        "meson-mass-splitting",
        // The vector nonet. Placed after the GMO null result it contrasts
        // with, so both uses[] edges run backward. Takes this section from
        // 2 to 3 blocks, into the detangler 3-18 band.
        "vector-meson-nonet",
      ],
    }),

    // ── §4. Baryon multiplets and the Borromean decuplet ─────────
    // Derive 3⊗3⊗3 = 10⊕8⊕8⊕1 from the three-fold ⊗_K product.
    // The symmetric channel yields the decuplet; the Borromean
    // baryon (def:borromean-baryon from Ch 9) provides the
    // structural realization.
    section({
      title: "Baryon multiplets and the Borromean decuplet",
      label: "sec:baryon-multiplets",
      blocks: [
        "schur-weyl-eightfold",
        "borromean-decuplet-derivation",
        // The N = 2 Delta quartet with its faithful 2I3 labelling (owner
        // decision 5b, bean qou-nmib). Not gated on N = 3. Placed after the
        // decuplet it contrasts with; its one uses[] edge (schur-weyl-eightfold)
        // runs backward. 5 -> 6 blocks, inside the band.
        "delta-quartet-isospin-ladder",
        // The equal-spacing / Omega-minus null result. Placed after the
        // decuplet block it interprets, so the edge runs backward. Takes
        // this section from 2 to 3 blocks, into the detangler 3-18 band.
        "decuplet-equal-spacing",
        // U-spin / Coleman–Glashow, the third null result. Placed after
        // both blocks it uses, so every uses[] edge runs backward. Takes
        // this section 3 -> 4, still inside the band. Also gives the
        // baryon octet its first real content (qou-7lio).
        "u-spin-coleman-glashow",
        // The octet itself: decomposition, weight table, and the weight-map
        // degeneracy — the one CONTENT-BEARING result of the family (a
        // weight-only mass formula is structurally impossible, refuted at
        // 77 MeV). Last, so all four uses[] edges run backward. 4 -> 5
        // blocks, inside the band. Closes qou-wd07.
        "baryon-octet-decomposition",
      ],
    }),

    // ── §5. Color algebra from octonionic stabilization ──────────
    // Derive the color SU(3) gauge symmetry from the octonionic
    // automorphism group G₂ → SU(3) stabilizer action.
    section({
      title: "Color algebra from octonionic stabilization",
      label: "sec:color-algebra",
      blocks: [
        "octonion-algebra",
        "octonion-algebra-remark",
        "color-su3-from-g2",
        // SU(N) framing of sigma: color factors (bean qou-sl3f, PR #7830)
        "sl-n-color-framing",
        "sl-n-color-frame-scope",
        // Cross-chapter references (blocks live in SM appendix):
        // conj:sm-colour-stabilizer-action — faithfulness of SU(3) on state space
        // TODO: color-tube-coords-intro (new block, from brings-surface)
      ],
    }),

    // ── §6. q-Deformation and the hyperbolic weight lattice ──────
    // How the substrate parameter q deforms the hexagonal weight
    // lattice: quantum Serre relations, effective angle deformation,
    // compact/non-compact root split, Thurston relaxation.
    section({
      title: "$q$-Deformation and the hyperbolic weight lattice",
      label: "sec:q-deformed-eightfold",
      blocks: [
        "q-deformation-weight-lattice",
        // TODO: thurston-relaxation (from brings-surface)
      ],
    }),

    // ── §7. The knot–particle–force dictionary ───────────────────
    // Consolidation and completeness audit of the full dictionary
    // mapping knot configurations to particles and forces.
    section({
      title: "The knot–particle–force dictionary",
      label: "sec:knot-particle-force-dictionary",
      blocks: [
        "dictionary-flavor-layer",
      ],
    }),

    // ── §8. Open problems in flavor and gauge structure ──────────
    // Consolidated ledger: three-generation structure, gauge
    // truncation summary, pointers to SM appendix.
    section({
      title: "Open problems in flavor and gauge structure",
      label: "sec:eightfold-open-problems",
      blocks: [
        "eightfold-open-problems",
      ],
    }),
  ],
});
