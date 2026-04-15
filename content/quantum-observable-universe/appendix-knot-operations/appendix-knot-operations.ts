import { chapter, section } from "../../schema/builders";

/**
 * Appendix: Knot Operation Actions Dictionary.
 *
 * Complete reference for Hecke algebra operations in H₃(q):
 * particle NFs, multiplication table, composite operations,
 * and the gluon model comparison.
 */
export default chapter({
  tabLabel: "K",
  title: "Knot Operation Actions Dictionary",
  label: "app:knot-operations",
  sections: [
    section({
      title: "Particle normal forms",
      label: "sec:particle-nf-table",
      blocks: [
        "particle-nf-table",
      ],
    }),
    section({
      title: "Hecke algebra operations",
      label: "sec:hecke-operations",
      blocks: [
        "hecke-operations",
      ],
    }),
    section({
      title: "Gluon models and nucleon NF",
      label: "sec:gluon-model-comparison",
      blocks: [
        "gluon-model-comparison",
      ],
    }),
    section({
      title: "Knot operator action on basis pairs",
      label: "sec:knot-operator-basis-table",
      blocks: [
        "knot-operator-basis-table",
      ],
    }),
    section({
      title: "Quark-level knot decomposition table",
      label: "sec:quark-level-knot-table",
      blocks: [
        "quark-level-knot-table",
      ],
    }),
  ],
});
