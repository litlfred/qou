import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:volume-from-rigidity",
  lean: { ref: "qou:QOU.volume_from_rigidity",
    validation: "not_checked",
  },
  title: "Volume form from rigidity and symplectic self-duality",
  uses: ["def:quantum-observable-universe"],
  proofs: ["prf:volume-from-rigidity"],
  examples: ["ex:frobenius-su2", "ex:dagger-su2", "ex:su2-volume-from-rigidity", "rem:spin-half-representation"],
  tags: ["category-theory", "volume"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/volume-from-rigidity-0.svg", blockIndex: 0, hash: "e112e206bddc" },
  ],

});
