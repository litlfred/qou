import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:frobenius-pairing",
  title: "Symmetric Frobenius pairing $\\langle a, b\\rangle_F$ on the Frobenius–Hopf aether and $H_n(q)$",
  uses: [
    "def:frobenius-hopf-substrate",
    "def:frobenius-pairing",
    "prop:frobenius-pairing-exists",
    "prop:frobenius-pairing-unique",
    "thm:frobenius-antipode-unifies-chirality-and-tower",
    "alg:gs-reduce-to-hecke-nf",
    "alg:markov-trace",
  ],
  tags: [
    "mba",
    "step-6",
    "frobenius-pairing",
    "self-duality",
    "aether",
    "canonical-chain",
  ],
});
