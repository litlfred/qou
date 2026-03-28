import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:skein-shell-correction",
  title:
    "Shell corrections from Skein polynomial factorization of the multi-nucleon link",
  tags: [
    "shell-correction",
    "skein-polynomial",
    "factorization",
    "stability-pairs",
    "closed-sublink",
    "binding-energy",
  ],
  uses: ["conj:elliptic-stability-locus"],
});
