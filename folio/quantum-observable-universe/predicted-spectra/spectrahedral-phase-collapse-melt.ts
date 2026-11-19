import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:spectrahedral-phase-collapse",
  label: "rem:spectrahedral-phase-collapse-melt",
  title: "The cosmological melt: topological hierarchy of dissolution thresholds",
  uses: ["prop:spectrahedral-phase-collapse", "rem:deconfinement-golden-threshold"],
  computation: {
    engine: "python+mpmath",
    script: "computations/hecke/h3_gram_degeneracy_is_wedderburn_weight_vanishing.py",
    witness: [
      "computations/hecke/h3-gram-degeneracy-is-wedderburn-weight-vanishing.witness.json",
      "computations/qbeta/qbeta-admissible-functional-hierarchy.witness.json",
    ],
    status: "verified",
  },
});
