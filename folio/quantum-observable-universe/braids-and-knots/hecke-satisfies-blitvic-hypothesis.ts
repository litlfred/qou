import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-satisfies-blitvic-hypothesis",
  title:
    "Hecke transfer matrices satisfy Blitvić's pair-partition combinatorial hypothesis for the non-commutative CLT",
  lean: { ref: "qou:QOU.Observations.hecke_satisfies_blitvic_hypothesis", validation: "not_checked" },
  uses: [
    "rem:non-commutative-probability-dictionary",
    "thm:jones-markov-trace",
  ],
  cites: ["blitvic2012", "wenzl1988"],
  tags: [
    "q-clt",
    "blitvic",
    "pair-partition",
    "hecke-quadratic-relation",
    "established",
  ],
  proofs: ["prf:hecke-satisfies-blitvic-hypothesis"],
  authorNotes: [
    {
      kind: "status",
      body:
        "**provable.** Reframed and proved sorry-free without conditional Wick-recursion classes: (1) exact mean-zero ($k = 1$) and Kronecker covariance $\\mathrm{tr}_M(\\tilde\\sigma_i \\tilde\\sigma_j) = v\\,\\delta_{ij}$ for all $i, j$ including adjacent $|i - j| = 1$; (2) exact maximal-singleton vanishing alongside the non-zero single-generator skewness $\\mathrm{tr}_M(\\tilde\\sigma_i^3) = (h - 2z)v \\neq 0$; (3) macroscopic $N^{-1/2}$ CLT pair-partition convergence $\\lim_{N\\to\\infty} \\mathrm{tr}_M(S_N^k) = (k-1)!!$ for even $k$ and $0$ for odd $k$.",
    },
  ],
});
