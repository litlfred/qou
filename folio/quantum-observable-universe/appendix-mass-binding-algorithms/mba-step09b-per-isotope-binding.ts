import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:per-isotope-binding",
  title: "Multi-scale per-isotope nuclear binding $B(Z, N)$",
  uses: [
    "prop:delta-lambda-dt-index-unification",
    "rem:term6-binding-density",
    "thm:knot-mass-formula-unified",
    "alg:markov-trace",
    "alg:wedderburn-decomposition",
    "alg:mass-identity",
    "prop:explicit-alpha-k-h4",
    "prop:spin-orbit-magic-closures",
    "prop:linear-chain-bond-count",
    "prop:reeb-pn-magnitude-criticality",
    "conj:reeb-linking-cwf-normalization",
  ],
  tags: [
    "mba",
    "step-9b",
    "binding-energy",
    "simplicial-ball",
    "spin-orbit",
    "temperley-lieb",
    "canonical-chain",
  ],
});
