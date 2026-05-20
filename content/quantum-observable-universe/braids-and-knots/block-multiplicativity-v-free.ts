import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:block-multiplicativity-v-free",
  title:
    "Block-multiplicativity of per-generator V̂ on the disjoint Hecke product",
  lean: {
    ref: "qou:QOU.BraidKnot.BlockMultiplicativityVFree",
    validation: "not_checked",
  },
  uses: [
    "def:ew-interface-knot",
    "prop:atomic-mass-gb-nf",
    "prop:mass-endomorphism-tower",
    "thm:jones-markov-trace",
  ],
  computation: {
    engine: "python",
    script:
      "folio-assistant/computations/binding_block_multiplicative.py",
    witness:
      "folio-assistant/computations/binding-block-multiplicative.witness.json",
    status: "verified",
  },
  tags: [
    "wedderburn",
    "block-multiplicativity",
    "disjoint-hecke-product",
    "constituent-vacuum",
    "interface-knot",
    "scaling",
  ],
});
