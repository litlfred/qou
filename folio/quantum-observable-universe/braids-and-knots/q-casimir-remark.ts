import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-casimir-remark",
  title: "Normalisation and role of the $q$-Casimir element",
  interprets: "def:q-casimir",
  tags: ["casimir", "quantum-group"],
  uses: [
    "def:q-casimir",
    "prop:q-casimir-exists",
  ],
});
