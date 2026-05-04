import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:markov-lambda-knot-operations",
  label: "rem:markov-chain-fluctuations",
  title: "Error bounds for the Markov chain: outer $q$-Plancherel, inner Perron--Frobenius",
  tags: [
    "markov-chain",
    "error-bound",
    "q-plancherel",
    "feray-meliot",
    "perron-frobenius",
    "q-gaussian",
    "caveat",
  ],
  cites: ["feray-meliot2012", "diaconis-ram2000"],
  uses: [
    "rem:markov-lambda-knot-operations",
    "conj:jet-convergence-classical-limit",
    "prop:hecke-convergence-bound",
  ],
});
