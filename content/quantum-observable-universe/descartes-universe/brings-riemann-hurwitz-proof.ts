import { proof } from "../../schema/builders";

export default proof({
  label: "prf:brings-riemann-hurwitz",
  title: "Proof of the Riemann--Hurwitz count for $\\Sigma_4 \\to \\mathbb{P}(V)$",
  uses: ["lem:brings-riemann-hurwitz"],
});
