import { proof } from "../../schema/builders";

export default proof({
  label: "prf:su2-emergence-dagger-unitarity",
  title: "Proof: Frobenius dagger forces $G \\subseteq \\mathrm{U}(2)$",
  uses: ["lem:su2-emergence-dagger-unitarity"],
});
