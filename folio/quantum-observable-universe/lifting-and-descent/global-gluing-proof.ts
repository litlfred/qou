import { proof } from "../../schema/builders";

export default proof({
  label: "prf:global-gluing",
  title: "Proof of global gluing via twisted quantization",
  uses: ["prop:global-gluing"],
  cites: [
    "yekutieli2008",
    "yekutieli2009",
    "yekutieli2015-twisted-dq",
  ],
});
