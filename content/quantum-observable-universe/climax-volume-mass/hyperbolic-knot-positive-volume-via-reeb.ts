import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:reeb-bundle-complement-equals-volume",
  label: "rem:hyperbolic-knot-positive-volume-via-reeb",
  title:
    "Garside / Borromean trajectories have positive hyperbolic volume via Reeb",
  tags: [
    "hyperbolic-volume",
    "borromean-rings",
    "jsj-decomposition",
    "garside-element",
    "reeb-flow",
    "figure-eight",
  ],
  uses: [
    "prop:six-canonical-knot-operators",
    "prop:reeb-bundle-complement-equals-volume",
    "prop:thurston-volume-additivity",
    "rem:garside-as-compound-flow",
  ],
});
