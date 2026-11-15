import { remark } from "../../schema/builders";

export default remark({
  label: "rem:body-asymptotics-catalog",
  title:
    "Catalog: body-paper analytic bounds in surreal $\\ordw$-form",
  interprets: "rem:conway-normal-form",
  uses: [
    "prop:hecke-convergence-bound",
    "conj:hoefsmit-scattering-pipeline",
    "prop:jet-tower-convergence",
    "prop:unified-iterative-correction",
    "prop:feynman-classical-limit",
    "prf:mobius-energy",
    "def:surreal-blowup-calculus",
  ],
  tags: [
    "surreal-numbers",
    "asymptotic",
    "valuation",
    "leading-exponent",
    "back-reference",
    "catalog",
    "big-o",
  ],
});
