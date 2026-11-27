import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bring-map-euler-characteristic",
  title: "Proof of the Euler characteristic of the Bring map",
  uses: ["lem:bring-map-euler-characteristic"],
});
