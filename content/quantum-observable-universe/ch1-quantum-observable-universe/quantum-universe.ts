import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-universe",
  title: "Quantum Universe",
  tags: ["category-theory", "quantum"],
  lean: {
    decl: "QOU.QuantumUniverse",
    file: "QOU/QuantumUniverse.lean",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:rigid-monoidal-category"],
  examples: ["ex:quantum-universe-su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quantum-universe-0.svg", blockIndex: 0, hash: "3f6c739d9d7e" },
    { mime: "image/svg+xml", url: "rendered/quantum-universe-1.svg", blockIndex: 1, hash: "3726e3d8332c" },
  ],

});
