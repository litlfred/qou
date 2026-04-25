import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-surreal-bound",
  title:
    "Surreal bound for Navier--Stokes: enstrophy transfinite exceeds mass-gap infinitesimal",
  interprets: "prop:blowup-yekutieli",
  uses: [
    "prop:blowup-yekutieli",
    "thm:q-ns-wellposedness",
    "lem:surreal-squeeze",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "prop:surreal-rate-calculus",
    "rem:conway-normal-form",
    "rem:body-asymptotics-catalog",
    "prop:ns-obstruction-computation",
  ],
  tags: [
    "navier-stokes",
    "millennium-problem",
    "surreal",
    "enstrophy",
    "blowup",
    "squeeze",
    "classical-limit",
  ],
  cites: ["conway1976"],
});
