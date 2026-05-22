import { proof } from "../../schema/builders";

export default proof({
  label: "prf:chebyshev-degree-genus",
  title: "Proof that Chebyshev degree equals Seifert genus",
  uses: ["lem:chebyshev-degree-genus"],
});
