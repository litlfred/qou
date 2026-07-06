import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hecke-baer-star-generic",
  label: "rem:hecke-baer-star-generic-interpretation",
  title:
    "Co-location with the volume conjecture and significance for B1 period witnesses",
  tags: [
    "baer-star",
    "hecke-algebra",
    "volume-conjecture",
    "period-classes",
    "wall-crossing",
  ],
  uses: [
    "prop:hecke-baer-star-generic",
    "conj:kashaev-volume-conjecture",
    "rem:vc-as-depth-2-instance",
    "conj:gb-depth-period-correspondence",
  ],
});
