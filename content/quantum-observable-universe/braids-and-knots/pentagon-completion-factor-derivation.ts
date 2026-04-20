import { remark } from "../../schema/builders";

export default remark({
  label: "rem:pentagon-completion-factor-derivation",
  title:
    "Theoretical derivation of the pentagon-completion factor $\\rho(\\lambda, A)$",
  interprets: "prop:tower-binding-energy",
  uses: [
    "prop:tower-binding-energy",
    "prop:pentagon-ascension-bound",
    "prop:single-vortex-to-log-form-reduction",
    "def:quantum-bloch-group",
  ],
  tags: [
    "pentagon-identity",
    "wedderburn",
    "r-factor",
    "rho-derivation",
    "quantum-dilogarithm",
  ],
});
