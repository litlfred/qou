import { remark } from "../../schema/builders";

export default remark({
  label: "rem:skein-shell-correction",
  interprets: "def:skein-binding-lagrangian",
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
  uses: ["rem:elliptic-stability-locus"],
});
