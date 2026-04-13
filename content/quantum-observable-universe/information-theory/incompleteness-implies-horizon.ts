import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:incompleteness-implies-horizon",
  title:
    "Turing completeness with $\\mathbb{N}$-embedding implies non-empty computational horizon",
  lean: {
    decl: "QOU.IncompletenessHorizon.exists_noncomputable",
    validation: "not_checked",
  },
  tags: [
    "incompleteness",
    "goedel",
    "turing-completeness",
    "diagonal-argument",
    "computational-horizon",
    "nat-embedding",
    "non-computable",
  ],
  uses: [
    "def:computational-horizon",
    "rem:skein-turing-machine",
  ],
  cites: ["goedel1931", "turing1936"],
});
