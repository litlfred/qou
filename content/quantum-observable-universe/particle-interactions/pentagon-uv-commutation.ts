import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pentagon-uv-commutation",
  title:
    "Pentagon identity at adjacent jet levels: $\\widehat U \\widehat V = q\\,\\widehat V \\widehat U$",
  tags: [
    "pentagon",
    "quantum-dilogarithm",
    "quantum-torus",
    "hecke-algebra",
    "jet-tower",
    "brane-tower",
  ],
  lean: {
    ref: "qou:QOU.QuantumBloch.pentagon_uv_commutation",
    validation: "not_checked",
  },
  uses: [
    "rem:quantum-bloch-group",
    "lem:vhat-pair-commutation-trace",
    "rem:mass-endomorphism-jet-tower",
    "prop:jet-tower-convergence",
    "prop:descended-level-zero",
  ],
  cites: ["kassel1995", "faddeev1994", "kashaev1997"],
});
