import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-surreal-bound",
  title:
    "Surreal rate comparison in the $q \\to 1^+$ limit: cascade ceiling versus viscous gap",
  interprets: "prop:blowup-yekutieli",
  uses: ["prop:blowup-yekutieli", "conj:critical-exponent"],
  tags: [
    "navier-stokes",
    "surreal",
    "enstrophy",
    "blowup",
    "squeeze",
    "classical-limit",
  ],
  cites: ["conway1976"],
});
