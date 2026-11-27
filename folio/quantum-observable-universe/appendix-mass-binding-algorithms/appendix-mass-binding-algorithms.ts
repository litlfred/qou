import { chapter, section } from "../../schema/builders";

/**
 * Annex B: Computational, Dual-Certificate, and Transfer-Matrix Algorithms.
 *
 * Consolidates the compact nine-block L_0..L_4 QOU-delta computational &
 * rationalized dual-certificate algorithms (qou-mba8), the 2x2 monotone
 * transfer-matrix recurrences and exact Laurent Pauli witnesses, and the
 * Lean-verified 5_2 trace-field and Habiro star-identity propositions.
 */
export default chapter({
  tabLabel: "B",
  title: "Computational, Dual-Certificate, and Transfer-Matrix Algorithms",
  label: "app:mass-binding-algorithms",
  sections: [
    section({
      title: "$\\mathcal{L}_0\\text{--}\\mathcal{L}_4$ computational and dual-certificate algorithms",
      label: "sec:mba-canonical-chain",
      blocks: [
        "mba-intro",
        "hecke-gs-monotone-transfer",
        "twisted-star-gram-radical-quotient",
        "ecat-radical-shadow-price",
        "confinement-tower-chamber-gs",
        "substrate-period-mass-resolvent",
        "q-beta-chirality-jet-evaluation",
        "rationalized-dual-slack-certificate",
        "lp-sdp-bootstrap-prior-art",
      ],
    }),
    section({
      title: "Transfer-matrix notation, general form, and knot-pair operators",
      label: "sec:tm-notation",
      blocks: [
        "tm-notation-intro",
        "tm-notation",
        "tm-notation-table1-data",
        "tm-notation-table2-data",
        "tm-notation-table3-data",
        "tm-notation-table4-data",
        "tm-general-form",
        "tm-knot-pairs-intro",
        "tm-knot-pairs",
        "tm-knot-pairs-table1-data",
        "tm-knot-pairs-table2-data",
        "tm-knot-pairs-table3-data",
        "tm-knot-pairs-table4-data",
      ],
    }),
    section({
      title: "Interaction matrices, inductive Gröbner--Shirshov normal forms, and Pauli witnesses",
      label: "sec:tm-interactions",
      blocks: [
        "tm-interactions-intro",
        "tm-interactions",
        "tm-interactions-table3-data",
        "tm-interactions-table2-data",
        "tm-interactions-table1-data",
        "tm-interaction-completeness",
        "tm-interaction-completeness-table-data",
        "qvalue-derivation-chain",
        "tm-inductive-construction",
        "tm-gs-normal-form",
        "tm-gs-normal-form-proof",
        "witness-4he",
        "witness-8be",
        "witness-12c",
        "witness-computation-method",
      ],
    }),
    section({
      title: "Worked light-nucleus transfer-matrix examples",
      label: "sec:tm-worked-examples",
      blocks: [
        "tm-worked-examples-intro",
        "tm-worked-examples",
        "tm-worked-examples-table10-data",
        "tm-worked-examples-table9-data",
        "tm-worked-examples-table8-data",
        "tm-worked-examples-table7-data",
        "tm-worked-examples-table6-data",
        "tm-worked-examples-table5-data",
        "tm-worked-examples-table4-data",
        "tm-worked-examples-table3-data",
        "tm-worked-examples-table2-data",
        "tm-worked-examples-table1-data",
      ],
    }),
    section({
      title: "Shell-structure and heavy-atom transfer-matrix examples",
      label: "sec:tm-heavy-atom-examples",
      blocks: [
        "tm-heavy-atom-examples-intro",
        "tm-heavy-atom-examples",
        "tm-heavy-atom-examples-table1-data",
        "tm-heavy-atom-examples-table2-data",
        "tm-heavy-atom-examples-table3-data",
        "tm-heavy-atom-examples-table4-data",
        "tm-heavy-atom-examples-table5-data",
        "tm-heavy-atom-examples-table6-data",
        "tm-heavy-atom-examples-table7-data",
        "tm-heavy-atom-examples-table8-data",
      ],
    }),
    section({
      title: "Exact $5_2$ trace-field and Habiro star identities",
      label: "sec:fivetwo-habiro-identities",
      blocks: [
        "habiro-tail-star-identity",
        "fivetwo-trace-field",
        "fivetwo-saddle-sum-rule",
        "fivetwo-bar-odd-arithmetic-home",
        "fivetwo-dt-spectrum-split",
        "fivetwo-stokes-unimodular",
        "fivetwo-level-seven-ladder",
        "fivetwo-three-sevens",
        "fivetwo-envelope-transport",
        "fivetwo-discriminant-vanishes",
      ],
    }),
  ],
});
