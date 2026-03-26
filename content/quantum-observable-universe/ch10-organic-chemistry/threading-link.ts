import { definition } from "../../schema/builders";

export default definition({
  label: "def:threading-link",
  title: "Threading link $T(2,N)$",
  tags: [
    "threading",
    "torus-link",
    "T26",
    "alexander-polynomial",
    "molecular",
    "ring",
    "non-local",
    "correlated",
  ],
  uses: [
    "def:molecular-hopf-chain",
    "def:crossing-energy",
    "def:substrate-parameter",
    "def:covalent-bond-types",
  ],
});
