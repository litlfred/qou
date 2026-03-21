import { remark } from "../../schema/builders";

export default remark({
  label: "rem:magnetic-friction",
  title: "Non-monotonic magnetic friction from collective rotor dynamics",
  uses: ["def:q-torsion-leaf", "def:substrate-parameter", "def:q-harmonic-form"],
  tags: ["friction", "lattice", "observation"],
});
