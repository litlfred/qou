import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quantum-dilogarithm-volume-motivation",
  title: "Three volumes of a knot: hyperbolic, Hecke weight, and dilogarithm",
  interprets: "prop:quantum-dilogarithm-volume",
  uses: ["prop:quantum-dilogarithm-volume", "thm:markov-trace-factorization"],
});
