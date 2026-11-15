import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-harmonic-form",
  label: "rem:schrodinger-jet-coaction",
  title: "q-Deformed Schrodinger equation",
  tags: ["schrodinger", "q-deformation", "jet-bundle"],
  uses: [
    "ex:q-reeb-vector-field",
    "def:q-harmonic-form",
    "rem:heisenberg-commutator",
    "prop:main-commutative-diagram",
  ],
});
