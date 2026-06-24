import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atom-knot-exists",
  proofs: ["prf:atom-knot-exists"],
  title: "Existence of the atom-knot for any (Z, N)",
  lean: { ref: "qou:QOU.BraidKnot.AtomKnot.exists",
    validation: "not_checked",
  },
  uses: [],
  tags: ["existence", "atom-knot", "borromean"],
});
