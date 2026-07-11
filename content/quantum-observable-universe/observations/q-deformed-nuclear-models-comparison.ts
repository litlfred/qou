import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-deformed-nuclear-models-comparison",
  title:
    "$q$-deformed nuclear and atomic models ($\\mathrm{SU}_q(2)$ rotor, $q$-oscillator, Elliott $\\mathrm{SU}(3)$)",
  interprets: "prop:magic-numbers-from-q",
  uses: ["def:q-angular-momentum", "prop:shell-schur-weyl-self-duality"],
  cites: ["minkov1996", "raychev1998", "mayer1955", "elliott1958"],
  tags: [
    "magic-numbers",
    "quantum-groups",
    "su_q_2-rotor",
    "q-deformed-oscillator",
    "elliott-su3",
    "literature-comparison",
    "interpretation",
  ],
});
