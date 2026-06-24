import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-baer-star-generic",
  proofs: ["prf:hecke-baer-star-generic"],
  title:
    "Iwahori--Hecke algebra $H_n(q)$ is a Baer-*-ring at generic $q$",
  lean: {
    ref: "qou:QOU.BraidKnot.HeckeBaerStarGeneric.hecke_baer_star_generic",
    validation: "not_checked",
  },
  uses: [
    "prop:explicit-central-idempotent",
    "rem:vc-as-depth-2-instance",
  ],
  cites: [],
  tags: [
    "baer-star",
    "hecke-algebra",
    "wedderburn",
    "bar-involution",
    "projection-generated",
    "annihilator-structure",
    "graded-mikusinski-foundation",
  ],
});
