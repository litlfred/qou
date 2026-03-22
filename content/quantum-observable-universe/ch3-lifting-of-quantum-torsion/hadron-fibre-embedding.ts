import { definition } from "../../schema/builders";

export default definition({
  label: "def:hadron-fibre-embedding",
  title: "Fibre-compatible hadron embedding",
  tags: ["hadron", "embedding", "fibre", "mobius-energy", "knot"],
  lean: {
    decl: "QOU.HadronFibreEmbedding",
    validation: "not_checked",
  },
  status: "not_started",
  uses: [
    "def:hadron",
    "def:localized-hadron",
    "def:projective-line-object",
  ],
});
