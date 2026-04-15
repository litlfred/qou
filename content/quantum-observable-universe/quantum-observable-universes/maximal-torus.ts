import { definition } from "../../schema/builders";

export default definition({
  label: "def:maximal-torus",
  title: "Maximal torus and weight subcategory",
  lean: {
    decl: "QOU.MaximalTorus",
    validation: "not_checked",
  },
  uses: ["prop:spin-labels"],
  examples: ["ex:maximal-torus-su2"],
  tags: ["torus", "weight"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/maximal-torus-0.svg", blockIndex: 0, hash: "34a7bde324f4" },
  ],

});
