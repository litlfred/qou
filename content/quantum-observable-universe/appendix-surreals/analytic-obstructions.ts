import { remark } from "../../schema/builders";

export default remark({
  label: "rem:analytic-obstructions",
  title:
    "Analytic obstructions: what breaks under surreal replacement",
  tags: [
    "surreal-numbers",
    "analytic",
    "hilbert-space",
    "measure-theory",
    "hyperbolic-volume",
    "obstruction",
  ],
  interprets: "def:quantum-observable-universe",
  uses: [
    "def:birthday-grading",
    "def:classical-limit-functor",
    "prop:hoefsmit-scattering-pipeline",
    "prf:mobius-energy",
    "rem:kashaev-volume-density",
  ],
  cites: ["alling1987", "conway1976"],
});
