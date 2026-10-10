import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-resolvent-properties",
  interprets: "def:q-resolvent",
  title: "Realisations of $R_q(s)$: Laplace characterisation, resolvent identity, Peter--Weyl poles, and base rings",
  tags: ["resolvent", "q-laplacian", "spectral", "hopf-algebra"],
  uses: [
    "def:q-resolvent",
    "def:categorical-laplace",
    "def:categorical-fourier",
    "prop:q-heat-kernel-peter-weyl",
  ],
});
