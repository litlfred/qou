import { example } from "../../schema/builders";

export default example({
  interprets: "thm:aether-parameter-exists",
  label: "ex:aether-parameter-brings",
  renamedFrom: ["ex:substrate-parameter-brings"],
  title:
    "Constructive extraction of $q$ on Bring's surface",
  tags: ["brings-surface", "substrate-parameter", "constructive", "hecke"],
  uses: [
    "ex:brings-surface-concrete",
    "rem:skein-mass-relation",
  ],
});
