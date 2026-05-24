import { chapter } from "../../schema/builders";

export default chapter({
  label: "app:surreals",
  title: "Surreal-number lift of QOU (appendix)",
  sections: [
    {
      title: "Motivation and scope",
      label: "sec:surreal-motivation",
      blocks: [
        "surreal-appendix-intro",
      ],
    },
    {
      title: "What survives and what breaks",
      label: "sec:surreal-survives-breaks",
      blocks: [
        "algebraic-core-survives",
        // Dual ledger: every transcendental in the paper, indexed
        // by Goncharov period-depth.
        "transcendental-accounting",
        "transcendental-accounting-table-data",
        // K-theory ↔ depth filtration Rosetta: Beilinson regulator
        // matches iterated-integral grading on H_q.
        "k-theory-period-rosetta",
        // Borel's theorem partial-discharges the keystone's
        // sharpness target with explicit Borel-rank dimensions.
        "borel-partial-resolution",
        "borel-partial-resolution-table2-data",
        "borel-partial-resolution-table1-data",
        // Depth-2 identification of G^(2) with K_3^ind ⊗ Q via
        // Bloch–Suslin — theorem-level discharge of the keystone
        // at depth 2 over every Bring-natural number field.
        "depth-2-identification-bloch-suslin",
        // QOU infra (Hecke NF + Bring S_5) potentially discharges
        // Goncharov's conjecture at F = Q(ζ_5) for depth 3.
        "qou-infra-discharges-goncharov-zeta5",
        "qou-infra-discharges-goncharov-zeta5-table2-data",
        "qou-infra-discharges-goncharov-zeta5-table1-data",
        // Soft-sharpness version of B1 is theorem-level (Borel + Lewin).
        "b1-soft-sharpness-theorem",
        // B1 at the figure-8 row is theorem (Bloch-Suslin + Murakami-Murakami).
        "b1-figure-8-row-theorem",
        // B1 at torus-knot rows is theorem (Bloch-Suslin + Garoufalidis-Lê).
        "b1-torus-knot-rows-theorem",
        "b1-torus-knot-rows-theorem-table-data",
        // B1 at additional hyperbolic-knot rows (Borromean, Whitehead).
        "b1-hyperbolic-rows-theorem",
        "b1-hyperbolic-rows-theorem-table2-data",
        "b1-hyperbolic-rows-theorem-table1-data",
        // Canonical B1 current-status synthesis (rounds 1-11).
        "b1-current-status",

        "b1-current-status-table1-data",
        "b1-current-status-table2-data",
        "b1-current-status-table3-data",
        "analytic-obstructions",
        "analytic-obstructions-table2-data",
        "analytic-obstructions-table1-data",
        "calculus-up-to-epsilon",
        "calculus-up-to-epsilon-table-data",
      ],
    },
    {
      title: "Surreal construction as a grading",
      label: "sec:surreal-construction-grading",
      blocks: [
        "birthday-grading",
        "hoefsmit-is-surreal-construction",
        "sign-sequence-of-braid",
        "jones-birthday",
      ],
    },
    {
      title: "Standard-part replaces classical limits",
      label: "sec:standard-part-classical-limits",
      blocks: [
        "standard-part-functor",
        "valuation-ring-finite-surreals",
        "classical-limit-stpart",
        "archimedean-stpart",
        "archimedean-stpart-strategy",
      ],
    },
    {
      title: "Conway normal form and asymptotic notation",
      label: "sec:conway-normal-form",
      blocks: [
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
        "surreal-blowup-calculus",
        "surreal-blowup-calculus-table-data",
        "bigbang-heatdeath",
      ],
    },
    {
      title: "Relaxing strict equalities to $1 + \\varepsilon$",
      label: "sec:relaxing-strict-equalities",
      blocks: [
        "infinitesimal-frobenius",
        "infinitesimal-observability",
        "vacuum-epsilon",
      ],
    },
    {
      title: "Speculative reformulations",
      label: "sec:surreal-speculative",
      blocks: [
        "hahn-substrate",
        "local-infinitesimal-field",
        "spectral-normal-form",
        "diophantine-birthday",
        "kashaev-surreal",
      ],
    },
    {
      title: "Characteristic-$p$ companion: nimber surreals",
      label: "sec:nimber-surreals",
      blocks: [
        "on-p-modular-hecke",
        "on-p-modular-hecke-table-data",
      ],
    },
    {
      title: "Surreal rate calculus and the squeeze inequality",
      label: "sec:surreal-rate-calculus",
      blocks: [
        "surreal-rate-calculus",
        "surreal-squeeze",
      ],
    },
    {
      title: "Millennium-problem surreal bounds",
      label: "sec:millennium-bounds-via-surreals",
      blocks: [
        // BSD
        "q-birch-swinnerton-dyer",
        "bsd-surreal-bound",
        // RH
        "rh-surreal-bound",
        // Yang-Mills
        "yang-mills-surreal-bound",
        // P vs NP
        "p-vs-np-conjecture",
        "p-vs-np-surreal-bound",
        // Collatz family
        "q-collatz-conjecture",
        "collatz-contact-boundary",
        "collatz-no-cycles",
        "collatz-three-forms",
        "collatz-hausdorff-comparison",
        "collatz-hausdorff-comparison-table-data",
        "q-collatz-interpretation",
        "collatz-surreal-bound",
        // Graded-Mikusiński unification of the bounds.
        "surreal-bounds-graded-mikusinski",
        "millennium-unification",
        "millennium-unification-table1-data",
      ],
    },
    {
      title: "Outlook",
      label: "sec:surreal-outlook",
      blocks: [
        "surreal-appendix-conclusion",
      ],
    },
  ],
});
