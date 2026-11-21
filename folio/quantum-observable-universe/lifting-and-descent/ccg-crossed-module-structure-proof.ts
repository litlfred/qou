import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ccg-crossed-module-structure",
  title: "Proof of the crossed-module structure",
  uses: ["lem:ccg-crossed-module-structure"],
  cites: ["yekutieli2014-descent"],
});
