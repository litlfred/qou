import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:skein-shell-correction",
  title:
    "Shell corrections from Skein polynomial factorization of the multi-nucleon link",
  lean: {
    ref: "qou:QOU.SkeinShellCorrection.SkeinShellCorrection",
    validation: "not_checked",
  },
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
