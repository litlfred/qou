import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:leray-profile",
  lean: {
    decl: "QOU.FluidDynamics.leray_profile",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title:
    "Self-similar blowup profile: the Leray equations with $\\mathrm{SU}_q(2)$ constraints",
  uses: [
    "thm:ns-singularity-descartes",
    "prop:vorticity-lower-bound",
    "prop:discrete-vortex-spectrum",
    "thm:quantum-peter-weyl",
    "prop:core-levi-form",
    "def:q-navier-stokes",
  ],
  tags: [
    "leray",
    "self-similar",
    "blowup-profile",
    "elliptic",
    "representation-theory",
    "construction",
  ],
});
