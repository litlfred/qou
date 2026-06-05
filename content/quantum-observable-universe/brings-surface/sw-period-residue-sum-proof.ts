import { proof } from "../../schema/builders";

export default proof({
  label: "prf:sw-period-residue-sum",
  title: "Proof that the Seiberg–Witten period is an algebraic residue sum",
  uses: [
    "prop:sw-period-residue-sum",
    "prop:mi-sw-abelianisation",
  ],
});
