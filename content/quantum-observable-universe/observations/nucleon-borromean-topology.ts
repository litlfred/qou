import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:nucleon-borromean-topology",
  lean: { ref: "qou:QOU.HadronicMass.nucleon_borromean_topology",
    validation: "not_checked",
  },
  title: "Nucleon Borromean topology and Hopf-link binding",
  tags: ["nucleon", "borromean", "hopf-link", "color-exchange"],
  uses: [],
  proofs: ["prf:nucleon-borromean-topology"],
});
