import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:tilting-module-rigidity",
  title: "Tilting module rigidity",
  lean: {
    ref: "qou:QOU.Archimedean.tilting_module_rigidity",
    validation: "not_checked",
  },
  tags: [
    "cemetery-group",
    "tilting-module",
    "rigidity",
  ],
  uses: ["prop:spectrahedral-phase-collapse"],
});
