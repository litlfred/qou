import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-fourier-unique",
  title: "Proof of uniqueness of the categorical Fourier transform",
  uses: ["prop:categorical-fourier-unique"],
});
