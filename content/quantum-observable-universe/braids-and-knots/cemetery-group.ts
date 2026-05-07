import { definition } from "../../schema/builders";

export default definition({
  label: "def:cemetery-group",
  title: "Cemetery group (subcategory annihilated by $\\tau$)",
  lean: { ref: "qou:QOU.BraidKnot.CemeteryGroup",
    validation: "not_checked",
  },
  uses: [
    "def:observation",
    "def:hecke-normal-form",
  ],
  cites: [
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "cemetery-group",
    "subcategory",
    "decoupling",
    "klr",
    "observation-frame",
  ],
  defines: ["cemetery-group"],
});
