import { definition } from "../../schema/builders";

export default definition({
  label: "def:cmb-functor",
  title: "CMB functor",
  tags: [
    "cmb-functor", "cmb", "horizon-functor",
    "colimit", "jet-quotient", "aeon",
  ],
  lean: { ref: "qou:QOU.CMBFunctor",
    validation: "not_checked",
  },
  uses: ["def:horizon-functor"],
});
