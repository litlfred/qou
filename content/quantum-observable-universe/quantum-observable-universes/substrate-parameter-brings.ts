import { example } from "../../schema/builders";

export default example({
  interprets: "thm:substrate-parameter-exists",
  label: "ex:substrate-parameter-brings",
  title:
    "Constructive extraction of $q$ on Bring's surface",
  tags: ["brings-surface", "substrate-parameter", "constructive", "hecke"],
  uses: [
    "thm:substrate-parameter-exists",
    "ex:brings-surface-concrete",
    "def:substrate-parameter",
  ],
});
