import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hecke-mass-trace",
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
    "conj:hecke-mass-trace",
    "def:frobenius-pairing",
  ],
});
