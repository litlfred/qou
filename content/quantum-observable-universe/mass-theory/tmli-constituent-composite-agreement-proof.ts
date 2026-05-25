import { proof } from "../../schema/builders";

export default proof({
  label: "prf:tmli-constituent-composite-agreement",
  title: "Proof that constituent and composite traces agree",
  uses: ["lem:tmli-constituent-composite-agreement"],
});
