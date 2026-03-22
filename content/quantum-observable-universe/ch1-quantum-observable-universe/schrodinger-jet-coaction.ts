import { remark } from "../../schema/builders";

export default remark({
  label: "rem:schrodinger-jet-coaction",
  title: "q-Deformed Schrodinger equation",
  tags: ["schrodinger", "q-deformation", "jet-bundle"],
  uses: [
    "def:q-reeb-vector-field",
    "def:q-harmonic-form",
    "def:quantum-planck-constant",
    "rem:heisenberg-commutator",
    "prop:main-commutative-diagram",
    "def:quantum-universe",
    "def:quantum-observable-universe",
  ],
});
