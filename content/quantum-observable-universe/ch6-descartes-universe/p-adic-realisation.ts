import { example } from "../../schema/builders";

export default example({
  interprets: "def:substrate-parameter",
  label: "ex:p-adic-realisation",
  title: "$\\mathbb{Q}_\\pp$ realisation",
  uses: [
    "ex:irreducible-connection",
    "rem:q-torsion-existence",
  ],
});
