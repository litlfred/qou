import { chapter, section } from "../../schema/builders";

export default chapter({
  title: "Riemann Hypothesis Framing",
  label: "chap:riemann-hypothesis-framing",
  sections: [
    section({
      title: "Local curve zeta functions versus global $L$-functions and $\\zeta(s)$",
      label: "sec:riemann-hypothesis-framing",
      blocks: [
        "riemann-hypothesis-framing-intro",
        "classical-riemann-hypothesis",
        "adelic-critical-line-persistence",
        "macroscopic-stability-equivalence",
        "rh-reeb-spectral-dictionary",
        "rh-surreal-bound",
      ],
    }),
  ],
});
