import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-spectral-sobolev",
  lean: { ref: "qou:QOU.FluidDynamics.p1_spectral_sobolev", validation: "not_started" },
  title:
    "Spectral theory and Sobolev embedding for the $q$-Laplacian on $\\Omega^1(A)$",
  uses: [
    "rem:hodge-laplacian-relation",
    "prop:kelvin-dispersion-derivation",
  ],
  tags: [
    "spectral-theory",
    "sobolev",
    "compact-resolvent",
    "q-laplacian",
    "regularity",
    "functional-analysis",
  ],
});
