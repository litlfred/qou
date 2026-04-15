import { definition } from "../../schema/builders";

export default definition({
  label: "def:hadron-fibre-embedding",
  title: "Fibre-compatible hadron embedding",
  tags: ["hadron", "embedding", "fibre", "mobius-energy", "knot"],
  lean: {
    decl: "QOU.HadronFibreEmbedding",
    validation: "not_checked",
  },
  uses: ["def:localized-hadron"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/hadron-fibre-embedding-0.svg", blockIndex: 0, hash: "01e2ca9922f0" },
  ],

});
