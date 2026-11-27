import { chapter } from "../../schema/builders";

/**
 * Annex D: Surreal and Non-Archimedean Substrate Lift and Continuum Boundary.
 *
 * Unifies the pre-Archimedean categorical surreal-number lift (Conway normal
 * form, birthday grading, Goncharov depth correspondence, Millennium surreal
 * bounds) with the post-wall Archimedean standard-part and Écalle–Borel
 * resummation blocks evaluated at q_0.
 */
export default chapter({
  tabLabel: "D",
  label: "app:surreals",
  title: "Surreal and Non-Archimedean Aether Lift and Continuum Boundary",
  sections: [
    {
      title: "Motivation, scope, and survival across the lift",
      label: "sec:surreal-survives-breaks",
      blocks: [
        "surreal-appendix-intro",
        "surreal-survives-breaks-intro",
      ],
      subsections: [
        {
          title: "Transcendental accounting and discharge",
          label: "sec:surreal-transcendental-discharge",
          blocks: [
            "transcendental-accounting",
            "transcendental-accounting-table-data",
            "k-theory-period-rosetta",
            "borel-partial-resolution",
            "borel-partial-resolution-table2-data",
            "borel-partial-resolution-table1-data",
            "depth-2-identification-bloch-suslin",
            "depth-2-identification-bloch-suslin-proof",
            "qou-infra-discharges-goncharov-zeta5",
            "qou-infra-discharges-goncharov-zeta5-table2-data",
            "qou-infra-discharges-goncharov-zeta5-table1-data",
          ],
        },
        {
          title: "Theorem-level rows of the depth correspondence",
          label: "sec:surreal-b1-theorem-rows",
          blocks: [
            "b1-soft-sharpness-theorem",
            "b1-soft-sharpness-theorem-proof",
            "b1-soft-sharpness-significance",
            "b1-figure-8-row-theorem",
            "b1-figure-8-row-theorem-proof",
            "b1-torus-knot-rows-theorem",
            "b1-torus-knot-rows-theorem-table-data",
            "b1-hyperbolic-rows-theorem",
            "b1-hyperbolic-rows-theorem-table2-data",
            "b1-hyperbolic-rows-theorem-table1-data",
          ],
        },
        {
          title: "Status of the depth correspondence",
          label: "sec:surreal-b1-status",
          blocks: [
            "b1-current-status",
            "b1-current-status-table1-data",
            "b1-current-status-table2-data",
            "calculus-up-to-epsilon",
            "calculus-up-to-epsilon-table-data",
          ],
        },
      ],
    },
    {
      title: "Surreal construction as a grading",
      label: "sec:surreal-construction-grading",
      blocks: [
        "surreal-construction-grading-intro",
        "birthday-grading",
        "birthday-grading-remark",
        "birthday-grading-archimedean",
        "birthday-grading-substrate",
        "sign-sequence-of-braid",
        "sign-sequence-of-braid-remark",
        "sign-sequence-of-braid-invariant",
        "hoefsmit-is-surreal-construction",
        "jones-birthday",
        "hoefsmit-is-surreal-construction-context",
        "hoefsmit-is-surreal-construction-proof",
      ],
    },
    {
      title: "Standard-part replaces classical limits",
      label: "sec:standard-part-classical-limits",
      blocks: [
        "standard-part-classical-limits-intro",
        "valuation-ring-finite-surreals",
        "classical-limit-stpart",
        "archimedean-stpart",
        "archimedean-stpart-strategy",
        "hyperreal-limit-transfer",
        "birthday-axioms-do-not-pin-the-birthday",
      ],
    },
    {
      title: "Conway normal form and asymptotic notation",
      label: "sec:conway-normal-form",
      blocks: [
        "conway-normal-form-intro",
        "surreal-blowup-calculus",
        "surreal-blowup-calculus-table-data",
        "conway-normal-form",
        "body-asymptotics-catalog",
        "body-asymptotics-catalog-table3-data",
        "body-asymptotics-catalog-table2-data",
        "body-asymptotics-catalog-table1-data",
      ],
    },
    {
      title: "Named surreals for singular objects",
      label: "sec:named-surreals-singular",
      blocks: [
        "surreal-blowup-literal",
        "surreal-blowup-examples",
        "mobius-surreal-renormalization",
        "bigbang-heatdeath",
        "cosmological-cone-visualization",
      ],
    },
    {
      title: "Relaxing strict equalities to $1 + \\varepsilon$",
      label: "sec:relaxing-strict-equalities",
      blocks: [
        "infinitesimal-observability",
        "vacuum-epsilon",
        "casimir-epsilon-vacuum",
        "casimir-first-q-correction",
      ],
    },
    {
      title: "Speculative reformulations",
      label: "sec:surreal-speculative",
      blocks: [
        "surreal-speculative-intro",
        "local-infinitesimal-field",
        "spectral-normal-form",
        "kashaev-surreal",
        "perpetual-obstruction-depth-omega",
      ],
    },
    {
      title: "Surreal rate calculus and the squeeze inequality",
      label: "sec:surreal-rate-calculus",
      blocks: [
        "surreal-squeeze",
        "surreal-squeeze-proof",
        "surreal-rate-calculus",
        "surreal-rate-calculus-setup",
        "surreal-rate-calculus-proof",
        "surreal-rate-calculus-interpretation",
        "surreal-squeeze-interpretation",
      ],
    },
    {
      title: "Millennium-problem surreal bounds",
      label: "sec:millennium-bounds-via-surreals",
      blocks: [
        "millennium-bounds-via-surreals-intro",
      ],
      subsections: [
        {
          title: "BSD, RH, and Yang-Mills bounds",
          label: "sec:millennium-bsd-rh-ym",
          blocks: [
            "rh-surreal-bound",
            "categorical-mordell-weil",
            "categorical-sha-local-global",
            "q-birch-swinnerton-dyer",
            "q-bsd-rank-zero",
            "q-bsd-classical-limit",
            "bsd-surreal-bound",
            "yang-mills-surreal-bound",
            "os-reflection-positivity-from-reeb",
          ],
        },
        {
          title: "P vs NP and the Collatz family",
          label: "sec:millennium-pnp-collatz",
          blocks: [
            "p-vs-np-conjecture",
            "p-vs-np-surreal-bound",
            "q-collatz-conjecture",
            "two-q-adic-valuation",
            "collatz-contact-boundary-defn",
            "collatz-contact-boundary",
            "collatz-parity-to-divisor",
            "collatz-no-cycles",
            "collatz-no-cycles-proof",
            "collatz-three-forms",
            "q-collatz-interpretation",
            "collatz-surreal-bound",
          ],
        },
        {
          title: "Graded-Mikusiński unification",
          label: "sec:millennium-unification",
          blocks: [
            "surreal-bounds-graded-mikusinski",
            "millennium-unification",
            "millennium-unification-table1-data",
          ],
        },
      ],
    },
    {
      title: "Archimedean specialisation: Écalle--Borel resummation and standard-part functor at $q_0$",
      label: "sec:surreals-archimedean-algebraic",
      blocks: [
        "algebraic-core-survives",
        "tarski-sign-decision-depth",
        "ecalle-borel-resummation",
        "analytic-obstructions",
        "analytic-obstructions-table1-data",
        "analytic-obstructions-table2-data",
        "ecalle-borel-resurgence-vocabulary",
        "habiro-tail-archimedean-action",
        "standard-part-functor",
        "st-is-median-resummation",
        "standard-part-classical-limit",
        "archimedean-functor-trace-commutativity",
      ],
    },
    {
      title: "Archimedean specialisation: Diophantine birthday and characteristic-$p$ companions",
      label: "sec:surreals-archimedean-speculative",
      blocks: [
        "diophantine-birthday",
        "diophantine-birthday-trajectory",
        "infinitesimal-frobenius",
        "surreal-limit-transfer",
        "on-p-modular-hecke",
        "on-p-modular-hecke-table-data",
        "on-p-modular-hecke-significance",
      ],
    },
    {
      title: "Archimedean specialisation: Wenzl positivity, Hausdorff comparison, and outlook",
      label: "sec:surreals-archimedean-millennium",
      blocks: [
        "wenzl-positivity-implies-substrate-positivity",
        "collatz-hausdorff-comparison",
        "collatz-hausdorff-comparison-table-data",
        "surreal-appendix-conclusion",
      ],
    },
  ],
});
