import { proof } from "../../schema/builders";

export default proof({
  label: "prf:sw-classical-jet-exactness",
  title: "Proof that the classical-jet prolongation is exact and period-free",
  uses: [
    "prop:sw-classical-jet-exactness",
    "prop:sw-period-residue-sum",
  ],
});
