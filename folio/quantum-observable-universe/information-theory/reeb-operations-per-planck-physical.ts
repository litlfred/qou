import { remark } from "../../schema/builders";

export default remark({
  label: "rem:reeb-operations-per-planck-physical",
  title: "Physical meaning of the Reeb operation count at $q = q_0$",
  interprets: "prop:reeb-operations-per-planck",
  tags: ["reeb", "planck-time", "substrate"],
  uses: ["prop:reeb-operations-per-planck", "prop:local-substrate-q"],
});
