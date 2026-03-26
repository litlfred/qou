import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hodge-laplacian-relation",
  title: "Self-adjointness of the $q$-Laplacian",
  uses: ["def:q-harmonic-form", "def:q-hodge-star", "rem:q-codifferential-formula"],
  tags: ["hodge", "laplacian", "self-adjoint"],
});
