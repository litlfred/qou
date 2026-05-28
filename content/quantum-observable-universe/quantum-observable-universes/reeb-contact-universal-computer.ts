import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-reeb-derivation",
  label: "rem:reeb-contact-universal-computer",
  title:
    "The Frobenius–Hopf contact structure is a universal computer",
  uses: [
    "rem:reeb-flow-bridge",
    "rem:reeb-turing-completeness",
  ],
  cites: ["cardona2021"],
  tags: [
    "reeb",
    "contact-geometry",
    "frobenius-hopf",
    "universal-computation",
    "miranda",
    "substrate",
  ],
});
