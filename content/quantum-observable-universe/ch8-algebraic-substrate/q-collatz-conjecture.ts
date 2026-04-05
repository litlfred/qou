import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-collatz",
  title:
    "The $q$-deformed Collatz conjecture via Hecke interpolation",
  uses: [
    "prop:skein-generation",
    "def:local-q-zeta-function",
    "thm:tannaka-krein-isomorphism",
    "conj:classical-riemann-hypothesis",
    "def:frobenius-hopf-substrate",
  ],
  tags: [
    "collatz",
    "hecke-algebra",
    "number-theory",
    "q-deformation",
    "skein-relation",
    "dynamical-system",
    "categorical",
  ],
  cites: ["collatz1937", "lagarias2010"],
});
