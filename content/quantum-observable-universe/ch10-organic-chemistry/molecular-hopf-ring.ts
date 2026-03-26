import { definition } from "../../schema/builders";

export default definition({
  label: "def:molecular-hopf-ring",
  title: "Molecular Hopf ring (closed)",
  tags: [
    "molecular",
    "hopf-ring",
    "closed-ring",
    "covalent-bond",
    "linking-matrix",
    "circulant",
    "cyclic",
  ],
  lean: {
    decl: "QOU.Organic.MolecularHopfRing",
    validation: "not_checked",
  },
  uses: [
    "def:molecular-hopf-chain",
    "def:threading-link",
    "def:covalent-bond-types",
    "def:crossing-energy",
    "def:substrate-parameter",
  ],
});
