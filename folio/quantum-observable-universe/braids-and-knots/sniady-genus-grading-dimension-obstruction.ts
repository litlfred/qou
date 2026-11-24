import { remark } from "../../schema/builders";

export default remark({
  label: "rem:sniady-genus-grading-dimension-obstruction",
  title:
    "Genus grading of character observables and the non-polynomiality of hook dimensions",
  interprets: "prop:hecke-satisfies-blitvic-hypothesis",
  uses: ["prop:hecke-satisfies-blitvic-hypothesis"],
  cites: ["sniady2006asymptotics"],
  tags: [
    "symmetric-group",
    "plancherel-measure",
    "free-cumulants",
    "genus-expansion",
    "young-diagrams",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Gives a durable, cited home (`[sniady2006asymptotics]`, Proposition 3.4 and Theorems 4.13–4.14) to the genus-grading scope boundary for the Plancherel Young-diagram covariance kernel (`QOU.BraidsAndKnots.YoungDiagramKernel`, `QOU.BraidsAndKnots.DeltaLambdaDReduction`, `QOU.BraidsAndKnots.WstdSuperExpBound`): normalized character observables such as $\\omega_3$ and $R_4$ lie in the Kerov–Olshanski algebra $\\mathcal{A}$ of polynomial functions on Young diagrams, whereas the hook-length dimension $f^\\lambda$ grows super-polynomially and lies outside $\\mathcal{A}$.",
    },
  ],
});
