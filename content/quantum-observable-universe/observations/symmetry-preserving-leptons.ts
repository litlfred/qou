import { remark } from "../../schema/builders";

export default remark({
  label: "rem:symmetry-preserving-leptons",
  title: "Symmetry-preserving versus symmetry-broken lepton generators",
  tags: ["leptons", "generations", "symmetry", "s5", "torus-knot"],
  uses: [
    "prop:s5-equivariant-torus-knots",
  ],
  interprets: "prop:s5-equivariant-torus-knots",
});
