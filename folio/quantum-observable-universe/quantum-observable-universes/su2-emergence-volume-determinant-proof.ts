import { proof } from "../../schema/builders";

export default proof({
  label: "prf:su2-emergence-volume-determinant",
  title: "Proof: volume constraint forces $\\det(g_V) = 1$",
  uses: ["lem:su2-emergence-volume-determinant", "def:quantum-observable-universe"],
});
