import { proof } from "../../schema/builders";

export default proof({
  label: "prf:brings-is-qou",
  title: "Proof of Bring's surface is a quantum observable universe",
  uses: [
    "prop:brings-is-qou",
    "prop:euler-char-stability",
    "lem:brings-euler-characteristic",
    "lem:brings-riemann-hurwitz",
  ],
});
