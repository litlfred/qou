import { remark } from "../../schema/builders";

export default remark({
  label: "rem:frobenius-simplification",
  title: "Frobenius structure of the C gauge algebra",
  tags: ["frobenius", "hopf-algebra", "gauge-theory"],
  uses: [
    "def:quantum-universe",
    "def:quantum-observable-universe",
    "def:c-quantum-universe",
    "def:c-quantum-observable-universe",
    "def:instanton",
    "lem:irreducible-connection",
    "rem:q-torsion-existence",
  ],
});
