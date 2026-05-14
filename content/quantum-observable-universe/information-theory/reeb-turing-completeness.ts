import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:quantum-computational-universality",
  label: "rem:reeb-turing-completeness",
  title:
    "Universal computation in 3D contact geometry: Cardona–Miranda–Peralta-Salas–Presas",
  uses: [
    "def:categorical-reeb-derivation",
    "prop:reeb-operations-per-planck",
    "rem:skein-turing-machine",
  ],
  cites: ["cardonamirandaperaltasalaspresas2021", "cardonamirandaperaltasalas2023", "tao2019"],
  tags: [
    "reeb-flow",
    "turing-completeness",
    "contact-geometry",
    "universal-computation",
    "information-theory",
    "miranda",
  ],
});
