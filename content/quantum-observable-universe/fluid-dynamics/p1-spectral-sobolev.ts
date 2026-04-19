import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-spectral-sobolev",
  lean: {
    decl: "QOU.FluidDynamics.q_spectral_sobolev",
    validation: "not_checked",
  },
  title:
    "Spectral theory and Sobolev embedding for the $q$-Laplacian on $\\Omega^1(A)$",
  uses: [
    "def:q-navier-stokes",
    "def:quantum-observable-universe",
    "def:categorical-q-ext-deriv",
    "def:frobenius-pairing",
    "rem:q-laplacian-interpretation",
    "rem:hodge-laplacian-relation",
    "rem:q-codifferential-formula",
    "prop:kelvin-dispersion-derivation",
    "def:q-hodge-star",
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
