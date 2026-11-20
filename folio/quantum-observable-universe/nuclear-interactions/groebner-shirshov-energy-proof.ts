import { proof } from "../../schema/builders";

export default proof({
  label: "prf:groebner-shirshov-energy",
  title: "Proof of groebner shirshov energy",
  uses: ["thm:groebner-shirshov-energy", "def:hecke-normal-form"],
});
