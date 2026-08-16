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
        "surreal-survives-breaks-intro",
      ],
      // Over-weight split (P4): 24-block survival analysis broken into
      // 3 reading-order sub-arcs. Order preserved; parent keeps the intro.
      subsections: [
        {
          title: "Transcendental accounting and discharge",
          label: "sec:surreal-transcendental-discharge",
          blocks: [
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
            "depth-2-identification-bloch-suslin-proof",
            // QOU infra (Hecke NF + Bring S_5) potentially discharges
            // Goncharov's conjecture at F = Q(ζ_5) for depth 3.
            "qou-infra-discharges-goncharov-zeta5",
            "qou-infra-discharges-goncharov-zeta5-table2-data",
            "qou-infra-discharges-goncharov-zeta5-table1-data",
          ],
        },
        {
          title: "Theorem-level rows of the depth correspondence",
          label: "sec:surreal-b1-theorem-rows",
          blocks: [
            // Soft-sharpness version of B1 is theorem-level (Borel + Lewin).
            "b1-soft-sharpness-theorem",
            "b1-soft-sharpness-theorem-proof",
            "b1-soft-sharpness-significance",
            // B1 at the figure-8 row is theorem (Bloch-Suslin + Murakami-Murakami).
            "b1-figure-8-row-theorem",
            "b1-figure-8-row-theorem-proof",
            // B1 at torus-knot rows is theorem (Bloch-Suslin + Garoufalidis-Lê).
            "b1-torus-knot-rows-theorem",
            "b1-torus-knot-rows-theorem-table-data",
            // B1 at additional hyperbolic-knot rows (Borromean, Whitehead).
            "b1-hyperbolic-rows-theorem",
            "b1-hyperbolic-rows-theorem-table2-data",
            "b1-hyperbolic-rows-theorem-table1-data",
          ],
        },
        {
          title: "Status of the depth correspondence",
          label: "sec:surreal-b1-status",
          blocks: [
            // Canonical B1 current-status synthesis (rounds 1-11).
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
        "birthday-grading-archimedean",
        "birthday-grading-substrate",
        "sign-sequence-of-braid",
        "sign-sequence-of-braid-invariant",
        "hoefsmit-is-surreal-construction",
        "hoefsmit-is-surreal-construction-context",
        "hoefsmit-is-surreal-construction-proof",
        "jones-birthday",
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
        "surreal-blowup-literal",
        "surreal-blowup-examples",
        // Möbius energy renormalization as a difference of infinite surreals
        // (the surreal-essential showcase; interprets prop:mobius-energy).
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
        // Conditional consequence of the ε-relaxed vacuum: the
        // Casimir force is the st-image of the ε·(unknot-mode-count)
        // product, with surreal-infinite mode-count gradient.
        "casimir-epsilon-vacuum",
        // First substrate correction to the Casimir force: carried by
        // the figure-eight knot 4_1 (the minimal hyperbolic mode);
        // weight J_{4_1} = 1 + (3/4)h² + O(h⁴), the 3/4 Lean-proved.
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
        // ε^ω = the perpetual obstruction as a single surreal grade
        // (narrowing of conj:motivic-perpetual-obstruction).
        "perpetual-obstruction-depth-omega",
      ],
    },
    {
      title: "Surreal rate calculus and the squeeze inequality",
      label: "sec:surreal-rate-calculus",
      blocks: [
        "surreal-rate-calculus",
        "surreal-rate-calculus-setup",
        "surreal-rate-calculus-proof",
        "surreal-rate-calculus-interpretation",
        "surreal-squeeze",
        "surreal-squeeze-proof",
        "surreal-squeeze-interpretation",
      ],
    },
    {
      title: "Millennium-problem surreal bounds",
      label: "sec:millennium-bounds-via-surreals",
      blocks: [
        "millennium-bounds-via-surreals-intro",
      ],
      // Over-weight (P4, advisory — within the 3-18 band but heavy vs the
      // appendix's small peers) split: 17-block section organised by
      // millennium problem. Order preserved; parent keeps the intro.
      subsections: [
        {
          title: "BSD, RH, and Yang-Mills bounds",
          label: "sec:millennium-bsd-rh-ym",
          blocks: [
            // BSD
            "categorical-mordell-weil",
            "categorical-sha-local-global",
            "q-birch-swinnerton-dyer",
            "q-bsd-rank-zero",
            "q-bsd-classical-limit",
            "bsd-surreal-bound",
            // RH
            "rh-surreal-bound",
            // Yang-Mills
            "yang-mills-surreal-bound",
            "os-reflection-positivity-from-reeb",
          ],
        },
        {
          title: "P vs NP and the Collatz family",
          label: "sec:millennium-pnp-collatz",
          blocks: [
            // P vs NP
            "p-vs-np-conjecture",
            "p-vs-np-surreal-bound",
            // Collatz family
            "q-collatz-conjecture",
            "two-q-adic-valuation",
            "collatz-contact-boundary-defn",
            // Swapped 2026-08-15: `collatz-parity-to-divisor` declares
            // `interprets: "prop:collatz-contact-boundary"` and was listed
            // immediately BEFORE it, so the remark interpreted a result the
            // reader had not met yet. Adjacent, one section — a listing-order
            // slip rather than a structural question.
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
      title: "Outlook",
      label: "sec:surreal-outlook",
      blocks: [
        "surreal-appendix-conclusion",
      ],
    },
  ],
});
