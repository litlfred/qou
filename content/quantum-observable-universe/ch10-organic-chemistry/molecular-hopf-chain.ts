import { definition } from "../../schema/builders";

export default definition({
  label: "def:molecular-hopf-chain",
  title: "Molecular Hopf chain (open)",
  tags: [
    "molecular",
    "hopf-chain",
    "open-chain",
    "covalent-bond",
    "linking-matrix",
    "tridiagonal",
    "spring",
  ],
  uses: [
    "def:covalent-bond-types",
    "def:crossing-energy",
    "def:hadron",
    "def:stable-nucleus",
  ],
});
