import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:free-config-chi-lr-equivalence",
  title:
    "Hecke disjoint-product character via Littlewood-Richardson",
  lean: {
    ref: "qou:QOU.BraidKnot.FreeConfigChiLrEquivalence",
    validation: "not_checked",
  },
  uses: [
    "def:ew-interface-knot",
    "prop:atomic-mass-gb-nf",
    "conj:block-multiplicativity-v-free",
  ],
  computation: {
    engine: "python+rust",
    script:
      "folio-assistant/computations/binding_depth_stratified_lr.py",
    witness:
      "folio-assistant/computations/binding-depth-stratified-lr.witness.json",
    status: "verified",
  },
  tags: [
    "littlewood-richardson",
    "wedderburn",
    "convolution",
    "disjoint-hecke-product",
    "interface-knot",
  ],
});
