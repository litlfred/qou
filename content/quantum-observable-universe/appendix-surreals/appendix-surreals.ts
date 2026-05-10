import { chapter } from "../../schema/builders";

export default chapter({
  label: "app:surreals",
  title: "Surreal-number lift of QOU (appendix)",
  sections: [
    {
      title: "Motivation and scope",
      blocks: [
        "surreal-appendix-intro",
      ],
    },
    {
      title: "What survives and what breaks",
      blocks: [
        "algebraic-core-survives",
        // Dual ledger: every transcendental in the paper, indexed
        // by Goncharov period-depth.
        "transcendental-accounting",
        // K-theory ↔ depth filtration Rosetta: Beilinson regulator
        // matches iterated-integral grading on H_q.
        "k-theory-period-rosetta",
        // Borel's theorem partial-discharges the keystone's
        // sharpness target with explicit Borel-rank dimensions.
        "borel-partial-resolution",
        "analytic-obstructions",
        "calculus-up-to-epsilon",
      ],
    },
    {
      title: "Surreal construction as a grading",
      blocks: [
        "birthday-grading",
        "hoefsmit-is-surreal-construction",
        "sign-sequence-of-braid",
        "jones-birthday",
      ],
    },
    {
      title: "Standard-part replaces classical limits",
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
      blocks: [
        "conway-normal-form",
        "body-asymptotics-catalog",
      ],
    },
    {
      title: "Named surreals for singular objects",
      blocks: [
        "surreal-blowup-calculus",
        "bigbang-heatdeath",
      ],
    },
    {
      title: "Relaxing strict equalities to $1 + \\varepsilon$",
      blocks: [
        "infinitesimal-frobenius",
        "infinitesimal-observability",
        "vacuum-epsilon",
      ],
    },
    {
      title: "Speculative reformulations",
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
      blocks: [
        "on-p-modular-hecke",
      ],
    },
    {
      title: "Outlook",
      blocks: [
        "surreal-appendix-conclusion",
      ],
    },
  ],
});
