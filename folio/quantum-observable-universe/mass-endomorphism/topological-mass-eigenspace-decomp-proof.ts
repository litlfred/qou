import { proof } from "../../schema/builders";

export default proof({
  label: "prf:topological-mass-eigenspace-decomp",
  title: "Proof of the eigenspace decomposition of the mass integrand",
  uses: ["lem:topological-mass-eigenspace-decomp"],
  cites: ["yekutieli2015"],
});
