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
        // Depth-2 identification of G^(2) with K_3^ind ⊗ Q via
        // Bloch–Suslin — theorem-level discharge of the keystone
        // at depth 2 over every Bring-natural number field.
        "depth-2-identification-bloch-suslin",
        // QOU infra (Hecke NF + Bring S_5) potentially discharges
        // Goncharov's conjecture at F = Q(ζ_5) for depth 3.
        "qou-infra-discharges-goncharov-zeta5",
        // Soft-sharpness version of B1 is theorem-level (Borel + Lewin).
        "b1-soft-sharpness-theorem",
        // B1 at the figure-8 row is theorem (Bloch-Suslin + Murakami-Murakami).
        "b1-figure-8-row-theorem",
        // B1 at torus-knot rows is theorem (Bloch-Suslin + Garoufalidis-Lê).
        "b1-torus-knot-rows-theorem",
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
