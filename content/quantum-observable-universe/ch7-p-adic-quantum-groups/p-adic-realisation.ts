import { example } from "../../schema/builders";

export default example({
  label: "ex:p-adic-realisation",
  title: "$\\mathbb{Q}_\\pp$ realisation",
  uses: [
    "def:substrate-parameter",
    "lem:irreducible-connection",
    "def:quantum-universe",
    "def:quantum-observable-universe",
    "rem:q-torsion-existence",
  ],
});
