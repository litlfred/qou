import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-harmonic-form",
  label: "rem:magnetic-friction",
  title: "Non-monotonic magnetic friction from collective rotor dynamics",
  uses: [
    "ex:q-torsion-leaf",
    "def:q-harmonic-form",
  ],
  tags: ["friction", "lattice", "observation"],
});
