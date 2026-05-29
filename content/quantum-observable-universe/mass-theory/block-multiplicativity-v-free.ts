import { remark } from "../../schema/builders";

export default remark({
  label: "rem:block-multiplicativity-v-free",
  interprets: "prop:atomic-mass-gb-nf",
  title:
    "Block-multiplicativity of per-generator V̂ on the disjoint Hecke product",
  lean: {
    ref: "qou:QOU.BraidKnot.BlockMultiplicativityVFree",
    validation: "not_checked",
  },
  uses: [
    // broken-ref removed (Phase 7): def:ew-interface-knot
    "prop:atomic-mass-gb-nf",
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
