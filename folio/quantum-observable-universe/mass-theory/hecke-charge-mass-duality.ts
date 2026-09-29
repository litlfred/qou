import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hecke-mass-trace",
  label: "rem:hecke-charge-mass-duality",
  title: "Charge--mass duality via the Frobenius pairing",
  tags: [
    "hecke-algebra",
    "charge",
    "mass",
    "duality",
    "frobenius-pairing",
    "vertex-operator",
  ],
  uses: [
    "def:crossing-energy",
    "prop:hecke-mass-trace",
    "def:frobenius-pairing",
  ],
});
