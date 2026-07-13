import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-universe",
  title: "Quantum Universe",
  tags: ["category-theory", "quantum"],
  lean: { ref: "qou:QOU.QuantumUniverse",
    validation: "not_checked",
  },
  uses: ["def:rigid-monoidal-category", "def:frobenius-hopf-substrate"],
  examples: ["ex:quantum-universe-su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quantum-universe-0.svg", blockIndex: 0, hash: "7d5b5776ad75" },
  ],

});
