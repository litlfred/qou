import { proof } from "../../schema/builders";

export default proof({
  label: "prf:yekutieli-leading-coefficient",
  title: "Proof that obstruction equals the leading Chebyshev coefficient",
  uses: ["lem:yekutieli-leading-coefficient"],
});
