import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:content-genfun-palindromic",
  lean: {
    ref: "qou:QOU.Mass.ContentGenfun.C4_palindromic",
  },
  title:
    "The content generating function $C_n(q) = \\sum_\\lambda f^\\lambda q^{\\mathrm{content}(\\lambda)}$ is palindromic and bar-even",
  uses: [
    "prop:binding-period-involution-statistic",
  ],
  proofs: ["prf:content-genfun-palindromic"],
});
