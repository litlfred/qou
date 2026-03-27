import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:magnetic-friction",
  title: "Non-monotonic magnetic friction from collective rotor dynamics",
  uses: ["ex:q-torsion-leaf", "def:substrate-parameter", "def:q-harmonic-form"],
  tags: ["friction", "lattice", "observation"],
});
