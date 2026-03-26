import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ring-closure-barrier",
  title: "Ring-closure energy barrier from braid rearrangement",
  tags: [
    "ring-closure",
    "energy-barrier",
    "braid",
    "rearrangement",
    "activation-energy",
    "topological",
    "crossing-energy",
  ],
  uses: [
    "def:molecular-hopf-chain",
    "def:molecular-hopf-ring",
    "def:threading-link",
    "def:crossing-energy",
    "def:covalent-bond-types",
    "def:substrate-parameter",
  ],
});
