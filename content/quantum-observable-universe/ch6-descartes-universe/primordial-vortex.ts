import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-planck-constant",
  label: "rem:primordial-vortex",
  title: "Primordial vortex and the deep-quantum limit",
  uses: [
    "def:quantum-planck-constant",
    "ex:q-torsion-leaf",
    "rem:heisenberg-commutator",
  ],
});
