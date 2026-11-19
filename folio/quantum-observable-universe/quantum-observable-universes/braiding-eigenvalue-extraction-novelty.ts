import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braiding-eigenvalue-extraction-novelty",
  interprets: "prop:braiding-eigenvalue-extraction",
  cites: ["kassel1995"],
  title: "Mathematical novelty: $q$ is extracted, not posited",
  tags: ["braiding", "eigenvalue", "substrate-parameter", "categorical"],
  uses: [
    "prop:braiding-eigenvalue-extraction",
    "prop:tannaka-krein-reconstruction",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/fibre_functor_dimension_not_categorical_probe.py",
    witness: "computations/probes/fibre-functor-dimension-not-categorical-probe.witness.json",
    status: "verified",
  },
});
