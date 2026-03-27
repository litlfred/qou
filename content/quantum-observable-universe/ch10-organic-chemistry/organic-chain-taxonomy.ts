import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:molecular-hopf-chain",
  label: "rem:organic-chain-taxonomy",
  title: "Organic chain taxonomy from bond-order patterns",
  tags: [
    "alkane",
    "alkene",
    "alkyne",
    "bond-order",
    "taxonomy",
    "organic",
    "chain",
    "saturated",
    "unsaturated",
  ],
  uses: [
    "def:molecular-hopf-chain",
    "def:molecular-hopf-ring",
    "def:covalent-bond-types",
    "rem:carbon-valence",
  ],
});
