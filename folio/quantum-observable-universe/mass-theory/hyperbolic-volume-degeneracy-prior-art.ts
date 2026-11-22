import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hyperbolic-volume-degeneracy-prior-art",
  title: "Prior art: hyperbolic volume does not determine the manifold",
  interprets: "prop:reeb-bundle-complement-equals-volume",
  uses: ["rem:hyperbolic-knot-positive-volume-via-reeb"],
  cites: ["hodgson2012"],
  tags: ["hyperbolic-volume", "volume-degeneracy", "figure-eight", "prior-art", "scope"],
});
