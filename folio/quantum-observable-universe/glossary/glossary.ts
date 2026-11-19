import { chapter, section } from "../../schema/builders";

/**
 * Glossary of mathematical and physical terms used across the monograph.
 *
 * Provides concise, self-contained definitions and cross-references to the
 * canonical definitions, theorems, and propositions of the Quantum Observable
 * Universe framework, together with standard categorical and homological
 * background.
 */
export default chapter({
  tabLabel: "G",
  title: "Glossary",
  label: "chap:glossary",
  sections: [
    section({
      title: "Foundations and aether calculus",
      label: "sec:glossary-foundations",
      blocks: [
        "glossary-quantum-universe",
        "glossary-quantum-observable-universe",
        "glossary-frobenius-hopf-aether",
        "glossary-fibre-functor",
        "glossary-frobenius-pairing",
        "glossary-aether-parameter",
        "glossary-quantum-planck-constant",
        "glossary-categorical-q-ext-deriv",
        "glossary-categorical-reeb",
        "glossary-categorical-connection-instanton",
        "glossary-categorical-dirac-operator",
        "glossary-categorical-lagrangian-action",
        "glossary-exceptional-divisor",
      ],
    }),

    section({
      title: "Lifting, descent, and Bring's surface",
      label: "sec:glossary-geometry",
      blocks: [
        "glossary-geometry-intro",
        "glossary-arc-space-brane-boundary",
        "glossary-yekutieli-lifting-condition",
        "glossary-descent",
        "glossary-descartes-condition",
        "glossary-brings-surface",
        "glossary-color-coordinates",
        "glossary-observed-value",
        "glossary-weierstrass-projection",
        "glossary-quantum-flatness",
        "glossary-reeb-gauge-group",
        "glossary-categorical-q-torsion-leaf",
        "glossary-categorical-transport",
        "glossary-s3-group",
      ],
    }),

    section({
      title: "Braids, Hecke algebras, and traces",
      label: "sec:glossary-braids-hecke",
      blocks: [
        "glossary-braid-group",
        "glossary-iwahori-hecke-algebra",
        "glossary-bar-involution",
        "glossary-markov-trace",
        "glossary-gpmt-modified-trace",
        "glossary-habiro-completions",
        "glossary-algebraic-quantum-volume",
        "glossary-crossing-energy",
        "glossary-curvature-rank",
        "glossary-cemetery-group",
      ],
    }),

    section({
      title: "Particles, confinement, and atomic braids",
      label: "sec:glossary-particles-atoms",
      blocks: [
        "glossary-fermion-boson-decomposition",
        "glossary-neutrino-antineutrino",
        "glossary-electron-positron",
        "glossary-switched-photon",
        "glossary-breit-wheeler-pair-production",
        "glossary-borromean-baryon",
        "glossary-confined-particle",
        "glossary-atomic-braid",
        "glossary-covalent-bond",
      ],
    }),

    section({
      title: "Dynamics, information, and $q$-geometric Langlands",
      label: "sec:glossary-dynamics-langlands",
      blocks: [
        "glossary-q-navier-stokes",
        "glossary-q-bit",
        "glossary-q-bit-skein",
        "glossary-aeon-cmb",
        "glossary-computational-horizon",
        "glossary-q-local-system",
        "glossary-q-hecke-eigensheaf",
        "glossary-adelic-aether",
        "glossary-birthday-grading",
      ],
    }),

    section({
      title: "Categories and enrichment",
      label: "sec:glossary-basic",
      blocks: [
        "glossary-hom-set",
        "glossary-r-linear-category",
        "glossary-no-quasi-zeros",
      ],
    }),

    section({
      title: "Monoidal and braided categories",
      label: "sec:glossary-monoidal",
      blocks: [
        "glossary-monoidal-intro",
        "glossary-monoidal-category",
        "glossary-braided-monoidal-category",
        "glossary-symmetric-monoidal-category",
        "glossary-monoidal-functor",
      ],
    }),

    section({
      title: "Duality, rigidity, and pivotal structure",
      label: "sec:glossary-rigidity",
      blocks: [
        "glossary-rigidity-intro",
        "glossary-exact-pairing",
        "glossary-left-dual",
        "glossary-right-dual",
        "glossary-rigid-category",
        "glossary-pivotal-category",
        "glossary-compact-closed-category",
      ],
    }),

    section({
      title: "Triangulated and derived categories",
      label: "sec:glossary-homological",
      blocks: [
        "glossary-distinguished-triangle",
        "glossary-derived-category",
        "glossary-dg-category",
        "glossary-fourier-mukai-transform",
      ],
    }),

  ],
});
