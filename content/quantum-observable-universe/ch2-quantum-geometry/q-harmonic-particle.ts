import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-harmonic-form",
  label: "rem:q-harmonic-particle",
  title: "Particles as $q$-harmonic forms: the logical chain",
  uses: [
    "def:q-harmonic-form",
    "def:categorical-q-ext-deriv",
    "rem:q-codifferential-formula",
    "rem:hodge-laplacian-relation",
  ],
  tags: ["particle", "harmonic", "pedagogy"],
});
