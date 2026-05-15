import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-causal-action-structure",
  title:
    "Algebraic causal-action structure on $H_n(R, q)$: Markov trace = Plancherel integral + LP active set",
  lean: {
    ref: "qou:QOU.Observations.AlgebraicCausalActionStructure",
    validation: "not_checked",
  },
  uses: [
    "thm:jones-markov-trace",
    "prop:wedderburn-weight-canonical",
    "prop:plancherel-term-7-formulation",
    "prop:operator-selection-lp",
  ],
  cites: [
    "finster2021",
    "finster2024",
    "wenzl1988",
  ],
  tags: [
    "causal-fermion-systems",
    "algebraic-side",
    "plancherel",
    "wedderburn-weight",
    "markov-trace",
    "lp-duality",
    "shadow-price",
    "pre-archimedean",
  ],
  proofs: ["prf:algebraic-causal-action-structure"],
});
