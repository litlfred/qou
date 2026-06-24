import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-mass-markov",
  proofs: ["prf:categorical-mass-markov"],
  title: "Categorical mass as Markov trace",
  uses: [],
  tags: [
    "mass",
    "categorical-trace",
    "markov-trace",
    "frobenius",
    "nakayama",
    "hecke-algebra",
  ],
  lean: { ref: "qou:QOU.CategoricalMassMarkov",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    script: "computations/canonical_isospin_pyhecke.py",
    witness:
      "computations/canonical-isospin-pyhecke.witness.json",
    status: "verified",
    requires: ["pyhecke"],
  },
});
