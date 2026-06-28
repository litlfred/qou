import { proof } from "../../schema/builders";

export default proof({
  label: "prf:toffoli-lp-stability",
  title: "Proof of toffoli lp stability",
  uses: ["prop:toffoli-lp-stability"],
});
