import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atom-knot-exists",
  title: "Existence of the atom-knot for any (Z, N)",
  lean: { ref: "qou:QOU.BraidKnot.AtomKnot.exists",
    validation: "not_checked",
  },
  uses: ["prop:atom-knot-unique"],
  tags: ["existence", "atom-knot", "borromean"],
});
