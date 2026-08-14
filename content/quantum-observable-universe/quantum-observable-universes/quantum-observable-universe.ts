import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-observable-universe",
  title: "Quantum Observable Universe",
  tags: ["quantum", "observable", "category-theory"],
  lean: { ref: "qou:QOU.QuantumObservableUniverse",
    validation: "not_checked",
  },
  // def:rigid-monoidal-category + def:snake-identity added 2026-08-14:
  // rigidity moved down from def:quantum-universe (which is now braided
  // only) and is condition 1 here, so this block now depends directly on
  // the rigid structure and on the snake identities it cites.
  uses: [
    "def:quantum-universe",
    "def:rigid-monoidal-category",
    "def:snake-identity",
    "unital-groebner-bases:def:admissible-system",
  ],
  examples: ["ex:qou-su2", "ex:c-quantum-observable-universe", "ex:c-quantum-universe", "rem:yekutieli-stokes"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quantum-observable-universe-0.svg", blockIndex: 0, hash: "6d717475f32e" },
    { mime: "image/svg+xml", url: "rendered/quantum-observable-universe-1.svg", blockIndex: 1, hash: "198957633587" },
  ],

});
