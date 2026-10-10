import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:reeb-bundle-complement-equals-volume",
  label: "rem:torus-knot-zero-volume-via-reeb",
  title: "Torus-knot trajectories have zero hyperbolic volume via Reeb",
  tags: [
    "torus-knot",
    "hyperbolic-volume",
    "jsj-decomposition",
    "seifert-fibered",
    "3-cycle",
    "reeb-flow",
  ],
  uses: ["prop:reeb-bundle-complement-equals-volume"],
  cites: ["murakami2004a"],
});
