import { remark } from "../../schema/builders";

export default remark({
  label: "rem:motivic-substrate-canonicity",
  title: "Canonicity, realizations, and scope of the motivic aether",
  interprets: "def:motivic-substrate",
  tags: [
    "motivic",
    "substrate",
    "realization-tower",
    "adelic",
    "habiro",
  ],
  uses: [
    "def:motivic-substrate",
    "def:frobenius-hopf-substrate",
    "def:adelic-substrate",
    "def:arc-space",
    "def:motivic-mass-measure",
  ],
  cites: ["kontsevich1995", "denef-loeser2001"],
});
