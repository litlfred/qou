import { remark } from "../../schema/builders";

export default remark({
  label: "rem:inductive-gb-complexity",
  title: "Complexity of Inductive Gröbner Reduction",
  tags: [
    "groebner-shirshov",
    "inductive",
    "computational-complexity",
  ],
  uses: ["prop:inductive-gb-reduction"],
});
