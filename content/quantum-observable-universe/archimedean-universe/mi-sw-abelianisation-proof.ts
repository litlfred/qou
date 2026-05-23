import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mi-sw-abelianisation",
  title: "Proof of Abelianisation of the MI integral on exceptional divisors",
  uses: [
    "prop:mi-sw-abelianisation",
    "lem:mi-sw-abelianisation-cartan",
  ],
});
