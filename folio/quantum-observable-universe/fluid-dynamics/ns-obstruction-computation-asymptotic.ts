import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-obstruction-computation-asymptotic",
  title: "Formal asymptotic content of the jet divergence",
  interprets: "prop:ns-obstruction-computation",
  uses: [
    "def:surreal-blowup-calculus",
    "def:standard-part-functor",
    "rem:conway-normal-form",
    "rem:body-asymptotics-catalog",
  ],
  tags: ["navier-stokes", "asymptotics", "surreal", "blowup"],
});
