import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-prefix-gb-filtration",
  title:
    "Jet-level prefix formula via Gröbner–Shirshov filtration (candidate Term 6)",
  lean: {
    decl: "QOU.BraidKnot.jet_prefix_gb_filtration",
    validation: "not_checked",
  },
  uses: [
    "def:confinement-level",
    "def:hecke-normal-form",
    "thm:knot-mass-formula-unified",
    "prop:gb-residue-spectral-sum",
    "prop:schur-weyl-mass-decomposition",
    "thm:jones-markov-trace",
  ],
  tags: [
    "jet-level",
    "prefix-formula",
    "gb-filtration",
    "groebner-shirshov",
    "term-6",
    "open-problem",
  ],
});
