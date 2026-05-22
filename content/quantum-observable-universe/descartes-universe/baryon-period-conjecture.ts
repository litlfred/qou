import { remark } from "../../schema/builders";

export default remark({
  label: "rem:baryon-period-ratio",
  title:
    "Proton--electron mass ratio as a corollary of the SW-period equivalence",
  interprets: "prop:sw-period-thimble-equivalence",
  tags: [
    "baryon",
    "mass-ratio",
    "proton",
    "electron",
    "corollary",
    "exposition",
  ],
  uses: [
    "prop:sw-period-thimble-equivalence",
    "conj:mobius-limit-from-thimble",
    "rem:picard-lefschetz-thimble",
  ],
});
