import { definition } from "../../schema/builders";

export default definition({
  label: "def:involutive-structure",
  title: "Involutive structure ($\\ast$-structure)",
  lean: { ref: "qou:QOU.InvolutiveStructure",
    validation: "not_checked",
  },
  uses: ["def:rigid-monoidal-category"],
  examples: ["ex:involutive-structure-example", "ex:dagger-su2"],
  tags: ["category-theory", "involutive"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/involutive-structure-0.svg", blockIndex: 0, hash: "2f4b328e0484" },
    { mime: "image/svg+xml", url: "rendered/involutive-structure-1.svg", blockIndex: 1, hash: "da7c73b14216" },
  ],

});
