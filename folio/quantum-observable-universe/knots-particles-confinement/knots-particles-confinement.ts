import { chapter, section } from "../../schema/builders";

/**
 * Chapter 9: Knots, Particles, and Confinement.
 *
 * Pure definitional chapter: defines particles as knot configurations,
 * establishes the hadron algebra, derives the knot-particle dictionary,
 * and develops the confinement/shell hierarchy. No mass computation,
 * no nuclear binding optimization — those live in Ch 11 (Nuclear
 * Interactions and Binding) and Ch 13 (Mass Analysis).
 *
 * Dependency role: upstream of both Ch 10 (Eightfold Way — classifies
 * these particles into multiplets) and Ch 13 (Mass Analysis — computes
 * their masses).
 *
 * Split from the former particle-interactions chapter (Phase 1,
 * eightfold-way-chapter-2026-08-03).
 */
export default chapter({
  title: "Knots, Particles, and Confinement",
  label: "chap:knots-particles-confinement",
  sections: [
    // ── §1. Interactions are pairwise ────────────────────────────
    // Scope-fixing opener: the braiding is a binary datum, so every
    // many-body interaction is a word in two-strand crossings, and
    // Yang-Baxter (Reidemeister III) makes that word well defined.
    // Everything downstream in this chapter is a two-strand operator.
    section({
      title: "Interactions are pairwise",
      label: "sec:interactions-are-pairwise",
      blocks: [
        "interactions-are-pairwise-intro",
        "pairwise-interaction-decomposition",
        "pairwise-interaction-decomposition-proof",
        "two-particle-sufficiency",
      ],
    }),

    // ── §2. Nucleon derivation from pair production ──────────────
    // Defines quarks, quark-antiquark production, nucleon construction.
    // crossing-energy + coulomb-charge moved up here from the electroweak
    // triplet group 2026-08-29. The quark blocks invoke the Coulomb charge,
    // and that dependency is Lean-proved rather than decorative
    // (QOU.Braiding.CoulombCharge.value_mirror and
    // mirror_odd_neutral_neutron_forces_zero), so it is declared rather than
    // left implicit in prose. Declaring it alone added two MEDIUM H1 forward
    // refs; moving both definitions here removes those and 18 more. Both stay
    // ahead of the electroweak consumers, so decision 5 of 2026-08-09 (which
    // put them there to stop the electroweak results forward-referencing
    // their own definitions) is preserved: its constraint is an order.
    //
    // KEEP EXPLANATORY COMMENTS OUTSIDE THE BLOCK LIST, as here.
    // content-graph-analysis parses this file with regexes, not a TS parser,
    // and harvests the list with a quoted-string pattern. A comment placed
    // INSIDE the list is scanned too: an apostrophe pairs with the next one
    // and captures the text between as a phantom entry, and a closing square
    // bracket truncates the capture. Drafting this note inside the list made
    // the group report 1 real entry instead of 17, then 0, then 17 fake ones
    // that showed up as two spurious H4 findings. run-validate stays green
    // throughout, because the TypeScript is valid either way.
    section({
      title: "Nucleon derivation from pair production",
      label: "sec:nucleon-derivation",
      blocks: [
        "nucleon-derivation-intro",
        "crossing-energy",
        "crossing-energy-sign",
        "coulomb-charge",
        "coulomb-charge-channels",
        "up-quark",
        "up-quark-properties",
        "down-quark",
        "down-quark-properties",
        "quark-antiquark-production",
        "quark-antiquark-production-reduction",
        "four-term-pair-nucleon",
        "four-term-pair-nucleon-table1-data",
        "four-term-pair-nucleon-table2-data",
        "four-term-pair-nucleon-table3-data",
        "confinement-universality",
        "confinement-universality-proof",
        "derived-atom",
        "derived-atom-normal-form",
        "nucleon-from-photons-summary",
        // `gluon-stabiliser-ledger` was here on landing (2026-08-24) and moved
        // to §12 the same day — see the note there. Placed by `interprets`,
        // measured by the detangler, and the two disagree.
      ],
    }),

    // ── §3. Hadron algebra and knot factorisation ────────────────
    section({
      title: "Hadron Algebra and Knot Factorisation",
      label: "sec:hadron-algebra",
      blocks: [
        "hadron-algebra-intro",
        "hadron",
        "hadron-exists",
        "hadron-exists-proof",
        "hadron-unique",
        "hadron-unique-proof",
        "hadron-interpretation",
        "hadron-operations-closure",
        "hadron-operations",
        "knot-factorization",
        "localized-hadron",
        "hadron-fibre-embedding",
        "hadron-fibre-embedding-remark",
      ],
    }),

    // ── §4. Skein generation and particle correspondence ─────────
    section({
      title: "Skein Generation and Particle Correspondence",
      label: "sec:skein-particle-generation",
      blocks: [
        "skein-particle-generation-intro",
        "atomic-braid",
        "atomic-braid-remark",
        "atomic-braid-table1-data",
        "knot-particle-generation",
        "linking-operations",
        "knot-particle-generation-table-data",
        "knot-particle-generation-consequences",
        // Merged from the former auto-split "Skein Generation and
        // Particle Correspondence : generation" (small base,
        // strongly-related continuation — the knot-particle dictionary;
        // reorg policy: strongly-related -> merge).
        "skein-particle-generation-knot-particle-generation-intro",
        "knot-particle-generation-interpretation",
        "knot-particle-correspondence",
        "knot-particle-correspondence-hadron-reading",
        "knot-particle-dictionary",
        "knot-particle-dictionary-table1-data",
        "knot-particle-dictionary-table2-data",
        "knot-particle-dictionary-table3-data",
        "knot-particle-dictionary-table4-data",
        "interaction-sector-taxonomy",
        "interaction-sector-taxonomy-remark",
        "fusion-process",
        "fusion-process-remark",
        "binding-knots-visual-inventory",
        "binding-knots-visual-inventory-table2-data",
        "binding-knots-visual-inventory-table1-data",
      ],
    }),

    // ── §5. Borromean baryons and Reidemeister invariance ─────────
    section({
      title: "Borromean Baryons and Reidemeister Invariance",
      label: "sec:borromean-reidemeister",
      blocks: [
        "borromean-reidemeister-intro",
        "borromean-baryon",
        "borromean-topological-confinement",
        "brunnian-property-of-borromean",
        "delta-skein-substrate-identity",
        "figure-8-muon-mass-cross-check",
        "typed-crossing-operator",
        "typed-crossing-operator-motivation",
        "nucleon-hecke-element",
        "nucleon-hecke-element-examples",
        "nucleon-hecke-element-normal-form",
        "hadron-proton-example",
        "fermion-boson-knot-link",
        "fermion-boson-knot-link-proof",
        "fermion-boson-knot-link-table-data",
        "shell-transition-knot",
        "shell-transition-knot-table1-data",
        "shell-transition-knot-table2-data",
        "shell-transition-knot-table3-data",
        "shell-transition-knot-interpretation",
      ],
    }),

    // ── §6. Confinement level and the cemetery group ──────────────
    section({
      title: "Confinement level and the cemetery group",
      label: "sec:confinement-level",
      blocks: [
        "intro-confinement-level",
        "confinement-level",
        "confinement-level-properties",
        "confinement-level-exists",
        "confinement-level-exists-proof",
        "confinement-level-unique",
        "confinement-level-unique-local-constancy",
        "cemetery-group",
        "cemetery-group-remark",
        "crystal-graph-realization",
        "confinement-grading-correspondence",
        "confinement-grading-correspondence-conditional",
        "confinement-grading-correspondence-conditional-witness",
        "cemetery-group-emergence",
        "ontological-agnosticism",
      ],
    }),

    // ── §7. Lepton–meson structural parallel ─────────────────────
    section({
      title: "Lepton–meson structural parallel",
      label: "sec:lepton-meson-structural-parallel",
      blocks: [
        "lepton-meson-parallel",
        "lepton-meson-torus-knot-dictionary",
        "lepton-meson-torus-knot-dictionary-proof",
        "c-equals-bar-iff-all-1dim",
        "c-equals-bar-iff-all-1dim-proof",
      ],
    }),

    // ── §8. Electroweak and Higgs torus-link triplet ─────────────
    // crossing-energy + coulomb-charge were relocated INTO this group
    // 2026-08-09 (decision 5) so the electroweak-triplet results below would
    // stop forward-referencing their own definitions. They moved again
    // 2026-08-29, further up the chapter to the nucleon group; decision 5
    // constrains the ORDER (crossing-energy, then coulomb-charge, then the
    // electroweak-triplet blocks), and moving them earlier preserves it.
    // spin-involution came from mass-theory sec:lp-dual-jucys-murphy, which
    // keeps the lp-dual-invariance arc and now reads backward for the
    // definition. See the note above the nucleon group for why explanatory
    // comments must stay OUTSIDE the block list.
    section({
      title: "Electroweak and Higgs sector as an even-twist torus-link triplet",
      label: "sec:electroweak-higgs-torus-link-triplet",
      blocks: [
        "spin-involution",
        "spin-involution-isospin",
        "electroweak-triplet-bring-embedding",
        "electroweak-triplet-far-commuting-minimal",
        "electroweak-triplet-far-commuting-minimal-proof",
        "electroweak-triplet-far-commuting-minimal-scope",
        "electroweak-higgs-torus-link-triplet",
        "electroweak-triplet-charge-spin-from-involution",
        "electroweak-triplet-charge-spin-from-involution-proof",
        "electroweak-triplet-charge-spin-from-involution-slot",
        "ew-slot-far-commutation-obstruction",
        "ew-slot-far-commutation-obstruction-proof",
        "ew-slot-far-commutation-obstruction-constraints",
        "electroweak-higgs-torus-link-triplet-table1-data",
        "electroweak-higgs-torus-link-triplet-table2-data",
        "electroweak-higgs-torus-link-triplet-table3-data",
      ],
    }),

    // ── §9. Confined particles and shells ─────────────────────────
    section({
      title: "Confined particles and shells",
      label: "sec:confined-particles-shells",
      blocks: [
        "intro-confined-particles-shells",
        "confined-particle",
        "confined-particle-remark",
        "confined-particle-examples",
        "confinement-category",
        "confinement-category-invertibility",
        "confinement-category-markov-functor",
        "confinement-category-atomic-chain",
        "dressed-particle",
        "dressed-particle-examples",
        "dressed-particle-properties",
        "shell-closure-stability",
        "shell-closure-stability-proof",
        "shell-closure-stability-interprets",
        "level-sufficiency",
        "level-sufficiency-proof",
        "level-sufficiency-interprets",
        "confinement-phase-stratification",
        "confinement-phase-stratification-proof",
        "confinement-phase-stratification-interpretation",
        "phase-scoped-applicability",
      ],
    }),

    // ── §10. Atom and isotope knots ────────────────────────────────
    section({
      title: "Atom and isotope knots",
      label: "sec:atom-isotope-knots",
      blocks: [
        "intro-atom-isotope-knots",
        "atom-knot",
        "atom-knot-remark",
        "atom-knot-exists",
        "atom-knot-exists-proof",
        "atom-knot-unique",
        "atom-knot-unique-proof",
        "isotope-knot",
        "isotope-knot-properties",
        "isotope-knot-equivalence",
        "isotope-knot-equivalence-proof",
        // Relocated from braids-and-knots sec:knot-fundamental-groups
        // 2026-08-09 (decision 5), where it had landed as a 2026-07-12
        // Ledger §5 orphan integration. The conjecture is stated over
        // isotopes (Z, N), so it belongs after the isotope-knot arc and
        // before the stability arc; its dep def:atom-knot is at the head of
        // this section, so the edge is now backward and intra-chapter.
        "jsj-decomposition-linearity",
        "stable-atom",
        "stable-atom-properties",
        "stable-atom-decidable",
        "stable-atom-decidable-proof",
        "unstable-atom",
        "unstable-atom-decay-phase",
        "unstable-atom-decay-channel",
        "unstable-atom-decay-channel-proof",
      ],
    }),

    // ── §11. Magic shells and the κ coupling ──────────────────────
    section({
      title: "Magic shells and the $\\\\kappa$ coupling",
      label: "sec:magic-shells",
      blocks: [
        "intro-magic-shells",
        "ilp-solution-count-unwrap",
        "shell-schur-weyl-self-duality",
        "shell-schur-weyl-self-duality-proof",
        "shell-schur-weyl-self-duality-interpretation",
        "compound-beta-shell-calibration",
        "compound-beta-shell-calibration-key-distinction",
        "compound-beta-shell-calibration-interpretation",
        "compound-beta-shell-calibration-table3-data",
        "compound-beta-shell-calibration-table2-data",
        "compound-beta-shell-calibration-table1-data",
        "magic-shell-coupling-kappa",
        "magic-shell-coupling-kappa-remark",
        "magic-shell-coupling-kappa-table-data",
        "quantum-dilogarithm-disambiguation",
        "quantum-dilogarithm-disambiguation-remark",
      ],
    }),

    // ── §12. Categorical proton, neutron, and meson ───────────────
    // The definitional blocks from the former orphan-reconnect section.
    // Structural definitions of composite hadrons: their categorical
    // construction and Reidemeister-invariant properties.
    section({
      title: "Categorical proton, neutron, and meson",
      label: "sec:categorical-hadrons",
      blocks: [
        "categorical-proton",
        "categorical-proton-properties",
        // Moved here from §2 on 2026-08-24, the day it landed, on the
        // detangler's measurement rather than on topic. It was placed in §2
        // because it `interprets: def:derived-atom` and explains that
        // definition's step 4 — a good reason, but the only one pointing
        // there. Against it: NO §2 block references it, both its referrers
        // are in this section, and both blocks it `uses` are in this section,
        // so in §2 it emitted two forward refs (`-> rem:ilp-solution-count-
        // unwrap`, `-> rem:categorical-proton-properties`) and here it emits
        // none — chapter total 10 -> 8. Checked against all nine detangler
        // criteria before and after: nothing new appears, and section-band,
        // topic-coherence and no-dependency-cycle pass either way. The
        // `interprets` edge now points backward, which is what a dependency
        // should do. Revert if the editorial call outweighs the measurement.
        "gluon-stabiliser-ledger",
        "categorical-neutron",
        "categorical-neutron-properties",
        "categorical-meson",
        "categorical-meson-normal-form",
        "meson-scale-independence",
        "meson-scale-independence-calibration",
        "meson-scale-independence-proof",
        // Placement chosen by the detangler's forward-ref metric rather than
        // by topic (bean `qou-bzy0`). The obvious home for the antiquark
        // ledger was §2 — it `interprets: def:derived-atom` and closes a gap
        // in that section's step 2 — but measured, §2 costs two new forward
        // refs (`-> def:categorical-meson` and
        // `-> rem:pion-mass-hyperbolic-threshold`) while here it costs none:
        // 10 chapter-wide either way, the same 10 that were already there.
        // Six placements tie at zero and all six are in this section; this is
        // the only one that does not split the `meson-scale-independence`
        // statement / calibration / proof triple.
        "pion-mass-hyperbolic-threshold",
        "antiquark-channel-ledger",
      ],
    }),
  ],
});
