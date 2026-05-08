import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ns-singularity-descartes",
  title:
    "The Descartes universe is NS-singular: Navier--Stokes admits finite-time blowup",
  uses: [
    "thm:observability-q-independent",
    "prop:ns-kummer-specialisation",
  ],
  tags: [
    "theorem",
    "navier-stokes",
    "blowup",
    "descartes",
    "millennium-problem",
    "categorical",
  ],
});
