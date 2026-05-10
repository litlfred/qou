import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:explicit-central-idempotent",
  title:
    "Explicit central primitive idempotents $e_\\lambda$ via Murphy elements",
  uses: [
    "prop:hoefsmit-seminormal-form",
    "prop:hecke-baer-star-generic",
    "conj:gb-depth-period-correspondence",
    "conj:bring-figure-eight-depth-2-witness",
  ],
  cites: [],
  tags: [
    "central-idempotent",
    "murphy-elements",
    "lagrange-interpolation",
    "hecke-algebra",
    "explicit-formula",
    "computability",
  ],
});
