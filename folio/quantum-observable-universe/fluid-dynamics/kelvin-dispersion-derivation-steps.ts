import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:kelvin-dispersion-derivation",
  label: "rem:kelvin-dispersion-derivation-steps",
  title: "Derivation of the Kelvin dispersion from the $q$-Laplacian eigenvalue problem",
  uses: ["prop:kelvin-dispersion-derivation", "def:q-navier-stokes"],
  tags: ["kelvin-wave", "dispersion", "q-laplacian", "eigenvalue", "derivation"],
});
