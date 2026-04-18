import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atom-knot-exists",
  title: "Existence of the atom-knot for any (Z, N)",
  lean: {
    decl: "QOU.BraidKnot.AtomKnot.exists",
    validation: "not_checked",
  },
  uses: [
    "def:atom-knot",
    "def:atomic-braid",
    "def:hecke-normal-form",
    "def:borromean-baryon",
    "prop:atom-knot-unique",
  ],
  tags: ["existence", "atom-knot", "borromean"],
});
