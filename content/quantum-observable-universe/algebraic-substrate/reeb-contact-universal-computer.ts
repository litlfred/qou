import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-reeb-derivation",
  label: "rem:reeb-contact-universal-computer",
  title:
    "The Frobenius–Hopf contact structure is a universal computer",
  uses: [
    "def:categorical-reeb-derivation",
    "def:frobenius-hopf-substrate",
    "rem:reeb-flow-bridge",
    "rem:reeb-turing-completeness",
    "rem:skein-turing-machine",
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
