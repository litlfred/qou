import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-ns-nonlinear-uniqueness",
  title:
    "Nonlinear estimates and uniqueness for the $q$-Navier--Stokes system",
  uses: [
    "prop:q-spectral-sobolev",
    "thm:q-ns-wellposedness",
  ],
  tags: [
    "nonlinear-estimate",
    "uniqueness",
    "enstrophy",
    "gronwall",
    "energy-method",
    "regularity",
  ],
});
