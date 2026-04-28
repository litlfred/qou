import { definition } from "../../schema/builders";

export default definition({
  label: "def:horizon-functor",
  title: "Horizon functor",
  tags: [
    "horizon-functor", "aeon", "jet-horizon",
    "boundary", "connected-components",
  ],
  lean: { ref: "qou:QOU.HorizonFunctor",
    validation: "not_checked",
  },
  uses: [
    "def:observable-subcategory",
    "def:aeon",
  ],
});
