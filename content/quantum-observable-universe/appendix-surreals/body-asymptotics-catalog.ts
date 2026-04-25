import { remark } from "../../schema/builders";

export default remark({
  label: "rem:body-asymptotics-catalog",
  title:
    "Catalog: body-paper analytic bounds in surreal $\\ordw$-form",
  interprets: "rem:conway-normal-form",
  uses: [
    "rem:conway-normal-form",
    "def:standard-part-functor",
    "def:surreal-blowup-calculus",
    "rem:calculus-up-to-epsilon",
    "prop:hecke-convergence-bound",
    "prop:hoefsmit-scattering-pipeline",
    "prop:jet-tower-convergence",
    "prop:unified-iterative-correction",
    "prop:universal-braid-branching",
    "prop:ns-obstruction-computation",
    "rem:kashaev-volume-density",
    "prop:feynman-classical-limit",
    "prf:mobius-energy",
    "rem:mass-endomorphism-jet-tower",
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
