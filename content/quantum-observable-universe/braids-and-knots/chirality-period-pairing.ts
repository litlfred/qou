import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chirality-period-pairing",
  title:
    "Chirality structure on Goncharov period classes via the bar involution",
  interprets: "prop:hecke-baer-star-generic",
  uses: [
    "prop:hecke-baer-star-generic",
    "prop:explicit-central-idempotent",
    "conj:gb-depth-period-correspondence",
    "rem:figure-8-archimedean-illustration",
    "conj:bring-trilog-depth-3-witness",
  ],
  cites: ["bloch2000"],
  tags: [
    "chirality",
    "amphichirality",
    "bar-involution",
    "period-pairing",
    "chern-simons",
    "tate-twist",
    "graded-mikusinski",
  ],
});
