import { remark } from "../../schema/builders";

export default remark({
  label: "rem:schrodinger-jet-coaction",
  title: "q-Deformed Schrödinger equation",
  tags: ["schrodinger", "q-deformed", "physics"],
  uses: [
    "def:q-reeb-vector-field",
    "def:quantum-planck-constant",
    "def:q-harmonic-form",
    "rem:heisenberg-commutator",
    "prop:main-commutative-diagram",
    "def:quantum-universe",
    "def:quantum-observable-universe",
  ],
});
