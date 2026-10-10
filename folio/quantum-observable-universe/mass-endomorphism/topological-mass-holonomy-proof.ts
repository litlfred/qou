import { proof } from "../../schema/builders";

export default proof({
  label: "prf:topological-mass-holonomy",
  title: "Proof that the descended term equals the unknot-core holonomy",
  uses: ["lem:topological-mass-holonomy"],
  cites: ["yekutieli2015"],
});
