import { proof } from "../../schema/builders";

export default proof({
  label: "prf:vertex-is-exceptional-divisor",
  of: "prop:vertex-is-exceptional-divisor",
  uses: ["prop:vertex-is-exceptional-divisor"],
});
