import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:jones-markov-trace",
  label: "rem:markov-lambda-jones-plancherel",
  title: "Jones polynomial as a Plancherel sum over $\\lambda$",
  tags: [
    "jones-polynomial",
    "plancherel",
    "wedderburn",
    "syt",
    "classical-quantum-factorisation",
  ],
  cites: ["jones1987"],
  uses: ["rem:markov-lambda-knot-operations"],
});
