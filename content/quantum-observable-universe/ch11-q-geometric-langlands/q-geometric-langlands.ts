import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-geometric-langlands",
  title: "$q$-Geometric Langlands correspondence",
  uses: [
    "def:q-local-system",
    "def:q-hecke-eigensheaf",
    "def:q-langlands-dual",
    "def:q-flat-connection",
  ],
  cites: ["frenkel2007", "aganagic2017"],
  tags: ["geometric-langlands", "q-deformation", "main-conjecture"],
});
