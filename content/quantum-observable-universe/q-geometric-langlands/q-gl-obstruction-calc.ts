import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-gl-obstruction-calc",
  lean: { ref: "qou:QOU.q_gl_obstruction_calc", validation: "not_checked" },
  title: "Obstruction to $q$-flatness",
  proofs: ["prf:q-gl-obstruction-calc"],
  // The flatness condition the obstruction is an obstruction TO.
  // def:quantum-characteristic-classes, fixed in the same statement
  // (kappa_0 = e(xi) in H^2(S, G_m)), is omitted: it is already reached
  // through this cone.
  uses: ["def:q-flat-connection"],
  tags: ["geometric-langlands", "yekutieli", "obstruction"],
});
