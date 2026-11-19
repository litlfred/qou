import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:gs-reduce-to-hecke-nf",
  title: "Gröbner–Shirshov reduction to reduced Coxeter normal form",
  uses: [
    "def:hecke-normal-form",
    "def:categorical-action",
    "alg:categorical-action",
  ],
  tags: [
    "mba",
    "step-2",
    "gs-reducer",
    "hecke-normal-form",
    "transfer-matrix",
    "canonical-chain",
  ],
});
