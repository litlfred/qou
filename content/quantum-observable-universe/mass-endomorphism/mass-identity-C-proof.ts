import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mass-identity-C",
  title: "Proof of archimedean mass identity",
  uses: ["cor:mass-identity-C"],
  cites: [
    "yekutieli2015",
  ],
});
