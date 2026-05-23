import { proof } from "../../schema/builders";

export default proof({
  label: "prf:brings-is-qou",
  title: "Proof of Bring's surface is a quantum observable universe",
  uses: [
    "prop:brings-is-qou",
    "lem:brings-euler-characteristic",
    "lem:brings-riemann-hurwitz",
  ],
  cites: [
    "woronowicz1987-twisted-su2",
  ],
});
