import { definition } from "../../schema/builders";

/**
 * No quasi-zeros condition on the ground ring R.
 *
 * An element a in an R-algebra A is a quasi-zero if bac = 0 for all
 * b, c in A not both the identity.  We require R to
 * have no quasi-zeros so that leading-term arguments are well-defined.
 *
 * Cross-references the Unital Gröbner Bases paper where this
 * condition is central to the division algorithm and monomial-basis
 * theory.
 */
export default definition({
  label: "def:no-quasi-zeros",
  title: "Algebra without quasi-zeros",
  lean: {
    decl: "QOU.NoQuasiZeros",
    validation: "not_checked",
  },
  tags: ["algebra", "ground-ring"],
  uses: [],
  cites: ["leitnerpawloski2004"],
});
