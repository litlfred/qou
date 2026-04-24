import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-surreal-bound",
  title:
    "Surreal bound for Navier--Stokes: enstrophy transfinite exceeds mass-gap infinitesimal",
  interprets: "prop:blowup-yekutieli",
  uses: ["lem:surreal-squeeze"],
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
