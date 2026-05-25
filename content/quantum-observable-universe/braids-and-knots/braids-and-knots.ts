import { chapter, section } from "../../schema/builders";

/**
 * Chapter 3: Braids and Knots.
 *
 * Categorical origin of braiding, braid group representations,
 * SU(2)/SO(3) framework, knot groups, quantum groups, abstract hadron
 * composites and topological mass, Möbius energy, and varying Euler
 * characteristic.
 *
 * Hadron/knot/bundle blocks absorbed from lifting-and-descent §11-12 during
 * chapter restructuring (2026-03).  Proton/neutron definitions moved
 * to the Descartes chapter (Option A: nuclear binding references the
 * abstract hadron, not specific particles).
 * Fluid dynamics and information theory moved to their own chapters.
 */
export default chapter({
  title: "Braids and Knots",
  label: "chap:path-integrals-braiding",
  sections: [
    section({
      title: "Introduction",
      label: "sec:path-integrals-intro",
      blocks: [
        "intro",
      ],
    }),

    // Detangler P5 split (2026-05-23): 19-block sec:categorical-braiding
    // split into braid-action + Hecke-eigenbasis.
    section({
      title: "Categorical origin of braiding: the braid action",
      label: "sec:categorical-braiding-action",
      blocks: [
        "categorical-braiding-intro",
        "braid-action-tensor",
        "braid-action-tensor-proof",
        "why-b3",
        "categorical-boson-fermion",
        "symmetric-quotient-colour",
        "braid-base-field",
        "braid-lifting-compatibility",
      ],
    }),
    section({
      title: "Categorical braiding: Hecke quotient and knot eigenbasis",
      label: "sec:categorical-braiding-hecke-eigenbasis",
      blocks: [
        "categorical-braiding-hecke-eigenbasis-intro",
        "jones-markov-trace",
        "trm-hopf-sigma1-sq-closed-form",
        "trm-hopf-sigma1-sq-closed-form-table2-data",
        "trm-hopf-sigma1-sq-closed-form-table1-data",
        "hecke-log-decomposition-table-data",
        "hecke-algebra-from-braiding",
        "hecke-normal-form",
        "dark-vision-strand-bandwidth",
        "markov-moves-brane-tower",
        "knot-eigenbasis-complete",
        "knot-eigenbasis-complete-proof",
        "knot-exhaustiveness",
        "feynman-eigenbasis",
      ],
    }),

    section({
      title: "Braid group and symmetric group",
      label: "sec:braid-symmetric",
      blocks: [
        "braid-symmetric-intro",
        "braid-group",
        "braid-group-su2",
        "knot-notation-convention",
        "knot-notation-convention-table2-data",
        "knot-notation-convention-table1-data",
      ],
    }),

    section({
      title: "$\\mathrm{SU}(2)$ and $\\mathrm{SO}(3)$ framework",
      label: "sec:su2-so3",
      blocks: [
        "su2-so3-intro",
        "su2-basis",
        "first-order-taylor",
        // su2-generators relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "so3-generators",
        "quaternion-so3-motivation",
      ],
    }),

    section({
      title: "Braid involutions and holonomy",
      label: "sec:braid-involutions",
      blocks: [
        "braid-involutions-intro",
        // prop:lagrange-resolvent-transform moved here from
        // archimedean-universe/sec:bring-algebraic-substructure per
        // detangler P37 (2026-05-22). 6 H1 fwd-refs cleared.
        // Emits new H2 to def:brings-surface @ archimedean-universe
        // (accepted §5).
        "lagrange-resolvent-transform",
        "braid-twist-flip",
        "holonomy-trefoil",
        "rho-s3-holonomy-exposition",
      ],
    }),

    section({
      title: "The trefoil knot",
      label: "sec:trefoil-knot",
      blocks: [
        "trefoil-knot-intro",
        "trefoil-knot-group",
        "trefoil-operator-algebra",
      ],
    }),

    section({
      title: "Knot fundamental groups",
      label: "sec:knot-fundamental-groups",
      blocks: [
        "knot-fundamental-groups-intro",
        "knot-complement-group",
        "kronheimer-mrowka",
        "reducible-reps",
      ],
    }),

    section({
      title: "Universal enveloping algebras and quantum groups",
      label: "sec:enveloping-algebras",
      blocks: [
        "enveloping-algebras-intro",
        "enveloping-algebra",
        "quantum-su2",
        "q-casimir",
        "q-casimir-exists",
        "q-casimir-exists-proof",
        "q-casimir-unique",
        "q-casimir-unique-proof",
        "r-matrix-braiding-structure",
        "r-matrix-braiding",
      ],
    }),

    // ── Calibration and algebraic mass formula ──────────────────────────
    // ── Calibration and algebraic mass formula (P2 split 2026-05-19,
    //    phase 1): the 134-block sec:calibration-algebraic-mass
    //    (7.4× over the 3-18 band) split into 7 topical sub-sections
    //    following the mass-formula pedagogy: derivation → Hoefsmit
    //    & convergence → q-beta precision ladder → Archimedean
    //    realization → cyclotomic depth-3 → Hecke-Baer-star →
    //    mutant Jones falsifiability. The existing
    //    calibration-algebraic-mass-intro stays at the top of A as
    //    the umbrella narrative. Phase-1 densities 15/19/37/12/10/4/13.
    //    Section C (37) remains over the upper bound; phase-2
    //    follow-up will internal-split.

    // §C — q-beta precision ladder (PHASE-2 split 2026-05-19): the
    //   37-block sec:q-beta-precision-ladder from the phase-1
    //   calibration-algebraic-mass split is split into 3 topical
    //   sub-sections (Markov + braid-link foundations / chi-character
    //   closed-forms / Kashiwara-Jones interpretations and quantum-
    //   dilogarithm). The 12/13/12 densities all land in the 3-18 band.

    // ── Atom, isotope, and confinement levels (P1 split 2026-05-19):
    //    the 43-block sec:atom-isotope-confinement is split into six
    //    topical sub-sections following the natural pedagogy:
    //    energy → confinement → pair production → particles & shells →
    //    atoms & isotopes → magic shells. The existing
    //    atom-isotope-confinement-intro stays at the top of A and
    //    previews all six sub-sections as an umbrella narrative.

    // ── Nuclear binding and beta stability ──────────────────────────────
    // ── Nuclear binding and beta stability (P2 split 2026-05-19,
    //    phase 1): the paper's largest section (sec:nuclear-binding-
    //    beta-stability, 134 blocks, 7.4× over the 3-18 band) split
    //    into 7 topical sub-sections following the substrate-binding
    //    pedagogy: setup → LP-dual → phi_q/Markov/Schur-Weyl tower →
    //    GS axiomatic backing → Frobenius nuclear structure →
    //    Plancherel/alpha/ribbon → alpha_k/Wenzl bridge. The
    //    existing nuclear-binding-beta-stability-intro stays at the
    //    top of A as the umbrella narrative for the whole 7-section
    //    arc. Densities 12/9/18/6/27/18/46. Sections E (27) and G
    //    (46) remain over the upper bound; phase 2 follow-up will
    //    apply internal splits to each.

    // §E — Frobenius nuclear structure (PHASE-2 split 2026-05-19):
    //   the 27-block sec:frobenius-nuclear-structure from the phase-1
    //   nuclear-binding split is split into 2 sub-sections: parity-
    //   classification-and-discrepancy (~12) and spectral-sequence-
    //   chirality-and-confinement (~15). Both within the 3-18 band.

    // §G — alpha_k derivation, Wenzl bridge, beta stability (PHASE-2
    //   split 2026-05-19): the 43-block sec:alpha-k-wenzl-bridge from
    //   the phase-1 nuclear-binding split is split into 4 sub-sections:
    //   alpha_k procedure (~9) / Wenzl bridge & cyclotomic (~13) /
    //   crystal & isospin & chirality (~9) / beta-stability closure
    //   (~12). All within the 3-18 band.

    // §G2 — Wenzl bridge, cyclotomic factorisation, and explicit alpha_k
    section({
      title: "Wenzl bridge, cyclotomic factorisation, and explicit $\\alpha_k$",
      label: "sec:wenzl-bridge-cyclotomic",
      blocks: [
        "intro-wenzl-bridge-cyclotomic",
        "y-lambda-cyclotomic-factorization",
        "y-lambda-recipe-from-partition",
        "graded-hecke-energy-truncation-bound",
        "graded-hecke-energy-truncation-bound-table-data",
        "descent-rate-probe-sim",
        "multi-level-jet-sum-sim",
        "macdonald-hook-telescope",
        "demazure-fiber-markov-trace",
        "wenzl-bridge-applicability-qou",
      ],
    }),
    section({
      title: "Wenzl bridge, cyclotomic factorisation, and explicit $\\alpha_k$ : generation",
      label: "sec:wenzl-bridge-cyclotomic-lr-tensor-character",
      blocks: [
        "wenzl-bridge-cyclotomic-lr-tensor-character-intro",
        "lr-tensor-character-bridge",
        "wenzl-qmn-synergy",
        "explicit-alpha-k-h3",
        "explicit-alpha-k-h4",
        "wedderburn-bratteli-recursion",
        "y-lambda-sign-pattern",
        "terms-2-6-higher-operations",
        "terms-2-6-higher-operations-table2-data",
        "terms-2-6-higher-operations-table1-data",
      ],
    }),

    // §G3 — Six-term, crystal, isospin, and chirality
    section({
      title: "Six-term mass formula, crystal, isospin, and chirality",
      label: "sec:six-term-crystal-isospin-chirality",
      blocks: [
        "intro-six-term-crystal-isospin-chirality",
        "six-term-mass-formula-complete",
        "six-term-mass-formula-complete-table-data",
        "six-term-per-derivation-weights",
        "six-term-per-derivation-weights-table1-data",
        "six-term-per-derivation-weights-table2-data",
        "six-term-per-derivation-weights-table3-data",
        "crystal-isospin-degeneracy",
        "crystal-isospin-degeneracy-table-data",
        "isospin-mass-split-em-localisation",
      ],
    }),
    section({
      title: "Six-term mass formula, crystal, isospin, and chirality : generation",
      label: "sec:six-term-crystal-isospin-chirality-option-e-isospin",
      blocks: [
        "six-term-crystal-isospin-chirality-option-e-isospin-intro",
        "option-e-isospin-test",
        "crystal-bases-path-a",
        "crystal-bases-path-a-table3-data",
        "crystal-bases-path-a-table2-data",
        "crystal-bases-path-a-table1-data",
        "chirality-dual-space-derivation",
        "chirality-dual-space-derivation-table3-data",
        "chirality-dual-space-derivation-table2-data",
        "chirality-dual-space-derivation-table1-data",
        "frobenius-antipode-unifies-chirality-and-tower",
      ],
    }),

    // §G4 — Beta stability closure
    section({
      title: "Beta stability closure",
      label: "sec:beta-stability-closure",
      blocks: [
        "intro-beta-stability-closure",
        "deuteron-first-principles",

        "deuteron-first-principles-table1-data",
        "deuteron-first-principles-table2-data",
        "deuteron-first-principles-table3-data",
        "deuteron-first-principles-table4-data",
        "markov-pair-z2",
        "pentagon-uv-commutation",
        "descended-level-zero",
        "jet-tower-convergence",
        "delta-max-uniform-bound",
        "mass-tower-syt-cells",
        "energy-scale-planck",
        "topological-mass-trefoil",
        "skein-binding-lagrangian",
        "beta-stability",
        "beta-stability-interpretation",
      ],
    }),

    // ── Derivation audit and pre-Archimedean framework ────────────────
    section({
      title: "Pre-Archimedean Derivation Chain and Audit",
      label: "sec:derivation-audit",
      blocks: [
        "derivation-audit-intro",
        "pre-archimedean-derivation-chain",
        "pre-archimedean-derivation-chain-table2-data",
        "pre-archimedean-derivation-chain-table1-data",
        "derivation-audit-report",
        "derivation-audit-report-table2-data",
        "derivation-audit-report-table1-data",
        "conj-canonical-knot-id-sdp",
        "conj-chirality-ribbon-frobenius",
        "conj-rho-prefactor-structural",
      ],
    }),

    // ── Varying Euler + mirror bundle (merged — 2+2 blocks + genus-2) ─
    section({
      title: "Varying Euler Characteristic and the Mirror Bundle",
      label: "sec:varying-euler-mirror",
      blocks: [
        "varying-euler-intro",
        "genus-2-intro",
        // ── Commutative-limit / genus-2 Track A ─────────────────────
        "commutative-qou",
        // hyperelliptic-quintic relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "hyperelliptic-z5-classification",
        // x5-z5-automorphism relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "bring-z5-descent",
        // x5-bring-weight-identification relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "x5-bring-prym-jacobian",
        "weight-identification-consequences",
        // u1-equivariant-reduction relocated to quantum-observable-universes/ (PR #823 fit-section-chapter audit)
        "u1-phase-tube",
        // ── Mirror bundle ───────────────────────────────────────────
        "descent-mirror-intro",
        "e-minus-one",
      ],
    }),

    // ── Classical limit and the macroscopic continuum ─────────────────
    // Absorbed from former `algebraic-substrate / sec:classical-limit`
    // (now dissolved). The classical-limit machinery (motivic + adelic
    // substrate, joint Galois-braid action, two-filtration bridge,
    // classical Riemann zeta / RH statement) is heavy braid-coupled
    // (32 uses → braids, 13 reverse) and belongs adjacent to the rest
    // of the braid content.
    //
    // NOTE: surreal-bound formalism (BSD, Collatz, P-vs-NP, RH,
    // Yang-Mills surreal bounds + millennium-unification + the
    // graded-Mikusiński unification remark) is in
    // `appendix-surreals/sec:millennium-bounds-via-surreals`, joining
    // the rest of the surreal-formalism story. Cheat-sheet remark for
    // first-time surreal notation should sit at the head of this
    // section's surreal-flavored sub-block (reeb-epsilon / q-from-epsilon).
    // Detangler P11 split (2026-05-22): the 23-block
    // sec:classical-limit was split into construction (the
    // functor + obstruction + joint-Galois-braid machinery) and
    // implications (graded Baer-star + two-filtration bridge +
    // classical zeta/RH + adelic squeeze + chapter outro). Each
    // new section sits in the 3-18 block band.
    section({
      title: "Classical limit: construction",
      label: "sec:classical-limit-construction",
      blocks: [
        "classical-limit-intro",
        "adelic-substrate",
        "classical-limit-functor",
        "quantum-gap-collapse",
        "classical-limit-obstruction",
        "qou-obstruction-reduction",
        "qou-obstruction-reduction-table4-data",
        "qou-obstruction-reduction-table3-data",
        "qou-obstruction-reduction-table2-data",
        "qou-obstruction-reduction-table1-data",
        // Surreal error calculus (substrate-level — see appendix
        // for the full surreal formalism). The cheat-sheet remark
        // immediately below is for first-time readers of $\omega$
        // and $\varepsilon$ notation; it points to app:surreals
        // for the Conway construction, sign sequences, standard-part
        // functor, etc.
        "surreal-notation-cheat-sheet",
        "surreal-notation-cheat-sheet-table-data",
        "reeb-epsilon",
        "q-from-epsilon",
        // Graded-Mikusiński / joint-Galois-braid machinery.
        // (conj:gb-depth-period-correspondence moved earlier to
        // sec:archimedean-realization-kashaev per detangler P35;
        // its downstream consumers here now reference it backward.)
        "hq-bi-filtration",
        "joint-galois-braid-action",
        "joint-galois-braid-figure-8-verified",
        "joint-galois-braid-discharged",
      ],
    }),
    section({
      title: "Classical limit: implications",
      label: "sec:classical-limit-implications",
      blocks: [
        "classical-limit-implications-intro",
        "graded-baer-star-Hq",
        "two-filtration-bridge",
        "two-filtration-bridge-small-cases",
        "two-filtration-bridge-small-cases-table-data",
        "two-filtration-bridge-general",
        "two-filtration-bridge-general-table-data",
        "cl3-zeta5-geometric-realization",
        // Classical (q = 1) zeta + RH statement.
        "classical-riemann-zeta",
        "classical-riemann-hypothesis",
        "macroscopic-stability-equivalence",
        // Adelic Tate squeeze — surreal-bound infrastructure used
        // by the appendix-surreal Millennium bounds; lives here as
        // the bridge to those bounds.
        "adelic-tate-squeeze",
        "outro-braids-and-knots",
      ],
    }),
  ],
});
