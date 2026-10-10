import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-fourier-unique",
  title: "Uniqueness of the categorical Fourier transform",
  lean: { ref: "qou:QOU.CategoricalFourier.unique",
    validation: "not_checked",
  },
  uses: [
    "prop:categorical-fourier-exists",
    "prop:categorical-laplace-unique",
  ],
  proofs: ["prf:categorical-fourier-unique"],
  tags: ["uniqueness", "fourier"],
});
