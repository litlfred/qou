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
    "prop:reeb-bundle-complement-equals-volume",
    "rem:garside-as-compound-flow",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/figure_eight_kashaev_volume.py",
    witness: "computations/figure-eight-kashaev-volume.witness.json",
    status: "verified",
  },
});
