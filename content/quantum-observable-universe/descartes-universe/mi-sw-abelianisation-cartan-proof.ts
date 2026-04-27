import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mi-sw-abelianisation-cartan",
  title: "Proof that the Cartan component recovers the SW differential",
  uses: ["lem:mi-sw-abelianisation-cartan"],
});
