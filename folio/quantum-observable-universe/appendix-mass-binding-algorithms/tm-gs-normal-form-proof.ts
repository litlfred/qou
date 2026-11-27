import { proof } from "../../schema/builders";

export default proof({
  label: "prf:tm-gs-normal-form",
  title: "Proof of the Hecke-only Gröbner--Shirshov reduction",
  uses: ["prop:tm-gs-normal-form"],
  cites: ["bergman1978"],
  tags: [
    "transfer-matrix",
    "groebner",
    "normal-form",
    "inductive",
    "appendix",
  ],
});
