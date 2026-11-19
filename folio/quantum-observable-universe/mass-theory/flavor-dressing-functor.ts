import { definition } from "../../schema/builders";

export default definition({
  label: "def:flavor-dressing-functor",
  lean: { ref: "qou:QOU.FlavorDressing.FlavorDressingFunctor",
    validation: "not_checked",
  },
  title: "Flavor dressing functor",
  tags: [
    "flavor",
    "dressing",
    "quark-mass",
    "categorical-functor",
    "substrate-derived",
  ],
  uses: [],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
