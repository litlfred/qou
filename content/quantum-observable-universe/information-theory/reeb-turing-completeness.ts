import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:quantum-computational-universality",
  label: "rem:reeb-turing-completeness",
  title:
    "Universal computation in 3D contact geometry: Cardona–Miranda–Peralta-Salas–Presas",
  uses: [
    "prop:reeb-turing-completeness-classical",
    "def:categorical-reeb-derivation",
    "def:computational-horizon",
    "def:observable-mtc",
    "prop:toffoli-transfer-matrix",
    "rem:skein-turing-machine",
  ],
  cites: ["cardona2021", "cardona2023", "tao2019"],
  tags: [
    "reeb-flow",
    "turing-completeness",
    "contact-geometry",
    "universal-computation",
    "information-theory",
    "miranda",
  ],
});
