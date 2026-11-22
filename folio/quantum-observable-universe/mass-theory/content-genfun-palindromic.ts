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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): which is proved for\nevery $n$ in the library module `QOU.AntiInvolutionPalindrome`\n(`palindromic_sum_of_antiInvolution` for the palindromy, and\n`first_moment_zero_of_antiInvolution`, $\\sum_\\lambda f^\\lambda\\,\\mathrm{content}(\\lambda) = 0$,\nfor the vanishing linear term). The Lean sibling here records the fully machine-checked\n$n=4$ instance, $C_4(q) = q^6 + 3q^2 + 2 + 3q^{-2} + q^{-6}$." },
  ],
});
