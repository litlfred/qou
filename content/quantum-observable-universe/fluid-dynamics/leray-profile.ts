import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:leray-profile",
  lean: { ref: "qou:QOU.FluidDynamics.leray_profile", validation: "not_checked" },
  title:
    "Self-similar blowup profile: the Leray equations with $\\mathrm{SU}_q(2)$ constraints",
  uses: ["thm:ns-singularity-descartes"],
  tags: [
    "leray",
    "self-similar",
    "blowup-profile",
    "elliptic",
    "representation-theory",
    "construction",
  ],
});
