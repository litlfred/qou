import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-baer-star-generic",
  title:
    "Iwahori--Hecke algebra $H_n(q)$ is a Baer-*-ring at generic $q$",
  lean: {
    ref: "qou:QOU.BraidKnot.HeckeBaerStarGeneric.hecke_baer_star_generic",
    validation: "not_checked",
  },
  uses: [
    "prop:wedderburn-weight-canonical",
    "prop:hoefsmit-seminormal-form",
    "prop:frobenius-gram-matrix",
    "prop:explicit-central-idempotent",
    "conj:gb-depth-period-correspondence",
    "conj:kashaev-volume-conjecture",
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
