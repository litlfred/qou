import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:baryon-period-ratio",
  title:
    "Proton--electron mass ratio from Picard--Lefschetz thimble periods",
  tags: [
    "picard-lefschetz",
    "baryon",
    "mass-ratio",
    "proton",
    "electron",
    "seiberg-witten",
    "thimble",
    "open-problem",
  ],
  uses: ["rem:picard-lefschetz-thimble"],
});
