import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:joint-galois-braid-discharged",
  label: "rem:joint-galois-braid-discharged-interpretation",
  title:
    "The joint-action conjecture was open in form, not content — what its discharge completes",
  uses: [
    "prop:joint-galois-braid-discharged",
    "conj:joint-galois-braid-figure-8-verified",
    "conj:joint-galois-braid-action",
    "conj:gb-depth-period-correspondence",
    "prop:hecke-baer-star-generic",
    "prop:explicit-central-idempotent",
    "prop:two-filtration-bridge-small-cases",
    "def:hq-bi-filtration",
  ],
});
