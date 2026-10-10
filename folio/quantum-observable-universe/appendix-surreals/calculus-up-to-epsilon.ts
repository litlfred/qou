import { remark } from "../../schema/builders";

export default remark({
  label: "rem:calculus-up-to-epsilon",
  title:
    "Calculus survives up to $\\varepsilon$: derivatives, integrals, limits",
  tags: [
    "surreal-numbers",
    "calculus",
    "jackson-derivative",
    "standard-part",
    "nonstandard-analysis",
    "infinitesimal",
  ],
  interprets: "def:classical-limit-functor",
  uses: ["def:classical-limit-functor"],
  cites: [
    "berarducci-mantova2018",
    "kuhlmann-matusinski-2012",
    "robinson1966",
    "alling1987",
  ],
});
