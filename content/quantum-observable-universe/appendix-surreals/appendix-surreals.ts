import { chapter } from "../../schema/builders";

export default chapter({
  label: "app:surreals",
  title: "Surreal-number lift of QOU (appendix)",
  sections: [
    {
      heading: "Motivation and scope",
      blocks: [
        "surreal-appendix-intro",
      ],
    },
    {
      heading: "What survives and what breaks",
      blocks: [
        "algebraic-core-survives",
        "analytic-obstructions",
        "calculus-up-to-epsilon",
      ],
    },
    {
      heading: "Surreal construction as a grading",
      blocks: [
        "birthday-grading",
        "hoefsmit-is-surreal-construction",
        "sign-sequence-of-braid",
        "jones-birthday",
      ],
    },
    {
      heading: "Standard-part replaces classical limits",
      blocks: [
        "standard-part-functor",
        "valuation-ring-finite-surreals",
        "classical-limit-stpart",
        "archimedean-stpart",
      ],
    },
    {
      heading: "Conway normal form and asymptotic notation",
      blocks: [
        "conway-normal-form",
        "big-o-surreal",
      ],
    },
    {
      heading: "Named surreals for singular objects",
      blocks: [
        "surreal-blowup-calculus",
        "bigbang-heatdeath",
      ],
    },
    {
      heading: "Relaxing strict equalities to $1 + \\varepsilon$",
      blocks: [
        "infinitesimal-frobenius",
        "infinitesimal-observability",
        "vacuum-epsilon",
      ],
    },
    {
      heading: "Speculative reformulations",
      blocks: [
        "hahn-substrate",
        "kashaev-surreal",
      ],
    },
    {
      heading: "Characteristic-$p$ companion: nimber surreals",
      blocks: [
        "on-p-modular-hecke",
      ],
    },
    {
      heading: "Outlook",
      blocks: [
        "surreal-appendix-conclusion",
      ],
    },
  ],
});
