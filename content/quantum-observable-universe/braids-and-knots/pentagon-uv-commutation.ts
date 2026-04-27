import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pentagon-uv-commutation",
  title:
    "Quantum-torus commutation $uv = q\\,vu$ for Hecke traced-volume pairs",
  tags: [
    "pentagon",
    "quantum-dilogarithm",
    "quantum-torus",
    "hecke-algebra",
    "jet-tower",
  ],
  lean: {
    ref: "qou:QOU.QuantumBloch.pentagon_uv_commutation",
    validation: "not_checked",
  },
  uses: [
    "rem:quantum-bloch-group",
    "prop:descended-level-zero",
  ],
  cites: ["kassel1995", "faddeev1994", "kashaev1997"],
});
