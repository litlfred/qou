import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-fourier-exists",
  title: "Existence of the categorical Fourier transform",
  lean: { ref: "qou:QOU.CategoricalFourier.exists",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-fourier",
    "prop:categorical-laplace-exists",
  ],
  proofs: ["prf:categorical-fourier-exists"],
  tags: ["existence", "fourier", "peter-weyl"],
});
