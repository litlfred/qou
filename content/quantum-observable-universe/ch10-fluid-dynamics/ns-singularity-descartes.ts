import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ns-singularity-descartes",
  title:
    "The Descartes universe is NS-singular: Navier--Stokes admits finite-time blowup",
  uses: [
    "thm:observability-q-independent",
    "def:ns-regular-qou",
    "def:substrate-line-bundle",
    "prop:ns-obstruction-tower",
    "prop:ns-kummer-specialisation",
    "thm:qu-to-qou",
    "thm:q-ns-wellposedness",
    "thm:q-aubin-lions",
    "prop:vorticity-lower-bound",
    "thm:q-bkm",
    "prop:core-levi-form",
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
